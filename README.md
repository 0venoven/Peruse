# Setting up

## On Windows
### Prerequisites
- download [Microsoft Visual C++ 2008 Redistributable Package](https://www.microsoft.com/en-us/download/details.aspx?id=26368) (prerequisite for the item below)
- download [THC-Hydra binaries for Windows](https://github.com/maaaaz/thc-hydra-windows/archive/master.zip) and extract it directly without changing the folder directory
(note: turn off windows defender temporarily before downloading the files and only turn it back on after extracting them)
- install [nmap](https://nmap.org/dist/nmap-7.94-setup.exe) into its default path using its default options
### Installation
- clone this repository or download ZIP into your desired location
- enter the following commands into command prompt or PowerShell:
```rb
> cd {folder_path}\src
> pip install -r requirements.txt
```
### Running the program
- make sure to cd into the correct directory if you have not already done so
```rb
> python3 main3.py
```