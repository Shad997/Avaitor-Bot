function show_msg(msg, type, timeout) {
  if (type == "danger") {type = "error"}
  $.toast({
    text: msg,
    icon: type,
    position: "top-right",
    showHideTransition: "slide",
    hideAfter: timeout,
  });
}
function updateStatus() {
  fetch(window.location.href, {method: 'PATCH'}).then(async function (d) {
    r = await d.json();
    for (let [id, status] of Object.entries(r)) {
      $(`#${id} .status`).text(status)
      if (status.toLowerCase().indexOf('run') != -1) {
        $(`#${id} .status`).addClass('text-success').removeClass('text-danger');
        $(`#${id} .stop`).show();$(`#${id} .start`).hide();
      } else {
        $(`#${id} .status`).removeClass('text-success').addClass('text-danger');
        $(`#${id} .stop`).hide();$(`#${id} .start`).show();
      }
    }
  }).catch(async function (e) {
    show_msg('Error while fetching data: ' + e, 'error', 10000)
  })
}
function operateBot() {
  let e = $(this);
  let bot = e.parent().parent().attr('id');
  let run = e.hasClass('start') ? 1 : 0;
  $.ajax({
    url: window.location.href,
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded"},
    data: `bot=${bot}&run=${run}`,
    success: function (r, s) {
      if (r.success) {
        show_msg(r.msg, 'success', 3000)
      } else {
        show_msg('The response is not in json, something went wrong!', 'error', 10000)
      }
    },
    error: function (e, s) {
      show_msg('Error while submitting data: ' + e, 'error', 10000)
    }
  });
}
window.addEventListener('load', function () {
  setInterval(updateStatus, 2000);
  updateStatus();
  $('.start, .stop').click(operateBot);
})