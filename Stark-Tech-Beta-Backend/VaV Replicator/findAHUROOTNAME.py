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