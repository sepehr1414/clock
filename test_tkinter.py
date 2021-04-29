import tkinter as tk
from time import strftime

root = tk.Tk()
root.title('clock')

def time():
    string = strftime('%H:%M:%S %a')
    label.config(text=string)
    label.after(1000, time)



label = tk.Label(font=('ds-digital', 80), background='black', foreground='cyan')
label.pack(anchor='center')
time()

root.mainloop()