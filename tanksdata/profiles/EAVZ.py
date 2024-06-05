def is_valid():
    return (True, '')

data = {
    'interface': PlayerInterfaceProfile({
        'minimum_version': Version('1.0'),
        'title': 'EAVZ + Xbox360',
        'bind': (PLAYER_INTERFACE_DIRECT_BIND, ),        
        'direct_methods': (PLAYER_INTERFACE_KEYS_METHOD, PLAYER_INTERFACE_MOUSE_MOTION_METHOD, PLAYER_INTERFACE_MOUSE_BUTTONS_METHOD),
        PLAYER_INTERFACE_KEYS_METHOD: [
            ('e', PLAYER_INTERFACE_MOVE_BY_FUNCTION, ( 0, -1)),
            ('a', PLAYER_INTERFACE_MOVE_BY_FUNCTION, (-1,  0)),
            ('v', PLAYER_INTERFACE_MOVE_BY_FUNCTION, ( 0, +1)),
            ('z', PLAYER_INTERFACE_MOVE_BY_FUNCTION, (+1,  0)),
            ('r', PLAYER_INTERFACE_SHOOT_PROJECTILE_FUNCTION, ()),
            ],    
        PLAYER_INTERFACE_MOUSE_MOTION_METHOD: [
            PLAYER_INTERFACE_POINT_FROM_EVENT_FUNCTION,
            ],
        PLAYER_INTERFACE_MOUSE_BUTTONS_METHOD: [
            ('Button-1', PLAYER_INTERFACE_SHOOT_PROJECTILE_FUNCTION, ()),
            ],
        }),
    }
