document.addEventListener('DOMContentLoaded', function () {
    const timeElement = document.getElementById('time');
    const startButton = document.getElementById('start');
    const stopButton = document.getElementById('stop');
    const resetButton = document.getElementById('reset');
    const form = document.forms['form'];
    let startTime, stopTime = 0, timeoutID;

    function displayTime() {
        const elapsedTime = Date.now() - startTime + stopTime;
        const h = String(Math.floor(elapsedTime / 3600000)).padStart(2, '0');
        const m = String(Math.floor((elapsedTime % 3600000) / 60000)).padStart(2, '0');
        const s = String(Math.floor((elapsedTime % 60000) / 1000)).padStart(2, '0');
        timeElement.textContent = `${h}:${m}:${s}`;
        timeoutID = setTimeout(displayTime, 10);
    }

    startButton.addEventListener('click', () => {
        startButton.disabled = true;
        stopButton.disabled = false;
        resetButton.disabled = true;
        startTime = Date.now();
        displayTime();
    });

    stopButton.addEventListener('click', () => {
        startButton.disabled = false;
        stopButton.disabled = true;
        resetButton.disabled = false;
        clearTimeout(timeoutID);
        stopTime += (Date.now() - startTime);
    });

    resetButton.addEventListener('click', () => {
        startButton.disabled = false;
        stopButton.disabled = true;
        resetButton.disabled = true;
        timeElement.textContent = '00:00:00';
        stopTime = 0;
    });

    form.addEventListener('submit', () => {
        const selectedSubject = document.getElementById('lang').value;
        const elapsedTime = timeElement.textContent;
        document.getElementById('selected-subject').value = selectedSubject;
        document.getElementById('elapsed-time').value = elapsedTime;
    });
});

document.getElementById('lang').addEventListener('change', function () {
    document.getElementById('selected-subject').value = this.value;
});
