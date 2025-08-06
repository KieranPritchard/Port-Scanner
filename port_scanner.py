import socket

def scan_all_ports(target):
    ports = range(1, 65535)

    print(f"Scanning {target}")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.timeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")
        sock.close()

def main():
    #banner for start up of program
    print("=" * 30)
    print("Port Scanner")
    print("=" * 30)
    print("Options")
    print("(1) Scan most used ports.")
    print("(2) Scan all ports on an IP")
    print("=" * 30)
    
    # takes user inputs and calls functions
    choice = int(input("Please select your option: "))

    if choice == 1:
        # function input logic here
        print("")
    elif choice == 2:
        # Scans all the ports on the ip address
        target = input("Please input your target ip address:")
        scan_all_ports(target)
    else:
        print("Invaild option")

if __name__ == "__main__":
    main()