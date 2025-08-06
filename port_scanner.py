import socket

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
        # function input logic here
        print("")
    else:
        print("Invaild option")

if __name__ == "__main__":
    main()