p1 = 0
p2 = None
prev = None
for line in open('input.in'):
    line = line.strip()
    x = int(line)
    if prev and x > prev:
        p1 += 1

    prev = x

print(p1)
print(p2)