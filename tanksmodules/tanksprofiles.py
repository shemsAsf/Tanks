"""
1.0: Profils mal gérés, sans logique vis-à-vis des pluriels et des différences noms/adjectifs. Notation "Physics",  "Graphic", "KeyBinds" et autres.
1.1: Cohérences des pluriels et des noms/adjectifs. Remplacement "KeyBinds" par "Interface"
1.2: Documentation actuelle. Aout d'un profil stratégique vide à la classe Bot. Placement de la balise "#please tabify" entre le baackup et la constnte de version pour éviter les problèmes d'indentation liés au passage de code depuis différents IDE. Ajout de l'importations de tanksutils et tanksconsts
1.3: Déplacement des modules vers le dossier tanksmodules
1.4: Reformulation du DEFAULT_MAP_PROFILE (changement dictionnaires vers des listes pour les tanks)
1.5 Rectification erreur copier coller sur les profils Bot/Player. Ajout de DEFAULT_PLAYER_INTERFACE_PROFILE.
1.6. Modification des couleurs des profils graphiques et des valeurs de vitesse des profils physiques.
1.7. Modification des la solidité des murs et d'un s à solid_for_projectiles.
2.0.0: Récupération du code de la version finale de Tanks1 (version fonctionnelle basique).
2.0.1: Passage au nouveau format des versions
2.1.0: Changmement de la strcuture des dictionnaires: passage vers l'intérieur des classes.
2.1.1: Modification des valeurs par défaut de PlayerInterfaceProfile.
2.1.2: Changement de valeur pour le bouton gauche de la souris de l'interface par défaut.
2.2.0: Retour des dictionnaires de valeurs mais modification des __init__ pour assurer des valeurs indépendantes aux différents profils.
2.2.1: Ajout des adresses relatives des murs.
2.2.2: Ajout des adresses relatives des tanks.
2.2.3: Ajout des adresses relatives des tanks.
2.3.0: Ajout des profils séparés des projectiles des players et des bots.
"""


from tanksmodules.tankstoolbox import *
from tanksmodules.tanksutils import *
from tanksmodules.tanksconsts import *



globals().update(new_version('2.3.0', __name__))
#please tabify)
exec(-backup-'Team'>>'D:\\Backups')



class WallGraphicProfile():
    def __init__(self, data={}):
        self.color = None
        self.image_adress = None
        default = {i:DEFAULT_WALL_GRAPHIC_PROFILE_DATA[i] for i in DEFAULT_WALL_GRAPHIC_PROFILE_DATA}
        for i in default:
            if i not in data:
                data.update({i: default[i]})
        for i in data:
            setattr(self, i, new(data[i]))
        
class WallProfile():
    def __init__(self, data={}):
        self.resistance = None
        self.solid_for_projectiles = None
        self.graphics = None
        default = {i:DEFAULT_WALL_PROFILE_DATA[i] for i in DEFAULT_WALL_PROFILE_DATA}
        for i in default:
            if i not in data:
                data.update({i: default[i]})
        for i in data:
            setattr(self, i, new(data[i]))



class ProjectileGraphicProfile():
    def __init__(self, data={}):
        self.color = None
        self.height = None
        self.width = None
        self.point_width = None
        self.image_adress = None
        default = {i:DEFAULT_PROJECTILE_GRAPHIC_PROFILE_DATA[i] for i in DEFAULT_PROJECTILE_GRAPHIC_PROFILE_DATA}
        for i in default:
            if i not in data:
                data.update({i: default[i]})
        for i in data:
            setattr(self, i, new(data[i]))

class ProjectilePhysicalProfile():
    def __init__(self, data={}):
        self.max_speed = None
        default = {i:DEFAULT_PROJECTILE_PHYSICAL_PROFILE_DATA[i] for i in DEFAULT_PROJECTILE_PHYSICAL_PROFILE_DATA}
        for i in default:
            if i not in data:
                data.update({i: default[i]})
        for i in data:
            setattr(self, i, new(data[i]))

class ProjectileProfile():
    def __init__(self, data={}):
        self.graphics = ProjectileGraphicProfile()
        self.physics = ProjectilePhysicalProfile()
        self.destruction_power = None
        self.max_rebound = None
        default = {i:DEFAULT_PROJECTILE_PROFILE_DATA[i] for i in DEFAULT_PROJECTILE_PROFILE_DATA}
        for i in default:
            if i not in data:
                data.update({i: default[i]})
        for i in data:
            setattr(self, i, new(data[i]))



