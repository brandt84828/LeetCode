nums = [1,3,2,3,5,0]
record = {}
count = 0

for num in nums:
    if num in record:
        record[num] = record[num] + 1
    else:
        record[num] = 1

for key in record:
    if record.get(key+1):
        count = count + record[key]
        
print(count)
