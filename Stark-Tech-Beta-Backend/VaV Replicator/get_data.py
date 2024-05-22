
import xml.etree.ElementTree as ET
import csv
import os
import re
from ProcessString import process_string

from edit_xml import edit_xml

# Define the process_string function
global script_dir
script_dir = os.path.dirname(os.path.abspath(__file__))

    

def get_data(filename,XMLFILESCR,XMLFILECOOLIN,XMLStageCooling):
    """
    Parses a CSV file and checks if a condition is met, then edits the XML file accordingly.

    Args:
        filename: The filename of the CSV file.
        NewVaVName: The new name to replace in the XML file.
        XMLFILE: The filename of the XML file to edit.

    Returns:
        The number of rows in the CSV file (excluding header).
    """
    information=[]
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            # Skip the header row
            next(reader, None)
            i = 0
            heatingstage=0
            for row in reader:
                i += 1
                # Check if a condition is met in the CSV row
                if row[12] == 'None':
                    print("Condition met at row", i)
                 
                    NewVaVName= row[0]
                    NewAHUNAme=row[2]
                    NewMaxFlowSetpoint = row[13]
                    NewMinFlowSetpoint = row[14]
                    NewIntermediateFlowSetpoint = row[16]
                    BoxCoef= row[27]
                    OriginalVaVName="VAV-RPV5-ClgOnly"
                    OriginalAHU="AHU-XX"
                    NewAHUNAme=process_string(NewAHUNAme)
                    NewVaVName=process_string(NewVaVName)
                    Room = row[4]
                    # Edit the XML file
                    XMLFILE = "Template Cooling Only VAV Controlers/RP-V-5A.xml"
                    information.append(edit_xml(NewVaVName, XMLFILECOOLIN, OriginalAHU, OriginalVaVName, NewAHUNAme, NewMaxFlowSetpoint, NewMinFlowSetpoint, NewIntermediateFlowSetpoint, BoxCoef, heatingstage, Room))
                    print('\n')

                if row[12] == 'SCR EH':
                    print("Condition met at row", i)
                   
                    NewVaVName= row[0]
                    NewAHUNAme=row[2]
                    NewMaxFlowSetpoint = row[13]
                    NewMinFlowSetpoint = row[14]
                    NewIntermediateFlowSetpoint = row[16]
                    BoxCoef= row[27]
                    OriginalVaVName="VAV-RPV5-SCR"
                    OriginalAHU="AHU-XX"
                    NewAHUNAme=process_string(NewAHUNAme)
                    NewVaVName=process_string(NewVaVName)
                    Room = row[4]
                    XMLFILE = "Template VAV SCR Controlers/RP-V4-A.xml"
                    information.append(edit_xml(NewVaVName, XMLFILESCR, OriginalAHU, OriginalVaVName, NewAHUNAme, NewMaxFlowSetpoint, NewMinFlowSetpoint, NewIntermediateFlowSetpoint, BoxCoef, heatingstage, Room))
                    print('\n')
                    
                    
                if row[12] is not None and row[12] not in ['None', 'SCR EH']:
                    print("Condition met at row", i)
                  
                    NewVaVName= row[0]
                    NewAHUNAme=row[2]
                    NewMaxFlowSetpoint = row[13]
                    NewMinFlowSetpoint = row[14]
                    NewIntermediateFlowSetpoint = row[16]
                    BoxCoef= row[27]
                    OriginalVaVName="VAV-RPV5-Staged"
                    OriginalAHU="AHU-XX"
                    NewAHUNAme=process_string(NewAHUNAme)
                    NewVaVName=process_string(NewVaVName)
                    Room = row[4]
                    XMLFILE = "Template VAV SCR Controlers/RP-V4-A.xml"
                    heatingstage=0
                    if "2" in row[12]:
                        print("2 Stage")
                        heatingstage="2"
                    if "3" in row[12]:
                        print("3 Stage")
                        heatingstage="3"
                   
                    
                    information.append(edit_xml(NewVaVName, XMLStageCooling, OriginalAHU, OriginalVaVName, NewAHUNAme, NewMaxFlowSetpoint, NewMinFlowSetpoint, NewIntermediateFlowSetpoint, BoxCoef, heatingstage, Room))
                    print('\n')
            return i,information
           
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return 0  # Indicate error by returning 0

# Example usage

