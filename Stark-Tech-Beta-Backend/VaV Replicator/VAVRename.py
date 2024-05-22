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
    VAVRenameoutput=f"Replaced all instances of '{OriginalVaVName}' with '{NewVaVName}' in the 'NAME' and 'Value' attributes of the XML."
    return VAVRenameoutput