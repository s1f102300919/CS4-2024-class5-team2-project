document.addEventListener('DOMContentLoaded', function () {
  const deleteButtons = document.querySelectorAll('.delete-button');
  const timeElement = document.getElementById('time');
  const startButton = document.getElementById('start');
  const stopButton = document.getElementById('stop');
  const resetButton = document.getElementById('reset');
  const form = document.forms['form'];
  let startTime, stopTime = 0, timeoutID;


  deleteButtons.forEach(button => {
    button.addEventListener('click', function (event) {
        const form = event.target.closest('.delete-form');
        const subjectName = form.querySelector('input[name="subject_name"]').value;

        // 確認ダイアログを表示
        if (confirm(`本当に「${subjectName}」を削除しますか？`)) {
            form.submit(); // ユーザーが「はい」を選択した場合にフォームを送信
        }
    });
});




  // 時間を表示する関数
  function displayTime() {
      const elapsedTime = Date.now() - startTime + stopTime; // 経過時間 (ミリ秒)
      const h = String(Math.floor(elapsedTime / 3600000)).padStart(2, '0'); // 時間
      const m = String(Math.floor((elapsedTime % 3600000) / 60000)).padStart(2, '0'); // 分
      const s = String(Math.floor((elapsedTime % 60000) / 1000)).padStart(2, '0'); // 秒
      timeElement.textContent = `${h}:${m}:${s}`;
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
  stopButton.addEventListener('click', () => {
      startButton.disabled = false;
      stopButton.disabled = true;
      resetButton.disabled = false;
      clearTimeout(timeoutID);
      stopTime += (Date.now() - startTime);
  });

  // リセットボタンがクリックされたら時間を0に戻す
  resetButton.addEventListener('click', () => {
      startButton.disabled = false;
      stopButton.disabled = true;
      resetButton.disabled = true;
      timeElement.textContent = '00:00:00';
      stopTime = 0;
  });

  // フォーム送信時に選択した科目と経過時間を追加
  form.addEventListener('submit', () => {
      const selectedSubject = document.getElementById('lang').value;
      const elapsedTime = timeElement.textContent;
      document.getElementById('selected-subject').value = selectedSubject;
      document.getElementById('elapsed-time').value = elapsedTime;
  });
});
