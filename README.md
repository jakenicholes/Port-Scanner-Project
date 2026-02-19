# Port Scanner Project
Creating a port scanner to help identify open ports on a network with the goal of being able to identify ports, find their status, and export that information into a tangible report.

# Requires NMAP to be manually installed
Add a manual path to your nmap executable as a variable.

# Update 1
Set up the NMAP scanner to accept input for list of IP and Port ranges

# Update 2
Structured the raw output from NMAP into something more human-readable.

# Update 3
Put in an IF to skip over closed ports.
    I explored using nmap3 for a while but could not figure out how to change my 
    code to make this adjustment. I ended up finding out that nmap3 does not support
    the kind of scan that I want. My options were top port scan or list scan, neither
    were what I am looking for.