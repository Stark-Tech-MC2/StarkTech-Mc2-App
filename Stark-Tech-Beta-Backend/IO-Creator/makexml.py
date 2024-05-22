
def makexml(file_path):
    xml_content = '''<ObjectSet ExportMode="Special" Note="TypesFirst" SemanticsFilter="Special" Version="5.0.3.117">
  <MetaInformation>
    <ExportMode Value="Special" />
    <SemanticsFilter Value="None" />
    <RuntimeVersion Value="5.0.3.117" />
    <SourceVersion Value="5.0.3.117" />
    <ServerFullPath Value="/Typical" />
  </MetaInformation>
  <Types>
      <PropertyType Name="udt.enum.aaaif6v63pob7ocsujg6mccqyx.aaaif6v63pob7ocsujg4ao466p" DisplayName="Custom enumeration" Description="Custom enumeration" Base="system.pt.Boolean" RegExp=".*" Translate="1" EnumType="Strict" Icon="" Abstract="0">
                 <Enum Name="Normal" Value="0" />
                 <Enum Name="Alarm" Value="1" />
      </PropertyType>
      <PropertyType Name="udt.enum.aaaic256pscofocffvw36g7ybz.aaaic256pscofocffvwyaoqpds" DisplayName="Custom enumeration" Description="Custom enumeration" Base="system.pt.Boolean" RegExp=".*" Translate="1" EnumType="Strict" Icon="" Abstract="0">
                 <Enum Name="Off" Value="0" />
                 <Enum Name="On" Value="1" />
      </PropertyType>
  </Types>
  <ExportedObjects>
    <OI NAME="IO" TYPE="system.base.Folder">
      <PI Name="ContentType">
        <Reference DeltaFilter="0" Locked="1" Object="~/System/Content Types/BACnet IO" Retransmit="0" TransferRate="10" />
      </PI>
      <PI Name="UseContentTypeFromRule" Value="0" />
    </OI>
  </ExportedObjects>
</ObjectSet>'''
    # Write to the file
    with open(file_path, 'w') as f:
        f.write(xml_content)