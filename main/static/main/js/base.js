//logout 버튼 클릭시 알림창

(function() {
  'use strict';
  window.addEventListener('load', function() {
    const logoutButton = document.getElementById('logout-btn');

    function onLogoutBtnClick() {
      alert("성공적으로 로그아웃 되었습니다!")
    };

    logoutButton.addEventListener("click", onLogoutBtnClick);

    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl)
    })
  }, false);
})();

function goPage(url) {
  
}

function disabled() {
  alert('학습 기간이 아닙니다.')
};
  
  