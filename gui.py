import tkinter as tk


def threadGUI():
    gui = GUI()

    
class GUI:
    def __init__(self):
        form = tk.Tk()
        form.resizable(width=False, height=False)
        form.title("proj")

        ################
        frm_coeff = tk.Frame(master = form)
        lbl_coeff = tk.Label(
            master=frm_coeff,
            text="coeff.:"
        )

        ent_coeff = tk.Entry(
            master=frm_coeff,
            width=7 
        )
        ent_coeff.grid(row=0,column=1, sticky='w')
        lbl_coeff.grid(row=0,column=0, sticky="e")
        ################

        chk_stab = tk.Checkbutton(
            text="stabilizacja"
        )

        frm_coeff.grid(row=0, column=0, padx=10)
        chk_stab.grid(row=1,column=0, padx=10)


        form.mainloop()