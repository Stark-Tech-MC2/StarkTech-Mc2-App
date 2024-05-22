from AddIOP import AddIOP
from getmax import getmaxmin
from unitsparser import makeunit


def AO(type, iopin, COVIncrement, MaxPresValue, MinPresValue, VarName, Description,offset, ElecTopOfScale, EngBottomOfScale, EngTopOfScale,ThermistorType,ActiveText,InactiveText,newxmlIOfolder,unit):
        unit=makeunit(unit, VarName)
        ElecTopOfScale, ElecBottomOfScale=getmaxmin(ThermistorType)
        insert=f'''<OI DESCR="Voltage Derived Analog Output {Description}" NAME="{VarName}" TYPE="bacnet.mpx.point.VoltageOutput" flags="libExcluded">
      <PI Name="BACnetName" Value="{VarName}"/>
      <PI Name="COVIncrement" Unit="{unit}" Value="{COVIncrement}"/>
      <PI Name="ElecBottomOfScale" Value="{ElecBottomOfScale}"/>
      <PI Name="ElecTopOfScale" Value="{ElecTopOfScale}"/>
      <PI Name="EngBottomOfScale" Unit="{unit}" Value="{EngBottomOfScale}"/>
      <PI Name="EngTopOfScale" Unit="{unit}" Value="{EngTopOfScale}"/>
      <PI Name="ForeignAddress" Value="&lt;analog-output,     628&gt;"/>
      <PI Name="MaxPresValue" Unit="{unit}" Value="{MaxPresValue}"/>
      <PI Name="MinPresValue" Unit="{unit}" Value="{MinPresValue}"/>
      <PI Name="Priority10" VariableReference="Application">
        <Reference DeltaFilter="0" Object="../../../Programs/{VarName}Ctrl" Property="{VarName}_p10" Retransmit="0" TransferRate="10"/>
      </PI>
      <PI Name="Terminal">
        <Reference DeltaFilter="0" Object="../../../../IO Resources/Onboard IO/{iopin}" Retransmit="0" TransferRate="10"/>
      </PI>
      <PI Name="Value" Unit="{unit}"/>
    </OI>
        '''
        AddIOP( insert,newxmlIOfolder)
       
        