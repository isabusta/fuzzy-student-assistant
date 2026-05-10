RULES = [
    {
        "if": [("understanding", "high")],
        "then": {"readiness": "high"},
        "text": "IF understanding is high THEN readiness is high"
    },
    {
        "if": [("understanding", "low")],
        "then": {"readiness": "low"},
        "text": "IF understanding is low THEN readiness is low"
    },
    {
        "if": [("understanding", "medium"), ('deadline', 'far')],
        "then": {"readiness": "medium"},
        "text": "IF understanding is medium AND deadline is far THEN readiness is medium"
    },
    {
        "if": [("understanding", "medium"), ('deadline','close')],
        "then": {"readiness": "medium"},
        "text": "IF understanding is medium AND deadline is close THEN readiness is medium"
    },
    {
        "if": [("understanding", "medium"), ('deadline', 'very_close')],
        "then": {"readiness": "low"},
        "text": "IF understanding is medium and deadline is very close THEN readiness is low"
    },
    {
        "if": [("direct_attention_fatigue", "high"), ("deadline", "very_close")],
        "then": {"study": "medium"},
        "text": "IF focus battery is low AND deadline is very close THEN take a restorative break"
    },

    {
        "if": [("direct_attention_fatigue", "high"), ("deadline", "close")],
        "then": {"study": "medium"},
        "text": "IF focus battery is low AND deadline is close THEN take a restorative break"
    },

    {
        "if": [("mental_sharpness", "low"), ("deadline", "far")],
        "then": {"study": "low"},
        "text": "IF mental capacity is low AND deadline is far THEN stop and sleep"
    },
    {   "if": [("mental_sharpness", "low"), ("deadline", "close")],
        "then": {"study": "low"},
        "text": "IF mental capacity is low AND deadline is close THEN stop and sleep"
    },
    {   "if": [("mental_sharpness", "low"), ("deadline", "very_close")],
        "then": {"study": "medium"},
        "text": "IF mental capacity is low AND deadline is very close is moderate THEN stop forcing it, so light review only"
    },
    {
        "if": [("mental_sharpness", "high"), ("direct_attention_fatigue", "low")],
        "then": {"study": "high"},
        "text": "IF mental capacity is high AND focus battery is high THEN study"
    },
    {
        "if": [("mental_sharpness", "medium"), ("direct_attention_fatigue", "low")],
        "then": {"study": "high"},
        "text": "IF mental capacity is high AND focus battery is high THEN Study"
    },
    {
        "if": [("mental_sharpness", "medium"), ("direct_attention_fatigue", "medium")],
        "then": {"study": "medium"},
        "text": "IF state is average THEN do standard, paced study session"
    }

]
