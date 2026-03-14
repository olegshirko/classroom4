# Напиши решение здесь

# Read log file and count 404 errors
count = 0
with open('server.log', 'r') as f:
    for line in f:
        if '404' in line:
            count += 1

# Write count to stats file
with open('stats.txt', 'w') as f:
    f.write(str(count))
