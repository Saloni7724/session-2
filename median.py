# Task 2

delivery_times = [30, 25, 40, 35, 30, 45, 30]

delivery_times.sort()

n = len(delivery_times)

if n % 2 == 1:
    median = delivery_times[n // 2]
else:
    median = (delivery_times[n // 2 - 1] + delivery_times[n // 2]) / 2

print("Sorted delivery times:", delivery_times)
print("Median delivery time:", median, "minutes")