from AddIOP import AddIOP
from getmax import getmaxmin
from unitsparser import makeunit

def AI(type, iopin, COVIncrement, MaxPresValue, MinPresValue, VarName, Description,offset, ElecTopOfScale, EngBottomOfScale, EngTopOfScale,ThermistorType,ActiveText,InactiveText,newxmlIOfolder,unit):
        # Your Analog Input code here
        unit=makeunit(unit, VarName)
        if ThermistorType == "2-10 VDC" or ThermistorType == "0-10 VDC":
            ElecTopOfScale, ElecBottomOfScale=getmaxmin(ThermistorType)
            insertvoltage = f'''<OI DESCR="Voltage Derived Analog Input {Description}" NAME="{VarName}" TYPE="bacnet.mpx.point.VoltageInput" flags="libExcluded">
        <PI Name="BACnetName" Value="{VarName}"/>
        <PI Name="COVIncrement" Unit="{unit}" Value="{COVIncrement}"/>
        <PI Name="ElecTopOfScale" Value="{ElecTopOfScale}"/>
        <PI Name="ElecBottomOfScale" Value="{ElecBottomOfScale}"/>
        <PI Name="EngBottomOfScale" Unit="{unit}" Value="{EngBottomOfScale}"/>
        <PI Name="EngTopOfScale" Unit="{unit}" Value="{EngTopOfScale}"/>
        <PI Name="ForeignAddress" Value="&lt;analog-input,     625&gt;"/>
        <PI Name="MaxPresValue" Unit="{unit}" Value="{MaxPresValue}"/>
        <PI Name="MinPresValue" Unit="{unit}" Value="{MinPresValue}"/>
        <PI Name="Offset" Unit="{unit}" Value="{offset}"/>
        <PI Name="Terminal">
            <Reference DeltaFilter="0" Object="../../../../IO Resources/Onboard IO/{iopin}" Retransmit="0" TransferRate="10"/>
        </PI>
        <PI Name="Value" Unit="{unit}"/>
        </OI> 
        '''
            AddIOP( insertvoltage,newxmlIOfolder)
        else:                     
            if ThermistorType == "10K Thermistor (Curve 3) w/11K Shunt":
                ThermistorType="7"
            else:
                ThermistorType="0"
            inserttemperture = f'''<OI DESCR="Temperture Derived Analog Input {Description}" NAME="{VarName}" TYPE="bacnet.mpx.point.TemperatureInput" flags="libExcluded">
        <PI Name="BACnetName" Value="{VarName}" />
        <PI Name="COVIncrement" Unit="{unit}" Value="{COVIncrement}" />
        <PI Name="ForeignAddress" Value="&lt;analog-input,      20&gt;" />
        <PI Name="MaxPresValue" Unit="{unit}" Value="{MaxPresValue}" />
        <PI Name="MinPresValue" Unit="{unit}" Value="{MinPresValue}" />
        <PI Name="Offset" Unit="{unit}" Value="{offset}" />
        <PI Name="Terminal">
            <Reference DeltaFilter="0" Object="../../../../IO Resources/Onboard IO/{iopin}" Retransmit="0" TransferRate="10" />
        </PI>
        <PI Name="ThermistorType" Value="{ThermistorType}" />
        <PI Name="Value" Unit="{unit}" />
        </OI>
        '''
            AddIOP( inserttemperture, newxmlIOfolder)