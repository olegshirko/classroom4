# Напиши решение здесь

try:
    with open('data.txt', 'r') as f:
        content = f.read()
    with open('log.txt', 'w') as f:
        f.write(content)
except FileNotFoundError:
    with open('log.txt', 'w') as f:
        f.write('ERROR')
