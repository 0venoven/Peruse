# Peruse

## Proof-of-concept vulnerability scanner

Peruse is a desktop app that allows you to identify devices in your home that have weak passwords. It currently makes use of the python-nmap library to scan your network to identify devices connected to it and open ports on these devices. It then uses THC-Hydra binaries to attempt dictionary attacks (using rockyou.txt) on SSH to test for weak and commonly used passwords.

## On Windows
### Prerequisites
- download [Microsoft Visual C++ 2008 Redistributable Package](https://www.microsoft.com/en-us/download/details.aspx?id=26368) (prerequisite for the item below)
- download and extract [THC-Hydra binaries for Windows](https://github.com/maaaaz/thc-hydra-windows/archive/master.zip)
- install [nmap](https://nmap.org/dist/nmap-7.94-setup.exe) into its default path using its default options
### Installing and running the program
- clone this repository or download ZIP into your desired location
- open the repository and in peruse2.py, change the path of the hydra binaries to your own under the run_hydra function (for now, this must be manually done but we are looking into automatic detection of file path)
- run the command prompt or PowerShell as administrator, then enter the following commands:
```rb
> cd {folder_path}\peruse
> pip install -r requirements.txt
> python3 main3.py
```