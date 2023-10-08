# strip() function only works with single item of the list not with whole list object

std_dict = {
    "names" : ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"],
    "score" : [59,88,44,99,77,69]
}
# for v in std_dict:
#     print(std_dict[v])
import pandas
df_dict = pandas.DataFrame(std_dict)
print(df_dict)
# for (key, value) in df_dict.items():
    # print(key)

for (index, row) in df_dict.iterrows():
    print(row.names == 'Dave')