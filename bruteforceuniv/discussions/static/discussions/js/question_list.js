function enterKeyPress(event) {
  if(event.keyCode == 13) {
    document.getElementById('btn_search').click();
  }
}

document.addEventListener('keydown', enterKeyPress)