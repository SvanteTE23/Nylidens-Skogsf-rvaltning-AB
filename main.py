#Nylined skogsförvalrning 
# Skapad av: Svante Lindström TE23

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import calculation_funcs as calc

#Skapa huvud fönstret
root = ttk.Window(iconphoto=None, title="Nylidens skogsförvaltning AB", themename="darkly", size=[800, 400])

#Skapa en label för titeln
title = ttk.Label(root, text="Beräkning av priser för skogsförvaltning", font=("Helvetica", 14)).place(x=10, y=10)

#Skapa en label för menyn
menu_info = ttk.Label(root, text="Välj en av följande alternativ för att beräkna priser", font=("Helvetica", 10)).place(x=10, y=50)
#Skapa en combobox för att välja vad som ska beräknas
menu = ttk.Combobox(root, values=["Plantering", "Avverknings planering", "Markberedning", "Avverkning", "Gallring"], state="readonly")
menu.place(x=10, y=70)
menu.current(0)

#Skapa en frame för input fälten så att den är avdelad med en anna parent
inptu_parent = ttk.Frame(root)
inptu_parent.place(x=0, y=100, width=600, height=300)


#Funktion för att rensa input fälten
def clear_gui(parent):
    for widget in parent.winfo_children():
        if isinstance(widget, ttk.Label) or isinstance(widget, ttk.Entry):
            widget.place_forget()

#Funktion för att generera input fälten beroende på vad som ska beräknas
def gui_generate(type):

    global labMain, lab1, ent1, lab2, ent2, lab3, ent3, lab4, ent4
    
    #Rensa input fälten för vareje gång en ny typ av beräkning ska göras
    clear_gui(inptu_parent)
    
    #Skapa labels och entry fält
    labMain = ttk.Label(inptu_parent, text="Ange följande uppgifter för att beräkna priser", font=("Helvetica", 12)).place(x=10, y=5)
    lab1 = ttk.Label(inptu_parent, text="Hektar:", font=("Helvetica", 10))
    ent1 = ttk.Entry(inptu_parent, text="Hektar")
    lab2 = ttk.Label(inptu_parent, text="Antal arbetare:", font=("Helvetica", 10))
    ent2 = ttk.Entry(inptu_parent, text="Antal arbetare")
    lab3 = ttk.Label(inptu_parent, text="Antal avverkare:", font=("Helvetica", 10))
    ent3 = ttk.Entry(inptu_parent, text="Antal avverkare")
    lab4 = ttk.Label(inptu_parent, text="Sträcka till plats(km):", font=("Helvetica", 10))
    ent4 = ttk.Entry(inptu_parent, text="Sträcka till plats")
    
    #Placera labels och entry fält beroende på vilken typ av beräkning som ska göras
    if type == "Plantering":
        lab1.place(x=10, y=30)
        ent1.place(x=10, y=50)
        lab2.place(x=10, y=80)
        ent2.place(x=10, y=100)
        lab4.place(x=10, y=130)
        ent4.place(x=10, y=150)
    if type == "Avverknings planering":
        lab1.place(x=10, y=30)
        ent1.place(x=10, y=50)
        lab4.place(x=10, y=80)
        ent4.place(x=10, y=100)
    if type == "Markberedning":
        lab1.place(x=10, y=30)
        ent1.place(x=10, y=50)
        lab2.place(x=10, y=80)
        ent2.place(x=10, y=100)
        lab4.place(x=10, y=130)
        ent4.place(x=10, y=150)
    if type == "Avverkning":
        lab1.place(x=10, y=30)
        ent1.place(x=10, y=50)
        lab2.place(x=10, y=80)
        ent2.place(x=10, y=100)
        lab3.place(x=10, y=130)
        ent3.place(x=10, y=150)
        lab4.place(x=10, y=180)
        ent4.place(x=10, y=200)
    if type == "Gallring":
        lab1.place(x=10, y=30)
        ent1.place(x=10, y=50)
        lab2.place(x=10, y=80)
        ent2.place(x=10, y=100)
        lab4.place(x=10, y=130)
        ent4.place(x=10, y=150)
    

#Funktion som får valet ur comboboxen och ger den till gui_generate funktionen
gui_generate("Plantering")
def display_calc(e):
    gui_generate(menu.get())

#Definiera labels för att visa priset och tiden och även en label för att visa varningar
price_calculated = ttk.Label(root, text=" ", font=("Helvetica", 12))
time_calculated = ttk.Label(root, text=" ", font=("Helvetica", 12))
warn_message = ttk.Label(root, text=" ", foreground="red",font=("Helvetica", 12))

