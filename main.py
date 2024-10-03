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
    

root = ttk.Window(iconphoto=None, title="Nylidens skogsförvaltning", themename="darkly", size=[600, 400])

title = ttk.Label(root, text="Beräkning av priser för skogsförvaltning", font=("Helvetica", 14)).place(x=10, y=10)

menu_info = ttk.Label(root, text="Välj en av följande alternativ för att beräkna priser", font=("Helvetica", 10)).place(x=10, y=50)
menu = ttk.Combobox(root, values=["Plantering", "Avverknings planering", "Markberedning", "Avverkning", "Gallring"], state="readonly")
menu.place(x=10, y=70)
menu.current(0)

par = ttk.Frame(root)
par.place(x=0, y=100, width=600, height=300)

submit_button = ttk.Button(par, text="Beräkna", command=lambda: print("Hello")).place(x=160, y=50)

def clear_gui(parent):
    for widget in parent.winfo_children():
        if isinstance(widget, ttk.Label) or isinstance(widget, ttk.Entry):
            widget.place_forget()

def gui_generate(type):

    
    clear_gui(par)
    
    labMain = ttk.Label(par, text="Ange följande uppgifter för att beräkna priser", font=("Helvetica", 12)).place(x=10, y=5)
    lab1 = ttk.Label(par, text="Hektar:", font=("Helvetica", 10))
    ent1 = ttk.Entry(par, text="Hektar")
    lab2 = ttk.Label(par, text="Antal arbetare:", font=("Helvetica", 10))
    ent2 = ttk.Entry(par, text="Antal arbetare")
    lab3 = ttk.Label(par, text="Antal arbetare:", font=("Helvetica", 10))
    ent3 = ttk.Entry(par, text="Antal arbetare")
    lab4 = ttk.Label(par, text="Sträcka till plats:", font=("Helvetica", 10))
    ent4 = ttk.Entry(par, text="Sträcka till plats")
    
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
    

menu.bind("<<ComboboxSelected>>", display_calc)



root.mainloop()