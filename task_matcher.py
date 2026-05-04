import numpy as np
from membership import triangular, trapezoidal

# Variables
# Mental state (from Step 2): mental_sharpness, direct_attention_fatigue, tiredness
# Task properties: cognitive_load, urgency, clarity, interest
#
# Theoretical grounding:
#   cognitive_load  — Cognitive Load Theory (Sweller 1988): intrinsic demand of the task
#   urgency         — time management / deadline pressure
#   clarity         — Goal-Setting Theory (Locke & Latham 1990): vague tasks add extraneous load
#   interest        — Self-Determination Theory (Ryan & Deci 2000): intrinsic motivation sustains attention

TASK_RULES = [
    # --- Cognitive fit: mental state x cognitive load ---
    {
        "if": [("mental_sharpness", "high"), ("direct_attention_fatigue", "low"), ("cognitive_load", "high")],
        "then": "high",
        "text": "IF Mentally Sharp AND Fresh AND Task is Demanding THEN excellent fit"
    },
    {
        "if": [("mental_sharpness", "high"), ("direct_attention_fatigue", "low"), ("cognitive_load", "medium")],
        "then": "high",
        "text": "IF Mentally Sharp AND Fresh AND Task is Moderate THEN excellent fit"
    },
    {
        "if": [("mental_sharpness", "medium"), ("direct_attention_fatigue", "low"), ("cognitive_load", "high")],
        "then": "medium",
        "text": "IF Moderately Sharp AND Fresh AND Task is Demanding THEN moderate fit"
    },
    {
        "if": [("mental_sharpness", "medium"), ("direct_attention_fatigue", "medium"), ("cognitive_load", "medium")],
        "then": "medium",
        "text": "IF Average State AND Task is Moderate THEN moderate fit"
    },
    {
        "if": [("mental_sharpness", "medium"), ("cognitive_load", "low")],
        "then": "high",
        "text": "IF Moderately Sharp AND Task is Easy THEN good fit"
    },
    {
        "if": [("mental_sharpness", "low"), ("cognitive_load", "high")],
        "then": "low",
        "text": "IF Mental Sharpness is Low AND Task is Demanding THEN poor fit"
    },
    {
        "if": [("mental_sharpness", "low"), ("cognitive_load", "medium")],
        "then": "low",
        "text": "IF Mental Sharpness is Low AND Task is Moderate THEN poor fit"
    },
    {
        "if": [("mental_sharpness", "low"), ("cognitive_load", "low")],
        "then": "medium",
        "text": "IF Mental Sharpness is Low AND Task is Easy THEN acceptable fit"
    },
    # --- Directed attention fatigue x cognitive load (ART) ---
    {
        "if": [("direct_attention_fatigue", "high"), ("cognitive_load", "high")],
        "then": "low",
        "text": "IF Attention Fatigue is High AND Task is Demanding THEN poor fit (ART)"
    },
    {
        "if": [("direct_attention_fatigue", "high"), ("cognitive_load", "medium")],
        "then": "low",
        "text": "IF Attention Fatigue is High AND Task is Moderate THEN poor fit (ART)"
    },
    {
        "if": [("direct_attention_fatigue", "high"), ("cognitive_load", "low"), ("clarity", "high")],
        "then": "medium",
        "text": "IF Fatigued BUT Task is Easy AND Clear THEN acceptable fit"
    },
    # --- Clarity rules (Goal-Setting Theory) ---
    {
        "if": [("direct_attention_fatigue", "high"), ("clarity", "low")],
        "then": "low",
        "text": "IF Fatigued AND Task is Vague THEN poor fit — vague tasks drain extra attention"
    },
    {
        "if": [("mental_sharpness", "low"), ("clarity", "low")],
        "then": "low",
        "text": "IF Mental Sharpness Low AND Task is Vague THEN poor fit — structuring unclear tasks needs cognitive resources"
    },
    {
        "if": [("clarity", "high"), ("cognitive_load", "low")],
        "then": "high",
        "text": "IF Task is Clear AND Easy THEN strong fit regardless of state"
    },
    {
        "if": [("clarity", "high"), ("direct_attention_fatigue", "low")],
        "then": "high",
        "text": "IF Task is Clear AND Attention is Fresh THEN strong fit"
    },
    # --- Tiredness x cognitive load ---
    {
        "if": [("tiredness", "high"), ("cognitive_load", "high")],
        "then": "low",
        "text": "IF Tired AND Task is Demanding THEN poor fit"
    },
    {
        "if": [("tiredness", "high"), ("cognitive_load", "medium")],
        "then": "low",
        "text": "IF Tired AND Task is Moderate THEN poor fit"
    },
    {
        "if": [("tiredness", "high"), ("cognitive_load", "low"), ("clarity", "high")],
        "then": "medium",
        "text": "IF Tired BUT Task is Easy AND Clear THEN acceptable fit"
    },
    # --- Interest rules (Self-Determination Theory) ---
    {
        "if": [("interest", "high"), ("mental_sharpness", "medium")],
        "then": "high",
        "text": "IF High Interest AND Moderately Sharp THEN motivation boosts fit (SDT)"
    },
    {
        "if": [("interest", "high"), ("direct_attention_fatigue", "medium")],
        "then": "medium",
        "text": "IF High Interest THEN partially compensates for fatigue (SDT)"
    },
    {
        "if": [("interest", "low"), ("urgency", "low")],
        "then": "low",
        "text": "IF Low Interest AND No Urgency THEN procrastination risk — poor fit"
    },
    # --- Urgency override rules ---
    {
        "if": [("urgency", "high"), ("clarity", "high")],
        "then": "high",
        "text": "IF Urgent AND Clear THEN prioritize now"
    },
    {
        "if": [("urgency", "high"), ("cognitive_load", "low")],
        "then": "high",
        "text": "IF Urgent AND Easy THEN do it now"
    },
    {
        "if": [("urgency", "high"), ("mental_sharpness", "low")],
        "then": "medium",
        "text": "IF Urgent even if not sharp THEN still prioritize"
    },
]


