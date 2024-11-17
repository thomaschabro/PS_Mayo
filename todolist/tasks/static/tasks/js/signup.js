function checkLogin() {
  var login = document.getElementById("login").value;

  if (login.length < 3) {
    createLoginError("Login must be at least 3 characters long.");
  } else if (login.length > 20) {
    createLoginError("Login must be at most 20 characters long.");
  } else if (login.includes(" ")) {
    createLoginError("Login cannot contain spaces.");
  } else if (login.includes("@")) {
    // Check if the login as email is valid
    if (!validateEmail(login)) {
      createLoginError("Invalid email address.");
    }
  } else {
    // Remove the error message if it exists
    var errorElement = document.getElementById("loginError");
    if (errorElement) {
      errorElement.remove();
    }
  }
}

function checkPassword() {
  var password = document.getElementById("pswd").value;

  if (password.length < 6) {
    createPswdError("Password must be at least 6 characters long.");
  } else if (password.length > 20) {
    createPswdError("Password must be at most 20 characters long.");
  } else if (password.includes(" ")) {
    createPswdError("Password cannot contain spaces.");
  } else {
    // Remove the error message if it exists
    var errorElement = document.getElementById("pswdError");
    if (errorElement) {
      errorElement.remove();
    }
  }
}

function checkPasswordConfirmation() {
  var pswd = document.getElementById("pswd").value;
  var pswdConfirmation = document.getElementById("pswdConfirmation").value;

  if (pswd !== pswdConfirmation) {
    console.log("Passwords are not the same");
    createPswdsMatchError("Passwords must be the same.");
  } else {
    // Remove the error message if it exists
    var errorElement = document.getElementById("pswdMatchError");
    if (errorElement) {
      errorElement.remove();
    }
  }
}

function createLoginError(message) {
  // Check if the error message already exists
  var errorElement = document.getElementById("loginError");
  if (errorElement) {
    // Update the error message
    errorElement.innerHTML = message;
    return;
  }

  var loginElement = document.getElementById("login");
  // Create a new element under it to display the error message
  var errorElement = document.createElement("p");
  errorElement.innerHTML = message;
  errorElement.style.color = "red";
  // Change font size
  errorElement.style.fontSize = "0.8em";
  errorElement.style.marginBottom = "1em";
  errorElement.id = "loginError";
  // Insert the new element after the login element
  loginElement.parentNode.insertBefore(errorElement, loginElement.nextSibling);
}

function createPswdError(message) {
  // Check if the error message already exists
  var errorElement = document.getElementById("pswdError");
  if (errorElement) {
    // Update the error message
    errorElement.innerHTML = message;
    return;
  }

  var pswdElement = document.getElementById("pswd");
  // Create a new element under it to display the error message
  var errorElement = document.createElement("p");
  errorElement.innerHTML = message;
  errorElement.style.color = "red";
  // Change font size
  errorElement.style.fontSize = "0.8em";
  errorElement.style.marginBottom = "1em";
  errorElement.id = "pswdError";
  // Insert the new element after the login element
  pswdElement.parentNode.insertBefore(errorElement, pswdElement.nextSibling);
}

function createPswdsMatchError() {
  // Check if the error message already exists
  var errorElement = document.getElementById("pswdMatchError");
  if (errorElement) {
    return;
  }

  var pswdElement = document.getElementById("pswdConfirmation");
  // Create a new element under it to display the error message
  var errorElement = document.createElement("p");
  errorElement.innerHTML = "Passwords must be the same.";
  errorElement.style.color = "red";
  // Change font size
  errorElement.style.fontSize = "0.8em";
  errorElement.style.marginBottom = "1em";
  errorElement.id = "pswdMatchError";
  // Insert the new element after the login element
  pswdElement.parentNode.insertBefore(errorElement, pswdElement.nextSibling);
}

function validateEmail(email) {
  var re = /\S+@\S+\.\S+/;
  return re.test(email);
}
