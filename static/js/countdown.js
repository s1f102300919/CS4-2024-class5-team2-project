// ボタンをクリックするとアニメーションが始まる処理
document.getElementById('animateButton').addEventListener('click', function() {
    const box = document.getElementById('animatedBox');
    
    // 'animate'クラスを追加または削除
    box.classList.toggle('animate');
  });
  