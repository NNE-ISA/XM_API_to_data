import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile, askdirectory
from tkinter import messagebox as mb
from tkcalendar import Calendar, DateEntry
from datetime import date, datetime
import xm_query as xq
import os

tr = {'Horaria' : 'Hour', 'Diaria':'Day'}

def get_date():
    def cal_done():
        top.withdraw()
        root.quit()
        root.destroy()

    root = tk.Tk()
    root.withdraw() # keep the root window from appearing

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1")
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=cal_done).pack()

    selected_date = None
    root.mainloop()
    return cal.selection_get()

class gui_xm_API:
    def __init__(self, root):
        self.root= root
        # FRAME
        self.frm = tk.Frame(self.root, width='300', height='400') # New frame
        self.frm.pack() # package frame in root window

        # ENTRIES
        # Start date
        tk.Label(self.frm, text='Fecha inicial', font=12).place(x=10, y=20) # start date label
        self.start_cal = tk.Button(self.frm, text='Calendario', command=self.startDate).place(x=220,y=50) # start calendar
        self.start = date.today()
        self.start_date = tk.Label(self.frm, text=self.start, font=11)
        self.start_date.place(x=10,y=50) # Selected date

        # End Date
        tk.Label(self.frm, text='Fecha final', font=12).place(x=10, y=80) # end date label
        self.end_cal = tk.Button(self.frm, text='Calendario', command=self.endDate).place(x=220,y=110) # end calendar
        self.end = date.today()
        self.end_date = tk.Label(self.frm, text=self.end, font=11)
        self.end_date.place(x=10,y=110) # Selected date

        # Intance about need data
        tk.Label(self.frm, text='Seleccione la Instancia', font=12).place(x=10, y=150) # end date label
        self.combo = ttk.Combobox(self.frm, state="readonly") # Create the options menu
        self.combo.place(x=10, y=170) # Position from the option menu
        self.combo['values'] = list(xq.instances.keys())
        self.combo.current(0)
        self.combo.bind("<<ComboboxSelected>>", self.sel)

        # Frecuency of register
        tk.Label(self.frm, text='Frecuencia (Diaria, Horaria)', font=12).place(x=10, y=210) # end date label
        self.frequency = ttk.Combobox(self.frm, state="readonly") # Create the options menu
        self.frequency.place(x=10, y=230) # Position from the option menu
        self.frequency['values'] = xq.instances[self.combo.get()]['Freq']
        self.frequency.set(self.frequency['values'][0])

        # Make the query and save in a file
        self.save_btn = ttk.Button(self.frm, text = 'Consultar y guardar',
                                   command = self.SaveFile)
        self.save_btn.place(x=10,y=290) # Selected date

        tk.Label(self.frm, text='Equipo de nuevos negocios', font=3).place(x=10, y=380)

    def startDate(self):
        self.start = get_date() # select start date on calendar
        self.start_date.config(text = str(self.start)) # show date

    def endDate(self):
        self.end = get_date() # select end date on calendar
        self.end_date.config(text = str(self.end)) # show

    def sel(self, event):
        self.frequency['values'] = xq.instances[self.combo.get()]['Freq']
        self.frequency.set(self.frequency['values'][0])

    def SaveFile(self):
        file_name = self.combo.get()+'_'+str(self.start)+'_'+str(self.end)+'_('+self.frequency.get()+').csv'
        df = xq.xmQueryAPI(self.combo.get(), self.start, self.end, tr[self.frequency.get()])
        phat = askdirectory()
        os.chdir(phat)
        df.to_csv(file_name, sep=',', index=False)
        mb.showinfo("Información", "La consulta se ha guardado correctamente")



def main():

    # ROOT
    root = tk.Tk()
    root.title('Consulta datos XM') # window title
    root.resizable(0,1) # (width, height)
    root.iconbitmap('logo.ico')
    app = gui_xm_API(root)
    root.mainloop()

if __name__ == '__main__':
    main()