class TaskMatcher:
    def __init__(self):
        self.domain = np.linspace(0, 10, 201)

    def fuzzify(self, name, x):
        sets = {
            "mental_sharpness": {
                "low": trapezoidal(x, 0, 0, 2, 4),
                "medium": triangular(x, 2, 5, 8),
                "high": trapezoidal(x, 6, 8, 10, 10),
            },
            "direct_attention_fatigue": {
                "low": trapezoidal(x, 0, 0, 2, 4),
                "medium": triangular(x, 2, 5, 8),
                "high": trapezoidal(x, 6, 8, 10, 10),
            },
            "tiredness": {
                "low": trapezoidal(x, 0, 0, 2, 4),
                "medium": triangular(x, 2, 5, 8),
                "high": trapezoidal(x, 6, 8, 10, 10),
            },
            "cognitive_load": {
                "low": trapezoidal(x, 0, 0, 2, 4),
                "medium": triangular(x, 2, 5, 8),
                "high": trapezoidal(x, 6, 8, 10, 10),
            },
            "urgency": {
                "low": trapezoidal(x, 0, 0, 2, 4),
                "medium": triangular(x, 2, 5, 8),
                "high": trapezoidal(x, 6, 8, 10, 10),
            },
            "clarity": {
                "low": trapezoidal(x, 0, 0, 2, 4),
                "medium": triangular(x, 2, 5, 8),
                "high": trapezoidal(x, 6, 8, 10, 10),
            },
            "interest": {
                "low": trapezoidal(x, 0, 0, 2, 4),
                "medium": triangular(x, 2, 5, 8),
                "high": trapezoidal(x, 6, 8, 10, 10),
            },
        }
        return sets[name]

    def output_membership(self, label, x):
        return {
            "low": trapezoidal(x, 0, 0, 2, 4),
            "medium": triangular(x, 3, 5, 7),
            "high": trapezoidal(x, 6, 8, 10, 10),
        }[label]

    def centroid(self, x, mu):
        total = np.sum(mu)
        if total == 0:
            return 0.0
        return np.sum(x * mu) / total

    def score_task(self, mental_state, task_props):
        all_inputs = {**mental_state, **task_props}
        fuzzified = {k: self.fuzzify(k, v) for k, v in all_inputs.items()}

        agg = np.zeros_like(self.domain)
        fired_rules = []

        for rule in TASK_RULES:
            if not all(var in fuzzified for var, _ in rule["if"]):
                continue
            activation = min(fuzzified[var][label] for var, label in rule["if"])
            if activation > 0:
                fired_rules.append({
                    "rule": rule["text"],
                    "activation": round(float(activation), 3)
                })
            for i, x in enumerate(self.domain):
                mu = min(activation, self.output_membership(rule["then"], x))
                agg[i] = max(agg[i], mu)

        score = self.centroid(self.domain, agg)
        return round(float(score) * 10, 1), fired_rules[:3]

    def rank_tasks(self, mental_state, tasks):
        scored = []
        for task in tasks:
            task_props = {
                "cognitive_load": float(task["cognitive_load"]),
                "urgency": float(task["urgency"]),
                "clarity": float(task["clarity"]),
                "interest": float(task["interest"]),
            }
            score, fired = self.score_task(mental_state, task_props)
            scored.append({
                "name": task["name"],
                "match_score": score,
                "fired_rules": fired,
            })
        scored.sort(key=lambda t: t["match_score"], reverse=True)
        for i, t in enumerate(scored):
            t["rank"] = i + 1
        return scored
