import sys
import math
from decimal import Decimal

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

gymnasts = input()
categories = input()
n = int(input())

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

for i in range(n):
    row = input()

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

                data_incomeing = insert_score(split_categories, cate_bars, cate_beam, cate_floor, spilt_data_input)
                for (key_income, value_income), (key_cate, value_cate) in zip(data_incomeing.items(), data_cate.items()):
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
