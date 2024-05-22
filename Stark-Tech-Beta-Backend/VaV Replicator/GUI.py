
import xml.etree.ElementTree as ET
import csv
import tkinter as tk
from tkinter import filedialog
import os
from tkinter import messagebox
import re
from XmlTEst import get_data
global script_dir
script_dir = os.path.dirname(os.path.abspath(__file__))

global status_label
script_dir = os.path.dirname(os.path.abspath(__file__))
def display_message(selected_option, selected_option1, selected_option2,selected_option3):
    # Constructing the message
    message = f"Heating And Cooling VAV: {selected_option.get()}\n\nCooling Only VAV: {selected_option1.get()}\n\nSpreadsheets: {selected_option2.get()}"
    print(selected_option1, selected_option)

    # Validating the selected options
    if selected_option.get() == "PY_VAR0" or selected_option1.get() == "PY_VAR1":
        messagebox.showinfo("ERROR", "Please select an option for Everything")
    else:  
        messagebox.showinfo("Parameters",message)
        print(message)


        filename = os.path.join("Spreadsheets", f"{selected_option2.get()}")
        XMLFILESCR=os.path.join("Template VAV SCR Controlers", f"{selected_option.get()}")
        XMLFILECOOLIN = os.path.join("Template Cooling Only VAV Controlers", f"{selected_option1.get()}")
        XMLStageCooling = os.path.join("Template Staged Heating VAV Controlers", f"{selected_option3.get()}")
        print(selected_option,selected_option1,selected_option2)

        num_rows = get_data(filename,XMLFILESCR,XMLFILECOOLIN,XMLStageCooling)

        if num_rows > 0:
            print(f"The CSV file '{filename}' has {num_rows} rows (excluding header).")
        else:
            print(f"Error processing file '{filename}'.")




            
def display_files():
    files = os.listdir(script_dir)
    file_list = "\n".join(files)
    status_label.config(text=f"Files in directory:\n{file_list}")
def display_selection(selected_option):
    selected_option.set("Selected option: " + selected_option.get())
   
def show_selected(selected_option):
    selected = selected_option.get()
    print("Selected option:", selected)
def display_selection1(selected_option1):

    selected_option1.set("Selected option: " + selected_option1.get())
def show_selected1(selected_option1):
    selected1 = selected_option1.get()
 
    print("Selected option:", selected1)
def display_selection2(selected_option2):

    selected_option2.set("Selected option: " + selected_option2.get())
def show_selected2(selected_option2):
    selected2 = selected_option2.get()
 
    print("Selected option:", selected2)
def display_selection3(selected_option3):

    selected_option3.set("Selected option: " + selected_option3.get())
def show_selected3(selected_option3):
    selected3 = selected_option3.get()
 
    print("Selected option:", selected3)