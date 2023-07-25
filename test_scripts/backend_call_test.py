import requests

url = "http://localhost:5000/nmap-results"
data = {
    # sample json data
    "nmap":{
        "command_line":"nmap -oX - 192.168.5.0/24",
        "scaninfo":{
            "tcp":{
                "method":"syn",
                "services":"1,3-4,6-7,9,13"
            }
        },
        "scanstats":{
            "downhosts":"253",
            "elapsed":"10.70",
            "timestr":"Mon Jul 24 17:04:43 2023",
            "totalhosts":"256",
            "uphosts":"3"
        }
    },
    "scan":{
        "192.168.5.1":{
            "hostnames":[
                {
                    "name":"",
                    "type":""
                }
            ],
            "addresses":{
                "ipv4":"192.168.5.1"
            },
            "vendor":{
                
            },
            "status":{
                "state":"up",
                "reason":"localhost-response"
            },
            "tcp":{
                "135":{
                    "state":"open",
                    "reason":"syn-ack",
                    "name":"msrpc",
                    "product":"",
                    "version":"",
                    "extrainfo":"",
                    "conf":"3",
                    "cpe":""
                },
                "139":{
                    "state":"open",
                    "reason":"syn-ack",
                    "name":"netbios-ssn",
                    "product":"",
                    "version":"",
                    "extrainfo":"",
                    "conf":"3",
                    "cpe":""
                }
            }
        }
    }
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Data sent successfully!")
else:
    print(f"Failed to send data. Status code: {response.status_code}")

# take note of these for requirements.txt
# certifi-2023.7.22 charset-normalizer-3.2.0 idna-3.4 requests-2.31.0 urllib3-2.0.4