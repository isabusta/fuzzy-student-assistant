let currentWindow = 0;
const totalWindows = 4;

function updateValue(id) {
  document.getElementById(id + "Value").textContent = document.getElementById(id).value;
}

function goToWindow(index) {
  document.querySelectorAll(".window").forEach((window, i) => {
    window.classList.toggle("active", i === index);
  });

  for (let i = 0; i < totalWindows; i++) {
    document.getElementById(`step-indicator-${i}`).classList.toggle("active", i === index);
  }

  currentWindow = index;

  if (index === 2) {
    fillReview();
  }
}

function nextWindow() {
  if (currentWindow < totalWindows - 1) {
    goToWindow(currentWindow + 1);
  }
}

function prevWindow() {
  if (currentWindow > 0) {
    goToWindow(currentWindow - 1);
  }
}

function fillReview() {
  document.getElementById("reviewCourses").textContent =
    document.getElementById("courses").value.trim() || "Not provided";

  document.getElementById("reviewDeadlines").textContent =
    document.getElementById("deadlines").value.trim() || "Not provided";

  document.getElementById("reviewTiredness").textContent = document.getElementById("tiredness").value;
  document.getElementById("reviewWorkload").textContent = document.getElementById("workload").value;
  document.getElementById("reviewDeadline").textContent = document.getElementById("deadline").value;
  document.getElementById("reviewUnderstanding").textContent = document.getElementById("understanding").value;
}

function resetWizard() {
  document.getElementById("courses").value = "";
  document.getElementById("deadlines").value = "";

  ["tiredness", "workload", "deadline", "understanding"].forEach(id => {
    document.getElementById(id).value = 5;
    updateValue(id);
  });

  document.getElementById("studyScore").textContent = "--";
  document.getElementById("readinessScore").textContent = "--";
  document.getElementById("action").textContent = "No result yet";
  document.getElementById("rules").innerHTML = "<li>No rules yet.</li>";

  goToWindow(0);
}

window.addEventListener("DOMContentLoaded", () => {
  ["tiredness", "workload", "deadline", "understanding"].forEach(updateValue);
});