class TankGraphicProfile():
    def __init__(self, data={}):
        self.base_color = None
        self.canon_color = None
        self.height = None
        self.width = None
        self.base_image_adress = None
        self.canon_image_adress = None
        default = {i:DEFAULT_TANK_GRAPHIC_PROFILE_DATA[i] for i in DEFAULT_TANK_GRAPHIC_PROFILE_DATA}
        for i in default:
            if i not in data:
                data.update({i: default[i]})
        for i in data:
            setattr(self, i, new(data[i]))
        
class TankPhysicalProfile():
    def __init__(self, data={}):
        self.max_speed = None
        self.rotation_speed = None
        default = {i:DEFAULT_TANK_PHYSICAL_PROFILE_DATA[i] for i in DEFAULT_TANK_PHYSICAL_PROFILE_DATA}
        for i in default:
            if i not in data:
                data.update({i: default[i]})
        for i in data:
            setattr(self, i, new(data[i]))

class TankProfile():
    def __init__(self, data={}):
        self.graphics = None
        self.physics = None
        self.projectiles = None
        self.ammo_max = None
        default = {i:DEFAULT_TANK_PROFILE_DATA[i] for i in DEFAULT_TANK_PROFILE_DATA}
        for i in default:
            if i not in data:
                data.update({i: default[i]})
        for i in data:
            setattr(self, i, new(data[i]))



class PlayerGraphicProfile(TankGraphicProfile):
    def __init__(self, data={}):
        super(__class__, self).__init__()
        self.base_color = None
        self.base_image_adress = None
        self.canon_image_adresscanon_image_adress = None
        default = {i:DEFAULT_PLAYER_GRAPHIC_PROFILE_DATA[i] for i in DEFAULT_PLAYER_GRAPHIC_PROFILE_DATA}
        for i in default:
            if i not in data:
                data.update({i: default[i]})
        for i in data:
            setattr(self, i, new(data[i]))

class PlayerPhysicalProfile(TankPhysicalProfile):
    def __init__(self, data={}):
        super(__class__, self).__init__()
        default = {i:DEFAULT_PLAYER_PHYSICAL_PROFILE_DATA[i] for i in DEFAULT_PLAYER_PHYSICAL_PROFILE_DATA}
        for i in default:
            if i not in data:
                data.update({i: default[i]})
        for i in data:
            setattr(self, i, new(data[i]))
            
class PlayerInterfaceProfile():
    def __init__(self, data={}):
        super(__class__, self).__init__()
        self.minimum_version = None
        self.title = None
        self.bind = None
        self.direct_methods = None
        self.extern_code = None
        self.extern_path = None
        self.extern_interval = None
        self.extern_events = None
        self.extern_data = None
        default = {i:DEFAULT_PLAYER_INTERFACE_PROFILE_DATA[i] for i in DEFAULT_PLAYER_INTERFACE_PROFILE_DATA}
        for i in default:
            if i not in data:
                data.update({i: default[i]})
        for i in data:
            setattr(self, i, new(data[i]))

class PlayerProfile(TankProfile):
    def __init__(self, data={}):
        super(__class__, self).__init__()
        self.graphics = None
        self.physics = None
        self.interface = None
        self.projectiles = None
        default = {i:DEFAULT_PLAYER_PROFILE_DATA[i] for i in DEFAULT_PLAYER_PROFILE_DATA}
        for i in default:
            if i not in data:
                data.update({i: default[i]})
        for i in data:
            setattr(self, i, new(data[i]))



class BotGraphicProfile(TankGraphicProfile):
    def __init__(self, data={}):
        super(__class__, self).__init__()
        self.base_color = None
        self.base_image_adress = None
        self.canon_image_adress = None
        default = {i:DEFAULT_BOT_GRAPHIC_PROFILE_DATA[i] for i in DEFAULT_BOT_GRAPHIC_PROFILE_DATA}
        for i in default:
            if i not in data:
                data.update({i: default[i]})
        for i in data:
            setattr(self, i, new(data[i]))

class BotPhysicalProfile(TankPhysicalProfile):
    def __init__(self, data={}):
        super(__class__, self).__init__()
        default = {i:DEFAULT_BOT_PHYSICAL_PROFILE_DATA[i] for i in DEFAULT_BOT_PHYSICAL_PROFILE_DATA}
        for i in default:
            if i not in data:
                data.update({i: default[i]})
        for i in data:
            setattr(self, i, new(data[i]))

class BotStrategicProfile():
    def __init__(self, data={}):
        default = {i:DEFAULT_BOT_STRATEGIC_PROFILE_DATA[i] for i in DEFAULT_BOT_STRATEGIC_PROFILE_DATA}
        for i in default:
            if i not in data:
                data.update({i: default[i]})
        for i in data:
            setattr(self, i, new(data[i]))

