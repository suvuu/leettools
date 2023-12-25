import nmap
import re

def run():

  nm = nmap.PortScanner()
  ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
  port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
  port_min = 0
  port_max = 65535

  while True:
      ip_add_entered = input("Enter IP: ")
      if ip_add_pattern.search(ip_add_entered):
          print(f"{ip_add_entered} is valid")
          break
      else:
          print("that dont work, try again!")

  while True:
      print("enter the range of ports in format: <int>-<int>")
      port_range = input("port range: ")
      port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
      if port_range_valid:
          port_min = int(port_range_valid.group(1))
          port_max = int(port_range_valid.group(2))
          print(f"lets see what they got from {port_min} to {port_max}")
          break
      else:
          print("bad ports, try again!")
  
  while True:
      scan_options = input("""
Enter nmap scan options or press enter for default!
      -sV : Check open ports to determine service/version information
      -sC : Runs default scripts
      -O : OS detection
      -A : Aggressive scan and is thorough
""")
      scan_options = scan_options.strip()

      if scan_options == '':
          scan_options = '-sV'  # Default option if user presses enter
          print(f"Using default option: {scan_options}")
      else:
          print(f"Using custom options: {scan_options}")
      break

    # Perform the scan
  nm.scan(ip_add_entered, f"{port_min}-{port_max}", arguments=scan_options)

    # Process and display detailed scan results
  for host in nm.all_hosts():
      print(f"Host : {host} ({nm[host].hostname()})")
      print(f"State : {nm[host].state()}")

      for proto in nm[host].all_protocols():
          print(f"----------\nProtocol : {proto}")

          lport = nm[host][proto].keys()
          for port in sorted(lport):
              service_info = nm[host][proto][port]
              
              if service_info['state'] == 'open':
                  print(f"Port : {port}/tcp")

              if 'name' in service_info:
                  print(f"Service : {service_info['name']}")

              if 'version' in service_info:
                  print(f"Version : {service_info['version']}")

              if 'product' in service_info:
                  print(f"Product : {service_info['product']}")

              if 'extrainfo' in service_info:
                  print(f"Extra Info : {service_info['extrainfo']}")

              if 'script' in service_info:
                  for script_id, output in service_info['script'].items():
                      print(f"{script_id} : {output}")

              print()  # Empty line for readability

if __name__ == "__main__":
    run()      
  
