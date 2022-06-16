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

const loginInputUserID = document.getElementById("floatingUserID");
const loginInputPassword = document.getElementById("floatingPassword");
const loginButton = document.getElementById("login-btn");

// function onLoginBtnClick() {
//   const userID = loginInputUserID.value;
//   const userPassword = loginInputPassword.value;
//   if (!userID) {
//     alert("아이디를 입력해주세요!")
//   } else if (!userPassword) {
//     alert("비밀번호를 입력해주세요!")
//   }
// }
//
// //loginButton.addEventListener("click", onLoginBtnClick);

var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})



//data를 서버로 전송, 전송된 데이터는 views에서 처리
function checkLogin() {
  let username = loginInputUserID.value
  let password = loginInputPassword.value
  console.log(typeof username)
  console.log(username, password)

  if (!username) {
    alert("아이디를 입력해주세요!")
    return
  } else if (!password) {
    alert("비밀번호를 입력해주세요!")
    return
  }

  let formData = new FormData();
  formData.append('username', username)
  formData.append('password', password)
  console.log(formData.get('username'));
  console.log(formData.get('password'));
  console.log(...formData);

  const xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
    console.log("response", this.responseText);
    let result = JSON.parse(this.responseText);
    console.log("result", result);
    if(result.result) {
      window.location.href = "/"
      alert('로그인 되었습니다.')
    } else {
      alert('아이디 또는 비밀번호가 일치하지 않습니다.')
    }
  }
  xhttp.open("POST", "/mypage/check/login", true);
  xhttp.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
  xhttp.send(formData);

  }


//엔터키로 로그인 수행
function enterKeyPress(event) {
  if(event.keyCode == 13) {
    checkLogin();
  }
}

document.addEventListener('keydown', enterKeyPress)