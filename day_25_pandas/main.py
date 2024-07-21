import pandas as pd
df1 = pd.read_csv(r"day_25_pandas\data\2018_Central_Park_Squirrel_Census_Data.csv")

df2 = df1[["Primary Fur Color"]]

uniques_color = df2["Primary Fur Color"].unique()
# print(uniques_color)

# squaral_count = []
# for color in uniques_color:
#     if pd.isna(color):
#         count_val = df2["Primary Fur Color"].isna().sum()
#     else:
#         count_val = len(df2[df2["Primary Fur Color"]==f"{color}"])
#     squaral_count.append(count_val)

squaral_count = [df2["Primary Fur Color"].isna().sum() if pd.isna(color) else len(df2[df2["Primary Fur Color"]==f"{color}"]) for color in uniques_color ]

color_list = ["Undefined" if pd.isna(color) else color for color in uniques_color]    
# color_list = []  
# for color in uniques_color:
#     if pd.isna(color):
#         color_list.append("Undefined")
#     else:
#         color_list.append(color)
# print(color_list)

data_dict = {
    "fur_color":color_list,
    "count": squaral_count
}
# print(data_dict)

df3 = pd.DataFrame(data_dict)
print(df3)
# df3.to_csv("day_25_pandas/data/squral_data.csv")

# Method #2

# count_squaral = []
# squral_data = df2["Primary Fur Color"].value_counts(dropna=False)
# df3 = squral_data.reset_index()
# df3.columns = ["color","count"]
# df3["color"] = df3.color.fillna("Undefined")
# print(df3)
# df3.to_csv("day_25_pandas/data/squral_data.csv")