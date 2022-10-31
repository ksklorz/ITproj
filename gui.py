import tkinter as tk

from globals import *


def threadGUI():
    gui = GUI()

    
class GUI:
    def __init__(self):
        self.form = tk.Tk()
        self.form.resizable(width=False, height=False)
        self.form.title("proj")

        ################
        self.frm_coeff = tk.Frame(master = self.form)
        self.lbl_coeff = tk.Label(
            master=self.frm_coeff,
            text="coeff.:"
        )

        self.ent_coeff = tk.Entry(
            master=self.frm_coeff,
            width=7 
        )
        self.ent_coeff.grid(row=0,column=1, sticky='w')
        self.lbl_coeff.grid(row=0,column=0, sticky="e")
        ################

        self.chk_stab = tk.Checkbutton(
            text="stabilizacja",
            command=self.chk_stabChange
        )

        self.frm_coeff.grid(row=0, column=0, padx=10)
        self.chk_stab.grid(row=1,column=0, padx=10)


        self.form.mainloop()

    def chk_stabChange(self):
        message = self.ent_coeff.get()
        cmdGui.put(message)
    

