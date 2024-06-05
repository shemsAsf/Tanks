i = 0

data = {
    'title': 'Toto',
    'grid_size': Point(24, 10),     
    'background_color': 'bisque',
    'background_image_adress': r'tanksdata|images|default|default_map2.png'.replace('|', SEP),
    'player_list': [
        (Point(2, 2), PlayerProfile()),
        (Point(2, 8), PlayerProfile()),
        (Point(2, 4), PlayerProfile()),
        (Point(2, 6), PlayerProfile()),
        ],
    'bot_list': [
        (Point(21, 2), BotProfile()),
        (Point(21, 7), BotProfile()),
        ],
    'wall_list': {
        Corners(i+3, 3, i+6, 4): WallProfile(),
        Corners(i+4, 4, i+5, 7): WallProfile(),
        Corners(i+8, 3, i+11, 4): WallProfile(),
        Corners(i+8, 4, i+9, 6): WallProfile(),
        Corners(i+10, 4, i+11, 6): WallProfile(),
        Corners(i+8, 6, i+11, 7): WallProfile(),
        },
    }

i = 10

data['wall_list'].update({
        Corners(i+3, 3, i+6, 4): WallProfile(),
        Corners(i+4, 4, i+5, 7): WallProfile(),
        Corners(i+8, 3, i+11, 4): WallProfile(),
        Corners(i+8, 4, i+9, 6): WallProfile(),
        Corners(i+10, 4, i+11, 6): WallProfile(),
        Corners(i+8, 6, i+11, 7): WallProfile(),
        })

del i
