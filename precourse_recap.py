number_of_game = 38
current_game_play = 29
total_points = 72
point_for_win = 3
point_for_draw = 1
point_for_loss = 0

def game_to_go():
    games_left = number_of_game - current_game_play
    points_left = point_for_win * games_left
    print(f"only {games_left} games and {points_left} points to go!")

def motivation():
    print("C'mon you Arsenal!!!")

game_to_go()
motivation()        


