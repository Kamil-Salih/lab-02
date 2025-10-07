#Name: Kamil Salih
#Student number: C00307549
#Group: CW_KCCYB_B
#Date: 06/10/2025
# lab2.3_starter.py
import json
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime
from datetime import timedelta

incidents = []
window = timedelta(minutes=10)
rank = 1
ips = []
counts = []

LOGFILE = "sample_auth_small.log"

def parse_auth_line(line):
    """
    Parse an auth log line and return (timestamp, ip, event_type)
    Example auth line:
    Mar 10 13:58:01 host1 sshd[1023]: Failed password for invalid user admin from 203.0.113.45 port 52344 ssh2
    We will:
     - parse timestamp (assume year 2025)
     - extract IP (token after 'from')
     - event_type: 'failed' if 'Failed password', 'accepted' if 'Accepted password', else 'other'
    """
    parts = line.split()
    # timestamp: first 3 tokens 'Mar 10 13:58:01'
    ts_str = " ".join(parts[0:3])
    try:
        ts = datetime.strptime(f"2025 {ts_str}", "%Y %b %d %H:%M:%S")
    except Exception:
        ts = None
    ip = None
    event_type = "other"
    if "Failed password" in line:
        event_type = "failed"
    elif "Accepted password" in line or "Accepted publickey" in line:
        event_type = "accepted"
    if " from " in line:
        try:
            idx = parts.index("from")
            ip = parts[idx+1]
        except (ValueError, IndexError):
            ip = None
    return ts, ip, event_type

if __name__ == "__main__":
    per_ip_timestamps = defaultdict(list)
    with open(LOGFILE) as f:
        for line in f:
            ts, ip, event = parse_auth_line(line)
            if ts and ip and event == "failed":   # checks that ts and ip are not null, and that event=="failed"
                per_ip_timestamps[ip].append(ts)


    for ip in per_ip_timestamps: #added part
        per_ip_timestamps[ip].sort()

    # quick print
    for ip, times in per_ip_timestamps.items():
        print(ip, len(times))


for ip, times in per_ip_timestamps.items():
    times.sort()
    n = len(times)
    i = 0
    while i < n:
        j = i
        while j + 1 < n and (times[j+1] - times[i]) <= window:
            j += 1
        count = j - i + 1
        if count >= 5:
            incidents.append({
                "ip": ip,
                "count": count,
                "first": times[i].isoformat(),
                "last": times[j].isoformat()
            })
            # advance i past this cluster to avoid duplicate overlapping reports:
            i = j + 1
        else:
            i += 1

print("\n")
print(f"Detected {len(incidents)} brute-force incidents")

for incident in incidents[:5]:
    print(incident)




failed_attempt_counts = defaultdict(int)
for ip, timestamps in per_ip_timestamps.items():
    failed_attempt_counts[ip] = len(timestamps)


def top_n(counts_dict, n=10):
    return sorted(counts_dict.items(), key=lambda kv: kv[1], reverse=True)[:n]

print("\nTop attacker IPs (sorted by failed attempts):")

top_10_attacker_ips = top_n(failed_attempt_counts, n=10)


for ip, failed_count in top_10_attacker_ips:
    print(f"{rank}. {ip} — {failed_count}")
    rank=rank+1


with open('failed_counts.txt', 'w') as f1:
    f1.write("ip,failed_count\n")
    for ip, failed_count in sorted(failed_attempt_counts.items(), key=lambda kv: kv[1], reverse=True):
        f1.write(f"{ip},{failed_count}\n")




for ip, failed_count in top_10_attacker_ips:
    ips.append(ip)
    counts.append(failed_count)


plt.figure(figsize=(8,4))
plt.bar(ips, counts)
plt.title("Top attacker IPs")
plt.xlabel("IP")
plt.ylabel("Failed attempts")
plt.tight_layout()
plt.savefig("top_attackers.png")
plt.show()
