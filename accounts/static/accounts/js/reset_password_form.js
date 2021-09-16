const spinnerHTML = '<div class="spinner-border m-3" role="status"> \
<span class="visually-hidden">Loading...</span> \
</div>';

const emailForm = document.getElementById('form');
const submitBtn = document.getElementById('submit-btn');


emailForm.onsubmit = function() {
  document.body.style.cursor = "progress";
  submitBtn.style.cursor = "progress";
  document.getElementById('spinner_div').innerHTML = spinnerHTML
}
