
import xml.etree.ElementTree as ET
import csv
import os
import re

from BaseIO import BaseIO
from maketrendxml import maketrendxml
from makexml import makexml
from trendIO import trendIO


# Define the process_string function
global script_dir
script_dir = os.path.dirname(os.path.abspath(__file__))
from datetime import datetime

def current_datetime_with_seconds():
    return datetime.now().strftime("%Y%m%d_%H%M%S.xml")  # Using underscores (_) instead of spaces, removing colon (:)
def iopinString(iopin):
    letters = re.findall('[A-Za-z]+', iopin)  # Extract letters
    numbers = re.findall('[0-9]+', iopin)  # Extract numbers
    return ' '.join(letters) + " " + ' '.join(numbers)
    

def get_data(csvfile):
    
    """
    Parses a CSV file and checks if a condition is met, then edits the XML file accordingly.

    Args:
        filename: The filename of the CSV file.
        NewVaVName: The new name to replace in the XML file.
        XMLFILE: The filename of the XML file to edit.

    Returns:
        The number of rows in the CSV file (excluding header).
    """
    directory = os.path.join(os.path.dirname(__file__), 'SpreadSheets')
    filename = csvfile 
    filename = os.path.join(directory, filename)

    directory2 = os.path.join(os.path.dirname(__file__), 'CreatedIO')
    directory3 = os.path.join(os.path.dirname(__file__), 'CreatedTrend')

    print(directory2)
    

    output = "IO_XML_Folder_"+current_datetime_with_seconds()
    output2 = "Trend_XML_Folder_"+current_datetime_with_seconds()
    newxmlIOfolder = os.path.join(directory2, output)
  
    newxmTrendfolder = os.path.join(directory3, output2)
    makexml(newxmlIOfolder)
    maketrendxml(newxmTrendfolder)
    ListOfVals=[]
    PointsMade = []
    point=[]
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            type = "0"  # Initialize type variable
            iopin = "0"  # Initialize iopin variable
            COVIncrement = "1"  # Initialize COVIncrement variable
            MaxPresValue = "0"  # Initialize MaxPresValue variable
            MinPresValue = "0"  # Initialize MinPresValue variable
            VarName = "0"  # Initialize VarName variable
            Description = "0"  # Initialize Description variable
            offset = "0"  # Initialize offset variable
            ElecTopOfScale = "0"  # Initialize ElecTopOfScale variable
            EngBottomOfScale = "0"  # Initialize EngBottomOfScale variable
            EngTopOfScale = "0"  # Initialize EngTopOfScale variable
            ThermistorType = "0"  # Initialize ThermistorType variable
            ActiveText =  "ALARM"
            InactiveText = "NORMAL"
            Unit = "Binary"
            # Skip the header row
            next(reader, None)
            i = 0
            for row in reader:
                i += 1
                
                if row[8] in ListOfVals:
                    print("Duplicated value")
                    
                else:
                    iopin=iopinString(row[6])
                    VarName=row[8]
                    type=row[14]
                    EngBottomOfScale=row[16]
                    EngTopOfScale = row[17]
                    ThermistorType=row[15]
                    ActiveText=row[19]
                    InactiveText=row[20]
                    unit=row[18]
                    BaseIO(type, iopin, COVIncrement, MaxPresValue, MinPresValue, VarName, Description,offset, ElecTopOfScale, EngBottomOfScale, EngTopOfScale,ThermistorType,ActiveText,InactiveText,newxmlIOfolder,unit)
                    trendIO(type, iopin, COVIncrement, MaxPresValue, MinPresValue, VarName, Description,offset, ElecTopOfScale, EngBottomOfScale, EngTopOfScale,ThermistorType,ActiveText,InactiveText,newxmTrendfolder,unit)

                    point={
                        'IO Name':row[8],
                        'Type Of Input':row[14],
                        'IO PIN Number': row[6],
                        'Eng Bottom Of Scale':row[16],
                        'Eng Top Of Scale' : row[17],
                        'Voltage Min-Max':row[15],
                        'Active Text':row[19],
                        "Inactive Text":row[20],
                        "COV Increment" : COVIncrement,
                        "Max Pressure Value" :MaxPresValue,
                        "Unit":unit

                    }
                    PointsMade.append(point)
                    ListOfVals.append(row[8])

                 
            
            return PointsMade 
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return 0  # Indicate error by returning 0

# Example usage