class BotProfile(TankProfile):
    def __init__(self, data={}):
        self.graphics = None
        self.physics = None
        self.startegies = None
        self.projectiles = None
        super(__class__, self).__init__()
        default = {i:DEFAULT_BOT_PROFILE_DATA[i] for i in DEFAULT_BOT_PROFILE_DATA}
        for i in default:
            if i not in data:
                data.update({i: default[i]})
        for i in data:
            setattr(self, i, new(data[i]))



class MapProfile():
    def __init__(self, data={}):
        self.title = None
        self.grid_size = None
        self.background_color = None
        self.background_image_adress = None
        self.player_list = None
        self.bot_list = None
        self.wall_list = None
        default = {i:DEFAULT_MAP_PROFILE_DATA[i] for i in DEFAULT_MAP_PROFILE_DATA}
        for i in default:
            if i not in data:
                data.update({i: default[i]})
        for i in data:
            setattr(self, i, new(data[i]))



DEFAULT_WALL_GRAPHIC_PROFILE_DATA = {
    'color': 'saddle brown',
    'image_adress': r'tanksdata|images|default|default_wall.png'.replace('|', SEP),
    }
DEFAULT_WALL_GRAPHIC_PROFILE = WallGraphicProfile()

DEFAULT_WALL_PROFILE_DATA = {
    'resistance': 1000,
    'solid_for_projectiles': True,
    'graphics': WallGraphicProfile,
    }
DEFAULT_WALL_PROFILE = WallProfile()



DEFAULT_PROJECTILE_GRAPHIC_PROFILE_DATA = {
    'color': 'grey',
    'height': 15,
    'width': 28,
    'point_width': 5,
    'image_adress': r'tanksdata|images|default|default_projectile.png'.replace('|', SEP),
    }
DEFAULT_PROJECTILE_GRAPHIC_PROFILE = ProjectileGraphicProfile()

DEFAULT_PROJECTILE_PHYSICAL_PROFILE_DATA = {
    'max_speed': 125
    }
DEFAULT_PROJECTILE_PHYSICAL_PROFILE = ProjectilePhysicalProfile()

DEFAULT_PROJECTILE_PROFILE_DATA = {
    'graphics': ProjectileGraphicProfile,
    'physics': ProjectilePhysicalProfile,
    'destruction_power': 1,
    'max_rebound': 2,
    }
DEFAULT_PROJECTILE_PROFILE = ProjectileProfile()

DEFAULT_PLAYER_GRAPHIC_PROJECTILE_PROFILE = ProjectileGraphicProfile({
    'image_adress': r'tanksdata|images|default|default_player_projectile.png'.replace('|', SEP),
    })
DEFAULT_PLAYER_PROJECTILE_PROFILE = ProjectileProfile({
    'graphics': DEFAULT_PLAYER_GRAPHIC_PROJECTILE_PROFILE
    })

DEFAULT_BOT_GRAPHIC_PROJECTILE_PROFILE = ProjectileGraphicProfile({
    'image_adress': r'tanksdata|images|default|default_bot_projectile.png'.replace('|', SEP),
    })
DEFAULT_BOT_PROJECTILE_PROFILE = ProjectileProfile({
    'graphics': DEFAULT_BOT_GRAPHIC_PROJECTILE_PROFILE
    })


DEFAULT_TANK_GRAPHIC_PROFILE_DATA = {
    'base_color': 'white',
    'canon_color': 'grey',
    'height': 32,
    'width': 32,
    'base_image_adress': r'tanksdata|images|default|default_tank_base.png'.replace('|', SEP),
    'canon_image_adress': r'tanksdata|images|default|default_tank_canon.png'.replace('|', SEP),
    }
DEFAULT_TANK_GRAPHIC_PROFILE = TankGraphicProfile()

DEFAULT_TANK_PHYSICAL_PROFILE_DATA = {
    'max_speed': 100, #pix/s
    'rotation_speed': None,
    }
DEFAULT_TANK_PHYSICAL_PROFILE = TankPhysicalProfile()

DEFAULT_TANK_PROFILE_DATA = {
    'graphics': TankGraphicProfile,
    'physics': TankPhysicalProfile,
    'projectiles': ProjectileProfile,
    'ammo_max': 5,
    }
DEFAULT_TANK_PROFILE = TankProfile()



