data = {
    'title': 'Bois',
    'grid_size': Point(32, 16),     
    'background_color': 'bisque',
    'background_image_adress': r'tanksdata|images|default|default_map.png'.replace('|', SEP),
    'player_list': [
        (Point(8, 13), PlayerProfile()),
        (Point(2, 3), PlayerProfile()),
        (Point(3, 14), PlayerProfile()),
        (Point(17, 13), PlayerProfile()),
        ],
    'bot_list': [
        (Point(16, 3), BotProfile()),
        (Point(29, 2), BotProfile()),
        (Point(28, 9), BotProfile()),
        ],
    'wall_list': {
        Corners(5, 1, 6, 3): WallProfile(),
        Corners(27, 5, 31, 6): WallProfile(),
        Corners(1, 11, 4, 12): WallProfile(),
        Corners(26, 12, 27, 15): WallProfile(),
        Corners(10, 6, 11, 9): WallProfile(),
        Corners(10, 6, 21, 7): WallProfile(),
        Corners(21, 6, 22, 10): WallProfile(),
        Corners(10, 9, 21, 10): WallProfile(),
        },
    }
