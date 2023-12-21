import subprocess
subprocess.run(["ifconfig","eth0","down"]) 
subprocess.run(["sudo","macchanger","--random","eth0"])  
subprocess.run(["ifconfig","eth0","up"])
print("Mac Address Successfully Changed.")
