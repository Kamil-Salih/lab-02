# lab2.py
import re

# Step 1: Print the file lines
with open("auth.log", "r") as f:
    for line in f:
        print(line.strip())

# Step 2: Extract IP addresses
pattern = r"\d+\.\d+\.\d+\.\d+"
ips = []  # list to store IPs

with open("auth.log", "r") as f:
    for line in f:
        found_ips = re.findall(pattern, line)
        for ip in found_ips:
            ips.append(ip)

print("\nAll IPs found:")
print(ips)

# Step 3: Get unique IPs
unique_ips = set(ips)

print("\nUnique IPs:")
for ip in unique_ips:
    print(ip)

# Step 4: Save results
with open("unique_ips.txt", "w") as f:
    for ip in unique_ips:
        f.write(ip + "\n")
