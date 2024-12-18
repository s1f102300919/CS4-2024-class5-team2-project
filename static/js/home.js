const apiKey = 'e757a6dbe37dbd19d164af7be435fd39';
const city = 'q=Tokyo';
const apiUrl = `https://api.openweathermap.org/data/2.5/weather?`;
const url = apiUrl + city + '&appid=' + apiKey + '&units=metric';

fetch(url)
    .then(response => response.json())
    .then((data) => {
        // 天気情報の表示
        document.getElementById("weather").innerHTML = data.weather[0].main;
        document.getElementById("temparature").innerHTML = data.main.temp;
        document.getElementById("wind").innerHTML = data.wind.speed;

        // 日付と時間の表示
        let dateObj = new Date(data.dt * 1000); // UNIXタイムをミリ秒に変換
        let month = dateObj.getMonth() + 1; // 0始まりなので+1
        let date = dateObj.getDate();
        let hours = dateObj.getHours();
        let minutes = dateObj.getMinutes(); // 2桁に0埋め
        let formattedDate = `${month}月${date}日 ${hours}時${minutes}分`;

        // 日時情報をHTMLに表示
        document.getElementById("datetime").innerHTML = formattedDate;

        // コンソールにも日時を表示（デバッグ用）
        console.log(formattedDate);
    })
    .catch(error => console.error('エラーが発生しました:', error));
