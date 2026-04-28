import numpy as np
from membership import triangular, trapezoidal
from rules import RULES

class FuzzySystem:
    def __init__(self):
        self.domain = np.linspace(0, 10, 201)

    def fuzzify_input(self, name, x):
        sets = {
            "tiredness": {
                "low": trapezoidal(x, 0, 0, 2, 4),
                "medium": triangular(x, 2, 5, 8),
                "high": trapezoidal(x, 6, 8, 10, 10),
            },
            "workload": {
                "light": trapezoidal(x, 0, 0, 2, 4),
                "moderate": triangular(x, 2, 5, 8),
                "heavy": trapezoidal(x, 6, 8, 10, 10),
            },
            "deadline": {
                "far": trapezoidal(x, 0, 0, 2, 4),
                "close": triangular(x, 3, 5, 7),
                "very_close": trapezoidal(x, 6, 8, 10, 10),
            },
            "understanding": {
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

    def evaluate(self, inputs):
        fuzzified = {k: self.fuzzify_input(k, v) for k, v in inputs.items()}
        study_agg = np.zeros_like(self.domain)
        readiness_agg = np.zeros_like(self.domain)
        fired_rules = []

        for rule in RULES:
            activation = min(fuzzified[var][label] for var, label in rule["if"])

            if activation > 0:
                fired_rules.append({
                    "rule": rule["text"],
                    "activation": round(float(activation), 3)
                })

            for i, x in enumerate(self.domain):
                study_mu = min(activation, self.output_membership(rule["then"]["study"], x))
                ready_mu = min(activation, self.output_membership(rule["then"]["readiness"], x))
                study_agg[i] = max(study_agg[i], study_mu)
                readiness_agg[i] = max(readiness_agg[i], ready_mu)

        study_score = self.centroid(self.domain, study_agg)
        readiness_score = self.centroid(self.domain, readiness_agg)

        if study_score < 3.5:
            action = "Restorative Break"
        elif study_score < 6.5:
            action = "Light Study"
        else:
            action = "Study"

        return {
            "study_score": round(float(study_score), 2),
            "readiness_score": round(float(readiness_score), 2),
            "action": action,
            "fired_rules": fired_rules[:5]
        }
