import xml.etree.ElementTree as ET
import csv
import tkinter as tk
from tkinter import filedialog
import os
from tkinter import messagebox
import re
from ProcessString import process_string
from RoomNum import RoomNum
from findVAVROOTNAME import findVAVROOTNAME
from findAHUROOTNAME import findAHUROOTNAME
from VAVRename import VAVRename
from AHURename import AHURename
from SetPoints import SetPoints
from SetHEatingStage import SetHEatingStage
global script_dir
script_dir = os.path.dirname(os.path.abspath(__file__))
def edit_xml(NewVaVName, XMLFILE,OriginalAHU,OriginalVaVName,NewAHUNAme,NewMaxFlowSetpoint,NewMinFlowSetpoint,NewIntermediateFlowSetpoint,BoxCoef,heatingstage,Room):
    """
    Edits an existing XML file and saves the changes.

    Args:
        NewVaVName: The new name to replace in the XML file.
        XMLFILE: The filename of the XML file to edit.
    """
    output_folder = "CreatedVAV"
    output_folder1 = "4-5-2024"
    output_folder_pathforSpreadsheets = os.path.join(script_dir, output_folder,output_folder1)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder_pathforSpreadsheets):
        os.makedirs(output_folder_pathforSpreadsheets)
    try:
        tree = ET.parse(XMLFILE)
        root = tree.getroot()
    
        # Call the VAVRename function to perform specific edits
       
        SetPointsoutputs=SetPoints(root,NewMaxFlowSetpoint,NewMinFlowSetpoint,NewIntermediateFlowSetpoint)
        VAVRenameoutput=VAVRename(root, NewVaVName,OriginalVaVName)
        AHURenameoutput=AHURename(root,OriginalAHU,NewAHUNAme)
        RoomNumoutput= RoomNum(root,Room)
        if int(heatingstage) > 0:
            SetHEatingStage(root,heatingstage)
        # Write the modified XML tree to the file
        
       
        NewFileName = os.path.join(output_folder_pathforSpreadsheets, NewVaVName + '.xml')

        tree.write(NewFileName)
        print(f"XML file edited and saved successfully: {XMLFILE}")
        edit_xmlreturn=f"XML file edited and saved successfully: {XMLFILE}"
        return(edit_xmlreturn,SetPointsoutputs,VAVRenameoutput,AHURenameoutput,RoomNumoutput,heatingstage)
    except FileNotFoundError:
        print(f"Error: File not found: {XMLFILE}")
        edit_xmlreturn=f"Error: File not found: {XMLFILE}"
        return(edit_xmlreturn)
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        edit_xmlreturn=f"Error parsing XML file: {e}"
        return(edit_xmlreturn)
