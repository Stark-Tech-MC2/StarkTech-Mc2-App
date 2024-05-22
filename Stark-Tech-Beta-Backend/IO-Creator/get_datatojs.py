import os
import json
from get_data import get_data

def main(filename):
    # Your main function logic here
    
   

   
    get_data(filename)
    #print("we printed information", information)
   
    # Prepare data to send back to Electron
    data_to_send = {
        'information': "information"
    }
    
    # Serialize data to JSON format
    json_data = json.dumps(data_to_send)
    
    # Output JSON data
    

# Receive data from Electron's main process
def receive_data():
    print("Waiting for data...")
    try:
        # Read data from stdin
        data_from_electron = input().rstrip()
        print("Data received from Electron:", data_from_electron)
        
        # Deserialize JSON data
        #data = json.loads(data_from_electron)

        # Access individual strings
      

        # Call the main function with the data received from Electron
        print("Values received in main:",data_from_electron)
        main(data_from_electron)
    except Exception as e:

        print("WE ARE DUMMIES Error:", e)

receive_data()
