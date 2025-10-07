#Name: Kamil Salih
#Student number: C00307549
#Group: CW_KCCYB_B
#Date: 05/10/2025

import re

pattern = r"\d+\.\d+\.\d+\.\d+"
ips = []     # creates an empty list called ips



with open('auth.log', 'r') as f1:
    for line in f1:
        print(line.strip())
        found_ips=re.findall(pattern, line)
        for ip in found_ips:
            ips.append(ip) # Add each ip to our list


# Convert to a set to remove duplicates
unique_ips = set(ips)
unique_ips = list(ips)


# Print each unique IP
print("\n")
print("Unique IPs:")
for ip in unique_ips:
    print(ip)

with open('unique_ips.txt', 'w') as f2:
    for item in unique_ips:
        f2.write(item)
        f2.write("\n")