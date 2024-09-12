import prices as priser

def hektar_till_kvadratmeter(hektar):
    return hektar * 1000

def plantering_kostnad(hektar, antal_plantörer, avstånd):
    pris_planta = priser["Plantering"]["Plantpris"] * 1.12 #Kr per planta + semester erstänning
    
    antal_plantor = hektar * 2500 #Antal plantor per hektar
    
    antalt_timmar = (antal_plantor / (antal_plantörer * 1500)) * 8 #Antal timmar som behövs för att plantera, plantor / antal plantörer om de sätter 1800 plant per dag
    
    plantbas_kostnad = priser["Plantering"]["Plantbas"] * antalt_timmar
    
    kostand_bil = priser["Pris per mil"] * avstånd
    
    total_kostnad = plantbas_kostnad + (pris_planta * antal_plantor) + kostand_bil
    
    print("Total kostnad för plantering: " + '{:,.0f}'.format(total_kostnad).replace(',', ' '))
    print("Beräknat antal plantor som går ut: " + str(antal_plantor))
    
    return round(total_kostnad)

def avverknings_planering(hektar):
    kostnad = priser["Avvekrnings planering"] * hektar
    
    
    
    print("Total kostnad för avverknings planering: " + '{:,.0f}'.format(kostnad).replace(',', ' '))
    
    return round(kostnad)