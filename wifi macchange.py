import subprocess
subprocess.run(["ifconfig","wlan0","down"]) 
subprocess.run(["sudo","macchanger","--random","eth0"])  
subprocess.run(["ifconfig","wlan0","up"])
print("Mac Address Successfully Changed.")