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
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      });
  
      const result = await response.json();
  
      document.getElementById("studyScore").textContent = result.study_score;
      document.getElementById("readinessScore").textContent = result.readiness_score;
      document.getElementById("action").textContent = result.action;

      if (document.getElementById("advice")){
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
  
      goToWindow(3);
    } catch (error) {
      document.getElementById("studyScore").textContent = "--";
      document.getElementById("readinessScore").textContent = "--";
      document.getElementById("action").textContent = "Connection error";
      if (document.getElementById("advice")){
        document.getElementById("advice").textContent = "Could not fetch advice.";
      }
      document.getElementById("rules").innerHTML = "<li>Could not connect to the Python backend.</li>";
      goToWindow(3);
    }
  }
  