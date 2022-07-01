import sys
import math
import operator

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# 1
# gymnasts = "Simone Biles"
# categories = "floor"
# input = ["Simone Biles,8,7,9"]

# 2
# gymnasts = "Aly Raisman"
# categories = "bars"
# input = [
#     "Aly Raisman,7.7,8.4,8.0",
#     "Aly Raisman,7.9,7.6,9.3",
#     "Aly Raisman,8.3,8.3,7.7",
# ]

# 3
# gymnasts = "Laurie Hernandez"
# categories = "bars"
# input = [
#     "Nadia Comaneci,7.98,9.17,7.84",
#     "Laurie Hernandez,8.57,8.68,7.86",
#     "McKayla Maroney,8.18,9.29,8.47",
# ]

# 4
gymnasts = "Laurie Hernandez,Ragan Smith"
categories = "beam"
input = [
    "Alicia Sacramone,7.99,8.01,8.39",
    "Alicia Sacramone,7.13,7.1,6.9",
    "Amy Jo Johnson,7.97,6.71,6.32",
    "Amy Jo Johnson,7.08,7.22,6.52",
    "Amy Jo Johnson,6.84,6.25,7.73",
    "Gabby Douglas,7.53,8.26,6.98",
    "Gabby Douglas,7.47,7.85,7.82",
    "Gabby Douglas,8.87,8.9,8.67",
    "Kacy Catanzaro,8.47,7.15,7.26",
    "Ragan Smith,7.79,6.24,6.25",
    "Kacy Catanzaro,8.07,7.09,6.96",
    "Kerri Strug,8.83,7.5,8.32",
    "Kerri Strug,8.81,8.2,7.52",
    "Kerri Strug,8.52,7.84,8.06",
    "Laurie Hernandez,8.57,8.68,7.86",
    "Shawn Johnson,7.45,8.06,8.98",
    "Laurie Hernandez,9.57,9.72,8.65",
    "Laurie Hernandez,8.68,8.81,8.01",
    "Nadia Comaneci,7.98,9.17,7.84",
    "Nadia Comaneci,8.26,9.43,8.63",
    "Nadia Comaneci,7.89,9.66,9.42",
    "Olga Korbut,6.85,6.7,7.36",
    "Olga Korbut,8.26,6.83,7.92",
    "Olga Korbut,7.98,7.16,7.55",
    "Alicia Sacramone,8.25,7.32,6.55",
    "Kacy Catanzaro,7.23,7.82,7.4",
    "Ragan Smith,6.69,8.1,7.23",
    "Ragan Smith,8.12,7.35,6.92",
    "Shawn Johnson,9.39,8.09,8.03",
    "Shawn Johnson,8.29,8.95,9.02",
]


# 5
# gymnasts="Boris Shakhlin,Nadia Comaneci,Akinori Nakayama"
# categories="beam,floor"
# input = [
#     "Nikolai Andrianov,7.95,9.7,9",
#     "Nikolai Andrianov,8.94,8.3,9.29",
#     "Simone Biles,8.7,8.2,8.6",
#     "Boris Shakhlin,9.55,8.31,9.5",
#     "Boris Shakhlin,8.55,9.02,8.64",
#     "Aly Raisman,9.55,8.38,8.21",
#     "Aly Raisman,8.38,8.04,9.23",
#     "Takashi Ono,8.77,9.48,9.08",
#     "Takashi Ono,8.65,9.19,7.88",
#     "Nadia Comaneci,8.32,8.48,8.88",
#     "Nadia Comaneci,8.92,7.98,8.04",
#     "Sawao Kato,8.34,8.28,8.19",
#     "Sawao Kato,9.5,7.98,8.94",
#     "Laurie Hernandez,9.08,9.02,8.17",
#     "Viktor Chukarin,7.67,8.75,8.94",
#     "Laurie Hernandez,8.22,8.57,8.84",
#     "Alexei Nemov,9.27,9.38,7.98",
#     "Alexei Nemov,7.92,7.91,8.11",
#     "McKayla Maroney,9.32,8.48,8.97",
#     "McKayla Maroney,8.78,8.21,7.87",
#     "Viktor Chukarin,8.07,9.05,7.66",
#     "Katelyn Ohashi,8.03,7.63,9.15",
#     "Katelyn Ohashi,9.06,8.88,9.01",
#     "Akinori Nakayama,8.83,8.9,9.16",
#     "Akinori Nakayama,9.05,8.54,8.56",
#     "Shawn Johnson,8.95,8.11,8.07",
#     "Shawn Johnson,7.6,8.62,8.33",
#     "Simone Biles,8.62,9.56,8.72",
# ]

def insert_score(split_categories, cate_bars, cate_beam, cate_floor, spilt_data_input):

    data_income = {}
    for cate in split_categories:
        if cate in cate_bars:
            data_income[cate] = float(spilt_data_input[cate_bars["bars"]])
        if cate in cate_beam:
            data_income[cate] = float(spilt_data_input[cate_beam["beam"]])
        if cate in cate_floor:
            data_income[cate] = float(spilt_data_input[cate_floor["floor"]])

    return data_income

data_master_pack = {}
data_master = {}
cate_bars = {"bars" : 1}
cate_beam = {"beam" : 2}
cate_floor = {"floor" : 3}
data_cate = {'bars' : 0,'beam': 0, 'floor': 0}
count_name = 0
for row in input:
    spilt_data_input = row.split(",")
    split_name_gymneast = gymnasts.split(",")
    split_categories = categories.split(",")

    if spilt_data_input[0] in split_name_gymneast:
        for name in split_name_gymneast:
            if name == spilt_data_input[0]:
                
                # reset data_cate
                if count_name == 2:
                    data_cate = {'bars' : 0,'beam': 0, 'floor': 0}
                    count_name = 0

                data_incoming = insert_score(split_categories, cate_bars, cate_beam, cate_floor, spilt_data_input)
                for (key_income, value_income), (key_cate, value_cate) in zip(data_incoming.items(), data_cate.items()):
                    if value_income > value_cate:
                        data_cate[key_cate] = value_income
                data_master[name] = data_cate
                count_name += 1
        data_master_pack = data_master


        sorted_data_master_pack = data_master_pack
        if len(split_name_gymneast) < 3:
            sorted_data_master_pack = dict(sorted(data_master_pack.items(), key=lambda t: t[1]['bars'], reverse=True))

for key_gymneast, value_gymneast in sorted_data_master_pack.items():
    check_print = False
    for key_best_score, value_best_score in value_gymneast.items():
        if value_best_score != 0:
            print(f'{value_best_score:g}', end="")
            if len(split_categories) > 1 and check_print == False:
                print(",", end="")
                check_print = True
    print("")
