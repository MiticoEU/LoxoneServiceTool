from cProfile import label
import os
import tkinter as tk

#Variablen
max_x= 2



#Startroutine
def programmstart(pro_version):
    oldpath = os.getcwd()
    os.chdir(str (pro_version))
    os.startfile("LoxoneConfig.exe")
    os.chdir(oldpath)

#icon
def icon():
    oldpath = os.getcwd()
    for file in os.listdir(): 
        if os.path.isdir(file):
            os.chdir(str (file))
            root.iconbitmap("LoxoneConfig.exe")

    os.chdir(oldpath)

#Loxone Versionen einlesen
def einlesen():
    loxone= 0
    for file in os.listdir(): 
        if os.path.isdir(file):
            tk.Button(root, text= str(file[13:]), width = 20, command= lambda name=file: programmstart(name)).pack()
            loxone= 1

    if loxone== 0:
        tk.Label(root, text="").pack()
        tk.Label(root, text="Keine Loxone Config gefunden",fg= "red", font = "Verdana 10 bold").pack()
        tk.Label(root, text="").pack()
        
            

#GUI
root = tk.Tk()
root.title("Loxone Config")
root.resizable(0,0)
root.minsize(250, 0)
icon()

tk.Label(root, text="Loxone Version auswählen.", font = "Verdana 10 bold").pack()
einlesen()
tk.Label(root, text="").pack()
root.mainloop()


