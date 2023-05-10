# input value
hour_val = int(input())
count = 0

# Check 
for i in range(hour_val+1):
    for j in range(60):
        for k in range(60):
            value = str(i)+str(j)+str(k)
            if '3' in value:
                # print(value)
                count += 1

print(count)