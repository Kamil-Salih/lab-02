#Name: Kamil Salih
#Student number: C00307549
#Group: CW_KCCYB_B
#Date: 05/10/2025

import re

pattern = r"[A-Za-z]+"
text = "Order 123 was placed on 2023-05-01."

print(re.findall(pattern, text))