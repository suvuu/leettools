from tools import ip_scanner, name_gen, domain_to_ip
import tkinter as tk

# Importing tools from the tools package


def gui_ip_scanner():
    # Code to run the IP scanner
    ip_scanner.gui()


def gui_name_gen():
    # Code to run the name/email generator
    name_gen.gui()


def gui_domain_to_ip():
    # Code to convert domain name to IP
    domain_to_ip.gui()


def main_gui():
    # Create a new window for the GUI
    gui_window = tk.Tk()
    gui_window.title("Tool Selection")

    # Create buttons for each tool
    ip_scanner_button = tk.Button(
        gui_window, text="IP Scanner", command=gui_ip_scanner)
    ip_scanner_button.pack(pady=5)

    name_gen_button = tk.Button(
        gui_window, text="Name/Email Generator", command=gui_name_gen)
    name_gen_button.pack(pady=5)

    domain_to_ip_button = tk.Button(
        gui_window, text="Domain to IP", command=gui_domain_to_ip)
    domain_to_ip_button.pack(pady=5)

    # Start the GUI event loop
    gui_window.mainloop()


def main_cli():
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


def on_gui_button_click():
    # Close the initial popup and proceed with GUI
    root.destroy()
    main_gui()


def on_cli_button_click():
    # Close the initial popup and proceed with CLI
    root.destroy()
    main_cli()


root = tk.Tk()
root.title("Choose Mode")

# Create GUI button
gui_button = tk.Button(root, text="Continue in GUI",
                       command=on_gui_button_click)
gui_button.pack()

# Create CLI button
cli_button = tk.Button(root, text="Enter CLI", command=on_cli_button_click)
cli_button.pack()


root.mainloop()
