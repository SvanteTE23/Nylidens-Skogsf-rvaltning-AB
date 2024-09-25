import prices as p

def hektar_till_kvadratmeter(hektar):
    return hektar * 1000

def plantering_kostnad(hektar, antal_plantörer, avstånd):
    pris_planta = p.priser["Plantering"]["Plantpris"] * 1.12 #Kr per planta + semester erstänning
    
    antal_plantor = hektar * 2500 #Antal plantor per hektar
    
    antalt_timmar = (antal_plantor / (antal_plantörer * 1500)) * 8 #Antal timmar som behövs för att plantera, plantor / antal plantörer om de sätter 1800 plant per dag
    
    plantbas_kostnad = p.priser["Plantering"]["Plantbas"] * antalt_timmar
    
    kostand_bil = p.priser["Pris per mil"] * avstånd
    
    total_kostnad = plantbas_kostnad + (pris_planta * antal_plantor) + kostand_bil
    
    print("Total kostnad för plantering: " + '{:,.0f}'.format(total_kostnad).replace(',', ' '))
    print("Beräknat antal plantor som går ut: " + str(antal_plantor))
    
    return round(total_kostnad)

def avverknings_planering(hektar, dist):
    uppskattad_tid = hektar * 5 + dist / 80 #5 timmar per hektar + distans i timmar om man kör ca 80km/h
    
    #Berkäkna kostnaden för avverknings planering beroende på tid och avstånd
    kostnad = p.priser["Avvekrnings planering"]["Skogsvårdare"] * uppskattad_tid + p.priser["Pris per mil"] * dist
    
    
    #Visa användaren kostnaden och uppskattad tid
    print("Total kostnad för avverknings planering: " + '{:,.0f}'.format(kostnad).replace(',', ' '))
    print("Uppskattad tid för avverknings planering: " + str(uppskattad_tid) + " timmar")
    
    return round(kostnad)

def markberedning_kostnad(hektar, dist, antal_beredare):
    uppskattad_tid = (hektar * 2) / antal_beredare + (dist / 10) /2 #2 timmar per hektar för varje markberedare + avstpånd 30min för varje mil
    
    if uppskattad_tid > 48:
        #Varna företagsägaren att det skulle ta för lång tid med för lite markberedare
        print("Fler markberedare rekomenderas annars tar det för lång tid!")
        print(f"Åt mindsonde {antal_beredare + 1} då skulled det ta {uppskattad_tid / (antal_beredare + 1)} timmar")
    
    #Berkäkna kostnaden för markberedning beroende på tid och antal markberedare, samt avstånd till platsen
    kostnad = p.priser["Markberedning"]["Markberedare"] * uppskattad_tid + p.priser["Markberedning"]["Maskinkostnad"] * antal_beredare
    
    kostnad + p.priser["Pris per mil"] * dist
    
    #Visa användaren kostnaden och uppskattad tid
    print("Total kostnad för markberedning: " + '{:,.0f}'.format(kostnad).replace(',', ' '))
    print("Uppskattad tid för markberedning: " + str(uppskattad_tid) + " timmar")
    
def avverkning_kostnad(hektar, dist, antal_arbetare_skot, antal_arbetare_av):
    antal_träd = 2000 * hektar #Antal träd per hektar, ca 2000 träd per hektar
    
    tid_avverkning = antal_träd / 200 #200 träd per timme med en modern skogsmaskin
    
    #Beräkna kostnaden för avverkning beroende på tid och antal arbetare
    pris_avverkning = tid_avverkning * (p.priser["Avverkning"]["Skogsmaskinförare"] * antal_arbetare_av) + tid_avverkning * p.priser["Avverkning"]["Maskinkostnad_Averkning"]
    
    
    tid_skotning = antal_träd / 100 #100 träd per timme med en skotare
    
    #Beräkna kostnaden för skotning beroende på tid och antal arbetare
    pris_skotning = tid_skotning * (p.priser["Avverkning"]["Skotare"] * antal_arbetare_skot) + tid_skotning * p.priser["Avverkning"]["Maskinkostnad_Skotare"]
    
    #Kostnad för att köra till platsen
    kör_kostnad = p.priser["Pris per mil"] * dist
    
    #Slå ihop priserna för avverkning och skotning och körning ohc räkna total tid
    totalt_pris = pris_avverkning + pris_skotning + kör_kostnad
    total_tid = tid_avverkning + tid_skotning
    
    if total_tid > 100:
        print("Varning! Det kommer ta mer än 100 timmar att avverka! Fler arbetare skulle behövas!")
    
    print("Total kostnad för avverkning: " + '{:,.0f}'.format(totalt_pris).replace(',', ' '))
    print("Uppskattad tid för avverkning: " + str(total_tid) + " timmar")
    
