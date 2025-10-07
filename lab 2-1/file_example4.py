#Name: Kamil Salih
#Student number: C00307549
#Group: CW_KCCYB_B
#Date: 05/10/2025

import re

pattern = r"at"
text = "The cat sat on the mat."

matches = re.findall(pattern, text)
print(matches)