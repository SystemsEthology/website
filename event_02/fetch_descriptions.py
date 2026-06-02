#!/usr/bin/env python3
"""
Wikipediaの日本語APIから各キーワードの説明を取得し、
clustered_keywords.json の description フィールドに書き込む。

使い方:
  python3 fetch_descriptions.py

オプション:
  --overwrite   既存の description を上書きする
"""
import json
import sys
import time
import urllib.parse
import urllib.request

JSON_PATH = "clustered_keywords.json"
MAX_DESC_LEN = 120
DELAY_SEC = 1.0
MAX_RETRIES = 4


def fetch_wikipedia_summary(keyword: str) -> str:
    """日本語Wikipediaのsummary APIからキーワードの説明を取得する。"""
    encoded = urllib.parse.quote(keyword)
    url = f"https://ja.wikipedia.org/api/rest_v1/page/summary/{encoded}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "keyword-map-fetcher/1.0 (research tool)"},
    )
    for attempt in range(MAX_RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=8) as resp:
                data = json.loads(resp.read())
                extract = data.get("extract", "").strip()
                if not extract:
                    return ""
                # 最初の一文だけ取得（「。」で区切る）
                first = extract.split("。")[0]
                desc = first + "。" if first else extract[:MAX_DESC_LEN]
                if len(desc) > MAX_DESC_LEN:
                    desc = desc[: MAX_DESC_LEN - 1] + "…"
                return desc
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return ""  # 記事なし
            if e.code == 429:
                wait = 2 ** attempt * 2
                print(f"    429 rate limit, {wait}秒待機...", flush=True)
                time.sleep(wait)
                continue
            raise
    return ""  # リトライ上限


def main():
    overwrite = "--overwrite" in sys.argv

    with open(JSON_PATH, encoding="utf-8") as f:
        data = json.load(f)

    keywords = data.get("keywords", [])
    updated = 0
    skipped = 0
    not_found = 0

    for i, item in enumerate(keywords):
        kw = item.get("keyword", "")
        if not kw:
            continue

        if item.get("description") and not overwrite:
            skipped += 1
            continue

        try:
            desc = fetch_wikipedia_summary(kw)
        except Exception as e:
            print(f"  ERROR [{kw}]: {e}", flush=True)
            desc = ""

        if desc:
            item["description"] = desc
            updated += 1
            print(f"  ✓ ({i+1}/{len(keywords)}) {kw}: {desc[:60]}…", flush=True)
        else:
            not_found += 1
            print(f"  – ({i+1}/{len(keywords)}) {kw}: Wikipedia記事なし", flush=True)

        time.sleep(DELAY_SEC)

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n完了: 更新={updated}, スキップ={skipped}, 記事なし={not_found}")
    print(f"{JSON_PATH} を保存しました。")


if __name__ == "__main__":
    main()
