def makeunit(unit, varname):
    print(unit)
    if unit == "Â°F":
        unit="0x280003"
        print("ferenheight")
        return unit
    if "FPM" in unit:
        unit = "0xF0004"
        print("fpm")
        return unit
    if "Pr" in varname:
        unit = "0x230005"
        print("pressue")
        return unit
    else:
        unit="0x200001"
        print("percent")
        return unit
    