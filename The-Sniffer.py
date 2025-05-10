from scapy.all import sniff
import subprocess

pattern = """
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$                                                                                                                         $
$   #     #                                                               #####                                           $
$   #  #  # ###### #       ####   ####  #    # ######    #####  ####     #     # #    # # ###### ######    #####  #   #   $
$   #  #  # #      #      #    # #    # ##  ## #           #   #    #    #       ##   # # #      #         #    #  # #    $
$   #  #  # #####  #      #      #    # # ## # #####       #   #    #     #####  # #  # # #####  #####     #    #   #     $
$   #  #  # #      #      #      #    # #    # #           #   #    #          # #  # # # #      #         #####    #     $
$   #  #  # #      #      #    # #    # #    # #           #   #    #    #     # #   ## # #      #      ## #        #     $
$    ## ##  ###### ######  ####   ####  #    # ######      #    ####      #####  #    # # #      #      ## #        #     $                                                                                                                      
$                                                                                                                         $
$                                                                                                                         $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  
      """

def main():
    while(True):
        display_interfaces()
        interface = input("Select the interface you want to sniff on from the following option: ")  #Specify the interface
        limit = int(input("Enter the number of packets to sniff (Enter 0 if you don't wish to sniff a specific number of packets): "))    #Specify the number of packets to stop sniffing after reaching
        answer = input("Do you wish to filter by a specific protocol? (Y/N) ")
        if limit == 0:
            if answer == "Y" or answer == "y":
                protocol=input("Specify the protocol: ")
                sniff(filter=protocol,iface= interface, prn=PcktInfo)  
            else:
                sniff(iface= interface, prn=PcktInfo)
        else:
            if answer == "Y" or answer == "y":
                protocol=input("Specify the protocol: ")
                sniff(filter=protocol,iface= interface, prn=PcktInfo, count=limit)  
            else:
                sniff(iface= interface, prn=PcktInfo, count=limit)
                
        #The sniff() is used for packet sniffing,
        #filter=protocol specifies a filter for the packets to capture. It indicates the protocol or types of packets to capture.
        #iface=interface specifies the interface we want to sniff on (taken as input from the user),
        #prn=PcktInfo indicates that the function named PcktInfo will be called for each captured packet,
        #count=limit means that the packet sniffing will stop after capturing limit number of packets (taken as input from the user).

        exit = input("Do you want to exit? (Y/N) ")
        if exit == "Y" or exit == "y":
            break

def PcktInfo(Packet):       #Callback Function used with sniff()
    print(Packet.show())    #Display detailed information about a packet including protocol-specific details.

def display_interfaces():
    try:
        # Run 'netsh interface show interface' on Windows
        result = subprocess.run(['netsh', 'interface', 'show', 'interface'], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

    except subprocess.CalledProcessError as e:
        # Handle errors, if any
        print(f"Error: {e.stderr}")

if __name__ == "__main__":
    print(pattern)
    main()
