# Напиши решение здесь
import csv
import json

# Read CSV file
with open('users.csv', 'r') as f:
    reader = csv.DictReader(f)
    users = list(reader)

# Write JSON file
with open('users.json', 'w') as f:
    json.dump(users, f)
