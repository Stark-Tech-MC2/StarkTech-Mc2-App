import xml.etree.ElementTree as ET
import csv
import tkinter as tk
from tkinter import filedialog
import os
import tkinter as tk
from tkinter import messagebox
import re
# Define the process_string function
def process_string(text):
    """
    Processes a string by adding leading zeros for single digits, removing spaces,
    replacing periods with hyphens, and keeping consecutive digits unchanged.

    Args:
        text: The input string to be processed.

    Returns:
        The processed string.
    """
    result = ""
    prev_char = ""  # Track the previous character

    for char in text:
        if char.isdigit():
            # Add leading zero only if single digit and not preceded by another digit or hyphen
            if len(result) > 0 and not prev_char.isdigit() and prev_char != "-":
                result += "0"
            result += char
        elif char == " ":
            result += "-"
        elif char == ".":
            if prev_char.isdigit():
                # Replace period with hyphen only if preceded by a digit
                result += "-"
            else:
                # Treat period as part of consecutive digits
                result += char
        else:
            result += char

        prev_char = char  # Update previous character for all characters

    # Remove any trailing hyphens
    result = result.rstrip("-")

    # Add leading zero to the last part if it's a single digit
    parts = result.split("-")
    last_part = parts[-1]
    if len(last_part) == 1 and last_part.isdigit():
        parts[-1] = "0" + last_part

    result = "-".join(parts)

    return result

def edit_xml(NewVaVName, XMLFILE,OriginalAHU,OriginalVaVName,NewAHUNAme,NewMaxFlowSetpoint,NewMinFlowSetpoint,NewIntermediateFlowSetpoint,BoxCoef,heatingstage):
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
       
        SetPoints(root,NewMaxFlowSetpoint,NewMinFlowSetpoint,NewIntermediateFlowSetpoint)
        VAVRename(root, NewVaVName,OriginalVaVName)
        AHURename(root,OriginalAHU,NewAHUNAme)
        if int(heatingstage) > 0:
            SetHEatingStage(root,heatingstage)
        # Write the modified XML tree to the file
        
       
        NewFileName = os.path.join(output_folder_pathforSpreadsheets, NewVaVName + '.xml')

        tree.write(NewFileName)
        print(f"XML file edited and saved successfully: {XMLFILE}")
    except FileNotFoundError:
        print(f"Error: File not found: {XMLFILE}")
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")

# Example edit function: Change the name of the first person element to "Jane Doe"
def findVAVROOTNAME(root):
    instances = []
    pattern = r'VAV-\d{2}-\d{2}|VAV-\d{2}'  # Regex pattern to match 'VAV-xx-xx'

    # Search through the XML tree for 'OI' elements
    for element in root.iter('OI'):
        # Get the value of the 'NAME' attribute
        name = element.get('NAME')
        if name is not None:
            # Use re.findall to find all instances of the pattern in the 'NAME' attribute
            matches = re.findall(pattern, name)
            if matches:
                instances.extend(matches)
    count = len(instances)
    print(instances)
    if instances:
        first_instance = instances[0]
        for instance in instances[1:]:
            if instance != first_instance:
                return [], 0
        return instances, len(instances), instances[0]
    else:
        return [], 0
def findAHUROOTNAME(root):
    instances = []
    pattern = r'AHU-\d{2}-\d{2}|AHU-\d{2}'  # Regex pattern to match 'AHU-xx-xx' or 'AHU-xx'

    # Search through the XML tree for 'PI' elements
    for element in root.iter('PI'):
        # Get the value of the 'Name' attribute
        name = element.get('Name')
        if name is not None:
            # Use re.findall to find all instances of the pattern in the 'Name' attribute
            matches = re.findall(pattern, name)
            if matches:
                instances.extend(matches)
    count = len(instances)
    print(instances)
    if instances:
        first_instance = instances[0]
        for instance in instances[1:]:
            if instance != first_instance:
                return [], 0
        return instances, len(instances), instances[0]
    else:
        return [], 0
