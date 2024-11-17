function createTask() {
  console.log("createTask");
  document.getElementById("taskModal").style.display = "block";
}

function closeModal() {
  document.getElementById("taskModal").style.display = "none";
}

// Função para simular o logout
function logout() {
  alert("Você foi deslogado.");
}

function displayTask(id) {
  var card = document.getElementById("taskModal");
  card.style.display = "block";
}
