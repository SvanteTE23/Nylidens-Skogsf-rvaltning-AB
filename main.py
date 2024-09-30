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

lab = ttk.Label(root, text="Ange följande uppgifter för att beräkna priser", font=("Helvetica", 12)).place(x=10, y=105)
ent1 = ttk.Entry(root, text="Hektar").place(x=10, y=130)
ent2 = ttk.Entry(root, text="Antal arbetare").place(x=10, y=160)
ent3 = ttk.Entry(root, text="Sträcka till plats").place(x=10, y=190)

def gui_generate(type):
    return
    

def display_calc():
    selected = menu.current()
    if selected == 1:
        gui_generate("Plantering")
    else:
        pass
    

menu.bind("<<ComboboxSelected>>", display_calc())



root.mainloop()