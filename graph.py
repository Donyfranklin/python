import matplotlib.pyplot as plt

temperature=[22,24,19,23,25,20,21]
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

sun_temp=sum(temperature)
no_days=len(temperature)

avg=sun_temp/no_days
print("AVG temp is : ",avg)

min_temp=min(temperature)
max_temp=max(temperature)

print(min_temp)
print(max_temp)

temp_data=dict(zip(days,temperature))

plt.bar(days,temperature)
plt.title("Temperature data over a week")
plt.xlabel("Days")
plt.xticks(rotation=30)
plt.ylabel("Temperature")



plt.tight_layout()
plt.show()

