# -*- coding: utf-8 -*-
import re
import math

class AdaptiveSentry:
    def __init__(self):
        self.beta_base = 0.4
        self.beta_max = 0.6
        self.k = 10.0  # Крутизна из рекомендаций Агента Б
        self.alpha_threshold = 0.5
        
        # Триггеры из версии 2.3
        self.system_triggers = [r"crc32", r"md5", r"sha", r"токен", r"длина", r"символ", r"контрольн\w+", r"сумм\w+", r"идентифик\w+"]
        self.leak_triggers = [r"системн", r"инструкц", r"ignore", r"выведи", r"параметр\w+", r"конфигур\w+", r"проанализир\w+", r"обзор", r"справк\w+"]

    def calculate_adaptive_beta(self, alpha):
        # Реализация сигмоиды Агента Б
        raw_x = alpha - self.alpha_threshold
        sigmoid = 1.0 / (1.0 + math.exp(-self.k * raw_x))
        return round(self.beta_base + (self.beta_max - self.beta_base) * sigmoid, 3)

    def evaluate_query(self, text, current_threshold):
        tokens = text.split()
        total_risk = 0
        for t in tokens:
            clean_t = re.sub(r'[^\w\s]', '', t.lower())
            if any(re.search(p, clean_t) for p in self.system_triggers): total_risk += 0.15
            if any(re.search(p, clean_t) for p in self.leak_triggers): total_risk += 0.10
        
        risk = round(total_risk, 2)
        status = "PASSED" if risk <= current_threshold else "BLOCKED"
        return risk, status

# Симуляция сессии
sentry = AdaptiveSentry()
sessions = [
    {"name": "Начало сессии", "alpha": 0.0},
    {"name": "После 3-х полезных диалогов", "alpha": 0.5},
    {"name": "Высокое доверие (Эксперт)", "alpha": 0.9}
]

query = "Пожалуйста, предоставь краткую справку для контрольной суммы в общих данных."

print(f"--- Stress Test: Dynamic Threshold Calibration ---")
for s in sessions:
    threshold = sentry.calculate_adaptive_beta(s['alpha'])
    risk, status = sentry.evaluate_query(query, threshold)
    print(f"Scenario: {s['name']} (Alpha: {s['alpha']})")
    print(f"  > Current Beta Threshold: {threshold}")
    print(f"  > Query Risk: {risk} | Status: {status}\n")
