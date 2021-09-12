//글자 수세기 
function checkLength(obj){
  const minLength = 50; //최소 200바이트 (100자)
  const text_val = obj.value; //입력한 문자
  const text_len = text_val.length; //입력한 문자수
  
  if(text_len<minLength){
    document.getElementById("counter").innerHTML = "(최소 50자 / " + text_len + ")";
      document.getElementById("counter").style.color = "red";
      }else{
        document.getElementById("counter").innerHTML = "(최소 50자 / " + text_len + ")";
          document.getElementById("counter").style.color = "green";
      }
  }


function validate() {
  const attendanceInput = document.getElementById("AttendanceInput").value;
  const fileInput = document.getElementById("FileInput").value;
  const urlInput  = document.getElementById("UrlInput").value;
  
  if (!attendanceInput && !fileInput && !urlInput) {
    alert('제출할 내용이 없네요 :(')
    return false
  } else if (attendanceInput.length < 50) {
    alert('학습 일지(출석)는 50자 이상 작성해주세요.')
    return false
  } else if (attendanceInput || fileInput || urlInput) {
    alert('잘하셨습니다! 이번주 학습을 완료하셨네요 :)')
    return true
  }
  return false
}
