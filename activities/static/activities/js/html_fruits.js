//엔터키로 로그인 수행

function enterKeyPress(event) {
  if(event.keyCode == 13) {
    document.getElementById('btn_search').click();
  }
}

document.addEventListener('keydown', enterKeyPress)

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

//ajax 먼소리야;;;;;;
document.getElementById('btn_get').addEventListener('click', function(event){
  const userId = document.getElementById('userID').innerHTML;
  const topic = document.getElementById('topic').innerHTML;
  const rightDiv = document.getElementById('right_div');

  const xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function(event) {
    //데이터를 다 받았고, 응답코드 200을 받았는지 체크
    if(xhttp.readyState == 4 && xhttp.status == 200) {
      //응답 받은 데이터 
      //const responseData = JSON.parse(this.responseText)
      const responseData = this.responseText
      //html innerhtml 바꾸기
      rightDiv.innerHTML = responseData
    }
  }

  xhttp.open("GET", `/activities/htmlcss_outputs/feedbacks/?author=${userId}&topic=${topic}`, true); 
  xhttp.send();
});

function post_feedback(submit_btn) {
  let feedbackContent = document.getElementById('input_feedback').value;
  const fruit_id  = submit_btn.closest('form').getAttribute('fruitid');
  const rightDiv = document.getElementById('right_div');

  if (!feedbackContent) {
    alert('피드백을 작성해주세요.')
    return false
  }

  let formData = new FormData();
  formData.append('content', feedbackContent)

  const xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function(event) {
    //데이터를 다 받았고, 응답코드 200을 받았는지 체크
    if(xhttp.readyState == 4 && xhttp.status == 200) {
      //응답 받은 데이터 
      //const responseData = JSON.parse(this.responseText)
      const responseData = this.responseText
      //html innerhtml 바꾸기
      rightDiv.innerHTML = responseData
    }
  }
  xhttp.open("POST", `/activities/htmlcss_outputs/create_feedback/${fruit_id}`, true);
  xhttp.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
  xhttp.send(formData);
}

function like(like) {
  const fruit_id  = like.closest('form').getAttribute('fruitid');
  const counts = document.getElementById('voter_counts');


  const xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function(event) {
    //데이터를 다 받았고, 응답코드 200을 받았는지 체크
    if(xhttp.readyState == 4 && xhttp.status == 200) {
      //응답 받은 데이터 
      //const responseData = JSON.parse(this.responseText)
      let result = JSON.parse(this.responseText)
      //html innerhtml 바꾸기
      alert(result.message)
      counts.innerHTML = result.counts
    }
  }
  xhttp.open("GET", `/activities/htmlcss_outputs/feedbacks/vote/${fruit_id}`, true); 
  xhttp.send();
}
