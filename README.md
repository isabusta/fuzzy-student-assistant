# Fuzzy Student Assistant

A fuzzy logic-based decision-support tool that helps students decide whether they should study or take a break, while also estimating exam readiness.

This project was developed as a Design Science Research artifact and implements a Mamdani Fuzzy Inference System in Python. The system is designed to support study decisions under uncertainty by using vague, human-like inputs such as tiredness, workload, deadline proximity, and understanding of the material. [file:2]

## Project idea

Students often make study decisions using subjective thoughts such as:

- “I am too tired.”
- “The deadline is close.”
- “My workload is heavy.”
- “I understand the material well.”

These situations are difficult to model with crisp thresholds. Fuzzy logic makes it possible to represent them with gradual membership values and generate smoother, more interpretable recommendations. [file:2]

## Goal

The goal of this project is to build an interpretable fuzzy decision-support system that:

- Recommends whether a student should study or take a break.
- Estimates exam readiness.
- Provides transparent rule-based explanations for the output. [file:2]

## Features

- Mamdani Fuzzy Inference System implementation in Python. [file:2]
- Linguistic input variables with triangular and trapezoidal membership functions. [file:2]
- Human-readable fuzzy rule base. [file:2]
- Centroid defuzzification. [file:2]
- Simple user interface for entering input values and viewing results. [file:2]
- Explanation panel showing activated rules. [file:2]

## Inputs

The current core model uses four input variables:

1. **Tiredness**: low, medium, high. [file:2]
2. **Workload**: light, moderate, heavy. [file:2]
3. **Deadline proximity**: far, close, very close. [file:2]
4. **Understanding of material**: low, medium, high. [file:2]

## Outputs

The system produces two main outputs:

1. **Study recommendation** on a scale from 0 to 10, ranging from taking a break to strongly studying. [file:2]
2. **Exam readiness**, represented using fuzzy levels such as low, medium, and high. [file:2]

Depending on the interface version, the result may also be shown as a suggested action such as:

- Take a restorative break
- Light study / review
- Focused study session

## Method

The project uses a **single Mamdani Fuzzy Inference System**, which was chosen to keep the artifact manageable while still demonstrating core fuzzy reasoning principles. [file:2]

Main components:

- Fuzzification of input values using membership functions. [file:2]
- Rule evaluation using interpretable IF-THEN rules. [file:2]
- Aggregation of rule outputs.
- Defuzzification using the centroid method. [file:2]

Example fuzzy rules include:

- IF deadline is very close AND understanding is low THEN recommendation is strongly study. [file:2]
- IF tiredness is high AND deadline is far THEN recommendation is take a break. [file:2]
- IF understanding is high AND workload is light THEN readiness is high. [file:2]

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
