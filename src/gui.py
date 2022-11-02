from multiprocessing.sharedctypes import Value
import tkinter as tk

from globals import *


def threadGUI():
    gui = GUI()

    
class GUI:
    def __init__(self):
        self.form = tk.Tk()
        self.form.resizable(width=False, height=False)
        self.form.title("proj")
        self.form.minsize(500,500)

        ################
        self.frm_coeff = tk.Frame(
            master = self.form,
            height=250)
        self.lbl_coeff = tk.Label(
            master=self.frm_coeff,
            text="coeff.:"
        )

        self.sv = tk.StringVar()

        self.ent_coeff = tk.Entry(
            master=self.frm_coeff,
            width=10,
            textvariable=self.sv,
        )
        self.ent_coeff.insert(0,"0.5")
        self.sv.trace("w", lambda name, index, mode, sv=self.sv: self.ent_coeffChange(sv))
        
        self.ent_coeff.bind('<Return>', self.ent_coeffKey)



        self.ent_coeff.grid(row=0,column=1, sticky='wn')
        self.lbl_coeff.grid(row=0,column=0, sticky="en")
        ################

        self.isStab = tk.BooleanVar()
        self.chk_stab = tk.Checkbutton(
            text="stabilizacja",
            variable= self.isStab,
            onvalue=True, offvalue=False,
            command=self.chk_stabChange
        )

        self.frm_coeff.grid(row=0, column=0, padx=220, pady= 150)
        self.chk_stab.grid(row=1,column=0, padx=10, pady= 0, sticky= 'n')


        self.form.mainloop()

    def chk_stabChange(self):
        stabCoeff.isStab = self.isStab.get()
        print(stabCoeff.isStab)

    def ent_coeffChange(self, sv):
        self.ent_coeff.config({"bg": "Yellow"})

    def ent_coeffKey(self, x):
        try:
            stabCoeff.coeff = float(self.ent_coeff.get())
            self.ent_coeff.config({"bg": "White"})
        except:
            print("conversion error")
        
    

