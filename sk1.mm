#define VER_FILENAME.VER  sk1.Ver

#include "SK1.MMH"

<$DirectoryTree Key="INSTALLDIR" Dir="c:\program files\sK1 Project\sK1" CHANGE="\" PrimaryFolder="Y">
<$Files "msi_build\*.*" DestDir="INSTALLDIR" SubDir="TREE">

<$Component "AdvertisedShortcut" Create="Y" Directory_="INSTALLDIR">
    ;--- Add the files to the "TryMe" component -----------------------------
    <$File SOURCE="msi_build\sk1.exe" KeyPath="Y">

    #(
        <$Shortcut
                   Dir="ProgramMenuFolder"
               Feature="."
                 Title="sK1 illustration program"
           Description=^sK1 illustration program^
                  Icon="@.\sk1.ico"
               WorkDir="INSTALLDIR"
        >
    #)
<$/Component>
