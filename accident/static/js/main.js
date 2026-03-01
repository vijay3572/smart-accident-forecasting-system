// static/js/main.js
// small helper: focus first input on load
document.addEventListener('DOMContentLoaded', function(){
  const firstInput = document.querySelector('input.form-control');
  if(firstInput) firstInput.focus();
});
