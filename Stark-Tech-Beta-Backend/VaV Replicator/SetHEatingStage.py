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

   