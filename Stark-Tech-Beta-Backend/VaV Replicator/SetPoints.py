def SetPoints(root, NewMaxFlowSetpoint, NewMinFlowSetpoint, NewIntermediateFlowSetpoint):
    """
    Edits the MaxFlowSetpoint and MinFlowSetpoint values in the XML file.
    Does converstion From American units in the spreadsheet to metric, as the xml bacnet is coded in metric 
    Parameters:
    root (Element): Root element of the XML file.
    NewMaxFlowSetpoint (str): New value for MaxFlowSetpoint.
    NewMinFlowSetpoint (str): New value for MinFlowSetpoint.
    """
     # Convert strings to doubles
    max_flow_ft3_per_min = float(NewMaxFlowSetpoint)
    min_flow_ft3_per_min = float(NewMinFlowSetpoint)
    mid_flow_ft3_per_min = float(NewIntermediateFlowSetpoint)
    # Conversion factors
    ft3_to_l = 28.3168466 / 60  # Conversion factor from ft³/min to L/s

    # Convert to metric
    max_flow_l_per_s = max_flow_ft3_per_min * ft3_to_l
    min_flow_l_per_s = min_flow_ft3_per_min * ft3_to_l
    mid_flow_l_per_s = mid_flow_ft3_per_min * ft3_to_l
    # Convert doubles back to strings
    NewMaxFlowSetpoint = str(max_flow_l_per_s)
    NewMinFlowSetpoint = str(min_flow_l_per_s)
    NewIntermediateFlowSetpoint = str(mid_flow_l_per_s)
    # Find all elements with 'PI' tag name
    for element in root.iter('PI'):
        # Check if the attribute 'Name' is 'MaxFlowSetpoint' or 'MinFlowSetpoint'
        if element.attrib.get('Name') == 'MaxFlowSetpoint':
            # Update the 'Value' attribute with the new MaxFlowSetpoint value
            element.set('Value', NewMaxFlowSetpoint)
        elif element.attrib.get('Name') == 'MinFlowSetpoint':
            # Update the 'Value' attribute with the new MinFlowSetpoint value
            element.set('Value', NewMinFlowSetpoint)
        elif element.attrib.get('Name') == 'IntermediateFlowSetpoint':
            # Update the 'Value' attribute with the new MinFlowSetpoint value
            element.set('Value', NewIntermediateFlowSetpoint)

    print(f"Updated MaxFlowSetpoint to '{NewMaxFlowSetpoint}' and MinFlowSetpoint to '{NewMinFlowSetpoint}' and MidFlowSetPoint to {NewIntermediateFlowSetpoint}, Keep in Mind this is METRIC")
    SetPointsoutput = f"Updated MaxFlowSetpoint to '{NewMaxFlowSetpoint}' and MinFlowSetpoint to '{NewMinFlowSetpoint}' and MidFlowSetPoint to {NewIntermediateFlowSetpoint}, Keep in Mind this is METRIC"
    return SetPointsoutput