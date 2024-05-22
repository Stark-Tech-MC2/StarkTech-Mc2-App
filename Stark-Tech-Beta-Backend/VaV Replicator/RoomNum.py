import xml.etree.ElementTree as ET

def RoomNum(root,Room):
    OgRoom="Room #"
    # Parse the XML file
    for element in root.iter():
        if 'Object' in element.attrib:
            # Check if the original name exists in the 'Object' attribute
            if OgRoom in element.attrib['Object']:
                # Replace the original name with the new name in the 'Object' attribute
                element.attrib['Object'] = element.attrib['Object'].replace(OgRoom, Room)
        if 'Value' in element.attrib:
            # Check if the original name exists in the 'Value' attribute
            if OgRoom in element.attrib['Value']:
                # Replace the original name with the new name in the 'Value' attribute
                element.attrib['Value'] = element.attrib['Value'].replace(OgRoom, Room)
        RoomNumoutput = OgRoom + " to " + Room

    return RoomNumoutput

   