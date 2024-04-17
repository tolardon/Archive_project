import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
sys.path.append(os.path.abspath("cmd/archivators.py"))
from archivators import *
password = None
compresslevel = None
algor = "None"
open_file = None
extract_file = 'Extract_files/archive.zip'
#extract_zip_archive(open_file, extract_file, password)

def encryption():
    if algor=="None":
        algorithm = 0
    elif algor=="Zip":
        algorithm = 8
    elif algor == "Bzip":
        algorithm = 12
    elif algor == "lzma":
        algorithm = 14
    global extract_file
    extract_file = os.path.relpath(extract_file)
    create_archive(open_file, extract_file, algorithm, compresslevel)

def open_dialog():
    global open_file
    open_file = filedialog.askopenfilename()
    open_entry1.replace("1.0","256.0", open_file)

def extract_dialog():
    global extract_file
    extract_file = filedialog.asksaveasfilename(initialdir="Extract_files", defaultextension="zip", initialfile="my_archive.zip")
    open_entry2.replace("1.0","256.0", extract_file)

def destroy_frame(event):
    for widget in frame_name.winfo_children():
        widget.destroy()
    frame_name.pack_forget()

def settingalgo():
    
    def writeselect():
        global algor
        algor = lang.get()
    
    algor_frame = ttk.Frame(borderwidth=0, relief=SOLID, padding=[8, 10])
    global frame_name
    frame_name = algor_frame

    position = {"padx":6, "pady":6, "anchor":NW}

    non = "None"
    zips = "Zip"
    bzip = "Bzip"
    lzma = "lzma"

    lang = StringVar(value=non)
    
    name_label = ttk.Label(algor_frame, text="Выберите один из алгоритмов архивации")
    name_label.pack(**position) 

    non_btn = ttk.Radiobutton(algor_frame, text=non, command=writeselect, value=non, variable=lang)
    non_btn.pack(**position)
    
    zips_btn = ttk.Radiobutton(algor_frame, text=zips, command=writeselect, value=zips, variable=lang)
    zips_btn.pack(**position)

    bzip_btn = ttk.Radiobutton(algor_frame, text=bzip, command=writeselect, value=bzip, variable=lang)
    bzip_btn.pack(**position)

    lzma_btn = ttk.Radiobutton(algor_frame, text=lzma, command=writeselect, value=lzma, variable=lang)
    lzma_btn.pack(**position)
    
    algor_frame.bind("<Leave>", destroy_frame)
         
    algor_frame.pack(anchor=NW, padx=5, pady=5)
        
    
def settinglevel():
    
    def compresslevelchange():
        global compresslevel
        compresslevel=spinbox.get()
    
    spinbox_frame = ttk.Frame(borderwidth=0, relief=SOLID, padding=[8, 10])
    global frame_name
    frame_name = spinbox_frame
    spinbox_var = StringVar(value=None)

    name_label = ttk.Label(spinbox_frame, text="Введите уровень сжатия")
    name_label.pack(anchor=NW)

    spinbox = ttk.Spinbox(spinbox_frame, from_=-1.0, to=9.0, textvariable=spinbox_var, command=compresslevelchange)
    spinbox.pack(anchor=NW)
    
    spinbox_frame.bind("<Leave>", destroy_frame)
         
    spinbox_frame.pack(anchor=NW, padx=5, pady=5)
        
    
root = Tk()
root.title("Архиватор")
root.geometry("800x600+400+100")
root.option_add("*tearOff", FALSE)

main_menu = Menu()
settings_menu = Menu()

settings_menu.add_cascade(label="Алгоритм архивации", command=settingalgo) 
settings_menu.add_cascade(label="Уровень сжатия", command=settinglevel)
settings_menu.add_cascade(label="Ключ / Пароль шиврования")  
main_menu.add_cascade(label="Параметры архивации", menu=settings_menu)

root.config(menu=main_menu)

name_label1 = ttk.Label(text="Входной файл")
name_label1.place(x=6, y=6)

open_entry1 = Text(warp=None)
open_entry1.place(x=6, y=40, width=300, height= 20)

open_btn1 = ttk.Button(text="Выбрать", command=open_dialog)
open_btn1.place(x=350,y=38)

name_label2 = ttk.Label(text="Файл экспорта")
name_label2.place(x=6, y=80)

open_entry2 = Text(warp=None)
open_entry2.place(x=6, y=112, width=300, height= 20)

open_btn2 = ttk.Button(text="Выбрать", command=extract_dialog)
open_btn2.place(x=350,y=108)

encrypt = ttk.Button(text="Архивировать", command=encryption)
encrypt.place(x=40,y=160)

decryption = ttk.Button(text="Деархивировать")
decryption.place(x=180,y=160)

root.mainloop()
