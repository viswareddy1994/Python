# with open("day_25\weather_data.csv", mode="r") as weather_data:
#     data_list = weather_data.readlines()
#     print(data_list)

# import csv
# with open("day_25\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     next(data)
#     temp = []
#     for row in data:
#         # print(row[1])
#         # if row[1]!= "temp":
#         temp.append(int(row[1]))

# print(temp)
import pandas as pd
data = pd.read_csv("day_25/weather_data.csv")
# print(data)
# print(data["temp"])
# print(data.condition.to_list())
# print(data.temp.to_dict())
# print(data.to_dict())
# avg = sum(data.temp.to_list())/len(data.temp.to_list())
# avg = data.temp.mean() 
# avg = data["temp"].mean()
# print(round(avg,2))
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.temp)
# fahrenheit_temp = monday.temp[0]* (9/5) + 35
# print(fahrenheit_temp)

data_dict = {
    "students": ["viswa","gnan","chintu","yash"],
    "scores": [95,90,86,89]
}
df1 = pd.DataFrame(data_dict)
print(df1)
df1.to_csv("new_data.csv")

































