data = {
    'title': 'Bois',
    'grid_size': Point(28, 24),     
    'background_color': 'bisque',
    'background_image_adress': r'tanksdata|images|default|default_map.png'.replace('|', SEP),
    'player_list': [
        (Point(3, 3), PlayerProfile()),
        (Point(12, 3), PlayerProfile()),
        ],
    'bot_list': [
        (Point(25, 11), BotProfile()),
        (Point(22, 20), BotProfile()),
        (Point(4, 19), BotProfile()),
        ],
    'wall_list': {
        Corners(20,1,21,8):WallProfile(),
        Corners(17,6,20,7):WallProfile(),
        Corners(1,8,8,9):WallProfile(),
        Corners(8,8,9,13):WallProfile(),
        Corners(16,14,20,15):WallProfile(),
        Corners(12,20,13,24):WallProfile(),
        Corners(23,17,27,18):WallProfile(),
        },
    }
