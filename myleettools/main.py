from tools import ip_scanner, name_gen

# Importing tools from the tools package

def main():
  print("""
Select a tool to use: 

      1. IP Scanner
      2. Name/email Generator      
        """)


  tool_option = input("pick a card any card -> ")

  if tool_option == "1":
    ip_scanner.run()
  elif tool_option == "2":
    name_gen.generate_names()

if __name__ == "__main__":
  main()

