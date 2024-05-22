from AO import AO
from AddIOP import AddIOP
from AI import AI
from DO import DO
from getmax import getmaxmin
from DI import DI
def BaseIO(type, iopin, COVIncrement, MaxPresValue, MinPresValue, VarName, Description,offset, ElecTopOfScale, EngBottomOfScale, EngTopOfScale,ThermistorType,ActiveText,InactiveText,newxmlIOfolder,unit):
  
    switch = {
        "AI": AI,
        "DI": DI,
        "AO": AO,
        "DO": DO
    }
    # Check if the type is in the switch dictionary
    if type in switch:
        # Call the function associated with the type
        switch[type](type, iopin, COVIncrement, MaxPresValue, MinPresValue, VarName, Description,offset, ElecTopOfScale, EngBottomOfScale, EngTopOfScale,ThermistorType,ActiveText,InactiveText,newxmlIOfolder,unit)
    else:
        print("Invalid type")