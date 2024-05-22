import os
import json
from get_data import get_data

def main(data1, data2, data3, data4):
    # Your main function logic here
    print("Received data:", data1, data2, data3, data4)

    directory = os.path.join(os.path.dirname(__file__), 'Spreadsheets')
    filename = data3 
    filename = os.path.join(directory, filename)
    directory1 = os.path.join(os.path.dirname(__file__), 'Template VAV SCR Controlers')
    XMLFILESCR = data1
    XMLFILESCR = os.path.join(directory1, XMLFILESCR)
    directory2 = os.path.join(os.path.dirname(__file__), 'Template Cooling Only VAV Controlers')
    XMLFILECOOLIN = data2 
    XMLFILECOOLIN = os.path.join(directory2, XMLFILECOOLIN)
    directory3 = os.path.join(os.path.dirname(__file__), 'Template Staged Heating VAV Controlers')
    XMLStageCooling = data4 
    XMLStageCooling = os.path.join(directory3, XMLStageCooling)
   
    num_rows, information = get_data(filename, XMLFILESCR, XMLFILECOOLIN, XMLStageCooling)
    #print("we printed information", information)
    
    # Prepare data to send back to Electron
    data_to_send = {
        'num_rows': num_rows,
        'information': information
    }
    
    # Serialize data to JSON format
    #json_data = json.dumps(data_to_send)
    
    # Output JSON data
    #print(json_data)

# Receive data from Electron's main process
def receive_data():
    print("Waiting for data...")
    try:
        # Read data from stdin
        data_from_electron = input().rstrip()
        print("Data received from Electron:", data_from_electron)
        
        # Deserialize JSON data
        data = json.loads(data_from_electron)

        # Access individual strings
        SCRVAV = data['SCRVAV']
        CoolingOnlyVAV = data['CoolingOnlyVAV']
        Spreadsheet = data['Spreadsheet']
        StagedVaV = data['StagedVaV']

        # Call the main function with the data received from Electron
        print("Values received in main:", SCRVAV, CoolingOnlyVAV, Spreadsheet, StagedVaV)
        main(SCRVAV, CoolingOnlyVAV, Spreadsheet, StagedVaV)
    except Exception as e:
        print("Error:", e)

receive_data()
