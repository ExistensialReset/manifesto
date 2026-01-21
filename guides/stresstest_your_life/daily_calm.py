
# daily_calm.py
# Measures daily calm (L) in everyday life. Run once per day.

import datetime
import statistics

def log_calm():
    print("Hello! This script logs moments of calm today (from DIVINE's L).")
    print("Enter minutes spent in calm activities (e.g., walk, breathing, rest).")
    print("Relevant for Baseline – calm is a right, not a luxury.")

    activities = []
    while True:
        minutes = input("Minutes of calm today (or 'done' to finish): ")
        if minutes.lower() == 'done':
            break
        try:
            activities.append(float(minutes))
        except ValueError:
            print("Invalid input – please enter a number.")
    
    if not activities:
        print("No data today. Remember: Calm exists even if not measured (Σ reminder).")
        return
    
    total_calm = sum(activities)
    average = statistics.mean(activities)
    date = datetime.date.today()
    
    print(f"\nReport for {date}:")
    print(f"Total calm: {total_calm} minutes.")
    print(f"Average per activity: {average:.1f} minutes.")
    print("Reflection: High L supports Flow. If low, prioritize Refugium Anima for recovery. No pressure – just observation.")

if __name__ == "__main__":
    log_calm()