def VAVRename(root, NewVaVName, OriginalVaVName):
    """
    Edits all instances of the original name with the new name in the 'NAME' and 'Value' attributes of the XML file.

    Args:
        root: The root element of the parsed XML tree.
        NewVaVName: The new name to replace the original name in the XML file.
        OriginalVaVName: The original name to replace in the XML file.
    """

    # Find all elements with any tag name that contain 'NAME' or 'Value' attribute
    for element in root.iter():
        if 'NAME' in element.attrib:
            # Check if the original name exists in the 'NAME' attribute
            if OriginalVaVName in element.attrib['NAME']:
                # Replace the original name with the new name in the 'NAME' attribute
                element.attrib['NAME'] = element.attrib['NAME'].replace(OriginalVaVName, NewVaVName)
        if 'DESCR' in element.attrib:
            # Check if the original name exists in the 'NAME' attribute
            if OriginalVaVName in element.attrib['DESCR']:
                # Replace the original name with the new name in the 'NAME' attribute
                element.attrib['DESCR'] = element.attrib['DESCR'].replace(OriginalVaVName, NewVaVName)
        if 'Value' in element.attrib:
            # Check if the original name exists in the 'Value' attribute
            if OriginalVaVName in element.attrib['Value']:
                # Replace the original name with the new name in the 'Value' attribute
                element.attrib['Value'] = element.attrib['Value'].replace(OriginalVaVName, NewVaVName)
        if 'Object' in element.attrib:
            # Check if the original name exists in the 'Value' attribute
            if OriginalVaVName in element.attrib['Object']:
                # Replace the original name with the new name in the 'Value' attribute
                element.attrib['Object'] = element.attrib['Object'].replace(OriginalVaVName, NewVaVName)
        # Check if the line matches the specified line
       

    print(f"Replaced all instances of '{OriginalVaVName}' with '{NewVaVName}' in the 'NAME' and 'Value' attributes of the XML.")

# Example usage:
# Assume 'root' is the root element of your parsed XML tree
# VAVRename(root, "NewName", "OldName")


def AHURename(root, OriginalAHU, NewAHUName):
    """
    Edits all instances of the original name with the new name in the 'NAME' and 'Value' attributes of the XML file.

    Args:
        root: The root element of the parsed XML tree.
        OriginalAHU: The original name to replace in the XML file.
        NewAHUName: The new name to replace the original name in the XML file.
    """
 
    # Find all elements with any tag name that contain 'NAME' or 'Value' attribute
    for element in root.iter():
        if 'Object' in element.attrib:
            # Check if the original name exists in the 'Object' attribute
            if OriginalAHU in element.attrib['Object']:
                # Replace the original name with the new name in the 'Object' attribute
                element.attrib['Object'] = element.attrib['Object'].replace(OriginalAHU, NewAHUName)
        if 'Value' in element.attrib:
            # Check if the original name exists in the 'Value' attribute
            if OriginalAHU in element.attrib['Value']:
                # Replace the original name with the new name in the 'Value' attribute
                element.attrib['Value'] = element.attrib['Value'].replace(OriginalAHU, NewAHUName)

    print(f"Replaced all instances of '{OriginalAHU}' with '{NewAHUName}' in the 'Object' and 'Value' attributes of the XML.")
def SetPoints(root, NewMaxFlowSetpoint, NewMinFlowSetpoint, NewIntermediateFlowSetpoint):
    """
    Edits the MaxFlowSetpoint and MinFlowSetpoint values in the XML file.
    Does converstion From American units in the spreadsheet to metric, as the xml bacnet is coded in metric 
    Parameters:
    root (Element): Root element of the XML file.
    NewMaxFlowSetpoint (str): New value for MaxFlowSetpoint.
    NewMinFlowSetpoint (str): New value for MinFlowSetpoint.
    """
     # Convert strings to doubles
    max_flow_ft3_per_min = float(NewMaxFlowSetpoint)
    min_flow_ft3_per_min = float(NewMinFlowSetpoint)
    mid_flow_ft3_per_min = float(NewIntermediateFlowSetpoint)
    # Conversion factors
    ft3_to_l = 28.3168466 / 60  # Conversion factor from ft³/min to L/s

    # Convert to metric
    max_flow_l_per_s = max_flow_ft3_per_min * ft3_to_l
    min_flow_l_per_s = min_flow_ft3_per_min * ft3_to_l
    mid_flow_l_per_s = mid_flow_ft3_per_min * ft3_to_l
    # Convert doubles back to strings
    NewMaxFlowSetpoint = str(max_flow_l_per_s)
    NewMinFlowSetpoint = str(min_flow_l_per_s)
    NewIntermediateFlowSetpoint = str(mid_flow_l_per_s)
    # Find all elements with 'PI' tag name
    for element in root.iter('PI'):
        # Check if the attribute 'Name' is 'MaxFlowSetpoint' or 'MinFlowSetpoint'
        if element.attrib.get('Name') == 'MaxFlowSetpoint':
            # Update the 'Value' attribute with the new MaxFlowSetpoint value
            element.set('Value', NewMaxFlowSetpoint)
        elif element.attrib.get('Name') == 'MinFlowSetpoint':
            # Update the 'Value' attribute with the new MinFlowSetpoint value
            element.set('Value', NewMinFlowSetpoint)
        elif element.attrib.get('Name') == 'IntermediateFlowSetpoint':
            # Update the 'Value' attribute with the new MinFlowSetpoint value
            element.set('Value', NewIntermediateFlowSetpoint)

    print(f"Updated MaxFlowSetpoint to '{NewMaxFlowSetpoint}' and MinFlowSetpoint to '{NewMinFlowSetpoint}' and MidFlowSetPoint to {NewIntermediateFlowSetpoint}, Keep in Mind this is METRIC")

