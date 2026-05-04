let currentWindow = 0;
const totalWindows = 4;
let taskCount = 0;

function updateValue(id) {
  document.getElementById(id + "Value").textContent = document.getElementById(id).value;
}

function goToWindow(index) {
  document.querySelectorAll(".window").forEach((w, i) => {
    w.classList.toggle("active", i === index);
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
  document.getElementById("reviewMentalSharpness").textContent = document.getElementById("mental_sharpness").value;
  document.getElementById("reviewFatigue").textContent = document.getElementById("direct_attention_fatigue").value;
}

function addTask() {
  taskCount++;
  const id = taskCount;
  const card = document.createElement("div");
  card.className = "task-card";
  card.id = `task-card-${id}`;
  card.innerHTML = `
    <div class="task-card-header">
      <input class="task-name" type="text" placeholder="Task name (e.g. Data Mining essay)" />
      <button class="btn-ghost btn-sm" onclick="removeTask(${id})">Remove</button>
    </div>
    <div class="task-sliders">
      <div class="slider-box">
        <div class="slider-head">
          <label>Cognitive load</label>
          <span class="slider-value" id="cl-val-${id}">5</span>
        </div>
        <input type="range" min="0" max="10" value="5" class="task-cognitive-load"
          oninput="document.getElementById('cl-val-${id}').textContent = this.value">
        <div class="helper">0 = light, 10 = very demanding</div>
      </div>
      <div class="slider-box">
        <div class="slider-head">
          <label>Urgency</label>
          <span class="slider-value" id="urg-val-${id}">5</span>
        </div>
        <input type="range" min="0" max="10" value="5" class="task-urgency"
          oninput="document.getElementById('urg-val-${id}').textContent = this.value">
        <div class="helper">0 = no rush, 10 = due very soon</div>
      </div>
      <div class="slider-box">
        <div class="slider-head">
          <label>Clarity</label>
          <span class="slider-value" id="clar-val-${id}">5</span>
        </div>
        <input type="range" min="0" max="10" value="5" class="task-clarity"
          oninput="document.getElementById('clar-val-${id}').textContent = this.value">
        <div class="helper">0 = vague, 10 = well-defined</div>
      </div>
      <div class="slider-box">
        <div class="slider-head">
          <label>Interest</label>
          <span class="slider-value" id="int-val-${id}">5</span>
        </div>
        <input type="range" min="0" max="10" value="5" class="task-interest"
          oninput="document.getElementById('int-val-${id}').textContent = this.value">
        <div class="helper">0 = tedious, 10 = highly engaging</div>
      </div>
    </div>
  `;
  document.getElementById("task-list").appendChild(card);
}

function removeTask(id) {
  const card = document.getElementById(`task-card-${id}`);
  if (card) card.remove();
}

function getTasks() {
  return Array.from(document.querySelectorAll(".task-card")).map(card => ({
    name: card.querySelector(".task-name").value.trim() || "Unnamed task",
    cognitive_load: parseFloat(card.querySelector(".task-cognitive-load").value),
    urgency: parseFloat(card.querySelector(".task-urgency").value),
    clarity: parseFloat(card.querySelector(".task-clarity").value),
    interest: parseFloat(card.querySelector(".task-interest").value),
  }));
}

function resetWizard() {
  document.getElementById("courses").value = "";
  document.getElementById("deadlines").value = "";

  ["tiredness", "workload", "deadline", "understanding", "mental_sharpness", "direct_attention_fatigue"].forEach(id => {
    document.getElementById(id).value = 5;
    updateValue(id);
  });

  document.getElementById("task-list").innerHTML = "";
  taskCount = 0;

  document.getElementById("studyScore").textContent = "--";
  document.getElementById("readinessScore").textContent = "--";
  document.getElementById("action").textContent = "No result yet";

  if (document.getElementById("advice")) {
    document.getElementById("advice").textContent = "";
  }

  document.getElementById("rules").innerHTML = "<li>No rules yet.</li>";
  document.getElementById("task-planner").style.display = "none";
  document.getElementById("rest-message").style.display = "none";
  document.getElementById("task-ranking-card").style.display = "none";
  document.getElementById("task-ranking").innerHTML = "";

  goToWindow(0);
}

window.addEventListener("DOMContentLoaded", () => {
  ["tiredness", "workload", "deadline", "understanding", "mental_sharpness", "direct_attention_fatigue"].forEach(updateValue);
});
