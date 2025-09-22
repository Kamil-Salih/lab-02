"""
Step 1: Print the file lines
Write a Python script (lab2.py) that opens auth.log and prints each line.

Step 2: Extract IP addresses
Use the regex r"\d+\.\d+\.\d+\.\d+" to find all IP addresses. Create a list 

Step 3: Get unique IPs
Convert the list to a set, then print each unique IP.

Step 4: Save results
Write the unique IPs to a new file unique_ips.txt, one per line.
"""

import re

pattern= r"\d+\.\d+\.\d+\.\d+" #Step 2
found_ips = []                       #Step 2. Creates an empty list called ips

with open('auth.log', 'r') as f: #Step 1
    for line in f:               #Step 1
        print(line.strip())      #Step 1

print()
found_ips[]=re.findall

for ip in found_ips:                 #Step 2
        ips.append(ip)         #Step 2 Add each ip to our list



