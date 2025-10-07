#Name: Kamil Salih
#Student number: C00307549
#Group: CW_KCCYB_B
#Date: 05/10/2025
# lab2-2_starter.py

LOGFILE = "sample_auth_small.log"  # change filename if needed
total_lines=0
ips=[]
unique_ips=[]
first_10_unique_ips=[]

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