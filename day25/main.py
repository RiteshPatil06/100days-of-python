import csv
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
Cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])

print("grey squirrels = ", grey_squirrels)
print("black squirrels = ", black_squirrels)
print("cinnamon squirrels = ", Cinnamon_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [grey_squirrels, black_squirrels, Cinnamon_squirrels]
}

df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_Count.csv")