# Fuzzy Student Assistant

A fuzzy logic-based decision-support tool that helps students decide whether they should study or take a break, while also estimating exam readiness.

This project was developed as a Design Science Research artifact and implements a Mamdani Fuzzy Inference System in Python. The system is designed to support study decisions under uncertainty by using vague, human-like inputs such as tiredness, workload, deadline proximity, and understanding of the material. 

You can access the web app here: https://fuzzy-student-assistant.onrender.com
## Project idea

Students often make study decisions using subjective thoughts such as:

- “I am too tired.”
- “The deadline is close.”
- “My workload is heavy.”
- “I understand the material well.”

These situations are difficult to model with crisp thresholds. Fuzzy logic makes it possible to represent them with gradual membership values and generate smoother, more interpretable recommendations.

## Goal

The goal of this project is to build an interpretable fuzzy decision-support system that:

- Recommends whether a student should study or take a break.
- Estimates exam readiness.
- Provides transparent rule-based explanations for the output. 

## Features

- Mamdani Fuzzy Inference System implementation in Python. 
- Linguistic input variables with triangular and trapezoidal membership functions. 
- Human-readable fuzzy rule base.
- Centroid defuzzification. 
- Simple user interface for entering input values and viewing results.
- Explanation panel showing activated rules. 

## Inputs

The current core model uses four input variables:

1. **Tiredness**: low, medium, high.
2. **Workload**: light, moderate, heavy. 
3. **Deadline proximity**: far, close, very close.
4. **Understanding of material**: low, medium, high.
5. **Mental sharpness**: low, medium, high.
6. **Direct attention fatigue**: low, medium, high.

## Outputs

The system produces two main outputs:

1. **Study recommendation** on a scale from 0 to 10, ranging from taking a break to strongly studying.
2. **Exam readiness**, represented using fuzzy levels such as low, medium, and high. 

Depending on the interface version, the result may also be shown as a suggested action such as:

- Take a restorative break
- Sleep
- Focused study session

## Method

The project uses a **single Mamdani Fuzzy Inference System**, which was chosen to keep the artifact manageable while still demonstrating core fuzzy reasoning principles. 

Main components:

- Fuzzification of input values using membership functions. 
- Rule evaluation using interpretable IF-THEN rules.
- Aggregation of rule outputs.
- Defuzzification using the centroid method. 

Example fuzzy rules include:

- IF Directed Attention Fatigue is High AND Task Urgency is high THEN Take a Restorative Break
- IF mental sharpness is Low AND deadline is Far THEN Stop and Sleep"
- IF mental sharpness is Low AND deadline is Far THEN Stop and Sleep"
- IF mental sharpness is Low AND deadline is Far THEN Stop and Sleep"
- IF mental sharpness is Low AND deadline is Far THEN Stop and Sleep"

## Project structure

A typical structure for this project is:

```text
fuzzy-student-assistant/
├── app.py
├── fuzzy_engine.py
├── membership.py
├── rules.py
├── scenarios.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
