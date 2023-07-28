# Setting up

## On Windows
### Prerequisites
- download [Microsoft Visual C++ 2008 Redistributable Package](https://www.microsoft.com/en-us/download/details.aspx?id=26368) (prerequisite for [THC-Hydra binaries for Windows](https://github.com/maaaaz/thc-hydra-windows/archive/master.zip))
- install [nmap](https://nmap.org/dist/nmap-7.94-setup.exe) into its default path using its default options
### Installation
- clone this repository or download ZIP into your desired location (note: you might have to turn off windows defender temporarily if it marks the hydra binaries as a trojan)
- enter the following commands into command prompt or PowerShell:
```rb
> cd {folder_path}\src
> pip install -r requirements.txt
```
### Running the program
- make sure to cd into the correct directory if you have not already done so
```rb
> python main3.py
```