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
            "mental_sharpness": {
                "low": trapezoidal(x, 0, 0, 2, 4),
                "medium": triangular(x, 2, 5, 8),
                "high": trapezoidal(x, 6, 8, 10, 10),
            },
            "direct_attention_fatigue":{
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
                    "rule": rule.get("text", "Unnamed Rule"),
                    "activation": round(float(activation), 3)
                })

            for i, x in enumerate(self.domain):

                if "study" in rule["then"]:
                    study_mu = min(activation, self.output_membership(rule["then"]["study"], x))
                    study_agg[i] = max(study_agg[i], study_mu)

                if "readiness" in rule["then"]:
                    ready_mu = min(activation, self.output_membership(rule["then"]["readiness"], x))
                    readiness_agg[i] = max(readiness_agg[i], ready_mu)

        study_score = self.centroid(self.domain, study_agg)
        readiness_score = self.centroid(self.domain, readiness_agg)

        if study_score < 3.5:
            action = "Stop & Sleep"
            advice = " Your Mental Capacity is depleted. You will not retain information efficiently now. Close the books, get some sleep, and let your brain consolidate what you've already learned"
        elif study_score < 6.5:
            action = "Restorative Break"
            advice = "Your Focus Battery is low. Trying to study right now will be highly inefficient. Step away from your screen an do a indirect attention activity(strolling in nature, looking out of the window) to recover."
        else:
            action = "Study"
            advice = " Your cognitive sharpness is intact right now. Dive into your study, but limit your session to avoid depleting your directed attention."

        return {
            "study_score": round(float(study_score), 2),
            "readiness_score": round(float(readiness_score), 2),
            "action": action,
            "advice": advice,
            "fired_rules": fired_rules[:5]
        }
