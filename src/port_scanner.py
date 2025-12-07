import socket

# This function scans all the ports in the target parameter
def scan_all_ports(target):
    # This scans all the ports up to 1025, for demo purposes
    ports = range(1, 1025)

    # Outputs the program is scanning the target
    print(f"Scanning {target}")
    # Loops through the ports in the range
    for port in ports:
        # creates a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # sets the time out to 5 seconds
        sock.settimeout(0.5)
        # Trys connecting to the target on that port
        try:
            # Stores the result of the connection
            result = sock.connect_ex((target, port))
            # Checks if the result is zero to see if it is open
            if result == 0:
                # Outputs that is is open
                print(f"Port {port} is OPEN")
            else:
                # Outputs that is is closed
                print(f"Port {port} is CLOSED")
            # Closes the connection
            sock.close()
        # catches and outputs the exception
        except Exception as e:
            print(f"Error encountered: {e}")

# Function scans the most used ports
def scan_most_used(target):
    # list of most used ports
    port_list = [20, 21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443]

    # Outputs the program is scanning the target
    print(f"Scanning {target}")

    # Loops through the ports in the range
    for port in port_list:
        # creates a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Sets timeout
        sock.settimeout(0.5)

        # Trys connecting to the target on that port
        try:
            # Stores the result of the connection
            result = sock.connect_ex((target, port))
            # Checks if the result is zero to see if it is open
            if result == 0:
                # Outputs that is is open
                print(f"Port {port} is OPEN")
            else:
                # Outputs that is is closed
                print(f"Port {port} is CLOSED")
            # Closes the connection
            sock.close()
        # catches and outputs the exception
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
    choice = input("Please select your option: ")

    if choice.isdigit():
        # checks for which choice the user wants
        if choice == 1:
            # Scans most used ports on the ip address
            target = input("Please input your target ip address:")
            # calls the function
            scan_most_used(target)
        elif choice == 2:
            # Scans all the ports on the ip address
            target = input("Please input your target ip address:")
            # calls the function
            scan_all_ports(target)
        else:
            # Output invaild option
            print("Invaild option")
    else:
            # Output invaild option
            print("Invaild option")

# starts the program
if __name__ == "__main__":
    main()