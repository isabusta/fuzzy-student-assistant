from flask import Flask, render_template, request, jsonify
from fuzzy_engine import FuzzySystem
from task_matcher import TaskMatcher

app = Flask(__name__)
system = FuzzySystem()
matcher = TaskMatcher()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.json
    inputs = {
        "tiredness": float(data["tiredness"]),
        "deadline": float(data["deadline"]),
        "understanding": float(data["understanding"]),
        "mental_sharpness": float(data["mental_sharpness"]),
        "direct_attention_fatigue": float(data["direct_attention_fatigue"]),
    }
    result = system.evaluate(inputs)
    return jsonify(result)

@app.route("/match_tasks", methods=["POST"])
def match_tasks():
    try:
        data = request.json
        mental_state = {
            "mental_sharpness": float(data["mental_sharpness"]),
            "direct_attention_fatigue": float(data["direct_attention_fatigue"]),
            "tiredness": float(data["tiredness"]),
        }
        ranked = matcher.rank_tasks(mental_state, data["tasks"])
        return jsonify({"ranked_tasks": ranked})
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
