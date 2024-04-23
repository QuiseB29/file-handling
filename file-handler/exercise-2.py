import re

text = "John Doe - john.doe@example.com Jane Smith - jane.smith@gmail.com For inquiries, please contact info@example.com"
pattern = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", text)
print(pattern)

file = open("contact.txt", 'w')
with open('contact.txt', 'w') as file:
    file.write("John Doe - john.doe@example.com Jane Smith - jane.smith@gmail.com For inquiries, please contact info@example.com")