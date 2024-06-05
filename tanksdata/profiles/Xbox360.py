def is_valid():
    try:
        import inputs
    except:
        return (False, 'Cette interface necessite l\'installation de la bibliothèque "inputs"')
    else:
        return (True, '')

data = {
    'interface': PlayerInterfaceProfile({
        'minimum_version': Version('1.0'),
        'title': 'Xbox360',
        'bind': (PLAYER_INTERFACE_DIRECT_BIND, PLAYER_INTERFACE_EXTERN_BIND),
        
        'extern_code': None,
        'extern_path': r'tanksdata|drivers|Xbox360GamepadDriver.py'.replace('|', SEP),
        'extern_interval': 50,
        'extern_events': {},
        'extern_data': {
            'move_position_x': 0,
            'move_position_y': 0,
            'canon_position_x': 0,
            'canon_position_y': 0,
            },
        'extern_methods': (PLAYER_INTERFACE_EXTERN_METHOD),
        PLAYER_INTERFACE_EXTERN_METHOD: [
            ('ABS_X_Y', PLAYER_INTERFACE_MOVE_BY_FUNCTION, ('move_position_x', 'move_position_y')),
            ('ABS_RX_RY', PLAYER_INTERFACE_POINT_TO, ('canon_position_x', 'canon_position_y')),
            ('ABS_RZ', PLAYER_INTERFACE_SHOOT_PROJECTILE_FUNCTION, ()),
            ],
        }),
    }
