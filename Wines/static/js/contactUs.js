function showAlertBox(message) {
    var alertBox = document.getElementById('alert-box');
    var alertMessage = document.getElementById('alert-message');
    alertMessage.innerHTML = message;
    alertBox.style.display = 'block';
  }
  
  // Function to close the alert box
  function closeAlertBox(button) {
    var alertBox = button.closest('.alert-box');
    if (alertBox) {
        alertBox.style.display = 'none';
    }
}
