import prices as p


def plantering_kostnad(hektar, antal_plantörer, avstånd):
    pris_planta = p.priser["Plantering"]["Plantpris"] * 1.12 #Kr per planta + semester erstänning
    
    antal_plantor = hektar * 2500 #Antal plantor per hektar
    
    antalt_timmar = (antal_plantor / (antal_plantörer * 1500)) * 8 #Antal timmar som behövs för att plantera, plantor / antal plantörer om de sätter 1800 plant per dag
    
    plantbas_kostnad = p.priser["Plantering"]["Plantbas"] * antalt_timmar
    
    kostand_bil = p.priser["Pris per mil"] * avstånd
    
    total_kostnad = plantbas_kostnad + (pris_planta * antal_plantor) + kostand_bil
    
    print("Total kostnad för plantering: " + '{:,.0f}'.format(total_kostnad).replace(',', ' '))
    print("Beräknat antal plantor som går ut: " + str(antal_plantor))
    
    kostnad = "Total kostnad för plantering: " + '{:,.0f}'.format(total_kostnad).replace(',', ' ') + " kr"
    antal_plant = "Beräknat antal plantor som går ut: " + str(antal_plantor)
    
    return kostnad, antal_plant



def avverknings_planering(hektar, dist):
    uppskattad_tid = hektar * 5 + dist / 80 #5 timmar per hektar + distans i timmar om man kör ca 80km/h
    
    #Berkäkna kostnaden för avverknings planering beroende på tid och avstånd
    kostnad = p.priser["Avvekrnings planering"]["Skogsvårdare"] * uppskattad_tid + p.priser["Pris per mil"] * dist
    
    
    #Visa användaren kostnaden och uppskattad tid
    print("Total kostnad för avverknings planering: " + '{:,.0f}'.format(kostnad).replace(',', ' '))
    print("Uppskattad tid för avverknings planering: " + str(uppskattad_tid) + " timmar")
    
    kostn = "Total kostnad för avverknings planering: " + '{:,.0f}'.format(kostnad).replace(',', ' ') + " kr"
    tid= "Uppskattad tid för avverknings planering: " + str(uppskattad_tid) + " timmar"
    
    return kostn, tid



def markberedning_kostnad(hektar, antal_beredare, dist):
    uppskattad_tid = (hektar * 2) / antal_beredare + (dist / 10) /2 #2 timmar per hektar för varje markberedare + avstpånd 30min för varje mil
    
    message = 0
    
    #Varna om det tar för lång tid och använd funtionen som räknar ut optimala antalet arbetare
    if uppskattad_tid > 48:
        #Varna företagsägaren att det skulle ta för lång tid med för lite markberedare
        print("Fler markberedare rekomenderas annars tar det för lång tid!")
        print(f"Det optimala antalet arbetare är {optimaltArbetare(hektar, antal_beredare, 48, 0.5)}")
        message = f"Det optimala antalet arbetare är {optimaltArbetare(hektar, antal_beredare, 48, 0.5)}"
    
    #Berkäkna kostnaden för markberedning beroende på tid och antal markberedare, samt avstånd till platsen
    kostnad = p.priser["Markberedning"]["Markberedare"] * uppskattad_tid + p.priser["Markberedning"]["Maskinkostnad"] * antal_beredare
    
    kostnad + p.priser["Pris per mil"] * dist
    
    #Visa användaren kostnaden och uppskattad tid
    print("Total kostnad för markberedning: " + '{:,.0f}'.format(kostnad).replace(',', ' '))
    print("Uppskattad tid för markberedning: " + str(uppskattad_tid) + " timmar")
    
    kostnad = "Total kostnad för markberedning: " + '{:,.0f}'.format(kostnad).replace(',', ' ') + " kr"
    tid = "Uppskattad tid för markberedning: " + str(uppskattad_tid) + " timmar"
    
    return kostnad, tid, message


   
def avverkning_kostnad(hektar, antal_arbetare_skot, antal_arbetare_av, dist):
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
    
    message = 0
    
    #Varna om det tar för lång tid och använd funtionen som räknar ut optimala antalet arbetare
    if total_tid > 100:
        print("Varning! Det kommer ta mer än 100 timmar att avverka! Fler arbetare skulle behövas!")
        print(f"Det optimala antalet arbetare är {optimaltArbetare(hektar, antal_arbetare_av, 100, 0.2)} skongsmaksiner, {optimaltArbetare(hektar, antal_arbetare_skot, 100, 0.1)} skotare")
        message = f"Det optimala antalet arbetare är {optimaltArbetare(hektar, antal_arbetare_av, 100, 0.2)} skongsmaksiner, {optimaltArbetare(hektar, antal_arbetare_skot, 100, 0.1)} skotare"
    
    print("Total kostnad för avverkning: " + '{:,.0f}'.format(totalt_pris).replace(',', ' '))
    print("Uppskattad tid för avverkning: " + str(total_tid) + " timmar")
    
    kostnad = "Total kostnad för avverkning: " + '{:,.0f}'.format(totalt_pris).replace(',', ' ') + " kr"
    tid = "Uppskattad tid för avverkning: " + str(total_tid) + " timmar"
    
    return kostnad, tid, message



def gallring_kostnad(hektar, arbetare, dist):
    tid = hektar / (arbetare * 0.125) #En gallrare kan gallra 0.125 hektar per timme

    message = 0
    
    #Varna om det tar för lång tid och använd funtionen som räknar ut optimala antalet arbetare
    if tid > 48:
        print("VARNING!")
        print(f"Det optimala antalet arbetare är {optimaltArbetare(hektar, arbetare, 48, 0.125)}")
        message = f"Det optimala antalet arbetare är {optimaltArbetare(hektar, arbetare, 48, 0.125)}"
        
    
    avståndskostnad = p.priser["Pris per mil"] * dist #Kostnad för att köra till platsen
    
    #Beräkna kostnaden för gallring beroende på tid och antal arbetare
    pris = tid * (p.priser["Gallring"]["Gallrare"] * arbetare) + p.priser["Gallring"]["Verktygskostnad"]
    pris_total = pris + avståndskostnad
    
    print("Total kostnad för gallring: " + '{:,.0f}'.format(pris_total).replace(',', ' '))
    print("Uppskattad tid för gallring: " + str(tid) + " timmar")
    
    kostnad = "Total kostnad för gallring: " + '{:,.0f}'.format(pris_total).replace(',', ' ')
    tid = "Uppskattad tid för gallring: " + str(tid) + " timmar"
    
    return kostnad, tid, message


  
#Funktion som räknar ut det optimala antalet arbetare som behövs för att tjäna maximalt
def optimaltArbetare(hektar, arbetare, tidM, multiplier):
    #tidM = maximal tid, multiplier är hur många hektar per timme en arbetare/masking klara av
    for i in range(10): #Loop som loopar igenom 10ggr för att hitta det minsta antalet arbetare som behövs så att man tjänar maximalt
            if hektar / ((arbetare + i) * multiplier) < tidM:
                return arbetare + i