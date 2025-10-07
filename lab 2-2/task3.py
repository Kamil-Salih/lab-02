#Name: Kamil Salih
#Student number: C00307549
#Group: CW_KCCYB_B
#Date: 05/10/2025
# lab2-2_starter.py

from collections import defaultdict
import time


counts = defaultdict(int)           # Create a dictionary to keep track of IPs

LOGFILE = "sample_auth_small.log"  # change filename if needed
#LOGFILE = "mixed_logs_5000.log"

total_lines=0
ips=[]
unique_ips=[]
first_10_unique_ips=[]
rank = 1

def ip_parse(line):
    """
    looks for the substring ' from ' and returns the following IP address.
    Returns None if no matching substring found.
    """
    if " from " in line:
        parts = line.split() # splits the line into tokens, seperates by spaces by default
        try:
            anchor = parts.index("from")    # Find the position of the token "from", our anchor
            ip = parts[anchor+1]          # the from value will be next token, anchor+1
            return ip.strip(',:;]')             # strip any trailing punctuation

        except (ValueError, IndexError):
            return None

    return None

## This is the main block that will run first. 
## It will call any functions from above that we might need.
if __name__ == "__main__":

    with open(LOGFILE, "r") as f:
        for line in f:
            total_lines=total_lines+1
            ip=ip_parse(line.strip())
            if ip:
                unique_ips.append(ip)
            print (line.strip())

unique_ips = set(unique_ips)



first_10_unique_ips=unique_ips
first_10_unique_ips=list(first_10_unique_ips)

first_10_unique_ips=sorted(first_10_unique_ips)

print("\n")
print(f"Lines read: {total_lines}")
print(f"Unique IPs: {len(unique_ips)}")
print(f"First 10 IPs: {first_10_unique_ips[0:10]}")
print("\n")

start = time.time()

with open("sample_auth_small.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            # extract ip
            ip = ip_parse(line)
            if ip:
                counts[ip] += 1
end = time.time()
print(counts)



def top_n(counts, n=5):
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]

print("\n")

top_5_attacker_ips=top_n(counts)


print(top_n(counts))
print("\n")


# run counting
for ip, count in top_5_attacker_ips:
    print(f"{rank}. {ip} — {count}")
    rank=rank+1

print("\n")

with open('failed_counts.txt', 'w') as f1:
    f1.write("ip,failed_count")
    f1.write("\n")
    for ip in counts:
        f1.write(f"{ip},{counts[ip]}")
        f1.write("\n")


print("Elapsed:", end-start, "seconds")



