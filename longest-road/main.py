import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# 1
path = [
    "#a###",
    "#a###",
    "#a###",
    "#aa##",
    "##a##"
]
road_player1_pack = {"A" : 
                        {"index_of_road": [],
                         "total_in_line": []
                        }
                    }
road_player1 = "a"

n = 5
for line in path:

    continuous_path = False
    player_1_index = road_player1_pack["A"]["index_of_road"]
    player_1_total = road_player1_pack["A"]["total_in_line"]

    for index_of_line, find_road in enumerate(line):
        if find_road == road_player1:

            # same index add in road
            if player_1_index != [] and index_of_line == player_1_index[-1]:
                player_1_index.append(index_of_line)
                player_1_total.append(line.count(road_player1))
                continuous_path = True

            # in one line more road
            if (continuous_path == True) and (index_of_line == player_1_index[-1]-1  or index_of_line == player_1_index[-1]+1):
                player_1_index.append(index_of_line)
                player_1_total.append(line.count(road_player1))

            if player_1_index == []:
                player_1_index.append(index_of_line)
                player_1_total.append(line.count(road_player1))

    total_length_of_player1 = len(player_1_total)
    road_player1_pack["A"]["total_length"] = len(player_1_total)
 
for key_pack, value_pack in road_player1_pack.items():
    print(key_pack, value_pack["total_length"])