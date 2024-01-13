from tools import ip_scanner, name_gen, domain_to_ip

# Importing tools from the tools package


def main():
    print("""
Select a tool to use:

      1. ip scanner
      2. name/email Generator & random secure password 
      3. domain name to ip
      
        """)

    tool_option = input("pick a card any card -> ")

    if tool_option == "1":
        ip_scanner.run()
    elif tool_option == "2":
        name_gen.run()
    elif tool_option == "3":
        domain_to_ip.run()


if __name__ == "__main__":
    main()
