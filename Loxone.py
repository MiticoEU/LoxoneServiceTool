# Setup
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from configparser import ConfigParser

#config
cfg = ConfigParser()
cfg.read('config.ini')


#Variablen


# Button actionen

def action_get_info_dialog():
	m_text = "\
************************\n\
Autor: Maikel Klee\n\
Date: 23.03.20\n\
Version: 0.0.1\n\
************************"
	messagebox.showinfo(message=m_text, title = "Infos")
	


# Fenster erstellen
fenster = Tk()
fenster.title(cfg.get('Einstellung', 'title'))
fenster.geometry("400x490")
fenster.iconbitmap("alert.ico")

def action_get_einstellungen():
    einstellung = Tk()
    einstellung.title('Einstellung')
    einstellung.geometry("400x490")
    einstellung.iconbitmap("alert.ico")


    version1 = IntVar()
    Checkbutton(einstellung, text="Version 5.0", variable=version1,onvalue=1,offvalue=0).grid(row=0, column=0, padx=5, pady=5, sticky=W)
    version2 = IntVar()
    Checkbutton(einstellung, text="Version 5.1", variable=version2).grid(row=0, column=1, padx=5, pady=5, sticky=W)
    version3 = IntVar()
    Checkbutton(einstellung, text="Version 6.0", variable=version3).grid(row=0, column=2, padx=5, pady=5, sticky=W)
    version4 = IntVar()
    Checkbutton(einstellung, text="Version 6.2.12.4", variable=version4).grid(row=1, column=0, padx=5, pady=5, sticky=W)
    version5 = IntVar()
    Checkbutton(einstellung, text="Version 6.2.12.17", variable=version5).grid(row=1, column=1, padx=5, pady=5, sticky=W)
    version6 = IntVar()
    Checkbutton(einstellung, text="Version 6.3.2.26", variable=version6).grid(row=1, column=2, padx=5, pady=5, sticky=W)
    version7 = IntVar()
    Checkbutton(einstellung, text="Version 6.3.3.11", variable=version7).grid(row=2, column=0, padx=5, pady=5, sticky=W)
    version8 = IntVar()
    Checkbutton(einstellung, text="Version 6.3.3.19", variable=version8).grid(row=2, column=1, padx=5, pady=5, sticky=W)
    version9 = IntVar()
    Checkbutton(einstellung, text="Version 6.4.5.20", variable=version9).grid(row=2, column=2, padx=5, pady=5, sticky=W)
    version10 = IntVar()
    Checkbutton(einstellung, text="Version 6.4.6.17", variable=version10).grid(row=3, column=0, padx=5, pady=5, sticky=W)
    version11 = IntVar()
    Checkbutton(einstellung, text="Version 7.0.8.17", variable=version11).grid(row=3, column=1, padx=5, pady=5, sticky=W)
    version12 = IntVar()
    Checkbutton(einstellung, text="Version 7.1.9.30", variable=version12).grid(row=3, column=2, padx=5, pady=5, sticky=W)
    version13 = IntVar()
    Checkbutton(einstellung, text="Version 7.1.12.31", variable=version13).grid(row=4, column=0, padx=5, pady=5, sticky=W)
    version14 = IntVar()
    Checkbutton(einstellung, text="Version 7.3.2.24", variable=version14).grid(row=4, column=1, padx=5, pady=5, sticky=W)
    version15 = IntVar()
    Checkbutton(einstellung, text="Version 7.4.4.14", variable=version15).grid(row=4, column=2, padx=5, pady=5, sticky=W)
    version16 = IntVar()
    Checkbutton(einstellung, text="Version 8.0.7.19", variable=version16).grid(row=5, column=0, padx=5, pady=5, sticky=W)
    version17 = IntVar()
    Checkbutton(einstellung, text="Version 8.1", variable=version17).grid(row=5, column=1, padx=5, pady=5, sticky=W)
    version18 = IntVar()
    Checkbutton(einstellung, text="Version 8.3", variable=version18).grid(row=5, column=2, padx=5, pady=5, sticky=W)
    version19 = IntVar()
    Checkbutton(einstellung, text="Version 9.0", variable=version19).grid(row=6, column=0, padx=5, pady=5, sticky=W)
    version20 = IntVar()
    Checkbutton(einstellung, text="Version 9.1", variable=version20).grid(row=6, column=1, padx=5, pady=5, sticky=W)
    version21 = IntVar()
    Checkbutton(einstellung, text="Version 9.3", variable=version21).grid(row=6, column=2, padx=5, pady=5, sticky=W)
    version22 = IntVar()
    Checkbutton(einstellung, text="Version 10.0", variable=version22).grid(row=7, column=0, padx=5, pady=5, sticky=W)
    version23 = IntVar()
    Checkbutton(einstellung, text="Version 10.2", variable=version23).grid(row=7, column=1, padx=5, pady=5, sticky=W)
    Button(einstellung, text='Speichern', width=15, command=action_get_speichern).grid(row=8, column=1, padx=5, pady=5, sticky=W)
    

def action_get_speichern():
    cfg.add_section('Versionen')

    cfg['Versionen']['5.0'] = version1
    cfg['Versionen']['5.1'] = version2
    cfg['Versionen']['6.0'] = version3
    cfg['Versionen']['6.2.12.4'] = version4
    cfg['Versionen']['6.2.12.17'] = version5
    cfg['Versionen']['6.3.2.26'] = version6
    cfg['Versionen']['6.3.3.11'] = version7
    cfg['Versionen']['6.3.3.19'] = version8
    cfg['Versionen']['6.4.5.20'] = version9
    cfg['Versionen']['6.4.6.17'] = version10
    cfg['Versionen']['7.0.8.17'] = version11
    cfg['Versionen']['7.1.9.30'] = version12
    cfg['Versionen']['7.1.12.31'] = version13
    cfg['Versionen']['7.3.2.24'] = version14
    cfg['Versionen']['7.4.4.14'] = version15
    cfg['Versionen']['8.0.7.19'] = version16
    cfg['Versionen']['8.1'] = version17
    cfg['Versionen']['8.3'] = version18
    cfg['Versionen']['9.0'] = version19
    cfg['Versionen']['9.1'] = version20
    cfg['Versionen']['9.3'] = version21
    cfg['Versionen']['10.0'] = version22
    cfg['Versionen']['10.2'] = version23
    
    

    with open('config.ini', 'w') as configfile:
        cfg.write(configfile)
	

# Menüleiste erstellen 
menuleiste = Menu(fenster)

# Menü Datei
datei_menu = Menu(menuleiste, tearoff=0)
menuleiste.add_cascade(label="Datei", menu=datei_menu)
datei_menu.add_command(label="Einstellungen", command=action_get_einstellungen)
datei_menu.add_command(label="Beenden", command=fenster.quit)

# Menü Hilfe

help_menu = Menu(menuleiste, tearoff=0)
menuleiste.add_cascade(label="Hilfe", menu=help_menu)
help_menu.add_command(label="Info", command=action_get_info_dialog)


# Label


# Feste Werte


# Abfrage




# Eingabefelder




# Buttons


# Fenster Aufbau
fenster.config(menu=menuleiste) 


 
# Ereignisschleife
fenster.mainloop()
