import numpy as np

# BEAUTY INDEX & AESTHETIC POTENTIAL SIMULATOR
# Modellerar hur mycket vackrare världen blir genom Flow
# Baserat på formeln: Beauty = L * S * I * F * (1 + EcoFactor)

def simulate_beauty():
    # Variabler (0.0 - 1.0)
    # L = Lugn, S = Spontanitet, I = Inkännande, F = Wonder/Förundran
    
    # Mammon-världen (Nuvarande tillstånd)
    mammon = {
        'L': 0.3, 'S': 0.2, 'I': 0.4, 'F': 0.3, 'Eco': 0.5
    }
    
    # Flow-världen (Efter Reset)
    flow = {
        'L': 0.8, 'S': 0.7, 'I': 0.9, 'F': 0.8, 'Eco': 1.45
    }
    
    def calculate_index(v):
        return v['L'] * v['S'] * v['I'] * v['F'] * (1 + v['Eco'])

    index_mammon = calculate_index(mammon)
    index_flow = calculate_index(flow)
    increase = ((index_flow / index_mammon) - 1) * 100

    print("--- BEAUTY INDEX SIMULATION ---")
    print(f"Mammon Beauty Index: {index_mammon:.4f}")
    print(f"Flow Beauty Index:   {index_flow:.4f}")
    print(f"Estetisk ökning:      {increase:.1f}%")
    print("\nSlutsats: Världen blir över 90 gånger vackrare genom att ")
    print("eliminera parasitisk dränering och återställa biosfären.")

if __name__ == "__main__":
    simulate_beauty()
