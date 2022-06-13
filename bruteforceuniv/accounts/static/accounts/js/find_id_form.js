const spinnerHTML = '<div class="spinner-border m-3" role="status"> \
<span class="visually-hidden">Loading...</span> \
</div>';

const InputForm = document.getElementById('form');


emailForm.onsubmit = function() {
  console.log('ㅇㅇ')
  document.getElementById('spinner_div').innerHTML = spinnerHTML
}