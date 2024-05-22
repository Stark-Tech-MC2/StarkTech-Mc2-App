
import xml.etree.ElementTree as ET



def addtrend(xml_to_insert,newxmlTrendfolder):
    # Parse the XML file
    print("we are here in addtrend",newxmlTrendfolder )
    tree = ET.parse(newxmlTrendfolder)
    root = tree.getroot()

    # Find the location to insert the XML snippet
    oi_elements = root.findall('.//OI[@NAME="Trends"]')
    
    # Check if there are any matching elements
    if oi_elements:
        # Assuming you want to insert into all matching elements
        for oi_element in oi_elements:
            # Parse the XML snippet to insert
            new_xml = ET.fromstring(xml_to_insert)

            # Insert the new XML snippet
            oi_element.append(new_xml)
    else:
        print("No <OI NAME='Trends'> elements found in the XML file.")

    # Write the updated XML back to the file
    tree.write(newxmlTrendfolder)
    