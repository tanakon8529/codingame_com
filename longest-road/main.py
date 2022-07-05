import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
    
path1 = [
    "#a###",
    "#a###",
    "#a###",
    "#aa##",
    "##a##"
]
road_player1_pack = {"player_1" : 
                        {"index_of_road": [],
                         "total_in_line": []
                        }
                    }
road_player1 = "a"

n = 5
for line, i in zip(path1, n):

    redirect = False
    player_1_index = road_player1_pack["player_1"]["index_of_road"]
    player_2_total = road_player1_pack["player_1"]["total_in_line"]

    if road_player1 in line:
        player_1_index.append(line.find(road_player1))
        player_2_total.append(line.count(road_player1))

        if player_2_total > 1 and player_1_index[i] != player_1_index[i-1]:
            redirect = True

print(road_player1_pack)