from AddIOP import AddIOP


def DI(type, iopin, COVIncrement, MaxPresValue, MinPresValue, VarName, Description,offset, ElecTopOfScale, EngBottomOfScale, EngTopOfScale,ThermistorType,ActiveText,InactiveText,newxmlIOfolder,unit):

        insertDI=f'''<OI DESCR="DigitalInput {Description} {VarName}" NAME="{VarName}" TYPE="bacnet.mpx.point.DigitalInput" flags="libExcluded">
      <PI Name="ActiveText" Value="{ActiveText}"/>
      <PI Name="BACnetName" Value="{VarName} (Input)"/>
      <PI Name="ForeignAddress" Value="&lt;binary-input,     621&gt;"/>
      <PI Name="InactiveText" Value="{InactiveText}"/>
      <PI Name="Terminal">
        <Reference DeltaFilter="0" Object="../../../../IO Resources/Onboard IO/{iopin}" Retransmit="0" TransferRate="10"/>
      </PI>
      <PI Name="Value" Type="udt.enum.aaaif6v63pob7ocsujg6mccqyx.aaaif6v63pob7ocsujg4ao466p"/>
    </OI>
    ''' 
        AddIOP( insertDI,newxmlIOfolder)
        
        # Your Digital Input code here