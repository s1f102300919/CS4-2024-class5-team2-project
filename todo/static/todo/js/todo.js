// ボタン
const addButton = document.getElementById("addButton");
// リスト（親）
const list = document.getElementById("mylist");

// 最初のリストの中の子であるアイテム数を数える
let itemCount = list.children.length;

addButton.addEventListener("click", () => {
  itemCount++;
  
  // チェックボックスの作成
  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.id = `checkbox${itemCount}`;

  // ラベルの作成
  const label = document.createElement("label");
  label.htmlFor = `checkbox${itemCount}`;
  label.textContent = `新しいタスク${itemCount}`;

  // 改行の追加
  const br = document.createElement("br");

  // リストに追加
  list.appendChild(checkbox);
  list.appendChild(label);
  list.appendChild(br);
});