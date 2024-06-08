#Ambrose Onapa
# Initial list of MAC addresses
mac_addresses = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]

# Function to convert MAC address to Cisco format
def convert_mac_to_cisco_format(mac_list):
    # Initialize an empty list to hold the converted MAC addresses
    result = []

    # Iterate through each MAC address in the input list
    for mac in mac_list:
        # Replace colons with dots to match the Cisco format
        cisco_mac = mac.replace(':', '.')
        # Append the formatted MAC address to the result list
        result.append(cisco_mac)
    
    # Return the list of converted MAC addresses
    return result

# Call the function with the initial MAC addresses list
converted_mac_addresses = convert_mac_to_cisco_format(mac_addresses)

# Print the result list of converted MAC addresses
print("Converted MAC Addresses in Cisco Format are:")
for address in converted_mac_addresses:
    print(address)