def SetHEatingStage(root, heatingstage):
    # Parse the XML file
    
    StageHeating ="Staged Heating"
    newstageheting= StageHeating+" "+heatingstage
    # Find the specific element
    for element in root.iter():
        if element.tag == 'PI' and \
           element.get('Name') == 'Value' and \
           element.get('RetainLevel') == 'ColdStart' and \
           element.get('Value') == '2':
            # Update the value of the 'Value' attribute
            element.set('Value', heatingstage)
        if 'DESCR' in element.attrib:
            # Check if the original name exists in the 'NAME' attribute
            if StageHeating in element.attrib['DESCR']:
                # Replace the original name with the new name in the 'NAME' attribute
                element.attrib['DESCR'] = element.attrib['DESCR'].replace(StageHeating, newstageheting)

   
    
    

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
                    OriginalVaVName="VAV-05-09"
                    OriginalAHU="AHU-05"
                    NewAHUNAme=process_string(NewAHUNAme)
                    NewVaVName=process_string(NewVaVName)
                    # Edit the XML file
                    XMLFILE = "Template Cooling Only VAV Controlers/RP-V-5A.xml"
                    edit_xml(NewVaVName, XMLFILECOOLIN,OriginalAHU,OriginalVaVName,NewAHUNAme,NewMaxFlowSetpoint,NewMinFlowSetpoint,NewIntermediateFlowSetpoint,BoxCoef,heatingstage)
                if row[12] == 'SCR EH':
                    print("Condition met at row", i)
                   
                    NewVaVName= row[0]
                    NewAHUNAme=row[2]
                    NewMaxFlowSetpoint = row[13]
                    NewMinFlowSetpoint = row[14]
                    NewIntermediateFlowSetpoint = row[16]
                    BoxCoef= row[27]
                    OriginalVaVName="VAV-01-01-01"
                    OriginalAHU="AHU-01-01"
                    NewAHUNAme=process_string(NewAHUNAme)
                    NewVaVName=process_string(NewVaVName)
                    XMLFILE = "Template VAV SCR Controlers/RP-V4-A.xml"
                    edit_xml(NewVaVName, XMLFILESCR,OriginalAHU,OriginalVaVName,NewAHUNAme,NewMaxFlowSetpoint,NewMinFlowSetpoint,NewIntermediateFlowSetpoint, BoxCoef,heatingstage)
                if row[12] is not None and row[12] not in ['None', 'SCR EH']:
                    print("Condition met at row", i)
                  
                    NewVaVName= row[0]
                    NewAHUNAme=row[2]
                    NewMaxFlowSetpoint = row[13]
                    NewMinFlowSetpoint = row[14]
                    NewIntermediateFlowSetpoint = row[16]
                    BoxCoef= row[27]
                    OriginalVaVName="VAV-1-1-1"
                    OriginalAHU="AHU-01-01"
                    NewAHUNAme=process_string(NewAHUNAme)
                    NewVaVName=process_string(NewVaVName)
                    XMLFILE = "Template VAV SCR Controlers/RP-V4-A.xml"
                    heatingstage=0
                    if "2" in row[12]:
                        print("two stage")
                        heatingstage="2"
                    if "3" in row[12]:
                        print("3 stage")
                        heatingstage="3"
                    

                    edit_xml(NewVaVName, XMLStageCooling,OriginalAHU,OriginalVaVName,NewAHUNAme,NewMaxFlowSetpoint,NewMinFlowSetpoint,NewIntermediateFlowSetpoint,BoxCoef,heatingstage)
            
            
            return i  # Count the rows excluding header
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return 0  # Indicate error by returning 0

