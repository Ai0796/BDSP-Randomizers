# Pokemon Brilliant Diamond Shining Pearl Randomizer 
## by Aldo796, Copycat, SanGawku, XLuma, and Red.#9015

# Usage

1. Extract the archive
2. Run main.exe and select your randomization settings
3. Once you click the randomize button select your **romfs** folder
4. Once finished it will automatically open a folder called "mods" in your randomizer directory, that folder contains all the modding files needed already pre set for Yuzu, Ryujinx, and Atmosphere

<img width="78" alt="image" src="https://user-images.githubusercontent.com/36570430/146627870-89078799-c079-4003-ab84-83a94c657608.png">

# Building

- Due to use of switch statements Python 3.10+ is required
- Run pip install -r requirements.txt
- If using cx_freeze, manually drag the 'Randomizers' folder into 'lib' in the generated output

# Required Files

Right now our randomizer modifies 6 different files:
- masterdatas
- ev_script
- personal_masterdatas
- gamesettings
- UgData
- English (We only change the starter name on the english version)

You can get those files by dumping your cartridge via tools such as [NXDumpTool](https://github.com/DarkMatterCore/nxdumptool)
