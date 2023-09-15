#-*- code: utf-8 -*-
import re

email = input("What's your email? ").strip()

if re.search(r"^(\w+\.)?\w+@\w+\.(com|edu|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# 
# # if "@" in email and "." in email:
# #     print("Valid")
# # else:
# #     print("Ivalid")
# 
# username, domain = email.split("@")
# 
# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")
