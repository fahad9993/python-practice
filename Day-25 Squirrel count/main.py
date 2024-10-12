import pandas

data = pandas.read_csv("004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
fur_color = data["Primary Fur Color"]
categories = fur_color.value_counts()
categories.to_csv("squirrels_data.csv")
