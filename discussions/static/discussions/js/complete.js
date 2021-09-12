function closeAndReload() {
  window.opener.location.reload();
  window.close();
  return false; 
}