const time = document.getElementById('time');
const startButton = document.getElementById('start');
const stopButton = document.getElementById('stop');
const resetButton = document.getElementById('reset');

// 開始時間
let startTime;
// 停止時間
let stopTime = 0;
// タイムアウトID
let timeoutID;

// 時間を表示する関数
function displayTime() {
  const elapsedTime = Date.now() - startTime + stopTime; // 経過時間 (ミリ秒)

  const h = String(Math.floor(elapsedTime / 3600000)).padStart(2, '0'); // 1時間 = 3600000ms
  const m = String(Math.floor((elapsedTime % 3600000) / 60000)).padStart(2, '0'); // 1分 = 60000ms
  const s = String(Math.floor((elapsedTime % 60000) / 1000)).padStart(2, '0'); // 1秒 = 1000ms

  time.textContent = `${h}:${m}:${s}`;
  timeoutID = setTimeout(displayTime, 10);
}

// スタートボタンがクリックされたら時間を進める
startButton.addEventListener('click', () => {
  startButton.disabled = true;
  stopButton.disabled = false;
  resetButton.disabled = true;
  startTime = Date.now();
  displayTime();
});

// ストップボタンがクリックされたら時間を止める
stopButton.addEventListener('click', function() {
  startButton.disabled = false;
  stopButton.disabled = true;
  resetButton.disabled = false;
  clearTimeout(timeoutID);
  stopTime += (Date.now() - startTime);
});

// リセットボタンがクリックされたら時間を0に戻す
resetButton.addEventListener('click', function() {
  startButton.disabled = false;
  stopButton.disabled = true;
  resetButton.disabled = true;
  time.textContent = '00:00:00';
  stopTime = 0;
});