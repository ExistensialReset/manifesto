# everyday_resilience.py
# Logs everyday resilience (R) – adapting to small challenges.

import datetime
import statistics

def log_resilience():
    print("Hello! This script logs resilience (R from DIVINE) in daily life.")
    print("Enter how you adapted to challenges (e.g., 'Missed bus – walked instead, felt stronger').")
    
    adaptations = []
    scores = []  # Self-assessed 1–10 after adaptation
    while True:
        challenge = input("Describe a challenge and adaptation (or 'done'): ")
        if challenge.lower() == 'done':
            break
        adaptations.append(challenge)
        score_input = input("How resilient did you feel afterward? (1-10, 10 = very resilient): ")
        try:
            scores.append(float(score_input))
        except ValueError:
            print("Skipped score.")

    if not adaptations:
        print("No challenges today. Resilience grows in small moments (from ECOLOGICAL_STEWARDSHIP.md).")
        return
    
    average_score = statistics.mean(scores) if scores else 0
    date = datetime.date.today()
    
    print(f"\nReport for {date}:")
    print(f"Number of adaptations: {len(adaptations)}")
    print(f"Average resilience score: {average_score:.1f}/10")
    print("Your adaptations:")
    for i, desc in enumerate(adaptations, 1):
        print(f"{i}. {desc}")
    
    print("Reflection: R is about transformation, not endurance. If low, prioritize EV (Everlasting Wisdom) for support.")

if __name__ == "__main__":
    log_resilience()