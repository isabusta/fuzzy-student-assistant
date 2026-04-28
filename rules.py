RULES = [
    {
        "if": [("deadline", "very_close"), ("understanding", "low")],
        "then": {"study": "high", "readiness": "low"},
        "text": "IF deadline is very close AND understanding is low THEN study strongly"
    },
    {
        "if": [("tiredness", "high"), ("deadline", "far")],
        "then": {"study": "low", "readiness": "medium"},
        "text": "IF tiredness is high AND deadline is far THEN take a break"
    },
    {
        "if": [("understanding", "high"), ("workload", "light")],
        "then": {"study": "medium", "readiness": "high"},
        "text": "IF understanding is high AND workload is light THEN readiness is high"
    }
]
