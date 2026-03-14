# Напиши решение здесь

# Read first 4 bytes of binary file
with open('file.bin', 'rb') as f:
    header = f.read(4)

# Check PNG signature (0x89 0x50 0x4E 0x47)
if header == b'\x89\x50\x4E\x47':
    result = 'PNG'
else:
    result = 'UNKNOWN'

# Write result to type.txt
with open('type.txt', 'w') as f:
    f.write(result)
