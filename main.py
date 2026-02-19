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
    print_scan_results(results)

def print_scan_results(results):
    # Make sure that the output is converted from raw data to something more human readable
    print("\n" + "+"*21)
    print("| PORT SCAN RESULTS |")
    print("+"*21)
    
    # Error handling
    if not results['scan']:
        print("No hosts found or scan failed.")
        return
    
    # Result structuring
    for host in results['scan']:

        print("\n\n--------------------NEW HOST--------------------")
        print(f"\nHost: {host}")
        host_data = results['scan'][host]
        print(f"Status: {host_data['status']['state']}")
        
        if 'tcp' in host_data:
            print("\nOpen Ports:")
            for port in sorted(host_data['tcp'].keys()):
                port_info = host_data['tcp'][port]
                state = port_info['state']
                service = port_info.get('name', 'Unknown')

                # Skip closed ports
                if state == 'closed':
                    continue
                else:
                    print(f"  Port {port} - {state} ({service})")
    
    print("\n" + "="*30 + "\n")

main()