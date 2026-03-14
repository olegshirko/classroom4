# Напиши решение здесь

# Read config file
with open('config.env', 'r') as f:
    lines = f.readlines()

# Replace DEBUG=False with DEBUG=True
with open('config.env', 'w') as f:
    for line in lines:
        if line.strip() == 'DEBUG=False':
            f.write('DEBUG=True\n')
        else:
            f.write(line)
