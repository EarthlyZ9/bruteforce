//엔터키로 로그인 수행

function enterKeyPress(event) {
  if(event.keyCode == 13) {
    document.getElementById('btn_search').click();
  }
}

document.addEventListener('keydown', enterKeyPress)