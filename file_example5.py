import re

pattern = r"[a-zA-Z]+"
text = "Order 123 was placed on 2023-05-01."

print(re.findall(pattern, text))