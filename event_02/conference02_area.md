---
layout: page_conference_02
title: 会場案内
order: 7
ogp_image: /event_02/images/systems_ethology_2026_01.png
---

 <br>

<!-- Leaflet.js（全マップ共通：1回のみ読み込み） -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

***

## 名古屋大学　豊田講堂
<div class="map__img">
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3262.130445576514!2d136.9654969760703!3d35.15336737276222!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60037abbaebc8843%3A0x8981e3dc29704377!2z6LGK55Sw6Kyb5aCC!5e0!3m2!1sja!2sjp!4v1775004647053!5m2!1sja!2sjp" width="400" height="400" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</div>

<br>

***

## ランチ：名古屋大学付近

会場周辺（名古屋大学駅・東山公園駅エリア）のおすすめランチスポットです。

<div id="map-lunch" style="width:100%;max-width:600px;height:300px;border:1px solid #ccc;border-radius:4px;"></div>
<script>
(function(){
  var map = L.map('map-lunch').setView([35.1520, 136.9660], 14);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);
  var places = [
    {lat:35.1538, lng:136.9637, name:'花の木（名大生協）', info:'食堂・定食 ／ 名古屋大学構内', url:'https://www.google.com/maps/search/花の木+名古屋大学生協'},
    {lat:35.1526, lng:136.9754, name:'蕎麦り ふ〜助',     info:'蕎麦 ／ 東山公園駅近く',      url:'https://www.google.com/maps/search/蕎麦り+ふ〜助+東山公園+名古屋'},
    {lat:35.1498, lng:136.9648, name:'武蔵坊',             info:'蕎麦・定食 ／ 名古屋大学駅付近', url:'https://www.google.com/maps/search/武蔵坊+名古屋大学'},
    {lat:35.1510, lng:136.9642, name:"BISTRO L'Assiette",  info:'フレンチ ／ 名古屋大学駅付近', url:'https://www.google.com/maps/search/BISTRO+L+Assiette+名古屋大学'}
  ];
  places.forEach(function(p){
    L.marker([p.lat,p.lng]).addTo(map)
      .bindPopup('<b><a href="'+p.url+'" target="_blank" rel="noopener">'+p.name+'</a></b><br>'+p.info);
  });
})();
</script>

