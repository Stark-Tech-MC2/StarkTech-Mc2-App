import xml.etree.ElementTree as ET



def AddIOP(xml_to_insert,newxmlIOfolder):
    # Parse the XML file
    xmlfilename= r"C:\Users\ponced\IO Creator\CreatedIO\NewIO.xml"
    
    tree = ET.parse(newxmlIOfolder)
    root = tree.getroot()

    # Find the location to insert the XML snippet
    oi_elements = root.findall('.//OI[@NAME="IO"]')
    
    # Check if there are any matching elements
    if oi_elements:
        # Assuming you want to insert into all matching elements
        for oi_element in oi_elements:
            # Parse the XML snippet to insert
            new_xml = ET.fromstring(xml_to_insert)

            # Insert the new XML snippet
            oi_element.append(new_xml)
    else:
        print("No <OI NAME='IO'> elements found in the XML file.")

    # Write the updated XML back to the file
    tree.write(newxmlIOfolder)