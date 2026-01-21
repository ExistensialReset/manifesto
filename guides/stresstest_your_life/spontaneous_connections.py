# spontaneous_connections.py
# Logs spontaneous connections (S × I) in everyday life.

import datetime

def log_connections():
    print("Hello! This script captures spontaneous moments today (S × I from DIVINE).")
    print("Enter brief descriptions of unexpected moments (e.g., 'Talked with a neighbor and got a new idea').")
    
    connections = []
    while True:
        entry = input("Describe a spontaneous moment (or 'done'): ")
        if entry.lower() == 'done':
            break
        connections.append(entry)
    
    count = len(connections)
    date = datetime.date.today()
    
    print(f"\nReport for {date}:")
    print(f"Number of spontaneous moments: {count}")
    if connections:
        print("Your moments:")
        for i, desc in enumerate(connections, 1):
            print(f"{i}. {desc}")
    else:
        print("None today. Remember: Σ does not appear on command. Let it flow naturally.")
    
    print("Reflection: High S × I strengthens cultural sustainability. Share if you wish – no pressure.")

if __name__ == "__main__":
    log_connections()