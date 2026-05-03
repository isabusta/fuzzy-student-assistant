RULES = [
    #{
    #    "if": [("deadline", "very_close"), ("understanding", "low")],
    #    "then": {"study": "high", "readiness": "low"},
    #   "text": "IF deadline is very close AND understanding is low THEN study strongly"
    #},
    #{
    #    "if": [("tiredness", "high"), ("deadline", "far")],
    #   "then": {"study": "low", "readiness": "medium"},
    #    "text": "IF tiredness is high AND deadline is far THEN take a break"
    #},
    #{
    #   "if": [("understanding", "high"), ("workload", "light")],
    #    "then": {"study": "medium", "readiness": "high"},
    #    "text": "IF understanding is high AND workload is light THEN readiness is high"
    #}
    {
        "if": [("direct_attention_fatigue", "high"), ("deadline", "very_close")],
        "then": {"study": "medium", "readiness": "medium"},
        "text": "IF Directed Attention Fatigue is High AND Deadline is Very Close THEN Take a Restorative Break"
    },

    {
        "if": [("direct_attention_fatigue", "high"), ("deadline", "close")],
        "then": {"study": "medium", "readiness": "medium"},
        "text": "IF Directed Attention Fatigue is High AND Deadline is Close THEN Take a Restorative Break"
    },

    {
        "if": [("mental_sharpness", "low"), ("deadline", "far")],
        "then": {"study": "low", "readiness": "low"},
        "text": "IF mental sharpness is Low AND deadline is Far THEN Stop and Sleep"
    },
    {   "if": [("mental_sharpness", "low"), ("deadline", "close")],
        "then": {"study": "low", "readiness": "low"},
        "text": "IF Mental Sharpness is Low AND Deadline is Close THEN Stop and Sleep"
    },
    {   "if": [("mental_sharpness", "low"), ("deadline", "very_close")],
        "then": {"study": "medium", "readiness": "low"},
        "text": "IF Mental Sharpness is Low AND Deadline is Very Close is moderate THEN Stop forcing it, so light review only"
    },
    {
        "if": [("mental_sharpness", "high"), ("direct_attention_fatigue", "low")],
        "then": {"study": "high", "readiness": "high"},
        "text": "IF Mental Sharpness is High AND Directed Attention Fatigue is Low THEN Study"
    },
    {
        "if": [("mental_sharpness", "medium"), ("direct_attention_fatigue", "low")],
        "then": {"study": "high", "readiness": "medium"},
        "text": "IF Mental Sharpness is High AND Directed Attention Fatigue is Low THEN Study"
    },
    {
        "if": [("mental_sharpness", "medium"), ("direct_attention_fatigue", "medium")],
        "then": {"study": "medium", "readiness": "medium"},
        "text": "IF State is average THEN do standard, paced study session"
    }

]
