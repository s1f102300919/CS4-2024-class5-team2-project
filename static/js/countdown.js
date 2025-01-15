// script.js

document.getElementById("startTimer").addEventListener("click", function() {
    const deadlineInput = document.getElementById("deadline").value;
  
    if (!deadlineInput) {
      alert("期限を入力してください。");
      return;
    }
  
    const deadline = new Date(deadlineInput);  // 期限をDate型に変換
    startCountdown(deadline);
  });
  
  function startCountdown(deadline) {
    const countdownDisplay = document.getElementById("countdownDisplay");
    const timerElement = document.getElementById("timer");
  
    const interval = setInterval(function() {
      const now = new Date().getTime();
      const timeLeft = deadline - now;
  
      if (timeLeft <= 0) {
        clearInterval(interval);
        timerElement.innerHTML = "タイムアップ！";
        timerElement.classList.remove("blink");
        timerElement.classList.add("blinking");
      } else {
        const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);
  
        timerElement.innerHTML = `${days}日 ${hours}時間 ${minutes}分 ${seconds}秒`;
        
        // 秒が減るごとにちらつき効果を追加
        if (seconds % 2 === 0) {
          timerElement.classList.add("blink");
        } else {
          timerElement.classList.remove("blink");
        }
      }
    }, 1000);
  }
  