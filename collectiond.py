from collections import Counter

device_temp = [13.5, 14.0, 14.2, 15.0, 14.2]
temp_count = Counter(device_temp)
print(temp_count[14.2])