# Example usage


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
def on_drop(event):
    file_path = event.data
    if file_path:
        file_name = os.path.basename(file_path)
        destination = os.path.join(script_dir, file_name)
        try:
            os.rename(file_path, destination)
            status_label.config(text=f"File '{file_name}' saved to {script_dir}")
        except Exception as e:
            status_label.config(text=f"Error: {e}")
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
def main():
    # Create the main window
    root = tk.Tk()
    root.title("VaV Duplicator")
    
    # Create a label widget
    label = tk.Label(root, text="Duplicate your VAV")
    label.pack()

    # Create a button widget
    button = tk.Button(root, text="Duplicate", command=lambda: display_message(selected_option, selected_option1, selected_option2,selected_option3))
    button.pack()
    button2 = tk.Button(root, text="Display Files", command=display_files)
    button2.pack()
    

    # Create radiobuttons
    selected_option = tk.StringVar()
    selected_option1 = tk.StringVar()
    selected_option2 = tk.StringVar()
    selected_option3 = tk.StringVar()
    

    # Run the main event loop
    global script_dir
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_nameforSpreadsheets = "Spreadsheets"
    folder_pathforSpreadsheets = os.path.join(script_dir, folder_nameforSpreadsheets)
    files_in_SpreadsheetsFolder = os.listdir(folder_pathforSpreadsheets)
    folder_nameforSCR = "Template VAV SCR Controlers"
    folder_pathforSCR = os.path.join(script_dir, folder_nameforSCR)
    files_in_SCRFolder = os.listdir(folder_pathforSCR)
    folder_nameforCooling = "Template Cooling Only VAV Controlers"
    folder_pathforCooling = os.path.join(script_dir, folder_nameforCooling)
    files_in_CoolingFolder = os.listdir(folder_pathforCooling)
    folder_nameforstage = "Template Staged Heating VAV Controlers"
    folder_pathforstage = os.path.join(script_dir, folder_nameforstage)
    files_in_stageHeating = os.listdir(folder_pathforstage)

    # Create a status label
    global status_label
    title_label = tk.Label(root, text="Heating And Cooling VAV:")
    title_label.pack(anchor=tk.W)
    display_label = tk.Label(root, textvariable=selected_option)
    display_label.pack()

    options = [("None", "None")]
    options.extend((file_name, file_name) for file_name in files_in_SCRFolder)
    for text, value in options:
        radio_button = tk.Radiobutton(root, text=text, variable=selected_option, value=value, command=display_selection(selected_option))
        radio_button.pack(anchor=tk.W)


    title_label = tk.Label(root, text="Cooling Only VAV:")
    title_label.pack(anchor=tk.W)
    display_label = tk.Label(root, textvariable=selected_option1)
    display_label.pack()
    options1 = [("None", "None")]
    options1.extend((file_name, file_name) for file_name in files_in_CoolingFolder)
    for text1, value1 in options1:
        radio_button = tk.Radiobutton(root, text=text1, variable=selected_option1, value=value1, command=display_selection1(selected_option1))
        radio_button.pack(anchor=tk.W)


    title_label = tk.Label(root, text="Multiple Stage Heating:")
    title_label.pack(anchor=tk.W)
    display_label = tk.Label(root, textvariable=selected_option2)
    display_label.pack()

    options3 = [("None", "None")]
    options3.extend((file_name, file_name) for file_name in files_in_stageHeating)
    for text3, value3 in options3:
        radio_button = tk.Radiobutton(root, text=text3, variable=selected_option3, value=value3, command=display_selection3(selected_option3))
        radio_button.pack(anchor=tk.W)










    
    title_label = tk.Label(root, text="Spreadsheets:")
    title_label.pack(anchor=tk.W)
    display_label = tk.Label(root, textvariable=selected_option2)
    display_label.pack()
    
    options2 = [(file_name, file_name) for file_name in files_in_SpreadsheetsFolder]
    for text2, value2 in options2:
        radio_button2 = tk.Radiobutton(root, text=text2, variable=selected_option2, value=value2, command=display_selection2(selected_option2))
        radio_button2.pack(anchor=tk.W)
        

    status_label = tk.Label(root, text="Click 'Display Files' to show all files in this directory.")
    status_label.pack()
    file_list = "\n".join(files_in_SpreadsheetsFolder)
    status_label.config(text=f"Files in directory:\n{file_list}")
    


    root.mainloop()

if __name__ == "__main__":
    main()