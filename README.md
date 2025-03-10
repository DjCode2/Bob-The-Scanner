
# **Bob the Scanner**  

Bob the Scanner is a command-line tool designed to scan and identify all accessible machines on a network based on an IP address provided in CIDR format. It uses `scapy` for network scanning, `argparse` for command-line argument parsing, `re` for input validation, and `colorama` for colorful outputs.

---

## **Features**  
- Scans a given network range and identifies accessible devices.  
- Accepts user input in CIDR format.  
- Provides real-time, visually appealing output with color-coded messages.  
- Validates user input to ensure proper CIDR format.  
- Lightweight and efficient, running directly via Python.  

---

## **Requirements**  
Bob the Scanner requires Python 3.6 or later. The following Python libraries must also be installed:  
- `scapy`  
- `argparse` (built-in with Python)  
- `re` (built-in with Python)  
- `colorama`  

Install `colorama` with:  
```bash
pip install colorama
```

---

## **How to Use**  
1. Clone or download the repository containing **Bob the Scanner**.  
2. Open a terminal in the project directory.  
3. Run the program with the following command:  
   ```bash
   python bob_the_scanner.py --ip_address_CIDR <your_network_CIDR>
   ```
   Replace `<your_network_CIDR>` with a valid CIDR address (e.g., `192.168.0.1/24`).  

4. Output:  
   - If the CIDR address is valid, the program will scan the network and display the results.  
   - If the CIDR address is invalid, an error message will be displayed.

---

## **Example Output**  
```plaintext
     ____        _       _______ _               _____                                 
    |  _ \      | |     |__   __| |             / ____|                                
    | |_) | ___ | |__      | |  | |__   ___    | (___   ___ __ _ _ __  _ __   ___ _ __ 
    |  _ < / _ \| '_ \     | |  | '_ \ / _ \    \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
    | |_) | (_) | |_) |    | |  | | | |  __/    ____) | (_| (_| | | | | | | |  __/ |   
    |____/ \___/|_.__/     |_|  |_| |_|\___|   |_____/ \___\__,_|_| |_|_| |_|\___|_|   

    v1.0    Using argparse, scapy, re & colorama.

IP address CIDR provided: 192.168.0.1/24  
========== Start of Scan ==========  

[Results of the ARP scan]

=========== End of Scan ===========
```

---

## **Code Overview**  

- **`main()`**: Handles argument parsing and initiates network scanning.  
- **`scan_network(ip_range)`**: Executes ARP scans on the provided IP range.  
- **`validate_ip_cidr(ip_cidr)`**: Validates whether the given IP address is in proper CIDR format.  
- **`print_logo()`**: Displays an ASCII logo to enhance user experience.  
