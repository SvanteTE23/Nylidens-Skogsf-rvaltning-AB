#Nylined skogsförvalrning 
# Skapad av: Svante Lindström TE23

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.icons import Icon
import calculation_funcs as calc

calc.plantering_kostnad(20, 5, 1.4)

calc.avverknings_planering(20, 100)

calc.markberedning_kostnad(20, 100, 1)

calc.avverkning_kostnad(20, 1, 1, 1)

calc.gallring_kostnad(20, 1, 2)
    

root = ttk.Window(iconphoto=None, title="Nylidens skogsförvaltning AB", themename="darkly", size=[800, 400])

title = ttk.Label(root, text="Beräkning av priser för skogsförvaltning", font=("Helvetica", 14)).place(x=10, y=10)

menu_info = ttk.Label(root, text="Välj en av följande alternativ för att beräkna priser", font=("Helvetica", 10)).place(x=10, y=50)
menu = ttk.Combobox(root, values=["Plantering", "Avverknings planering", "Markberedning", "Avverkning", "Gallring"], state="readonly")
menu.place(x=10, y=70)
menu.current(0)

inptu_parent = ttk.Frame(root)
inptu_parent.place(x=0, y=100, width=600, height=300)



def clear_gui(parent):
    for widget in parent.winfo_children():
        if isinstance(widget, ttk.Label) or isinstance(widget, ttk.Entry):
            widget.place_forget()

def gui_generate(type):

    global labMain, lab1, ent1, lab2, ent2, lab3, ent3, lab4, ent4
    
    clear_gui(inptu_parent)
    
    labMain = ttk.Label(inptu_parent, text="Ange följande uppgifter för att beräkna priser", font=("Helvetica", 12)).place(x=10, y=5)
    lab1 = ttk.Label(inptu_parent, text="Hektar:", font=("Helvetica", 10))
    ent1 = ttk.Entry(inptu_parent, text="Hektar")
    lab2 = ttk.Label(inptu_parent, text="Antal arbetare:", font=("Helvetica", 10))
    ent2 = ttk.Entry(inptu_parent, text="Antal arbetare")
    lab3 = ttk.Label(inptu_parent, text="Antal avverkare:", font=("Helvetica", 10))
    ent3 = ttk.Entry(inptu_parent, text="Antal avverkare")
    lab4 = ttk.Label(inptu_parent, text="Sträcka till plats(km):", font=("Helvetica", 10))
    ent4 = ttk.Entry(inptu_parent, text="Sträcka till plats")
    
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
    

gui_generate("Plantering")
def display_calc(e):
    gui_generate(menu.get())

price_calculated = ttk.Label(root, text=" ", font=("Helvetica", 12))
time_calculated = ttk.Label(root, text=" ", font=("Helvetica", 12))
warn_message = ttk.Label(root, text=" ", foreground="red",font=("Helvetica", 12))

def calculate_from_data():
    warn_message.place_forget()
    
    if menu.get() == "Plantering":
        try:
            PList = calc.plantering_kostnad(int(ent1.get()), int(ent2.get()), int(ent4.get()))
            price_calculated.config(text = PList[0])
            time_calculated.config(text = PList[1])
            if menu.get() == "Avverknings planering":
                APList = calc.avverknings_planering(int(ent1.get()), int(ent4.get()))
                price_calculated.config(text = APList[0])
                time_calculated.config(text = APList[1])
        except ValueError:
            warn_message.config(text = "Ange giltiga värden")
            warn_message.place(x=240, y=190)
    if menu.get() == "Markberedning":
        try:
            MList = calc.markberedning_kostnad(int(ent1.get()), int(ent2.get()), int(ent4.get()))
            price_calculated.config(text = MList[0])
            time_calculated.config(text = MList[1])
			
            if MList[2] != 0:
                warn_message.config(text = MList[2])
                warn_message.place(x=240, y=190)
            else:
                warn_message.place_forget()
        except ValueError:
            warn_message.config(text = "Ange giltiga värden")
            warn_message.place(x=240, y=190)
    if menu.get() == "Avverkning":
        try:
            AList = calc.avverkning_kostnad(int(ent1.get()), int(ent2.get()), int(ent3.get()), int(ent4.get()))
            price_calculated.config(text = AList[0])
            time_calculated.config(text = AList[1])
        
            if AList[2] != 0:
                warn_message.config(text = AList[2])
                warn_message.place(x=240, y=190)
            else:
                warn_message.place_forget()
        except ValueError:
            warn_message.config(text = "Ange giltiga värden")
            warn_message.place(x=240, y=190)
    if menu.get() == "Gallring":
        try:
            GList = calc.gallring_kostnad(int(ent1.get()), int(ent2.get()), int(ent4.get()))
            price_calculated.config(text = GList[0])
            time_calculated.config(text = GList[1])
        
            if GList[2] != 0:
                warn_message.config(text = GList[2])
                warn_message.place(x=240, y=190)
            else:
                warn_message.place_forget()
        except ValueError:
            warn_message.config(text = "Ange giltiga värden")
            warn_message.place(x=240, y=190)

menu.bind("<<ComboboxSelected>>", display_calc)

submit_button = ttk.Button(inptu_parent, text="Beräkna", command=calculate_from_data).place(x=160, y=50)

price_calculated.place(x=240, y=150)
time_calculated.place(x=240, y=170)

root.mainloop()