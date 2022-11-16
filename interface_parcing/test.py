import re

int_line = '  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec,'
match = re.search(r'1500', int_line)
match.group()
print(match.group())
