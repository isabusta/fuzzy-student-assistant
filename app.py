from flask import Flask, render_template, request, jsonify
from fuzzy_engine import FuzzySystem

app = Flask(__name__)
system = FuzzySystem()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.json

    inputs = {
        "tiredness": float(data["tiredness"]),
        "workload": float(data["workload"]),
        "deadline": float(data["deadline"]),
        "understanding": float(data["understanding"]),
        "mental_sharpness": float(data["mental_sharpness"]),
        "direct_attention_fatigue": float(data["direct_attention_fatigue"]),
    }

    result = system.evaluate(inputs)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
