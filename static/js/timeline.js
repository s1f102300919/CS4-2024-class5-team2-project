document.addEventListener('DOMContentLoaded',() =>{
    const likeButtons = document.querySelectorAll('.like-button');

    likeButtons.forEach(button =>{
        button.addEventListener('click',(event) =>{
            const likeCountElement = event.target.nextElementSibling;
            let currentCount = parseInt(likeCountElement.textContent,10);
            likeCountElement.textContent = currentCount+1;
        });
    });
});

const socket = new WebSocket('ws://localhost:8000/timeline/');

// 接続が確立したときの処理
socket.onopen = function (e) {
    console.log("WebSocket connected");
};

// メッセージを受信したときの処理
socket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    console.log("Received message:", data.message);

    // タイムラインにメッセージを追加
    const timeline = document.getElementById('timeline');
    const newMessage = document.createElement('div');
    newMessage.textContent = data.message;
    timeline.appendChild(newMessage);
};

// メッセージを送信
document.getElementById('sendButton').onclick = function () {
    const input = document.getElementById('messageInput');
    socket.send(JSON.stringify({
        'message': input.value
    }));
    input.value = '';
};
