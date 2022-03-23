import pandas

'''Isolate the column of Primary Fur Color while it has Gray Fur color'''

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
print(grey_squirrels)

'''Count how many Furs colors there are for each color'''

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(f"There are {grey_squirrels_count} squirrels with a Gray color fur, {red_squirrels_count} with red color, and {black_squirrels_count} with a black color")

''''Construct new data frame & export it to a csv file'''

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count_per_fur_color.csv")
