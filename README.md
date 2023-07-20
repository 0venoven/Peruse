# Peruse

## Proof-of-concept vulnerability scanner

Peruse is a standalone desktop app that allows you to identify devices in your home that have weak passwords. It currently makes use of the python-nmap library to scan your network to identify devices connected to it and open ports on these devices. It then uses THC-Hydra binaries to attempt dictionary attacks (using rockyou.txt) on SSH to test for weak and commonly used passwords.

## Running Peruse
### On windows:
- clone this repository or download ZIP into your desired location
- run the command prompt or PowerShell as administrator, then enter the following commands:
```rb
> cd {file_location}\peruse
> pip install -r requirements.txt
> python3 main3.py
```
