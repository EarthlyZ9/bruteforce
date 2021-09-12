var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

var myModal = document.getElementById('myModal')
var myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus()
})

function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

//data를 서버로 전송, 전송된 데이터는 views에서 처리
function checkUsernameAvailability() {
  let username_element = document.getElementById('id_username')
  let username = document.getElementById("id_username").value

  if (!username) {
    alert('아이디를 입력해주세요.')
    return false
  }

  let formData = new FormData();
  formData.append('username', username)

  const xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
    let result = JSON.parse(this.responseText)
    if(result.result) {
      alert('이미 존재하는 아이디입니다. 다른 아이디를 설정해주세요.')
      username_element.setCustomValidity('사용불가')
      username_element.classList.add('is-invalid')
      username_element.classList.remove('is-valid')
    } else {
      alert('사용가능한 아이디입니다.')
      username_element.setCustomValidity('')
      username_element.classList.add('is-valid')
      username_element.classList.remove('is-invalid')
    }

    }
  xhttp.open("POST", "/mypage/signup/usernameavailability", true);
  xhttp.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
  xhttp.send(formData);
}

function complete() {
  alert('회원가입이 완료되었습니다! 시작해볼까요?')
}


