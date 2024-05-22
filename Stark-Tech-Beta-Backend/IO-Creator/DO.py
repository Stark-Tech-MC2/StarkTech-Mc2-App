from AddIOP import AddIOP


def DO(type, iopin, COVIncrement, MaxPresValue, MinPresValue, VarName, Description,offset, ElecTopOfScale, EngBottomOfScale, EngTopOfScale,ThermistorType,ActiveText,InactiveText,newxmlIOfolder,unit):
        
        insert=f'''<OI DESCR="Digital Output {VarName}nb{Description}" NAME="{VarName}" TYPE="bacnet.mpx.point.DigitalOutput" flags="libExcluded">
      <PI Name="ActiveText" Value="{ActiveText}"/>
      <PI Name="BACnetName" Value="{VarName}"/>
      <PI Name="ForeignAddress" Value="&lt;binary-output,     290&gt;"/>
      <PI Name="InactiveText" Value="{InactiveText}"/>
      <PI Name="Priority1" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds"/>
      <PI Name="Priority10" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds" VariableReference="Application">
        <Reference DeltaFilter="0" Object="../../../Programs/{VarName}Control" Property="{VarName}_P10" Retransmit="0" TransferRate="10"/>
      </PI>
      <PI Name="Priority11" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds"/>
      <PI Name="Priority12" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds"/>
      <PI Name="Priority13" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds"/>
      <PI Name="Priority14" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds"/>
      <PI Name="Priority15" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds"/>
      <PI Name="Priority16" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds"/>
      <PI Name="Priority2" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds"/>
      <PI Name="Priority3" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds"/>
      <PI Name="Priority4" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds"/>
      <PI Name="Priority5" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds"/>
      <PI Name="Priority6" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds"/>
      <PI Name="Priority7" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds"/>
      <PI Name="Priority8" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds"/>
      <PI Name="Priority9" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds"/>
      <PI Name="RelinquishDefault" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds"/>
      <PI Name="Terminal">
        <Reference DeltaFilter="0" Object="../../../../IO Resources/Onboard IO/DO 2" Retransmit="0" TransferRate="10"/>
      </PI>
      <PI Name="Value" Type="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds"/>
    </OI>


        '''
        AddIOP(insert,newxmlIOfolder)
        # Your Digital Output code here