#Funktion för att beräkna priset och tiden beroende av det som matats in
def calculate_from_data():
    #Rensa alla varningar
    warn_message.place_forget()
    
    #Beräkna priset och tiden för planetering från input fälten
    if menu.get() == "Plantering":
        #Försök att beräkna priset och tiden, om det inte är nummer så visa en varning
        try:
            #Beräkna priset och tiden för plantering
            PList = calc.plantering_kostnad(int(ent1.get()), int(ent2.get()), int(ent4.get()))
            #Visa priset och tiden
            price_calculated.config(text = PList[0])
            time_calculated.config(text = PList[1])
        #Om det inte är nummer så visa en varning
        except ValueError:
            warn_message.config(text = "Ange giltiga värden")
            warn_message.place(x=240, y=190)
    #Beräkna priset och tiden för avverknings planering från input fälten
    if menu.get() == "Avverknings planering":
        #Försök att beräkna priset och tiden, om det inte är nummer så visa en varning
        try:
            APList = calc.avverknings_planering(int(ent1.get()), int(ent4.get()))
            price_calculated.config(text = APList[0])
            time_calculated.config(text = APList[1])
        #Om det inte är nummer så visa en varning
        except ValueError:
            warn_message.config(text = "Ange giltiga värden")
            warn_message.place(x=240, y=190)
        #Beräkna priset och tiden för markberedning från input fälten
    if menu.get() == "Markberedning":
        #Försök att beräkna priset och tiden, om det inte är nummer så visa en varning
        try:
            #Beräkna priset och tiden för markberedning
            MList = calc.markberedning_kostnad(int(ent1.get()), int(ent2.get()), int(ent4.get()))
            price_calculated.config(text = MList[0])
            time_calculated.config(text = MList[1])
			#Om det tredej valuet inte är noll så visa en varning som rekommenderar optimala antalet arbetare
            if MList[2] != 0:
                warn_message.config(text = MList[2])
                warn_message.place(x=240, y=190)
            else:
                warn_message.place_forget()
        #Om det inte är nummer så visa en varning
        except ValueError:
            warn_message.config(text = "Ange giltiga värden")
            warn_message.place(x=240, y=190)
    #Beräkna priset och tiden för avverkning från input fälten
    if menu.get() == "Avverkning":
		#Försök att beräkna priset och tiden, om det inte är nummer så visa en varning
        try:
            #Beräkna priset och tiden för avverkning
            AList = calc.avverkning_kostnad(int(ent1.get()), int(ent2.get()), int(ent3.get()), int(ent4.get()))
            price_calculated.config(text = AList[0])
            time_calculated.config(text = AList[1])

			#Om det tredej valuet inte är noll så visa en varning som rekommenderar optimala antalet arbetare
            if AList[2] != 0:
                warn_message.config(text = AList[2])
                warn_message.place(x=240, y=190)
            else:
                warn_message.place_forget()
        #Om det inte är nummer så visa en varning
        except ValueError:
            warn_message.config(text = "Ange giltiga värden")
            warn_message.place(x=240, y=190)
    #Beräkna priset och tiden för gallring från input fälten
    if menu.get() == "Gallring":
		#Försök att beräkna priset och tiden, om det inte är nummer så visa en varning
        try:
            #Beräkna priset och tiden för gallring
            GList = calc.gallring_kostnad(int(ent1.get()), int(ent2.get()), int(ent4.get()))
            price_calculated.config(text = GList[0])
            time_calculated.config(text = GList[1])
			#Om det tredej valuet inte är noll så visa en varning som rekommenderar optimala antalet arbetare
            if GList[2] != 0:
                warn_message.config(text = GList[2])
                warn_message.place(x=240, y=190)
            else:
                warn_message.place_forget()
        #Om det inte är nummer så visa en varning
        except ValueError:
            warn_message.config(text = "Ange giltiga värden")
            warn_message.place(x=240, y=190)

#Binda funktionen display_calc till comboboxen så att den uppdateras
menu.bind("<<ComboboxSelected>>", display_calc)

#Skapa en knapp för att beräkna priset och tiden
submit_button = ttk.Button(inptu_parent, text="Beräkna", command=calculate_from_data).place(x=160, y=50)

#Placera labels för att visa priset och tiden
price_calculated.place(x=240, y=150)
time_calculated.place(x=240, y=170)

#Visa huvud fönstret och allt som finns i det
root.mainloop()