function validate() {
  const titleInput = document.getElementById("title").value;
  const categoryInput = document.getElementById("selectCategory").value;
  const contentInput  = document.getElementById("content").value;
  
  if (!titleInput) {
    alert('제목은 필수 항목입니다.')
    return false
  } else if (!categoryInput) {
    alert('질문 카테고리를 선택해주세요.')
    return false
  } else if (!contentInput) {
    alert('질문할 내용을 작성해주세요.')
    return false
  } else if (titleInput && contentInput && categoryInput) {
    alert('질문을 등록하셨습니다!')
    return true
  }
  return false
}