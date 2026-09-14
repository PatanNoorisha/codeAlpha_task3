import re
import os

# Get the folder where task3.py is located
folder = os.path.dirname(os.path.abspath(__file__))

# Create the file paths
input_file = os.path.join(folder, "input.txt")
output_file = os.path.join(folder, "emails.txt")

# Read input.txt
with open(input_file, "r") as file:
    text = file.read()

# Find email addresses
emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

# Save emails
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email extraction completed!")
print("Emails found:")

for email in emails:
    print(email)