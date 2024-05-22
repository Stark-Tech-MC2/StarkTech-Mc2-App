def maketrendxml(file_path):
  
    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
    <ObjectSet ExportMode="Special" Note="TypesFirst" SemanticsFilter="Special" Version="5.0.3.117">
    <MetaInformation>
        <ExportMode Value="Special"/>
        <SemanticsFilter Value="None"/>
        <RuntimeVersion Value="5.0.3.117"/>
        <SourceVersion Value="5.0.3.117"/>
        <ServerFullPath Value="/OCPS 2024 Typicals"/>
    </MetaInformation>
    <ExportedObjects>
    <OI NAME="Trends" TYPE="system.base.Folder">
        <PI Name="ContentType">
        <Reference DeltaFilter="0" Locked="1" Object="~/System/Content Types/Trends" Retransmit="0" TransferRate="10"/>
        </PI>
        <PI Name="UseContentTypeFromRule" Value="0"/>



    </OI>



    </ExportedObjects>

    </ObjectSet>
    '''
    with open(file_path, 'w') as f:
        f.write(xml_content)