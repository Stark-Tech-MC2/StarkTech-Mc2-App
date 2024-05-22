

def getmaxmin(ThermistorType):
    # Split the ThermistorType string using the "-" delimiter
    min_max_values = ThermistorType.split("-")
    # Strip " VDC" from each value
    max_value = min_max_values[1].strip(" VDC")
    min_value = min_max_values[0].strip(" VDC")
    # Return the maximum and minimum values as separate strings
    return max_value, min_value