function validate() {
  const contentInput = document.getElementById("content").value;
  
  
  if (!contentInput) {
    alert('답변 내용을 입력해주세요.')
    return false
  } else if (contentInput) {
    return true
  }
  return false
}

function recommend(recommend) {
  const answer_id  = document.getElementById('comment_card').getAttribute('answerid')
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
  xhttp.open("GET", `/discussions/vote/answer/${answer_id}`, true); 
  xhttp.send();
}
