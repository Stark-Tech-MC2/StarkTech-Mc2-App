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
    AHURenameoutput= f"Replaced all instances of '{OriginalAHU}' with '{NewAHUName}' in the 'Object' and 'Value' attributes of the XML."
    return AHURenameoutput