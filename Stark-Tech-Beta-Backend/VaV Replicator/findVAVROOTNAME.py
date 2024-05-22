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