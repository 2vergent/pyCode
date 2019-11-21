import tkinter as tk
import pandas
import matplotlib

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def importcsv(): 

    column = entry1.get()
    sacromento = pandas.read_csv('D:/ICUP Assignment Problems/Problem Statement 10/csvfile.csv',usecols=['%s' % column])
    print(sacromento)
    label1 = tk.Label(root, text= "IMPORTED CSV FILE SUCCESSFULLY")
    canvas1.create_window(200, 230, window=label1)
    
button1 = tk.Button(text='IMPORT', command=importcsv)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
