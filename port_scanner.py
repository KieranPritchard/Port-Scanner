import socket

def scan_all_ports(target):
    ports = range(1, 1025)

    print(f"Scanning {target}")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            else:
                print(f"Port {port} is CLOSED")
            sock.close()
        except Exception as e:
            print(f"Error encountered: {e}")

def scan_most_used(target):
    port_list = [20, 21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443]

    print(f"Scanning {target}")
    for port in port_list:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            else:
                print(f"Port {port} is CLOSED")
            sock.close()
        except Exception as e:
            print(f"Error encountered: {e}")

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
        # Scans most used ports on the ip address
        target = input("Please input your target ip address:")
        scan_most_used(target)
    elif choice == 2:
        # Scans all the ports on the ip address
        target = input("Please input your target ip address:")
        scan_all_ports(target)
    else:
        print("Invaild option")

if __name__ == "__main__":
    main()