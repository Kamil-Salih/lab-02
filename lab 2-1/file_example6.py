#Name: Kamil Salih
#Student number: C00307549
#Group: CW_KCCYB_B
#Date: 05/10/2025

import re

pattern = r"\d+\.\d+\.\d+\.\d+"
text = "Failed login from 192.168.0.1 and 10.0.0.5 at 10:30"

print(re.findall(pattern, text))