data = {
    'title': 'Bois',
    'grid_size': Point(24, 12),     
    'background_color': 'bisque',
    'background_image_adress': r'tanksdata|images|default|default_map.png'.replace('|', SEP),
    'player_list': [
        (Point(2, 10), PlayerProfile()),
        (Point(2, 3), PlayerProfile()),
        (Point(7, 7), PlayerProfile()),
        ],
    'bot_list': [
        (Point(21, 6), BotProfile()),
        ],
    'wall_list': {
        Corners(4, 1, 5, 5): WallProfile(),
        Corners (8, 3, 9, 9): WallProfile(),
        Corners (4, 8, 5, 12): WallProfile(),
        Corners (20, 8, 21, 12): WallProfile(),
        Corners (20, 1, 21, 5): WallProfile(),
        Corners (16, 3, 17, 9): WallProfile(),
        Corners (11, 5, 14, 7): WallProfile(),
        },
    }
