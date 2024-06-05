"""
1.0: Premierères constantes DEFAULT_APP_SCALE, DEFAULT_TANK_BASE_ROTATION, DEFAULT_TANK_CANON_ROTATION.
1.1: Ajout constantees pour PlayerInterfaceProfile.
1.1.? Passage des constantes k1, k2, k3 pour le dessin du canon.
1.2.? Ajout de constantes.
2.0.0: Récupération du code de la version finale de Tanks1 (version fonctionnelle basique).
2.0.1: Passage au nouveau format des versions.
2.0.2: Ajout de constantes liées aux interfaces joueur externes.
2.0.3: Modification de TANK_CANON_WIDTH_RATIO
"""

from tanksmodules.tanksutils import *

globals().update(new_version('2.0.2', __name__))

SEP = os.path.sep

DEFAULT_APP_SCALE = 32
MESSAGE_BOX_TITLE = 'Tanks'
MAP_WINDOW_TITLE = 'Tanks'
DEFAULT_WINDOW_TITLE = 'Tanks'


START_MENU_GEOMETRY = Point(500, 360)
START_MENU_TITLE = 'Tanks'
START_MENU_BG_IMAGE_ADRESS = r'tanksdata|images|menus|bg.png'.replace('|', SEP)
START_MENU_BUTTON_NEW_GAME_BT_IMAGE_ADRESS = r'tanksdata|images|menus|bt.png'.replace('|', SEP)
START_MENU_DEBUG_ACCESS_IMAGE_BT_ADRESS = r'tanksdata|images|menus|bt.png'.replace('|', SEP)
START_MENU_HELP_BT_IMAGE_ADRESS = r'tanksdata|images|menus|bt.png'.replace('|', SEP)
START_MENU_QUIT_BT_IMAGE_ADRESS = r'tanksdata|images|menus|bt.png'.replace('|', SEP)
START_MENU_BUTTON_STYLE = {
    'compound': 'c',
    'relief': FLAT,
    'overrelief': GROOVE,
    'font': ('Calibri', 12),
    'fg': 'white',
    }

IDLE_MENU_SHORTCUT = '<Control-space>'
IDLE_MENU_TITLE = 'Tanks IDLE'
IDLE_MENU_GEOMETRY = Point(750, 500)
IDLE_MENU_MID_HEIGHT = 300

MAPS_MENU_GEOMETRY = Point(200, 250)
MAPS_MENU_TITLE = 'Sélection de la carte'

PLAYERS_MENU_GEOMETRY = Point(400, 280)
PLAYERS_MENU_TITLE = 'Sélection des joueurs'

DEFAULT_TANK_BASE_ROTATION = 270
DEFAULT_TANK_CANON_ROTATION = 270

DEFAULT_TANK_MOVE_INTERVAL = 100

TANK_CANON_WIDTH_RATIO = 1.15
TANK_CANON_HEIGHT_RATIO = 0.3
TANK_CANON_BACK_RATIO = 0.175



PLAYER_INTERFACE_DIRECT_BIND = 'player_interface_direct_bind'
PLAYER_INTERFACE_EXTERN_BIND = 'player_interface_extern_bind'
PLAYER_INTERFACE_HANDLED_BINDS = (PLAYER_INTERFACE_DIRECT_BIND, PLAYER_INTERFACE_EXTERN_BIND),
PLAYER_INTERFACE_KEYS_METHOD = 'player_interface_keys_method'
PLAYER_INTERFACE_EXTERN_METHOD = 'player_interface_extern_method'
PLAYER_INTERFACE_MOUSE_MOTION_METHOD = 'player_interface_mouse_motion_method'
PLAYER_INTERFACE_MOUSE_BUTTONS_METHOD = 'player_interface_mouse_buttons_method'
PLAYER_INTERFACE_HANDLED_METHODS = (PLAYER_INTERFACE_KEYS_METHOD, PLAYER_INTERFACE_MOUSE_MOTION_METHOD, PLAYER_INTERFACE_MOUSE_BUTTONS_METHOD)
PLAYER_INTERFACE_MOVE_BY_FUNCTION = 'move_by'
PLAYER_INTERFACE_SHOOT_PROJECTILE_FUNCTION = 'shoot'
PLAYER_INTERFACE_POINT_AT = 'rotate_canon_at'
PLAYER_INTERFACE_POINT_TO = 'rotate_canon_to'
PLAYER_INTERFACE_POINT_FROM_EVENT_FUNCTION = 'rotate_canon_from_event'
PLAYER_INTERFACE_POINT_TO_FUNCTION = 'rotate_canon_to'

DEFAULT_PLAYER_MOVE_BY_INTERVAL = 100



DEFAULT_BOT_MOVE_INTERVAL = 100
DEFAULT_BOT_ROTATION_CANON_INTERVAL = 15
DEFAULT_BOT_MINIMUM_DELAY = 500
DEFAULT_BOT_MAXIMUM_DELAY = 1000
DEFAULT_BOT_DELAY_STEP = 100

DEFAULT_BOT_RANDOM_ANGLE_STEP = 0.5
DEFAULT_BOT_MINIMUM_RANDOM_REMAINING_LOOPS = 5
DEFAULT_BOT_MAXIMUM_RANDOM_REMAINING_LOOPS = 10



if __name__ == '__main__':
	pass
elif 'VERSION' in globals():
	print(__name__ + str().join([' ' for i in range(30-len(__name__))]) + ' ' + VERSION + ' successfully imported') 
	del VERSION
