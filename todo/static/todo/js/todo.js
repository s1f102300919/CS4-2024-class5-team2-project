'use strict';

const table = document.querySelector('table');
const todo = document.getElementById('todo'); //ToDo
const deadline = document.querySelector('input[type="date"]'); //締め切り
const submit = document.getElementById('submit'); //追加ボタン

submit.addEventListener('click', () => {
  const item = {};

  item.todo = todo.value;
  item.deadline = deadline.value;
  item.done = false; // 完了はひとまずBoolean値で設定

  //コンソールで確認
  console.log(item);

  //フォームのリセット
  todo.value = '';
  deadline.value = '';

  const tr = document.createElement('tr'); //tr要素生清

  //オブジェクトの繰り返しはfor-in文
  for (const prop in item) {
    const td = document.createElement('td'); //td要素を生成
    td.textContent = item[prop];
    tr.appendChild(td); //生成したtd要素をtr要素に追加
  }

  // tbodyに行を追加
  table.append(tr); 
})