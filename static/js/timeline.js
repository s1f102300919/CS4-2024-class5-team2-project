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