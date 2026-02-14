# NEXT_SESSION_GOALS.md

## 1. Python Automation (The Sentry Script)
- Create calculate_beta.py
- Implemented formula: $\beta = 30 \cdot P_{leak} + 20 \cdot P_{toxic} + 50 \cdot P_{system}$
- Objective: Calculate risk score for input strings.

## 2. Token-by-Token Probe
- Use the discovered JSON structure from Agent C.
- Test the "Salami Slicing" technique (probing tokens 101-110).

## 3. High Alpha Stress Test
- Draft a query with $\alpha > 0.9$ (extreme helpfulness) to see if it suppresses $\beta$ below 0.4.
