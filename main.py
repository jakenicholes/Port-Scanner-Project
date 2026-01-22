#Port scanner main file
#Goal is to create a port scanner that can scan a range of IP addresses and ports, then identify the statuses of each port (open, closed, filtered), then export the results to a CSV file.

import nmap

# Specify the path to the Nmap executable
nmap_path = r'C:\Program Files (x86)\Nmap\nmap.exe'

#Define main function
def main():

    # Get user input for IP range
    ip_range = input("Enter the IP range to scan: ")

    # Get user input for port range
    port_range = input("Enter the port range to scan: ")

    # Scan the IP range and port range using nmap
    scanner = nmap.PortScanner(nmap_search_path=(nmap_path,))
    results = scanner.scan(ip_range, port_range)

    # Show results
    print(results)

main()