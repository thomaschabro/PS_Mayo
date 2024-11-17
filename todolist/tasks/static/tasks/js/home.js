function createTask() {
  console.log("createTask");
  document.getElementById("taskModal").style.display = "block";
}

function closeModal() {
  document.getElementById("taskModal").style.display = "none";
}

function saveTask() {
  const taskTitle = document.getElementById("taskTitle").value;
  if (taskTitle) {
    console.log("Nova tarefa criada:", taskTitle);
    closeModal();
  }
}

// Função para simular o logout
function logout() {
  alert("Você foi deslogado.");
}
