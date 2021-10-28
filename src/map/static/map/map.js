
// 現在地取得処理
function initMap() {
    // Geolocation APIに対応している
    if (navigator.geolocation) {
        // 現在地を取得
        navigator.geolocation.getCurrentPosition(
            // 取得成功した場合
            function (position) {
                // 緯度・経度を変数に格納
                var mapLatLng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
                // マップオプションを変数に格納
                if (searchAdress["None"] == 0) {
                    var mapOptions = {
                        zoom: 15,          // 拡大倍率
                        center: mapLatLng,  // 緯度・経度
                        styles : style
                    };
                } else {
                    var mapOptions = {
                        zoom: 15,          // 拡大倍率
                        center: new google.maps.LatLng(searchAdress["lat"], searchAdress["lng"]),  // 緯度・経度
                        styles: style
                    };
                }
                // マップオブジェクト作成
                var map = new google.maps.Map(
                    document.getElementById("map"), // マップを表示する要素
                    mapOptions         // マップオプション
                );
                //　マップにマーカーを表示する
                var currentmarker = new google.maps.Marker({
                    map: map,             // 対象の地図オブジェクト
                    position: mapLatLng,   // 緯度・経度
                    icon: {
                        fillColor: "#1E90FF",                //塗り潰し色
                        fillOpacity: 10,                    //塗り潰し透過率
                        path: google.maps.SymbolPath.CIRCLE, //円を指定
                        scale: 12,                           //円のサイズ
                        strokeColor: "#FFFFFF",              //枠の色
                        strokeWeight: 3.0                    //枠の透過率
                    }
                });
                // 現在表示されているinfoWindowオブジェクト
                let currentWindow;

                data.map(d => {
                // マーカーをつける
                //https://maps.google.com/mapfiles/ms/icons/red-dot.png
                //https://maps.google.com/mapfiles/ms/icons/blue-dot.png
                if (d.strong == "concentrations") {
                    const marker = new google.maps.Marker({
                        position: {lat: d.lat, lng: d.lng},
                        map: map,
                        icon: {
                            url:  "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=学|33cc00|ffffff",// マーカーの画像を変更
                            // url:  "https://as2.ftcdn.net/v2/jpg/01/58/00/45/500_F_158004591_vcqMK8Ykaii5kJI7p1R9DbKpWtfxMEA7.jpg",// マーカーの画像を変更
                            scaledSize : new google.maps.Size(ICON_W, ICON_H)
                        }
                    });
                    //マーカークリック時の操作
                    marker.addListener('click', () => {
                        currentWindow && currentWindow.close();
                        let placeid= d.id;
                        const windowContent =
                            '<div id="content">' +
                            '<h3 id="firstHeading" class="firstHeading">' + d.name + ' </h3>' +
                            '<div id="bodyContent">' +
                            '<p>' + d.adress + '</p>' +
                            // '<p>"集中度"の評価が高いです</p>' +
                            '<p>集中度：<span class="star5_rating" data-rate="' + d.para + '" ></span >'+' '+'('+d.para+')'+'</p>' +
                            '<p><a class="btn btn-secondary btn-sm" role="button" href="../space/space/' + placeid + '">詳細</a>' + '</p>' +
                            '</div>' +
                            '</div>';
                        const infoWindow = new google.maps.InfoWindow({ content: windowContent });
                        infoWindow.open(map, marker);
                        currentWindow = infoWindow;
                    });

                } else if (d.strong == "silence"){
                    const marker = new google.maps.Marker({
                        position: {lat: d.lat, lng: d.lng},
                        map: map,
                        icon: {
                            url: "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=静|0099ff|ffffff",
                            // url:  "https://cdn.xxl.thumbs.canstockphoto.jp/%E6%A6%82%E5%BF%B5-%E5%BF%83-%E3%83%95%E3%82%A9%E3%83%BC%E3%82%AB%E3%82%B9-%E3%82%A2%E3%82%A4%E3%82%B3%E3%83%B3-%E3%82%AF%E3%83%AA%E3%83%83%E3%83%97%E3%82%A2%E3%83%BC%E3%83%88%E3%83%99%E3%82%AF%E3%82%BF%E3%83%BC_csp44382367.jpg",// マーカーの画像を変更
                            scaledSize : new google.maps.Size(ICON_W, ICON_H)
                        }
                    });
                    //マーカークリック時の操作
                    marker.addListener('click', () => {
                        currentWindow && currentWindow.close();
                        let placeid= d.id;
                        const windowContent =
                            '<div id="content">' +
                            '<h3 id="firstHeading" class="firstHeading">' + d.name + ' </h3>' +
                            '<div id="bodyContent">' +
                            '<p>' + d.adress + '</p>' +
                            // '<p>"静かさ"の評価が高いです</p>' +
                            '<p>静かさ：<span class="star5_rating" data-rate="' + d.para + '" ></span >' + ' ' + '(' + d.para + ')' +'</p>' +
                            '<p><a class="btn btn-secondary btn-sm" role="button" href="../space/space/' + placeid + '">詳細</a>' + '</p>' +
                            '</div>' +
                            '</div>';
                        const infoWindow = new google.maps.InfoWindow({ content: windowContent });
                        infoWindow.open(map, marker);
                        currentWindow = infoWindow;
                    });

                } else if (d.strong == "cost_pafo"){
                    const marker = new google.maps.Marker({
                        position: {lat: d.lat, lng: d.lng},
                        map: map,
                        icon: {
                            url:  "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=金|ffcc33|ffffff",// マーカーの画像を変更
                            scaledSize : new google.maps.Size(ICON_W, ICON_H)
                        }
                    });
                    //マーカークリック時の操作
                    marker.addListener('click', () => {
                        currentWindow && currentWindow.close();
                        let placeid= d.id;
                        const windowContent =
                            '<div id="content">' +
                            '<h3 id="firstHeading" class="firstHeading">' + d.name + ' </h3>' +
                            '<div id="bodyContent">' +
                            '<p>' + d.adress + '</p>' +
                            // '<p>"コスパ"の評価が高いです</p>' +
                            '<p>コスパ：<span class="star5_rating" data-rate="' + d.para + '" ></span >' + ' ' + '(' + d.para + ')' +'</p>' +
                            '<p><a class="btn btn-secondary btn-sm" role="button" href="../space/space/' + placeid + '">詳細</a>' + '</p>' +
                            '</p>' +
                            '</div>' +
                            '</div>';
                        const infoWindow = new google.maps.InfoWindow({ content: windowContent });
                        infoWindow.open(map, marker);
                        currentWindow = infoWindow;
                    });

                } else {
                    const marker = new google.maps.Marker({
                        position: {lat: d.lat, lng: d.lng},
                        map: map,
                        icon: {
                            url:  "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=空|ff6666|ffffff",// マーカーの画像を変更
                            scaledSize : new google.maps.Size(ICON_W, ICON_H)
                        },
                    });
                    //マーカークリック時の操作
                    marker.addListener('click', () => {
                        currentWindow && currentWindow.close();
                        let placeid= d.id;
                        const windowContent =
                            '<div id="content">' +
                            '<h3 id="firstHeading" class="firstHeading">'+ d.name +' </h3>' +
                            '<div id="bodyContent">' +
                            '<p>'+ d.adress +'</p>' +
                            // '<p>"空いてる度"の評価が高いです</p>'+
                            '<p>空いてる度：<span class="star5_rating" data-rate="'+ d.para +'" ></span>' + ' ' + '(' + d.para + ')' +'</p>'+
                            '<p><a class="btn btn-secondary btn-sm" role="button" href="../space/space/'+ placeid +'">詳細</a>' + '</p>' +
                            '</div>'+
                            '</div>';
                        const infoWindow = new google.maps.InfoWindow({content:windowContent});
                        infoWindow.open(map, marker);
                        currentWindow = infoWindow;
                    });
                }
                });
            },
            // 取得失敗した場合
            function (error) {
                // エラーメッセージを表示
                switch (error.code) {
                    case 1: // PERMISSION_DENIED
                        alert("位置情報の利用が許可されていません");
                        break;
                    case 2: // POSITION_UNAVAILABLE
                        alert("現在位置が取得できませんでした");
                        break;
                    case 3: // TIMEOUT
                        alert("タイムアウトになりました");
                        break;
                    default:
                        alert("その他のエラー(エラーコード:" + error.code + ")");
                        break;
                }
            }
        );
        // Geolocation APIに対応していない
    } else {
        alert("この端末では位置情報が取得できません");
    }
}
