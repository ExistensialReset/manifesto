import time

def calculate_friction():
    print("="*60)
    print("      EXISTENTIAL RESET: FRICTION CALCULATOR")
    print("="*60)
    
    lang = input("\nChoose language / Välj språk:\n1. Svenska\n2. English\n> ")
    
    # Texter för båda språken
    texts = {
        "1": {
            "title": "MAMMON-ROFFAR-ÅT-SIG CALCULATOR",
            "intro": "Det här verktyget mäter den dolda friktionen i ditt liv.",
            "part1": "[DEL 1: DEN EKONOMISKA RÄNTESNURRAN]",
            "inc": "Din lön efter skatt (netto): ",
            "int": "Månadskostnad för räntor (bolån, krediter, lån): ",
            "fees": "Dolda avgifter (försäkringar, bankavgifter, onödiga abonnemang): ",
            "part2": "[DEL 2: DEN LOGISTISKA LABYRINTEN]",
            "work": "Hur många timmar jobbar du i veckan? ",
            "admin": "Timmar/vecka på pendling, räkningar, bankärenden och system-admin: ",
            "part3": "[DEL 3: STRESS-SKATTEN]",
            "stress": "På en skala 1-10, hur mycket av din tid är fylld av 'måsten' och inre stress? ",
            "anal": "ANALYS: HUR MYCKET MAMMON ROFFAR ÅT SIG",
            "freedom": "Systemisk frihet",
            "drain": "Mammon Roffar Åt Sig",
            "potential": "av din totala livspotential",
            "hours": "Detta motsvarar ca {:.1f} timmar varje vecka som stjäls",
            "stolen": "direkt från ditt Lugn (L) och din Spontanitet (S).",
            "danger": "DOMSLUT: Du befinner dig i 'Mammon-fällan'.",
            "ok": "DOMSLUT: Du har lyckats hålla viss marginal, men friktionen finns där.",
            "action": "HANDLING: Läs THE_EVIDENCE.md i repot för att förstå hur vi gör en Reset."
        },
        "2": {
            "title": "THE MAMMON DRAIN CALCULATOR",
            "intro": "This tool measures the hidden friction in your life.",
            "part1": "[PART 1: THE FINANCIAL WHIRLPOOL]",
            "inc": "Monthly net income (after tax): ",
            "int": "Monthly interest payments (mortgage, loans): ",
            "fees": "Hidden fees (insurance, bank fees, unnecessary subscriptions): ",
            "part2": "[PART 2: THE LOGISTICAL LABYRINTH]",
            "work": "Hours worked per week: ",
            "admin": "Hours/week on commuting, bills, bank errands, and system-admin: ",
            "part3": "[PART 3: THE STRESS TAX]",
            "stress": "On a scale 1-10, how much of your day is spent in 'Urgency/Stress' (10=Max): ",
            "anal": "ANALYSIS: THE MAMMON DRAIN",
            "freedom": "Systemic Freedom",
            "drain": "Mammon's Take",
            "potential": "of your total life potential",
            "hours": "This equals approx {:.1f} hours every week stolen",
            "stolen": "directly from your Calm (L) and your Spontaneity (S).",
            "danger": "VERDICT: You are in the 'Mammon Trap'.",
            "ok": "VERDICT: You have some margin, but the friction is still there.",
            "action": "ACTION: Visit THE_EVIDENCE.md in the repo to learn how to Reset."
        }
    }

    t = texts.get(lang, texts["2"]) # Default till engelska om de skriver fel

    print("\n" + "="*60)
    print(f"      {t['title']}")
    print("="*60)
    print(f"\n{t['intro']}")
    
    try:
        # 1. EKONOMISK
        print(f"\n{t['part1']}")
        income = float(input(t['inc']))
        interest = float(input(t['int']))
        fees = float(input(t['fees']))
        financial_friction = (interest + fees) / income if income > 0 else 0

        # 2. LOGISTISK
        print(f"\n{t['part2']}")
        work_hours = float(input(t['work']))
        admin_hours = float(input(t['admin']))
        time_friction = admin_hours / work_hours if work_hours > 0 else 0

        # 3. EXISTENTIELL
        print(f"\n{t['part3']}")
        stress_level = float(input(t['stress']))
        l_factor_loss = stress_level / 10

        # BERÄKNING
        total_friction = (financial_friction + time_friction + l_factor_loss) / 3 * 100
        lost_hours = (total_friction / 100) * 168 
        
        print("\n" + "="*60)
        print(t['anal'])
        print("="*60)
        time.sleep(1)
        
        print(f"\n> {t['freedom']}: {100 - total_friction:.1f}%")
        print(f"> {t['drain']}: {total_friction:.1f}% {t['potential']}.")
        
        print(f"\n{t['hours'].format(lost_hours)}")
        print(t['stolen'])
        
        print("\n" + "-" * 60)
        if total_friction > 30:
            print(t['danger'])
        else:
            print(t['ok'])
            
        print(f"\n{t['action']}")
        print("="*60 + "\n")

    except ValueError:
        print("\nError: Please use numbers only. / Fel: Använd endast siffror.")

if __name__ == "__main__":
    calculate_friction()