DEFAULT_PLAYER_GRAPHIC_PROFILE_DATA = {
    'base_color': 'IndianRed3',
    'base_image_adress': r'tanksdata|images|default|default_player_base.png'.replace('|', SEP),
    'canon_image_adress': r'tanksdata|images|default|default_tank_canon.png'.replace('|', SEP),
    }
DEFAULT_PLAYER_GRAPHIC_PROFILE = PlayerGraphicProfile()

DEFAULT_PLAYER_PHYSICAL_PROFILE_DATA = {
    #Rien ne diffère de DEFAULT_TANK_PHYSICAL_PROFILE
    }
DEFAULT_PLAYER_PHYSICAL_PROFILE = PlayerPhysicalProfile()

DEFAULT_PLAYER_INTERFACE_PROFILE_DATA = {
    'minimum_version': Version('1.0'),
    'title': 'ZQSD',
    'bind': (PLAYER_INTERFACE_DIRECT_BIND, ), 
    'direct_methods': (PLAYER_INTERFACE_KEYS_METHOD, PLAYER_INTERFACE_MOUSE_MOTION_METHOD, PLAYER_INTERFACE_MOUSE_BUTTONS_METHOD),
    PLAYER_INTERFACE_KEYS_METHOD: [
        ('z', PLAYER_INTERFACE_MOVE_BY_FUNCTION, ( 0, -1)),
        ('q', PLAYER_INTERFACE_MOVE_BY_FUNCTION, (-1,  0)),
        ('s', PLAYER_INTERFACE_MOVE_BY_FUNCTION, ( 0, +1)),
        ('d', PLAYER_INTERFACE_MOVE_BY_FUNCTION, (+1,  0)),
        ('space', PLAYER_INTERFACE_SHOOT_PROJECTILE_FUNCTION, ()),
        ],
    PLAYER_INTERFACE_MOUSE_MOTION_METHOD: [
        PLAYER_INTERFACE_POINT_FROM_EVENT_FUNCTION,
        ],
    PLAYER_INTERFACE_MOUSE_BUTTONS_METHOD: [
        (1, PLAYER_INTERFACE_SHOOT_PROJECTILE_FUNCTION, ()),
        ],
    }
DEFAULT_PLAYER_INTERFACE_PROFILE = PlayerInterfaceProfile()

DEFAULT_PLAYER_PROFILE_DATA = {
    'graphics': PlayerGraphicProfile,
    'physics': PlayerPhysicalProfile,
    'interface': PlayerInterfaceProfile,
    'projectiles': DEFAULT_PLAYER_PROJECTILE_PROFILE,
    }
DEFAULT_PLAYER_PROFILE = PlayerProfile


DEFAULT_BOT_GRAPHIC_PROFILE_DATA = {
    'base_color': 'dark olive green',
    'base_image_adress': r'tanksdata|images|default|default_bot_base.png'.replace('|', SEP),
    'canon_image_adress': r'tanksdata|images|default|default_tank_canon.png'.replace('|', SEP),
    }
DEFAULT_BOT_GRAPHIC_PROFILE = BotGraphicProfile()

DEFAULT_BOT_PHYSICAL_PROFILE_DATA = {
    #Rien ne diffère de DEFAULT_TANK_PHYSICAL_PROFILE
    }
DEFAULT_BOT_PHYSICAL_PROFILE = BotPhysicalProfile()

DEFAULT_BOT_STRATEGIC_PROFILE_DATA = {
    #magienoire
    }
DEFAULT_BOT_STRATEGIC_PROFILE = BotStrategicProfile()

DEFAULT_BOT_PROFILE_DATA = {
    'graphics': BotGraphicProfile,
    'physics': BotPhysicalProfile,
    'startegies': BotStrategicProfile,
    'projectiles': DEFAULT_BOT_PROJECTILE_PROFILE,
    }
DEFAULT_BOT_PROFILE = BotProfile()



DEFAULT_MAP_PROFILE_DATA = {
    'title': 'Bois',
    'grid_size': Point(24, 12),     
    'background_color': 'bisque',
    'background_image_adress': r'tanksdata|images|default|default_map.png'.replace('|', SEP),
    'player_list': [
        (Point(5, 3), PlayerProfile()),
        ],
    'bot_list': [
        (Point(20, 5), BotProfile()),
        ],
    'wall_list': {
        Corners(9, 3, 10, 9): WallProfile(),
        Corners (14, 3, 15, 9): WallProfile(),
        },
    }
DEFAULT_MAP_PROFILE = MapProfile()

if __name__ == '__main__':
    pass
elif 'VERSION' in globals():
    print(__name__ + str().join([' ' for i in range(30-len(__name__))]) + ' ' + VERSION + ' successfully imported') 
    del VERSION
 
