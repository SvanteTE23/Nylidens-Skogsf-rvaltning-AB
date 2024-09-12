#Nylined skogsförvalrning 
# Skapad av: Svante

#Dict med priser
priser = {
    "Plantering": 0.5, #Kr per planta
    "Avvekrnings planering": 1, #Kr per hektar
    "Markberedning": 1, #Kr per hektar
    "Avverkning": 1, #Kr per hektar
    "Gallring": 1, #Kr per hektar
    "Anställda": {
      "Plantbas": 250, #Kr per timme
      "Skogsmaskinförare": 350, #Kr per timme
      "Markberedare": 300, #Kr per timme
      "Gallrare": 125, #Kr per timme
      "Skogsvårdare": 200, #Kr per timme
    },
    "Pris per mil": 30, #Kr per mil
}

def hektar_till_kvadratmeter(hektar):
    return hektar * 1000

def plantering_kostnad(hektar, antal_plantörer, avstånd):
    pris_planta = priser["Plantering"] * 1.12 #Kr per planta + semester erstänning
    
    antal_plantor = hektar * 2500 #Antal plantor per hektar
    
    antalt_timmar = (antal_plantor / (antal_plantörer * 1500)) * 8 #Antal timmar som behövs för att plantera, plantor / antal plantörer om de sätter 1800 plant per dag
    
    plantbas_kostnad = priser["Anställda"]["Plantbas"] * antalt_timmar
    
    kostand_bil = priser["Pris per mil"] * avstånd
    
    total_kostnad = plantbas_kostnad + (pris_planta * antal_plantor) + kostand_bil
    
    print("Total kostnad för plantering: " + '{:,.0f}'.format(total_kostnad).replace(',', ' '))
    print("Beräknat antal plantor som går ut: " + str(antal_plantor))
    
    return round(total_kostnad)

def avverknings_planering(hektar):
    print("s")

plantering_kostnad(20, 5, 1.4)