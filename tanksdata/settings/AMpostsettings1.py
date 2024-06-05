from auxlib import *
class EdoTensei():
    def __repr__(self):
        for i in app.map.tanks:
            if not i.active:
                i.activate()
        return ''
edotensei = EdoTensei()

if False:
    p1.profile.interface = PlayerInterfaceProfile({
        'minimum_version': Version('1.0'),
        'title': 'EAVZ + AMXbox',
        'bind': (PLAYER_INTERFACE_DIRECT_BIND, PLAYER_INTERFACE_EXTERN_BIND),
        
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
        
        'extern_code': None,
        'extern_path': r'D:\Libs\tankssettings\AMXboxInterface.py',
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
        })

    p1.load_interface()


class EmptyPlayerInterfaceProfile():
    def __init__(self):
        self.minimum_version = Version(0)
        self.title = 'Empty'
        self.bind = ()
        print('Empty being loaded')

p1.unload_interface()
p1.profile.interface = EmptyPlayerInterfaceProfile()
p1.profile.interface.__dict__.update({
    'bind': (PLAYER_INTERFACE_EXTERN_BIND, ),    
    'extern_code': None,
    'extern_path': r'D:\Libs\tankssettings\AMXboxInterface.py',
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
    })
p1.load_interface()


app.root.geometry(str(app.map.profile.grid_size.x*app.scale-30)
                  +'x'
                  +str(app.map.profile.grid_size.y*app.scale)
                  +'+0+500')
app.show_debug_graphics = True