| 店名 | ジャンル | 特徴 | アクセス |
|------|---------|------|---------|
| [花の木（名大生協）](https://www.google.com/maps/search/花の木+名古屋大学生協) | 食堂・定食 | 日替わりランチ・天ぷら定食など、リーズナブルな学内食堂 | 名古屋大学構内 |
| [蕎麦り ふ〜助](https://www.google.com/maps/search/蕎麦り+ふ〜助+東山公園+名古屋) | 蕎麦 | 出来立て熱々の蕎麦が人気、蕎麦がきも絶品 | 東山公園駅近く |
| [武蔵坊](https://www.google.com/maps/search/武蔵坊+名古屋大学) | 蕎麦・定食 | チキン南蛮カレーや丼物が充実、コスパ良好 | 名古屋大学駅付近 |
| [BISTRO L'Assiette](https://www.google.com/maps/search/BISTRO+L+Assiette+名古屋大学) | フレンチ | 気軽に楽しめる本格フレンチビストロ | 名古屋大学駅付近 |

<br>

***

## 飲み屋：本山駅付近

会場から**名城線で1駅（約3分）**の最寄りエリアです。アクセス抜群で1次会に最適。

<div id="map-motoyama" style="width:100%;max-width:600px;height:300px;border:1px solid #ccc;border-radius:4px;"></div>
<script>
(function(){
  var map = L.map('map-motoyama').setView([35.1645, 136.9555], 16);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);
  var places = [
    {lat:35.1630, lng:136.9512, name:'鉄板鶏舎 tori to tamago', info:'焼き鳥・鉄板 ／ 本山駅徒歩4分', url:'https://www.google.com/maps/search/鉄板鶏舎+tori+to+tamago+本山+名古屋'},
    {lat:35.1648, lng:136.9553, name:'串カツ どて ウラバン',     info:'串カツ居酒屋 ／ 本山駅徒歩1分', url:'https://www.google.com/maps/search/串カツ+どて+ウラバン+本山+名古屋'},
    {lat:35.1650, lng:136.9560, name:'べこや 本山店',            info:'炉端焼き ／ 本山駅1番出口徒歩1分', url:'https://www.google.com/maps/search/べこや+本山+名古屋'},
    {lat:35.1652, lng:136.9568, name:'Cafe Lembeek',             info:'ベルギービールバー ／ 本山駅1番出口徒歩2分', url:'https://www.google.com/maps/search/Cafe+Lembeek+本山+名古屋'}
  ];
  places.forEach(function(p){
    L.marker([p.lat,p.lng]).addTo(map)
      .bindPopup('<b><a href="'+p.url+'" target="_blank" rel="noopener">'+p.name+'</a></b><br>'+p.info);
  });
})();
</script>

| 店名 | ジャンル | 特徴 | アクセス |
|------|---------|------|---------|
| [鉄板鶏舎 tori to tamago](https://www.google.com/maps/search/鉄板鶏舎+tori+to+tamago+本山+名古屋) | 焼き鳥・鉄板 | 幻の地鶏「土佐ジロー」使用、イタリアビールも充実 | 本山駅徒歩4分 |
| [串カツ どて ウラバン](https://www.google.com/maps/search/串カツ+どて+ウラバン+本山+名古屋) | 串カツ居酒屋 | 千べろセット（ドリンク3杯＋串4本）でコスパ抜群 | 本山駅徒歩1分 |
| [べこや 本山店](https://www.google.com/maps/search/べこや+本山+名古屋) | 炉端焼き | 囲炉裏で豪快に焼く炉端料理、魚介も充実 | 本山駅1番出口徒歩1分 |
| [Cafe Lembeek](https://www.google.com/maps/search/Cafe+Lembeek+本山+名古屋) | ベルギービールバー | 自社輸入のベルギービール常時400種以上を取り揃える専門店 | 本山駅1番出口徒歩2分 |

<br>

***

## 飲み屋：栄付近

名古屋最大の繁華街。会場から**名城線で約15分**。多人数の懇親会にも対応する大型店が多数あります。

<div id="map-sakae" style="width:100%;max-width:600px;height:300px;border:1px solid #ccc;border-radius:4px;"></div>
<script>
(function(){
  var map = L.map('map-sakae').setView([35.1701, 136.9080], 17);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);
  var places = [
    {lat:35.1701, lng:136.9068, name:'濱匠 錦 本店',          info:'串焼き・和食 ／ 栄駅西隣ビル地下', url:'https://www.google.com/maps/search/濱匠+錦+本店+名古屋'},
    {lat:35.1706, lng:136.9086, name:'鉄板DINING 煌 錦邸',    info:'鉄板焼き ／ 栄駅徒歩3分',        url:'https://www.google.com/maps/search/鉄板DINING+煌+錦邸+名古屋'},
    {lat:35.1700, lng:136.9088, name:'個室 俵家商店マルコメ栄', info:'和食居酒屋 ／ 栄駅徒歩1分',      url:'https://www.google.com/maps/search/俵家商店+マルコメ+栄+名古屋'},
    {lat:35.1710, lng:136.9092, name:'BAR PARTAGE',           info:'バー ／ 栄駅徒歩3〜5分',         url:'https://www.google.com/maps/search/BAR+PARTAGE+栄+名古屋'}
  ];
  places.forEach(function(p){
    L.marker([p.lat,p.lng]).addTo(map)
      .bindPopup('<b><a href="'+p.url+'" target="_blank" rel="noopener">'+p.name+'</a></b><br>'+p.info);
  });
})();
</script>

| 店名 | ジャンル | 特徴 | アクセス |
|------|---------|------|---------|
| [濱匠 錦 本店](https://www.google.com/maps/search/濱匠+錦+本店+名古屋) | 串焼き・和食 | 串焼きと味噌おでんが名物、名古屋めしが揃う老舗 | 栄駅西隣ビル地下 |
| [鉄板DINING 煌 錦邸](https://www.google.com/maps/search/鉄板DINING+煌+錦邸+名古屋) | 鉄板焼き | 飛騨牛・旬の海鮮を目の前で焼いてくれる贅沢な鉄板焼き | 栄駅徒歩3分 |
| [個室 俵家商店マルコメ栄](https://www.google.com/maps/search/俵家商店+マルコメ+栄+名古屋) | 和食居酒屋 | 愛知県産食材にこだわった古民家風の個室居酒屋 | 栄駅徒歩1分 |
| [BAR PARTAGE](https://www.google.com/maps/search/BAR+PARTAGE+栄+名古屋) | バー | 洗練された雰囲気のカクテルバー、2軒目に最適 | 栄駅徒歩3〜5分 |

<br>

***

## 飲み屋：名古屋駅付近

新幹線でお越しの方にも便利なエリア。会場から**地下鉄で約30分**。ホテルバーから気軽な居酒屋まで幅広い選択肢があります。

<div id="map-nagoya-sta" style="width:100%;max-width:600px;height:300px;border:1px solid #ccc;border-radius:4px;"></div>
<script>
(function(){
  var map = L.map('map-nagoya-sta').setView([35.1706, 136.8816], 15);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);
  var places = [
    {lat:35.1720, lng:136.8838, name:'和食郷土料理茶寮 徳川', info:'和食居酒屋 ／ 名古屋駅徒歩3分',  url:'https://www.google.com/maps/search/和食郷土料理茶寮+徳川+名古屋駅'},
    {lat:35.1730, lng:136.8854, name:'那古野サルーン',         info:'居酒屋 ／ 名古屋駅徒歩10分',    url:'https://www.google.com/maps/search/那古野サルーン+名古屋'},
    {lat:35.1706, lng:136.8816, name:'エストマーレ',           info:'ホテルバー ／ 名古屋駅直結',     url:'https://www.google.com/maps/search/エストマーレ+名古屋マリオットアソシア'},
    {lat:35.1725, lng:136.8848, name:'バー ニート 名駅店',     info:'バー ／ 名古屋駅徒歩10分',      url:'https://www.google.com/maps/search/バー+ニート+名駅+名古屋'}
  ];
  places.forEach(function(p){
    L.marker([p.lat,p.lng]).addTo(map)
      .bindPopup('<b><a href="'+p.url+'" target="_blank" rel="noopener">'+p.name+'</a></b><br>'+p.info);
  });
})();
</script>

| 店名 | ジャンル | 特徴 | アクセス |
|------|---------|------|---------|
| [和食郷土料理茶寮 徳川](https://www.google.com/maps/search/和食郷土料理茶寮+徳川+名古屋駅) | 和食居酒屋 | 名古屋コーチン・飛騨牛、希少日本酒20種以上常備、完全個室あり | 名古屋駅徒歩3分 |
| [那古野サルーン](https://www.google.com/maps/search/那古野サルーン+名古屋) | 居酒屋 | 古民家改装の温かい雰囲気、おでんが安くておすすめ | 名古屋駅徒歩10分 |
| [エストマーレ](https://www.google.com/maps/search/エストマーレ+名古屋マリオットアソシア) | ホテルバー | 名古屋マリオットアソシア15階、バー百名店選出 | 名古屋駅直結 |
| [バー ニート 名駅店](https://www.google.com/maps/search/バー+ニート+名駅+名古屋) | バー | ジャズが流れる落ち着いたオーセンティックバー | 名古屋駅徒歩10分 |
