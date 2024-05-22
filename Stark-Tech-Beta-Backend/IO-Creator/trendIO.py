from addtrend import addtrend


def trendIO(type, iopin, COVIncrement, MaxPresValue, MinPresValue, VarName, Description,offset, ElecTopOfScale, EngBottomOfScale, EngTopOfScale,ThermistorType,ActiveText,InactiveText,newxmlIOfolder,unit):
    if type not in ["AI", "DI", "AO", "DO"]:
        print(type)
        print("we are returing")
        return
    if type in ["AI","AO"]:
      insertDI=f'''<OI NAME="{VarName}" TYPE="trend.TLog">
        <PI Name="DeltaValue" Value="0.10000000000000001"/>
        <PI Name="LogArray" Unit="0x280003"/>
        <PI Name="LogPoint" Unit="0x280003">
          <Reference DeltaFilter="0" Object="../../Values/IO/{VarName}" Property="Value" Retransmit="0" TransferRate="10"/>
        </PI>
        <PI Name="MeterEndTime" Value="Tx05bbf05af16e5728"/>
        <PI Name="MeterStartTime" Value="Tx05bbf05af16e5728"/>
        <PI Name="MeterTime" Value="Tx05bbf05af1723c28"/>
        <PI Name="StartTime" Value="Tx0610ebccd2f40028"/>
        <PI Name="Enabled" Value="1"/>
      </OI>
      ''' 
      addtrend(insertDI,newxmlIOfolder)
      return
    else:
      insertDI=f'''<OI NAME="{VarName}" TYPE="trend.TLogChangeOfValue">
      <PI Name="LogPoint">
        <Reference DeltaFilter="0" Object="../../Values/IO/{VarName}" Property="Value" Retransmit="0" TransferRate="10"/>
      </PI>
      <PI Name="MeterEndTime" Value="Tx05b37104022b6e28"/>
      <PI Name="MeterStartTime" Value="Tx05b37104022b6e28"/>
      <PI Name="MeterTime" Value="Tx05b3710402333528"/>
      <PI Name="StartTime" Value="Tx0610ebccd2f40028"/>
      <PI Name="Enabled" Value="1"/>
    </OI>
      '''
      addtrend(insertDI,newxmlIOfolder)
      return