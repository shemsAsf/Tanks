def is_valid():
    return (True, '')

data = {
    'interface': PlayerInterfaceProfile({
        'minimum_version': Version('1.0'),
        'title': 'Fleches',
        'bind': (PLAYER_INTERFACE_DIRECT_BIND, ),        
        'direct_methods': (PLAYER_INTERFACE_KEYS_METHOD, PLAYER_INTERFACE_MOUSE_MOTION_METHOD, PLAYER_INTERFACE_MOUSE_BUTTONS_METHOD),
        PLAYER_INTERFACE_KEYS_METHOD: [
            ('Up', PLAYER_INTERFACE_MOVE_BY_FUNCTION, ( 0, -1)),
            ('Left', PLAYER_INTERFACE_MOVE_BY_FUNCTION, (-1,  0)),
            ('Down', PLAYER_INTERFACE_MOVE_BY_FUNCTION, ( 0, +1)),
            ('Right', PLAYER_INTERFACE_MOVE_BY_FUNCTION, (+1,  0)),
            ('space', PLAYER_INTERFACE_SHOOT_PROJECTILE_FUNCTION, ()),            ('z', PLAYER_INTERFACE_MOVE_BY_FUNCTION, ( 0, -1)),
            ],    
        PLAYER_INTERFACE_MOUSE_MOTION_METHOD: [
            PLAYER_INTERFACE_POINT_FROM_EVENT_FUNCTION,
            ],
        PLAYER_INTERFACE_MOUSE_BUTTONS_METHOD: [
            ('Button-1', PLAYER_INTERFACE_SHOOT_PROJECTILE_FUNCTION, ()),
            ],
        }),
    }
