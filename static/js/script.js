
//完了、未完了ボタンを押したときの動き
$(document).ready(function() {
    $('.toggle-completed').click(function() {
      //1.タスクID取得
      var taskId = $(this).data('id');
      //2,Ajax送信処理
      $.ajax({
        url: '/djangotodo/' + taskId + '/complete/',
        type: 'POST',
        dataType: 'json',
        //3.CSRF処理
        beforeSend: function(xhr, settings) {
          xhr.setRequestHeader('X-CSRFToken', $('input[name="csrfmiddlewaretoken"]').val());
        },
        //4.Ajax受信処理
        success: function(data, textStatus, xhr) {
          if (data.is_completed) {
            $('tr[data-id="' + taskId + '"]').addClass('completed');
            $('.toggle-completed[data-id="' + taskId + '"]').text('未完了にする');
          } else {
            $('tr[data-id="' + taskId + '"]').removeClass('completed');
            $('.toggle-completed[data-id="' + taskId + '"]').text('完了にする');
          }
        },
      });
    });
  });