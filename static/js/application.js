$(document).ready(function() {
  $('#set_on').click(function() {
    $.post('/change_led_status/1');
  });
  $('#set_off').click(function() {
    $.post('/change_led_status/0');
  });
});
