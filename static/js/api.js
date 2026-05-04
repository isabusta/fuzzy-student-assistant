async function runAndOpenResults() {
  const payload = {
    tiredness: document.getElementById("tiredness").value,
    workload: document.getElementById("workload").value,
    deadline: document.getElementById("deadline").value,
    mental_sharpness: document.getElementById("mental_sharpness").value,
    direct_attention_fatigue: document.getElementById("direct_attention_fatigue").value,
    understanding: document.getElementById("understanding").value,
    courses: document.getElementById("courses").value,
    deadlines: document.getElementById("deadlines").value
  };

  try {
    const response = await fetch("/evaluate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const result = await response.json();

    document.getElementById("studyScore").textContent = result.study_score;
    document.getElementById("readinessScore").textContent = result.readiness_score;
    document.getElementById("action").textContent = result.action;

    if (document.getElementById("advice")) {
      document.getElementById("advice").textContent = result.advice;
    }

    const rulesList = document.getElementById("rules");
    rulesList.innerHTML = "";
    if (result.fired_rules && result.fired_rules.length > 0) {
      result.fired_rules.forEach(r => {
        const li = document.createElement("li");
        li.textContent = `${r.rule} (activation: ${r.activation})`;
        rulesList.appendChild(li);
      });
    } else {
      rulesList.innerHTML = "<li>No rules fired strongly enough to display.</li>";
    }

    // Show task planner only when the recommendation is Study
    const taskPlanner = document.getElementById("task-planner");
    const restMessage = document.getElementById("rest-message");

    if (result.action === "Study") {
      taskPlanner.style.display = "block";
      restMessage.style.display = "none";
    } else {
      taskPlanner.style.display = "none";
      restMessage.style.display = "block";
      const notes = {
        "Stop & Sleep": "Rest first — your brain cannot encode new information effectively right now. Task planning can wait until after you sleep.",
        "Restorative Break": "Take a break first — step away from your screen and let your directed attention recover. Come back to task planning when you feel ready."
      };
      document.getElementById("rest-note-text").textContent = notes[result.action] || "";
    }

    goToWindow(3);
  } catch (error) {
    document.getElementById("studyScore").textContent = "--";
    document.getElementById("readinessScore").textContent = "--";
    document.getElementById("action").textContent = "Connection error";
    if (document.getElementById("advice")) {
      document.getElementById("advice").textContent = "Could not fetch advice.";
    }
    document.getElementById("rules").innerHTML = "<li>Could not connect to the Python backend.</li>";
    goToWindow(3);
  }
}

async function rankTasks() {
  const tasks = getTasks();
  if (tasks.length === 0) {
    alert("Add at least one task before ranking.");
    return;
  }

  const payload = {
    mental_sharpness: document.getElementById("mental_sharpness").value,
    direct_attention_fatigue: document.getElementById("direct_attention_fatigue").value,
    tiredness: document.getElementById("tiredness").value,
    tasks
  };

  try {
    const response = await fetch("/match_tasks", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const result = await response.json();
    const rankingList = document.getElementById("task-ranking");
    rankingList.innerHTML = "";

    result.ranked_tasks.forEach(t => {
      const li = document.createElement("li");
      li.className = "task-rank-item";

      const header = document.createElement("div");
      header.className = "task-rank-header";
      header.innerHTML = `
        <span class="rank-badge">#${t.rank}</span>
        <strong>${t.name}</strong>
        <span class="match-score">${t.match_score}%</span>
      `;
      li.appendChild(header);

      if (t.fired_rules.length > 0) {
        const sub = document.createElement("ul");
        sub.className = "sub-rules";
        t.fired_rules.forEach(r => {
          const rli = document.createElement("li");
          rli.textContent = `${r.rule} (activation: ${r.activation})`;
          sub.appendChild(rli);
        });
        li.appendChild(sub);
      }

      rankingList.appendChild(li);
    });

    document.getElementById("task-ranking-card").style.display = "block";
  } catch (error) {
    console.error("Task ranking failed:", error);
    alert("Task ranking failed — check that Flask is running and restart it if you just made code changes.");
  }
}
