
from warnings import warn
from tkinter import *

VERSION_OF_tankmodules = ('2.0.1', __name__)

def race(loop1, loop2, caller, f1, f2, *args, **kargs):
    import time
    t1 = 0
    t2 = 0
    if caller in (None, 0, '', [], (), {}):
        for i in range(loop1):
            for j in range(loop2):
                t = time.time()
                f1(*args, **kargs)
                t1 += time.time() - t
            for j in range(loop2):
                t = time.time()
                f2(*args, **kargs)
                t2 += time.time() - t
    else:
        for i in range(loop1):
            for j in range(loop2):
                t = time.time()
                caller.f1(*args, **kargs)
                t1 += time.time() - t
            for j in range(loop2):
                t = time.time()
                caller.f2(*args, **kargs)
                t2 += time.time()   - t
    if t1>t2:
        return (t1/(loop1*loop2), '>', t2/(loop1*loop2))
    else:
        return (t1/(loop1*loop2), '<', t2/(loop1*loop2))
                            
def dictprint(var, margins='', name=''):
    if name != '':
        name_ = name + ' '
    if type(var) == dict:
        if margins == '':
            print(name_ + '<class \'dict\'>')
            dictprint(var, '    ')
        else:
            for i in sorted([i for i in var.keys()]):
                if type(var[i]) == dict:
                    print(margins, i, ' : ', '<class \'dict\'>', sep='')
                    dictprint(var[i], margins+' ')
                else:
                    print(margins, i, ' : ', var[i], sep = '')
    else:
        raise TypeError('type(var) must be '+str(type({}))+', not '+str(type(var)))

def rng(var1, var2=None):
    if type(var1) in (str, list):
        return [i for i in range(len(var1))]
    elif type(var1) == int:
        if var2 == None:
            return [i for i in range(var1+1)]
        else:
            return [i for i in range(var1, var2+1)]

def rng_(var):
    return [i for i in range(len(var))]

def forp(list, lower=None, upper=None, idx=False):
    if type(list) == dict:
        dictprint(list)
    else:
        l = list
        if lower == max:
            for i in l:
                print(i)
        elif lower != None and upper == None:
            for i in range(lower+1):
                if idx:
                    print(i, l[i])
                else:
                    print(l[i])
        elif lower != None and upper != None:
            for i in rng(lower, upper):
                if idx:
                    print(i, l[i])
                else:
                    print(l[i])
        elif len(l) < 30:
            for i in rng(l):
                if idx:
                    print(i, l[i])
                else:
                    print(l[i])
        else:      
            for i in range(30):
                if idx:
                    print(i, l[i])
                else:
                    print(l[i])
            
def str_dels(var, idx, nb):
    lv = [i for i in var]
    for i in range(nb):
        del lv[idx]
    result = ''
    for i in lv:
        result += i
    return result

#please tabify
class Backup():
    DEFAULT_WARN = True
    def __init__(self):
        self.self_delete = True
        self.warn = True
        self.author = ''
        self.script = \
"""
def temp_Backup_saveto(directory, author_=None):
    author = '_'
    if author_ != '':
        author += author_ + '_'
    from os import listdir, path
    from time import time
    code = '#' + str(time()) + '\\n'
    import builtins
    with builtins.open(__file__, 'r') as f:
        for i in f:
            code += i
    l = [i for i in __file__]
    while l[len(l)-1] not in '\|/':
        del l[len(l)-1]
    file_directory = ''
    file_name_without_ex = path.basename(__file__)
    file_name_without_ex = str_dels(file_name_without_ex, len(file_name_without_ex)-3, 3)
    for i in l:
        file_directory += i
    l = listdir(directory)
    i = 1
    while f'{file_name_without_ex}{author}v{str(i)}.py' in l:
        i += 1
    with builtins.open(directory+f'\\{file_name_without_ex}{author}v{str(i)}.py', 'x') as f:
        for i in code:
            f.write(i)
"""
    def __neg__(self):
        self.warn = not Backup.DEFAULT_WARN
        return self
    def __sub__(self, other):
        self.author = other
        return self
    def __invert__(self):
        self.self_delete = False
        return self
    def __rshift__(self, other):
        from os import path
        import builtins
        result = ''
        if path.exists(other):
            result = self.script +f"\ntemp_Backup_saveto(r'{other}\', '{self.author}')\ndel temp_Backup_saveto"
        elif self.warn:
            result = ''
            warn('Impossible to access backup directory')
        if self.self_delete:
            result += '\ndel backup'
        return result

class Tabify:
    
    BEACON = '#please tabify'
    REPLACEMENT = ('    ', '\t')

    WINDOW_TITLE = 'Tabify'
    MESSAGE_TITLE = 'Copied !'
    MESSAGE_TIMEOUT = 1500
    LOOP_INTERVAL = 100
    ACTIVE_TEXT = 'Active'
    INACTIVE_TEXT = 'Stoped'

    def __init__(self):
        self.last_data = ''
        self.active = True
        self.root = Tk()
        self.b = Button(self.root, text=Tabify.ACTIVE_TEXT, command=self.click)
        self.b.pack(fill=BOTH)
        self.root.title(Tabify.WINDOW_TITLE)
        self.loop()
        self.root.attributes('-topmost', True)
        self.root.mainloop()

    def loop(self):
        data = self.last_data
        try:
            data = self.root.clipboard_get()
        except:
            pass#warn('Can\'t read clipboard')
        if self.last_data != data:
            if Tabify.BEACON in data:
                notify = True  
                try:
                    if self.active:
                        self.root.clipboard_clear()
                        self.root.clipboard_append(data.replace(*Tabify.REPLACEMENT))
                except:
                    #warn('Can\'t write clipboard')
                    notify = False
                #print(notify, can_flash)
                if notify:
                    self.root.title(Tabify.MESSAGE_TITLE)
                    self.root.after(Tabify.MESSAGE_TIMEOUT, lambda: self.root.title(Tabify.WINDOW_TITLE))
        self.last_data = data
        self.root.after(Tabify.LOOP_INTERVAL, self.loop)

    def click(self):
        self.active = not self.active
        if self.active:
            self.b.config(text=Tabify.ACTIVE_TEXT)
        else:
            self.b.config(text=Tabify.INACTIVE_TEXT)

backup = Backup()

if __name__ == '__main__':
    try:
        exec(-backup-'AdrienMecibah'>>r'D:\Backups')
    except:
        raise Exception
from os import *
from math import sqrt, cos, sin, acos, asin, atan, degrees, radians
import os
import math

VERSION_OF_tankmodules = ('2.1.2', __name__)

GLOBAL_VERSION_PREFIX = 'VERSION_OF_'

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __invert__(self):
        return (self.x, self.y)
    def in_circle(self, x, y, r):
        return (x-self.x)**2+(y-self.y)**2 <= r**2

class Vect():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __invert__(self):
        return (self.x, self.y)
    def __abs__(self):
        return (self.x*self.x+self.y*self.y)**0.5

class Corners():
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
    def __invert__(self):
        return (self.left, self.top, self.right, self.bottom)
    def __contains__(self, other):
        return self.left < other.x < self.right and self.top < other.y < self.bottom
    

class SuperDict():
    def __init__(self, data={}):
        self.data = data
    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None
    def __setitem__(self, key, item):
        if key in self.data:
            self.data[key] = item
            return True
        else:
            return False
    def __add__(self, other):
        if type(other) == dict:
            new = dict()
            new.update(self.data)
            new.update(other)
            return SuperDict(new)
        else:
            raise TypeError('Second element is not dict')
    def __radd__(self, other):
        if type(other) == dict:
            self.data.update(other)
        else:
            raise TypeError('Second element is not dict')
    def __repr__(self):
        try:
            dictprint(self.data)
            return ''
        except:
            return self.data.__repr__()    
    def __str__(self):
        return self.data.__str__()
    def __invert__(self):
        return self.data
    def __len__(self):
        return  len(self.data)
    def __call__(self, other):
        if other in self.data:
            return self.data[other]
        else:
            return other
    def __contains__(self, other):
        return other in self.data
    def __iter__(self):
        return iter(self.data)
    def set(self, key, item):
        return self.__setitem__(key, item)



class Version():
    ORDER = {'     ':0, '   ':0, '?':26, 'a':0, 'A':0, 'b':1, 'B':1, 'c':2, 'C':2, 'd':3, 'D':3, 'e':4, 'E':4, 'f':5, 'F':5, 'g':6, 'G':6, 'h':7, 'H':7, 'i':8, 'I':8, 'j':9, 'J':9, 'k':10, 'K':10, 'l':11, 'L':11, 'm':12, 'M':12, 'n':13, 'N':13, 'o':14, 'O':14, 'p':15, 'P':15, 'q':16, 'Q':16, 'r':17, 'R':17, 's':18, 'S':18, 't':19, 'T':19, 'u':20, 'U':20, 'v':21, 'V':21, 'w':22, 'W':22, 'x':23, 'X':23, 'y':24, 'Y':24, 'z':25, 'Z':25, '0':26, '1':27, '2':28, '3':29, '4':30, '5':31, '6':32, '7':33, '8':34, '9':35, '10':36, '11':37, '12':38, '13':39, '14':40, '15':41, '16':42, '17':43, '18':44, '19':45, '20':46, '21':47, '22':48, '23':49, '24':50, '25':51, '26':52, '27':53, '28':54, '29':55, '30':56, '31':57, '32':58, '33':59, '34':60, '35':61, '36':62, '37':63, '38':64, '39':65, '40':66, '41':67, '42':68, '43':69, '44':70, '45':71, '46':72, '47':73, '48':74, '49':75, '50':76, '51':77, '52':78, '53':79, '54':80, '55':81, '56':82, '57':83, '58':84, '59':85, '60':86, '61':87, '62':88, '63':89, '64':90, '65':91, '66':92, '67':93, '68':94, '69':95, '70':96, '71':97, '72':98, '73':99, '74':100, '75':101, '76':102, '77':103, '78':104, '79':105, '80':106, '81':107, '82':108, '83':109, '84':110, '85':111, '86':112, '87':113, '88':114, '89':115, '90':116, '91':117, '92':118, '93':119, '94':120, '95':121, '96':122, '97':123, '98':124, '99':125}
    def __init__(self, value, name='unnamed'):
        self.name = name
        if type(value) == str:
            self.value = value.split('.')
        elif type(value) == float:
            self.value = str(value).split('.')
        elif type(value) == int:
            self.value = [i for i in str(value)]
        elif type(value) == list:
            self.value = value
        elif type(value) == Version:
            self.value = ~value
        else:
            raise TypeError()
    def __str__(self):
        result = str().join([i+'.' for i in [self.value[i] for i in range(len(self.value)-1)]])
        result += self.value[len(self.value)-1]
        return result
    def __invert__(self):
        return self.value
    def __neg__(self):
            return [Version.ORDER[i] for i in ~self]
    def __getitem__(self, key):
        return self.value[key]
    def __lt__(self, other):
        return -self < -Version(other)
    def __eq__(self, other):
        return -self == -Version(other)
    def __ne__(self, other):
        return -self != -Version(other)
    def __gt__(self, other):
        return -self > -Version(other)
    def __le__(self, other):
        return -self <= -Version(other)
    def __ge__(self, other):
        return -self >= -Version(other)

class ArtificialKeySymEvent():
    def __init__(self, keysym):
        self.keysym = keysym

class ArtificialNumEvent():
    def __init__(self, num):
        self.num = num

def new_version(version_number, version_name=None):
    if version_name:
        return {GLOBAL_VERSION_PREFIX+version_name.replace('.', '_'): Version(version_number, version_name), GLOBAL_VERSION_PREFIX+version_name: Version(version_number, version_name)}
    return {GLOBAL_VERSION_PREFIX+version_name.replace('.', '_'): Version(version_number), GLOBAL_VERSION_PREFIX+version_name: Version(version_number, version_name)}

def new(var):
    if type(var) == type:
        return var()
    elif type(var) in (int, str, float, list, tuple, dict, set):
        return type(var)(var)
    elif type(var) in (Point, Corners):
        return Point(*~var)
    else:
        return var

def point_to_degree_angle(x, y):
    angle = 0
    if not (x == 0 and y == 0):
        if x != 0:
            c = 0
            if x < 0:
                c = 180
            angle = (c+math.degrees(atan(y/x))) % 360
        else:
            angle = 90*(y / abs(y))%360
    return angle

def opacify(data, color, opacity):
    result = list()
    for i in data:
        if i == color:
            result += [(color[0], color[1], color[2], 255*opacity)]
        else:
            result += [i]
    return result

if True:
    import builtins
    open = builtins.open


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


def nickname_objects(app, globals_dict):
    for l, p in [(getattr(app.map, i), i[0]) for i in 'players bots static_items'.split(' ')]:
        for i in range(len(l)):
            globals_dict.update({p+str(i+1): l[i]})

def show_versions(globals_dict, suffix=' successfully imported'):
    max_length = 0
    for version_name in globals_dict:
        if GLOBAL_VERSION_PREFIX in version_name and '.' not in version_name:
            if type(globals_dict[version_name]) != Version:
                globals_dict[version_name] = Version(*globals_dict[version_name])
            version = globals_dict[version_name]
            line = version.name + str(version)
            if len(line) > max_length:
                max_length = len(line)
    max_length += 1
    for version_name in globals_dict:
        if (GLOBAL_VERSION_PREFIX in version_name or 'VERSION_OF' in version_name) and '.' not in version_name:
            if type(globals_dict[version_name]) != Version:
                globals_dict[version_name] = Version(*globals_dict[version_name])
            version = globals_dict[version_name]
            line = version.name + str(version)
            line = version.name + str().join([' ' for i in range(max_length-len(line))]) + str(version)
            print(line+suffix)

def import_personnal_settings(path, globals_dict, locals_dict, app=None, **kwargs):
    import builtins, os
    horz = '—'
    vert = ''
    show = True
    show_if_empty = False
    frame = True
    prefix = 'Personnal settings found | '
    if 'horz' in kwargs:
        horz = kwargs['horz']
    if 'vert' in kwargs:
        vert = kwargs['vert']
    if 'show' in kwargs:
        show = kwargs['show']
    if 'frame' in kwargs:
        frame = kwargs['frame']
    if 'show_if_empty' in kwargs:
        show_if_empty = kwargs['show_if_empty']
    if 'prefix' in kwargs:
        prefix = kwargs['prefix']
    if os.path.exists(path):
        with builtins.open(path) as file:
            code = ''
            for i in file:
                code += i
        code = code.split('\n')
        while len(code) > 0 and code[len(code)-1] == '':
            del code[len(code)-1]
        if show and (show_if_empty or code not in ([], [''])):
            print('')
            if frame:
                line = str().join([horz for i in range(len(prefix)+len(repr(path)))])
                max_length = len(line)
                for i in code:
                    if len(i) > max_length:
                        max_length = len(i)
                line = str().join([horz for i in range(max_length)])
                print(vert+line.replace('-', '—')+vert)
                print(vert+prefix+path+str().join([' ' for i in range(len(line)-len(prefix+path))])+vert)
                print(vert+line+vert)
                for i in code:
                    print(vert+i+str().join([' ' for i in range(len(line)-len(i))])+vert)
                print(vert+line+vert)
                print('')
            else:
                print(code)
        if True:#try:
            exec(str().join([i+'\n' for i in code]), globals_dict, locals_dict)
        if False:#except:
            warn(str().join([i+'\n' for i in code]))
        if app is not None:
            app.personnal_settings.scripts += [str().join([i+'\n' for i in code])]


globals().update(new_version('2.3.0', __name__))
#please tabify)




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

from time import time, sleep
from random import randrange
import tkinter.messagebox as messagebox

try:
    from PIL import Image, ImageTk
except ImportError:
    warn('PIL n\'est pas installé, utiliser les images est impossible.')

globals().update(new_version('3.2.2', __name__))


def try_destroy_root(root):
    try:
        root.destroy()
    except:
        pass

class App():

    class AppDebugParameters():        
        def __init__(self):
            self.show_item_margins = False
            self.intersection_is_defined = False
            self.print_interaction = False
            self.show_exception_error = False
            self.show_version_in_title = True

    class AppPersonnalSettings():        
        def __init__(self):
            self.first_run = True
            self.scripts = list()
            self.global_dict = dict()
            
    def __init__(self, *args, **kwargs):
        self.root = None
        self.canv = None

        self.start_root = None
        self.maps_root = None
        self.players_root = None
        self.help_root = None
        self.bg_help = 0

        self.scheduled_player_profiles = None
        self.scheduled_map_profile = None
        
        self.map = Map(self)

        self.scale = DEFAULT_APP_SCALE
        self.use_images = True
        self.pressed_keys = SuperDict()
        self.player_bindings = SuperDict()
        self.player_motion_bindings = SuperDict()
        self.player_buttons_bindings = SuperDict()
        self.debug_parameters = App.AppDebugParameters()
        self.personnal_settings = App.AppPersonnalSettings()
            
    def bind_debug_to_tk(self, root):        
        root.bind(IDLE_MENU_SHORTCUT, self.show_idle)

    def show_idle(self, event=None):
        self.idle_root = Tk()
        self.idle_root.title(IDLE_MENU_TITLE)
        self.idle_root.resizable(width=True, height=True)
        self.idle_root.geometry(str('x').join((str(i) for i in ~IDLE_MENU_GEOMETRY)))
        self.idle_root.resizable(width=False, height=False)
        self.idle_root.focus_force()
        input_memo = Text(self.idle_root, width=IDLE_MENU_GEOMETRY.x, height=IDLE_MENU_MID_HEIGHT)
        input_memo.pack()
        input_memo.place(x=0, y=0)
        output_memo = Text(self.idle_root, width=IDLE_MENU_GEOMETRY.x, height=IDLE_MENU_GEOMETRY.y-IDLE_MENU_MID_HEIGHT)
        output_memo.pack()
        output_memo.place(x=0, y=IDLE_MENU_MID_HEIGHT)
        def command(event):
            text = input_memo.get('1.0','end-1c').split('\n')
            del text[len(text)-1]
            line = text[len(text)-1]
            d = {'self': self, 'value': None}
            exec('value = '+line, globals(), d)
            output_memo.insert(END, str(d['value'])+'\n')
        self.idle_root.bind('<Control-Return>', command)
        self.idle_root.mainloop()
        
    def show_start_root(self):
        try_destroy_root(self.maps_root)
        try_destroy_root(self.players_root)
        try_destroy_root(self.root)
        try_destroy_root(self.start_root)
        self.start_root = Tk()
        self.bind_debug_to_tk(self.start_root)
        self.start_root.title(MAP_WINDOW_TITLE)
        self.start_root.resizable(width=True, height=True)
        self.start_root.geometry(str('x').join((str(i) for i in ~START_MENU_GEOMETRY)))
        self.start_root.resizable(width=False, height=False)
        self.start_root.focus_force()
        background_photo = PhotoImage(file=START_MENU_BG_IMAGE_ADRESS)
        background_label = Label(self.start_root, image=background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        photo_new_game = PhotoImage(file=START_MENU_BUTTON_NEW_GAME_BT_IMAGE_ADRESS)
        bt_new_game = Button(self.start_root, text='Nouvelle partie', image=photo_new_game, command=self.show_maps_root, **START_MENU_BUTTON_STYLE)
        bt_new_game.pack()
        bt_new_game.place(x=50, y=40, width=photo_new_game.width(), height=photo_new_game.height())
        photo_help = PhotoImage(file=START_MENU_HELP_BT_IMAGE_ADRESS)
        bt_help = Button(self.start_root, text='Aide', image=photo_help, command=self.show_help_root, **START_MENU_BUTTON_STYLE)
        bt_help.pack()
        bt_help.place(x=50, y=120, width=photo_help.width(), height=photo_help.height())
        photo_debug_access = PhotoImage(file=START_MENU_DEBUG_ACCESS_IMAGE_BT_ADRESS)
        bt_debug_access = Button(self.start_root, text='Accès développeurs', image=photo_debug_access, command=self.show_idle, **START_MENU_BUTTON_STYLE)
        bt_debug_access.pack()
        bt_debug_access.place(x=50, y=200, width=photo_debug_access.width(), height=photo_debug_access.height())
        photo_quit = PhotoImage(file=START_MENU_QUIT_BT_IMAGE_ADRESS)
        bt_quit = Button(self.start_root, text='Quitter', image=photo_quit, command=self.destroy, **START_MENU_BUTTON_STYLE)
        bt_quit.pack()
        bt_quit.place(x=50, y=280, width=photo_quit.width(), height=photo_quit.height())
        self.start_root.mainloop()

    def show_help_root(self):
        self.help_root = Tk()
        self.help_root.title('Aide')
        background_photo = PhotoImage(file='tanksdata|images|menus|help.png'.replace('|', SEP), master=self.help_root)
        background_label = Label(self.help_root, image=background_photo)
        #background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.place(x=0, y=0, width=background_photo.width(), height=background_photo.height())
        self.help_root.resizable(width=True, height=True)
        #self.help_root.geometry('531x681')
        self.help_root.geometry(str('x').join((str(i) for i in (background_photo.width(), background_photo.height()))))
        self.help_root.resizable(width=False, height=False)
        t1 = Text(self.help_root, font=('Courier New', 8))
        t1.pack()#in_=background_label)
        t1.place(x=0, y=610, width=background_photo.width(), height=28)
        t1.configure(state='normal')
        t1.insert(END, 'https://drive.google.com/drive/folders/1fiWfqbjBVbGYS3j43lD7zgHCtyN1mTtf?usp=sharing')
        t1.configure(state='disabled')
        t2 = Text(self.help_root, font=('Courier New', 8))
        t2.pack()#in_=background_label)
        t2.place(x=0, y=660, width=background_photo.width(), height=28)
        t2.configure(state='normal')
        t2.insert(END, 'https://drive.google.com/drive/folders/1Li-PCjku8PCFo0Gv4d8NHGoGf6S1SVVV?usp=sharing')
        t2.configure(state='disabled')
        t3 = Text(self.help_root, font=('Courier New', 8))
        t3.pack()#in_=background_label)
        t3.place(x=0, y=705, width=background_photo.width(), height=28)
        t3.configure(state='normal')
        t3.insert(END, 'https://drive.google.com/drive/folders/1neUfHjAZUD6DA9TzbDhwKxiasKBxiO0u?usp=sharing')
        t3.configure(state='disabled')
        self.help_root.mainloop()

    def show_maps_root(self):
        try_destroy_root(self.maps_root)
        self.maps_root = Tk()
        self.bind_debug_to_tk(self.maps_root)
        self.maps_root.title(MAPS_MENU_TITLE)
        self.maps_root.resizable(width=True, height=True)
        self.maps_root.geometry(str('x').join((str(i) for i in ~MAPS_MENU_GEOMETRY)))
        self.maps_root.resizable(width=False, height=False)
        self.maps_root.focus_force()
        def command1():
            self.show_start_root()                  
        def command2():
            if len(listbox.curselection()) > 0:
                path = 'tanksdata|maps|'.replace('|', SEP)+files[listbox.curselection()[0]]
                code = ''
                with open(path, 'r') as f:
                    for i in f:
                        code += i
                exec(code, globals(), locals())
                if 'data' in locals():
                    self.scheduled_map_profile = MapProfile(locals()['data'])
                    try_destroy_root(self.maps_root)
                    self.show_players_root()
                    #self.run_map(MapProfile(locals()['data']))
                else:
                    messagebox.showwarning(MESSAGE_BOX_TITLE, 'Cette carte n\'est pas reconnue')
        bt_back = Button(self.maps_root, text='Retour', command=command1)
        #bt_back.pack(side=TOP, fill=X)
        listbox = Listbox(self.maps_root)
        listbox.pack(fill=BOTH, expand=True)
        files = os.listdir('tanksdata|maps'.replace('|', SEP))
        for file in files:
            listbox.insert(END, file.replace('.py', ''))   
        bt_run = Button(self.maps_root, text='Suivant', command=command2)
        bt_run.pack(side=BOTTOM, fill=X)
        self.maps_root.mainloop()
        try_destroy_root(self.maps_root)
        self.maps_root = None  
        self.start_root.mainloop()

    def show_players_root(self):
        try_destroy_root(self.players_root)
        self.players_root = Tk()
        self.bind_debug_to_tk(self.players_root)
        self.players_root.title(PLAYERS_MENU_TITLE)
        self.players_root.resizable(width=True, height=True)
        self.players_root.geometry(str('x').join((str(i) for i in ~PLAYERS_MENU_GEOMETRY)))
        self.players_root.resizable(width=False, height=False)
        self.players_root.focus_force()
        
        def command1():
            self.show_start_root()
            try_destroy_root(self.maps_root)
            try_destroy_root(self.players_root)
        def command2():
            links.update({len(self.scheduled_player_profiles):-1})
            player = PlayerProfile()
            self.scheduled_player_profiles += [player]
            listbox1.insert(END, 'Joueur '+str(len(self.scheduled_player_profiles)))
        def command3():
            try_destroy_root(self.players_root)
            self.run_map(self.scheduled_map_profile)
        def select1(event):
            if len(listbox1.curselection()) > 0 and len(listbox2.curselection()) > 0:
                index1 = listbox1.curselection()[0]
                index2 = listbox2.curselection()[0]
                listbox2.selection_set(links[index1])
        def select2(event):
            if len(listbox1.curselection()) > 0 and len(listbox2.curselection()) > 0:
                index1 = listbox1.curselection()[0]
                index2 = listbox2.curselection()[0]
                interface = PlayerProfile()
                if index2 > 0:
                    code = ''
                    with open('tanksdata|profiles|'.replace('|', SEP)+files[index2]) as f:
                        for i in f:
                            code += i
                    d = {}
                    exec(code, globals(), d)
                    if 'is_valid' in d and 'data' in d:
                        if d['is_valid']()[0]:
                            interface = PlayerProfile(d['data'])
                        else:
                            messagebox.showwarning(MESSAGE_BOX_TITLE, d['is_valid']()[1]) 
                    else:
                        messagebox.showwarning(MESSAGE_BOX_TITLE, 'Cette interface n\'est pas valide.')  
                links[index1] = index2
                self.scheduled_player_profiles[index1] = interface
        links = dict()
        self.scheduled_player_profiles = list()
        bt_back = Button(self.players_root, text='Retour', command=command1)
        #bt_back.pack(side=TOP, fill=X)
        #bt_back.place(x=0, y=0, height=40, width=400)
        listbox1 = Listbox(self.players_root, exportselection=0)
        listbox1.pack()
        listbox1.place(x=0, y=0, height=240, width=200)
        listbox1.bind('<<ListboxSelect>>', select1)
        listbox2 = Listbox(self.players_root, exportselection=0)
        listbox2.pack()
        listbox2.place(x=200, y=0, height=240, width=240) 
        listbox2.bind('<<ListboxSelect>>', select2)
        listbox2.insert(END, DEFAULT_PLAYER_INTERFACE_PROFILE.title)
        files = os.listdir('tanksdata|profiles'.replace('|', SEP))
        for file in files:
            listbox2.insert(END, file.replace('.py', ''))
        files = [''] + files
        bt_add = Button(self.players_root, text='Ajouter un joueur', command=lambda:command2())
        bt_add.pack()
        bt_add.place(x=0, y=240, height=40, width=200)
        bt_run = Button(self.players_root, text='Lancer', command=command3)
        bt_run.pack()
        bt_run.place(x=200, y=240, height=40, width=200)
        command2()
        
        self.players_root.mainloop()
        try_destroy_root(self.players_root)
        self.players_root = None    


    def run(self):
        self.show_start_root()

    def run_map(self, profile=None):
        try_destroy_root(self.start_root)
        try_destroy_root(self.maps_root)
        try_destroy_root(self.players_root)
        try_destroy_root(self.root)
        self.root = Tk()
        self.bind_debug_to_tk(self.root)
        self.root.title(DEFAULT_WINDOW_TITLE)
        self.root.geometry('800x400')
        try:
            if self.debug_parameters.show_version_in_title:
                self.root.title(DEFAULT_WINDOW_TITLE+' '+str(VERSION_OF_tanksmodules_tanksmain))
        except:
            pass
        self.root.bind('<KeyPress>', self.keypress)
        self.root.bind('<KeyRelease>', self.keyrelease)
        self.root.bind('<Motion>', self.motion)
        self.root.bind('<Button>', self.buttons)
        
        self.pressed_keys = SuperDict()
        self.player_bindings = SuperDict()
        self.player_motion_bindings = SuperDict()
        self.player_buttons_bindings = SuperDict()
            
        try:
            self.canv.destroy()
        except:
            pass
        self.canv = Canvas(self.root, bg='white')
        self.canv.pack(fill=BOTH, expand=True)
        
        self.map = Map(self)
        if profile:
            self.map.profile = profile
        self.map.load()
        self.map.activate()
        self.map.draw()

        def command1(self):
            self.map.pause()
            if messagebox.askyesno(MESSAGE_BOX_TITLE, 'Quitter la partie ?'):
                try:
                    self.map.unpause()
                except:
                    pass
                try_destroy_root(self.destroy())
                self.show_start_root()
            self.map.unpause()
        self.menu_bar = Menu(self.root)  
        self.menu_bar.add_checkbutton(label='Accueil', command=lambda:command1(self))
        self.menu_bar.add_checkbutton(label='Pause', command=self.map.reverse_pause)
        self.root.config(menu=self.menu_bar)
        self.root.mainloop()
        
    def keypress(self, event):
        if self.debug_parameters.print_interaction:
            print(event.__dict__)
        if self.pressed_keys.set(event.keysym, True):
            for player in self.player_bindings[event.keysym]:
                player.press_key(event.keysym)
            
    def keyrelease(self, event):
        if self.pressed_keys.set(event.keysym, False):
            for player in self.player_bindings[event.keysym]:
                player.release_key(event.keysym)
            
    def motion(self, event):
        for player in self.player_motion_bindings:
            getattr(player, self.player_motion_bindings[player])(event)
            
    def buttons(self, event):
        for num in self.player_buttons_bindings:
            getattr(self.player_buttons_bindings[num][0], self.player_buttons_bindings[num][1])(*self.player_buttons_bindings[num][2])

    def run_again(self):
        scripts = self.personnal_settings.scripts
        global_dict = self.personnal_settings.global_dict
        profile = self.map.profile
        self.run_map(profile)
        for script in scripts:
            exec(script, global_dict, locals())

    def destroy(self):
        for obj in self.map.objects:
            obj.active = False
        self.map = Map(self)
        sleep(0.666)
        try:
            self.root.destroy()
        except:
            if self.debug_parameters.show_exception_error:
                warn('root already destroyed')
        try:
            self.start_root
        except:
            if self.debug_parameters.show_exception_error:
                warn('root already destroyed')
        try:
            self.maps_root
        except:
            if self.debug_parameters.show_exception_error:
                warn('root already destroyed')



class EmptyPlayerInterfaceProfile():
    def __init__(self):
        self.minimum_version = Version(0)
        self.title = 'Empty'
        self.bind = ()



class Map():

    def __init__(self, app):
        self.app = app
        self.profile = MapProfile()
        #listes des objects actifs
        self.objects = list()
        self.tanks = list()
        self.players = list()
        self.bots = list()
        self.projectiles = list()
        self.items = list()
        self.movable_items = list()
        self.static_items = list()
        #listes des objects actifs
        self.active_objects = list()
        self.active_tanks = list()
        self.active_players = list()
        self.active_bots = list()
        self.active_projectiles = list()
        self.active_items = list()
        self.active_movable_items = list()
        self.active_static_items = list()
        #
        self.pillow_background_image = None
        self.tk_background_image = None
        self.tag_background_image = None
        #
        self.after_functions = SuperDict()
        self.paused = False
        if self.app.root:
            self.prepare_after = self.app.root.after
        self.stoped_functions = []


    def load(self):
        if self.app.use_images:
            import PIL
            if False:
                global img1, img2
                img1 = PIL.Image.open(self.profile.background_image_adress)
                img1.putdata(opacify(img1.getdata(), (255, 0, 128, 255), 0))
                img1 = img1.resize(~self.profile.grid_size)
                img2 = ImageTk.PhotoImage(img1)
                self.tag_background_image = self.app.canv.create_image(self.profile.grid_size.x*self.app.scale/2, self.profile.grid_size.y*self.app.scale/2, image=img2)
            if True:
                self.pillow_background_image = PIL.Image.open(self.profile.background_image_adress)
                self.pillow_background_image = self.pillow_background_image.resize((i*self.app.scale for i in ~self.profile.grid_size))
                self.tk_background_image = ImageTk.PhotoImage(self.pillow_background_image, master=self.app.root)
                self.tag_background_image = self.app.canv.create_image(
                    self.profile.grid_size.x*self.app.scale/2,
                    self.profile.grid_size.y*self.app.scale/2,
                    image=self.tk_background_image)
            if False:
                import PIL
                self.pillow_image = PIL.Image.open(self.profile.graphics.image_adress)
                self.pillow_image.putdata(opacify(self.pillow_image.getdata(), (255, 0, 128, 255), 0))
                self.tk_pillow_image = ImageTk.PhotoImage(self.pillow_image)
                self.tag = self.app.canv.create_image(*~self.pos, image=self.tk_image)
            
        else:
            self.app.canv.config(bg=self.profile.background_image_adress)
        #Création des 4 murs sur les bords
        scale = self.app.scale
        height = self.profile.grid_size.y
        width = self.profile.grid_size.x
        self.app.root.resizable(width=True, height=True)
        self.app.root.geometry(str(width*scale)+'x'+str(height*scale))
        self.app.root.resizable(width=False, height=False)
        self.app.canv.config(height=height, width=width)
        wall1 = Wall(self.app, Corners(0, 0, width*scale, 1*scale))
        wall2 = Wall(self.app, Corners(0, 1*scale, 1*scale, (height-1)*scale))
        wall3 = Wall(self.app, Corners((width-1)*scale, 1*scale, width*scale, (height-1)*scale))
        wall4 = Wall(self.app, Corners(0, (height-1)*scale,(width*scale), (height*scale)))
        for i in range(min(len(self.profile.player_list), len(self.app.scheduled_player_profiles))):
            new_player = Player(self.app)
            #print(dir(self.app))
            #print(type(self.app.scheduled_players[i]))
            new_player.spawn_order = i
            old_spawn = self.profile.player_list[i][0]
            new_player.spawn = Point(old_spawn.x*self.app.scale, old_spawn.y*self.app.scale)
            new_player.pos = new_player.spawn
            new_player.profile = new(PlayerProfile)
            new_player.unload_interface()
            new_player.profile = new(EmptyPlayerInterfaceProfile)
            new_player.profile = self.app.scheduled_player_profiles[i]
            new_player.load_interface()
            #new_player.profile.interface.title = 'Toto'
            #self.schedueld_players[i].profile = self.profile.player_list[i][1]
        for i in range(len(self.profile.bot_list)):
            newbot = Bot(self.app)
            newbot.spawn_order = i
            old_spawn = self.profile.bot_list[i][0]
            newbot.spawn = Point(old_spawn.x*self.app.scale, old_spawn.y*self.app.scale)
            newbot.pos = newbot.spawn
            newbot.profile = self.profile.bot_list[i][1]
        for corners_info in self.profile.wall_list:
            newwall = Wall(self.app, Corners(*(i*scale for i in ~corners_info)))

    def activate(self):
        for obj in self.objects:
            if 'activate' in dir(obj):
                obj.activate()              
                
    def draw(self):
        #dessinage de tous les objets 
        for obj in self.objects:
            if 'draw' in dir(obj):
                obj.draw()

    def prepare_after(self, interval, func, params=()):
        length = len(self.after_functions)
        self.app.root.after(interval, self.do_after, length, func, params)
        self.after_functions += {length: [TK_PLANNED_FUNCTION, func, ()]}

    def do_after(self, tag, func, params):
        self.after_functions[tag][0] = TK_ONGOING_FUNCTION,
        func(*params)
        self.after_functions[tag][0] = TK_OVER_FUNCTION,

    def old_pause(self):
        self.paused = not self.paused
        if self.paused:
            for i in range(len(self.after_functions)):
                if self.after_functions[i][0] in (TK_PLANNED_FUNCTION, TK_ONGOING_FUNCTION,):
                    self.app.root.after_cancel('after#'+str(i))
                    self.after_functions[i][0] = TD_STOPED_FUNCTION,
        else:
            for i in self.after_functions:
                if self.after_functions[i][0] == TK_STOPED_FUNCTION:
                    self.do_after(i, self.after_functions[i][1], self.after_functions[i][2])

    def reverse_pause(self):
        if self.paused:
            self.unpause()
        else:
            self.pause()

    def pause(self):
        if not self.paused:
            self.paused = True
            self.stoped_functions = []
            for obj in self.active_objects:
                for func in obj.loop_functions:
                    self.stoped_functions += [(obj,  func)]
                obj.active = False

    def unpause(self):
        if self.paused:
            self.paused = False
            for obj in self.active_objects:
                obj.active = True
            for obj, func in self.stoped_functions:
                obj.active = True
                func()
            self.paused = False

    def check_endgame(self):
        s = ''
        if len(self.app.map.active_bots) == 0:
            s = 'Victoire'
        if len(self.app.map.active_players) == 0:
            s = 'Défaite'
        if s != '':
            for obj in self.objects:
                obj.active = False  
            if 'yes' == messagebox.askquestion(title=MESSAGE_BOX_TITLE, message='Partie terminée : ' + s + '\nRejouer ?'):
                self.app.run_again()
            else:
                self.app.destroy()



class MapObject():
    
    def __init__(self, app):
        self.app = app
        self.active = False
        self.history = []
        self.extern_points = []
        self.extern_radius = 1
        self.pos = Point(0, 0)
        self.app.map.objects += [self]
        self.loop_functions = {}

    def interact_with(self, other):
        if self.app.debug_parameters.print_interaction:
            print('('+repr(self)+')', 'interacting with', '('+repr(other)+')')
        pass

    def in_radius_of(self, other):
        for p in self.extern_points:
            if p.in_circle(other.pos.x, other.pos.y, r):
                return True
        return False

    def intersect_with(self, other):
        return True

    def true_intersect_with(self, obj, angle):
        if issubclass(type(self), (Tank, Projectile)):
            m_inf = Point(
                (self.extern_points[1].x+self.extern_points[2].x)/2,
                (self.extern_points[1].y+self.extern_points[2].y)/2,
                )
            rot_m_inf = Point(self.pos.x, self.pos.y-self.profile.graphics.height/2)
            alpha = point_to_degree_angle(m_inf.x-obj.pos.x, m_inf.y-obj.pos.y)
            length = sqrt((obj.pos.x-m_inf.x)**2+(obj.pos.y-m_inf.y)**2)
            rot_pos = Point(rot_m_inf.x + length*cos(alpha),rot_m_inf.y + length*sin(alpha))
            result = rot_pos in Corners(
                self.pos.x-self.profile.graphics.width/2,
                self.pos.y-self.profile.graphics.height/2,
                self.pos.x+self.profile.graphics.width/2,
                self.pos.y+self.profile.graphics.height/2,
                )
            print(result)
            return result
            

    def activate(self):        
        self.active = True
        self.app.map.active_objects += [self]



class MapItem(MapObject):

    def __init__(self, app):
        super(__class__, self).__init__(app) #Va chercher sa classe parente
        self.corners = None # on aurait aussi pu faire Corners(0, 0, 0, 0)
        self.app.map.items += [self]

    def activate(self):
        super(__class__, self).activate()
        self.app.map.active_items += [self]



class Wall(MapItem):

    def __init__(self, app, corners):
        super(__class__, self).__init__(app) #Va chercher sa classe parente 
        self.profile = WallProfile()
        self.corners = corners
        self.map = self.app.map
        self.canvas_tag = None
        self.pillow_image = None
        self.app.map.static_items += [self]
        self.pos = Point((corners.left+corners.right)/2, (corners.top+corners.bottom)/2)

    def __repr__(self):
        return 'Wall: ' + repr(~self.corners)

    def activate(self):
        super(__class__, self).activate()
        self.app.map.active_static_items += [self]
        if self.app.use_images:
            self.draw = self.draw_image
        else:
            self.draw = self.draw_poly

    def actualize_extern_points(self):
        self.extern_points = [
            Point(self.left, self.top),
            Point(self.left, self.bottom),
            Point(self.right, self.bottom),
            Point(self.right, self.top),
            ]
        self.extern_radius = sqrt(self.left**2+self.top**2)

    def draw(self):
        pass

    def draw_poly(self):
        if self.active:
            self.canvas_tag = self.app.canv.create_rectangle(self.corners.left, self.corners.top, self.corners.right, self.corners.bottom, fill=self.profile.graphics.color)

    def draw_image(self):
        if self.active:
            import PIL
            self.canvas_tag = []
            image = PIL.Image.open(self.profile.graphics.image_adress)
            image.putdata(opacify(image.getdata(), (255, 0, 128, 255), 0))
            self.pillow_image = ImageTk.PhotoImage(image, master=self.app.root)
            for x in range(round(self.corners.left/self.app.scale), round(self.corners.right/self.app.scale)):
                for y in range(round(self.corners.top/self.app.scale), round(self.corners.bottom/self.app.scale)):
                    params = (x*self.app.scale+self.app.scale/2, y*self.app.scale+self.app.scale/2)
                    self.app.canv.create_rectangle(params[0]-2, params[1]-2, params[0]+2, params[1]+2, fill='green')
                    new_tag = self.app.canv.create_image(*params, image=self.pillow_image )
                    self.canvas_tag += [new_tag]
    

    def interact_with(self, obj):
        super(__class__, self).interact_with(obj)
        if issubclass(type(obj), Projectile):
            if not self.profile.solid_for_projectiles:
                pass
            elif obj.remaining_rebounds > 0:
                if obj.profile.destruction_power >= self.profile.resistance:
                    self.desactivate()
                    obj.desactivate(self)
                else:   
                    #Sortir un nouveau vecteur              
                    if self.corners.left <= obj.pos.x <= self.corners.right:
                        obj.vect.y *= -1
                    elif self.corners.top <= obj.pos.y <= self.corners.bottom:
                        obj.vect.x *= -1
                    obj.remaining_rebounds += -1
                    obj.start()
                    do_next_loop = False
            else:
                if obj.profile.destruction_power >= self.profile.resistance:
                    self.desactivate()
                    do_next_loop = False
                obj.desactivate(self)
                
    def desactivate(self):
        if self.active:
            self.active = False
            for i in self.app.map.active_objects:
                if self == i:
                    del self.app.map.active_objects[self.app.map.active_objects.index(i)]
            for i in self.app.map.active_static_items:
                if self == i:
                    del self.app.map.active_static_items[self.app.map.active_static_items.index(i)]
            self.app.canv.delete(self.canvas_tag)   
            self.canvas_tag = None



class Tank(MapObject):

    def __init__(self, app):
        super(__class__, self).__init__(app) #Va chercher sa classe parente
        self.profile = TankProfile()
        self.pos = None
        self.spawn = None
        self.base_tag = None
        self.canon_tag = None
        self.move_vect = None
        self.move_angle = None
        self.app.map.tanks += [self]
        self.base_rotation = DEFAULT_TANK_BASE_ROTATION
        self.canon_rotation = DEFAULT_TANK_CANON_ROTATION
        self.move_interval = DEFAULT_TANK_MOVE_INTERVAL
        self.remaining_ammo = self.profile.ammo_max
        self.tk_base_image = None
        self.tk_canon_image = None
        self.pillow_base_image = None
        self.pillow_canon_image = None
        self.old_base_rotation = 0

    def activate(self):
        super(__class__, self).activate()
        self.active = True
        self.extern_points = [
            Point(self.pos.x-self.profile.graphics.width/2, self.pos.y-self.profile.graphics.height/2),
            Point(self.pos.x-self.profile.graphics.width/2, self.pos.y+self.profile.graphics.height/2),
            Point(self.pos.x+self.profile.graphics.width/2, self.pos.y+self.profile.graphics.height/2),
            Point(self.pos.x+self.profile.graphics.width/2, self.pos.y-self.profile.graphics.height/2),
            ]
        if self.app.use_images:
            import PIL
            self.pillow_base_image = PIL.Image.open(self.profile.graphics.base_image_adress)
            self.pillow_base_image.putdata(opacify(self.pillow_base_image.getdata(), (255, 0, 128, 255), 0))
            self.tk_pillow_image = ImageTk.PhotoImage(self.pillow_base_image, master=self.app.root)
            self.base_tag = self.app.canv.create_image(*~self.pos, image=self.tk_base_image)            
            self.pillow_canon_image = PIL.Image.open(self.profile.graphics.canon_image_adress)
            self.pillow_canon_image.putdata(opacify(self.pillow_canon_image.getdata(), (255, 0, 128, 255), 0))
            self.tk_canon_image = ImageTk.PhotoImage(self.pillow_canon_image, master=self.app.root)
            self.canon_tag = self.app.canv.create_image(*~self.pos, image=self.tk_canon_image)   
        else:
            self.base_tag = self.app.canv.create_polygon(0,0, 0,0, 0,0, 0,0, fill=self.profile.graphics.base_color)
            self.canon_tag = self.app.canv.create_polygon(0,0, 0,0, 0,0, 0,0, fill=self.profile.graphics.canon_color)
        self.app.map.active_tanks += [self]

    def actualize_graphics(self, base_params={}, canon_params={}):
        if self.app.use_images:
            pass
        else:
            self.app.canv.itemconfigure(self.base_tag, fill=self.profile.graphics.base_color)
            self.app.canv.itemconfigure(self.canon_tag, fill=self.profile.graphics.canon_color)
        if base_params != {}:
            self.app.canv.itemconfigure(self.base_tag, **base_params)
        if canon_params != {}:
            self.app.canv.itemconfigure(self.canon_tag, **canon_params)

    def actualize_extern_points(self):
        h = self.profile.graphics.height
        w = self.profile.graphics.width
        d_1 = sqrt(h/2*h/2+w/2*w/2)
        B_1 = 180 - degrees(acos((w/2)/d_1))
        B_2 = 180 + degrees(acos((w/2)/d_1))
        B_3 = 360 - degrees(acos((w/2)/d_1))
        B_4 = degrees(acos((w/2)/d_1))
        x = self.pos.x
        y = self.pos.y
        angle = self.base_rotation
        self.extern_points = [
            Point(x+d_1*cos(radians(angle+B_1)), +(y+d_1*sin(radians(angle+B_1)))),
            Point(x+d_1*cos(radians(angle+B_2)), +(y+d_1*sin(radians(angle+B_2)))),
            Point(x+d_1*cos(radians(angle+B_3)), +(y+d_1*sin(radians(angle+B_3)))),
            Point(x+d_1*cos(radians(angle+B_4)), +(y+d_1*sin(radians(angle+B_4)))),
            ]
        self.extern_radius = d_1
        
    def draw(self):
        if self.active:
            self.rotate_base_at(self.base_rotation)
            self.rotate_canon_at(self.canon_rotation)

    def move_to(self, x, y):
        if self.active:
            old_pos = Point(*~self.pos)
            self.pos = Point(x, y)
            self.actualize_extern_points()
            do_move = True
            contact_point_index = -1
            contact_obj = None
            for obj in self.app.map.active_objects:
                if issubclass(type(obj), MapItem):
                    for i in range(len(self.extern_points)): 
                        if self.extern_points[i] in obj.corners:
                            contact_point_index = i
                            contact_obj = obj
                            do_move = False
                            break
                elif self != obj and not issubclass(type(obj), Projectile):
                    for i in range(len(self.extern_points)):                    
                        if self.extern_points[i].in_circle(obj.pos.x, obj.pos.y, obj.extern_radius):
                            contact_point_index = i
                            contact_obj = obj
                            do_move = False
                            break
                    if self.intersect_with(obj) and self.app.debug_parameters.intersection_is_defined:
                        do_move = False
                        break
            if not do_move:
                self.pos = Point(*~old_pos)
                self.actualize_extern_points()
                if contact_point_index > -1:
                    old_contact_point = Point(*~self.extern_points[contact_point_index])
                    new_contact_point = Point(*~self.extern_points[contact_point_index])
                    if issubclass(type(obj), MapItem):
                        i = 0
                        d = -3
                        small_corners = Corners(contact_obj.corners.left+d, contact_obj.corners.top+d, contact_obj.corners.right-d, contact_obj.corners.bottom-d)
                        while new_contact_point not in small_corners and i < 100:
                            new_contact_point.x += self.move_vect.x/10
                            new_contact_point.y += self.move_vect.y/10
                            i += 1
                        if self.app.debug_parameters.show_item_margins:
                            self.app.canv.create_line(small_corners.left, small_corners.top, small_corners.left, small_corners.bottom, fill='green')
                            self.app.canv.create_line(small_corners.left, small_corners.bottom, small_corners.right, small_corners.bottom, fill='green')
                            self.app.canv.create_line(small_corners.right, small_corners.bottom, small_corners.right, small_corners.top, fill='green')
                            self.app.canv.create_line(small_corners.right, small_corners.top, small_corners.left, small_corners.top, fill='green')
                        if self.app.debug_parameters.show_item_margins:
                            self.app.canv.create_polygon(new_contact_point.x-d, new_contact_point.y-d, new_contact_point.x-d, new_contact_point.y+d, new_contact_point.x+d, new_contact_point.y+d, new_contact_point.x+d, new_contact_point.y-d,fill='yellow')
                            self.app.canv.create_polygon(old_contact_point.x-d, old_contact_point.y-d, old_contact_point.x-d, old_contact_point.y+d, old_contact_point.x+d, old_contact_point.y+d, old_contact_point.x+d, old_contact_point.y-d, fill='blue')
                        if ~old_contact_point != ~new_contact_point:
                            self.pos = Point(self.pos.x+new_contact_point.x-old_contact_point.x, self.pos.y+new_contact_point.y-old_contact_point.y)
                            self.actualize_extern_points()
                            self.draw()
            else:
                self.draw()

    def move_at(self, angle):
        self.move_vect = Vect(cos(radians(angle)), sin(radians(angle)))
        do_move = True
        #A RETIRER ??????????????????????????????????????????????????????????
        if False:
            for t in self.app.map.active_tanks:
                if t != self:
                    tx = t.pos.x
                    ty = t.pos.y
                    distance = self.profile.physics.max_speed*self.move_interval / 1000
                    new_x = self.pos.x+distance*cos(radians(angle))
                    new_y = self.pos.y+distance*sin(radians(angle))   
                    rayon_t = sqrt((t.profile.graphics.width/2)**2 +(t.profile.graphics.height/2)**2)
                    if sqrt((tx-new_x)**2+(ty-new_y)**2) <= rayon_t*3/2:
                        do_move = False
                        break
        if do_move:
            angle = (angle) % 360
            distance = self.profile.physics.max_speed*self.move_interval / 1000
            self.move_to(self.pos.x+distance*cos(radians(angle)),self.pos.y+distance*sin(radians(angle)))
            self.old_base_rotation = self.base_rotation
            self.base_rotation = angle

    def move_by(self, x, y):
        self.move_at(point_to_degree_angle(x, y))

    def rotate_base_at(self, angle):
        if True:#self.base_rotation != angle:
            if self.app.use_images:
                import PIL
                self.pillow_base_image = PIL.Image.open(self.profile.graphics.base_image_adress)
                self.pillow_base_image.putdata(opacify(self.pillow_base_image.getdata(), (255, 0, 128, 255), 0))
                self.pillow_base_image = self.pillow_base_image.rotate(270-angle, expand=True)
                self.tk_base_image = ImageTk.PhotoImage(self.pillow_base_image, master=self.app.root)
                self.app.canv.itemconfigure(self.base_tag, image=self.tk_base_image)
                self.app.canv.coords(self.base_tag, *~self.pos)
            else:
                params = []
                for p in self.extern_points:
                    params += [p.x, p.y]
                self.app.canv.coords(self.base_tag, *params)
        self.base_rotation = angle

    def rotate_canon_at(self, angle):
        if self.app.use_images:
            import PIL
            self.pillow_canon_image = PIL.Image.open(self.profile.graphics.canon_image_adress)
            self.pillow_canon_image.putdata(opacify(self.pillow_canon_image.getdata(), (255, 0, 128, 255), 0))
            self.pillow_canon_image = self.pillow_canon_image.rotate(angle+270, expand=True)
            self.tk_canon_image = ImageTk.PhotoImage(self.pillow_canon_image, master=self.app.root)
            self.app.canv.itemconfigure(self.canon_tag, image=self.tk_canon_image)
            self.app.canv.coords(self.canon_tag, *~self.pos)
        else:
            h = self.profile.graphics.height
            w = self.profile.graphics.width
            k1 = TANK_CANON_WIDTH_RATIO
            k2 = TANK_CANON_HEIGHT_RATIO
            k3 = TANK_CANON_BACK_RATIO
            h2 = h*k2
            w2 = w*k1
            o = w2*k3 
            d_1 = sqrt((h2/2)*(h2/2)+(w2-o)*(w2-o))
            d_2 = sqrt ((h2/2)*(h2/2)+(o*o))
            B_1 = 180 - degrees(acos(o/d_2))
            B_2 = 180 + degrees(acos(o/d_2))
            B_3 = 360 - degrees(acos((w2-o)/d_1))
            B_4 = degrees(acos((w2-o)/d_1))
            x = self.pos.x		
            y = self.pos.y
            params = (
                x+d_2*cos(radians(-angle+B_1)), y+d_2*sin(radians(-angle+B_1)),
                x+d_2*cos(radians(-angle+B_2)), y+d_2*sin(radians(-angle+B_2)),
                x+d_1*cos(radians(-angle+B_3)), y+d_1*sin(radians(-angle+B_3)),
                x+d_1*cos(radians(-angle+B_4)), y+d_1*sin(radians(-angle+B_4)),
                )
            self.app.canv.coords(self.canon_tag, *params)

    def rotate_canon_to(self, x, y):
        if not (x == 0 and y == 0):
            angle = point_to_degree_angle(x, y)   
            self.canon_rotation = angle
            self.draw()
        
    def rotate_canon_from_event(self, event): #la classe Event de tkinter a des attributs x et y comme Point, on peut donc utiliser les deux types comme paramètres
        x = event.x - self.pos.x
        y = self.pos.y - event.y #inversion axe x/y par rapport au cercle trionométrique
        self.rotate_canon_to(x, y)
    
    
    def shoot(self):
        if self.active and self.remaining_ammo > 0:
            self.remaining_ammo += -1
            newprojectile = Projectile(self.app)
            newprojectile.profile = self.profile.projectiles
            newprojectile.shooter = self
            newprojectile.done_loops = 0
            newprojectile.vect = Vect(100*cos(radians(self.canon_rotation)), -100*sin(radians(self.canon_rotation)))
            new_x = self.pos.x + self.profile.graphics.width * TANK_CANON_WIDTH_RATIO * cos(radians(self.canon_rotation))
            new_y = self.pos.y - self.profile.graphics.width * TANK_CANON_WIDTH_RATIO * sin(radians(self.canon_rotation))          
            newprojectile.pos = Point(new_x, new_y)
            newprojectile.activate()
            newprojectile.start()

    def interact_with(self, obj):
        super(__class__, self).interact_with(obj)
        if issubclass(type(obj), Projectile):
            obj.interact_with(self)


    def desactivate(self):
        if self.active:
            self.active = False
            for i in self.app.map.active_tanks:
                if self == i:
                    del self.app.map.active_tanks[self.app.map.active_tanks.index(i)]
            for i in self.app.map.active_objects:
                if self == i:
                        del self.app.map.active_objects[self.app.map.active_objects.index(i)]
            self.app.canv.delete(self.base_tag)
            self.app.canv.delete(self.canon_tag)
            self.base_tag = None
            self.canon_tag = None



class Player(Tank):

    def __init__(self, app):
        super(__class__, self).__init__(app)
        self.profile = PlayerProfile()
        self.move_interval = DEFAULT_PLAYER_MOVE_BY_INTERVAL#A changer dans tanksconsts
        self.app.map.players += [self]
        self.function_keybindings = SuperDict()
        self.move_pressed_keys = SuperDict()
        self.move_keybindings = SuperDict()
        self.has_keys_pressed = False
        self.chrono = 0

    def __repr__(self):
        return 'Player at : ' + str(~self.pos)

    def activate(self):
        super(__class__, self).activate()
        self.app.map.active_players += [self]
        self.load_interface()
        if PLAYER_INTERFACE_EXTERN_BIND in self.profile.interface.bind:
            self.extern_loop()

    def check_interface_specs(self, interface):
        result = True
        module_version = globals()[GLOBAL_VERSION_PREFIX+__name__]
        try:
            if -Version(interface.minimum_version) > -Version(module_version):
                return (False, 'try: version not supported: '+str(~Version(interface.minimum_version))+'>'+str(~Version(module_version)))
        except:
            return (False, 'except: version not supported: '+str(~Version(interface.minimum_version))+'>'+str(~Version(module_version)))
        if type(interface.title) != str:
            return (False, 'title is not str')
        if interface.bind not in PLAYER_INTERFACE_HANDLED_BINDS:
            return (False, 'non handled bind')
        for method in interface.direct_bind:
            if method not in PLAYER_INTERFACE_HANDLED_METHODS:
                return (False, 'non handled method')
        return (True, 'success')


        
    def load_interface(self):
        if False:# self.check_interface_specs(self.profile.interface)[0]:
            self.profile.interface = PlayerInterfaceProfile()
            warn('interface is not compatible: ' + self.check_interface_specs(self.profile.interface)[1])
        if PLAYER_INTERFACE_DIRECT_BIND in self.profile.interface.bind:
            if PLAYER_INTERFACE_KEYS_METHOD in self.profile.interface.direct_methods:
                for item in getattr(self.profile.interface, PLAYER_INTERFACE_KEYS_METHOD):
                    self.app.pressed_keys += {item[0]: False}
                    if item[0] in self.app.player_bindings.data:
                        self.app.player_bindings[item[0]] += [self]
                    else:
                        self.app.player_bindings += {item[0]: [self]}
                    self.move_pressed_keys += {item[0]: False}
                    if item[1] in (PLAYER_INTERFACE_MOVE_BY_FUNCTION, ):
                        self.move_keybindings += {item[0]: (item[1], item[2])}
                    else:
                        self.function_keybindings += {item[0]: (item[1], item[2])}
            if PLAYER_INTERFACE_MOUSE_MOTION_METHOD in self.profile.interface.direct_methods:
                for item in getattr(self.profile.interface, PLAYER_INTERFACE_MOUSE_MOTION_METHOD):
                    self.app.player_motion_bindings += {self: item}
            if PLAYER_INTERFACE_MOUSE_BUTTONS_METHOD in self.profile.interface.direct_methods:
                for item in getattr(self.profile.interface, PLAYER_INTERFACE_MOUSE_BUTTONS_METHOD):
                    self.app.player_buttons_bindings += {item[0]: (self, item[1], item[2])}
        if PLAYER_INTERFACE_EXTERN_BIND in self.profile.interface.bind:
            if PLAYER_INTERFACE_EXTERN_METHOD in self.profile.interface.extern_methods:
                for item in getattr(self.profile.interface, PLAYER_INTERFACE_EXTERN_METHOD):
                    self.app.pressed_keys += {item[0]: False}
                    if item[0] in self.app.player_bindings.data:
                        self.app.player_bindings[item[0]] += [self]
                    else:
                        self.app.player_bindings += {item[0]: [self]}
                    self.move_pressed_keys += {item[0]: False}
                    if item[1] in (PLAYER_INTERFACE_MOVE_BY_FUNCTION, ):
                        self.move_keybindings += {item[0]: [item[1], item[2]]}
                    else:
                        self.function_keybindings += {item[0]: [item[1], item[2]]}
            if self.active:
                self.extern_loop()

    def unload_interface(self):
        class Empty():
            def __init__(self):
                self.minimum_version = Version(0)
                self.title = 'Empty'
                self.bind = ()
        self.profile.interface = Empty()
        for key in self.app.player_bindings:
            i = 0
            while i < len(self.app.player_bindings[key]):
                if self.app.player_bindings[key][i] == self:
                    del self.app.player_bindings[key][i]
                    if len(self.app.player_bindings[key]) == 0:
                        try:
                            del (~self.app.pressed_keys)[key]
                        except:
                            pass
                else:
                    i += 1
        for player in [i for i in self.app.player_motion_bindings]:
            if player == self:
                try:
                    del (~self.app.player_motion_bindings)[player]
                except:
                    pass
        for num in [i for i in self.app.player_buttons_bindings]:
            if self.app.player_buttons_bindings[num][0] == self:
                try:
                    del (~self.app.player_buttons_bindings)[num]
                except:
                    pass
        self.function_keybindings = SuperDict()
        self.move_pressed_keys = SuperDict()
        self.move_keybindings = SuperDict()
        self.has_keys_pressed = False

    def press_key(self, key):
        f = self.function_keybindings[key]
        if f == None:
            self.move_pressed_keys[key] = True
            if not self.has_keys_pressed:
                self.has_keys_pressed = True
                self.move_loop()
            self.has_keys_pressed = True
        elif len(key) == 1:
            getattr(self, f[0])(*f[1])
        else:
            getattr(self, f[0])(*tuple(self.profile.interface.extern_data[i] for i in f[1]))
            
    def release_key(self, key):
        self.move_pressed_keys.set(key, False)
        self.has_keys_pressed = False
        for i in self.move_pressed_keys.data:
            if self.move_pressed_keys.data[i]:
                self.has_keys_pressed = True
                break
            
    def move_loop(self):
        if self.has_keys_pressed and self.active: 
            self.loop_functions.update({self.move_loop: False})              
            x = 0
            y = 0 
            for i in self.move_keybindings.data:
                if self.move_pressed_keys[i]:
                    if type(self.move_keybindings[i]) == tuple:
                        x += self.move_keybindings[i][1][0]
                        y += self.move_keybindings[i][1][1]
                    elif type(self.move_keybindings[i]) == list:
                        x = self.profile.interface.extern_data[self.move_keybindings[i][1][0]]
                        y = self.profile.interface.extern_data[self.move_keybindings[i][1][1]]
                        break
            self.move_by(x, y)
            self.app.map.prepare_after(self.move_interval, self.move_loop)
            self.loop_functions.update({self.move_loop: True})

    def extern_loop(self):
        if self.active:
            self.loop_functions.update({self.extern_loop: False})  
            if PLAYER_INTERFACE_EXTERN_BIND in self.profile.interface.bind:
                if self.profile.interface.extern_code == None:
                    code = str().join(list([i for i in open(self.profile.interface.extern_path, 'r')]))
                else:
                    code = self.profile.interface.extern_code
                exec(code)
                if self.profile.interface.extern_interval > 0:
                    self.app.map.prepare_after(self.profile.interface.extern_interval, self.extern_loop)
                    self.loop_functions.update({self.extern_loop: True})
            else:
                self.unload_interface()
            
    def desactivate(self):
        super(__class__, self).desactivate()
        i = 0
        while self != self.app.map.active_players[i] and i < 10000:
            i += 1
        if i < len(self.app.map.active_players):
            del self.app.map.active_players[i]
        self.app.map.check_endgame()



class Bot(Tank):

    def __init__(self, app):
        super(__class__, self).__init__(app) #Va chercher sa classe parente
        self.profile = BotProfile()
        self.move_interval = DEFAULT_BOT_MOVE_INTERVAL
        self.rotation_canon_interval = DEFAULT_BOT_ROTATION_CANON_INTERVAL
        self.maximum_shoot_delay = DEFAULT_BOT_MAXIMUM_DELAY
        self.minimum_shoot_delay = DEFAULT_BOT_MINIMUM_DELAY
        self.shoot_delay_step = DEFAULT_BOT_DELAY_STEP
        self.random_angle_step = DEFAULT_BOT_RANDOM_ANGLE_STEP
        self.minimum_random_remaining_loops = DEFAULT_BOT_MINIMUM_RANDOM_REMAINING_LOOPS
        self.maximum_random_remaining_loops = DEFAULT_BOT_MAXIMUM_RANDOM_REMAINING_LOOPS
        self.target_type = Player
        self.target = None
        self.old_pos = Point(-1, -1)
        self.random_remaining_loops = None
        self.random_angle = None
        self.debug_move_loop_count = 0#temporaire, destiné à disparaître.
        self.app.map.bots += [self]

    def __repr__(self):
        return 'Bot at : ' + str(~self.pos)

    def activate(self):
        super(__class__, self).activate()
        self.app.map.active_bots += [self]
        self.loop_canon_rotation()
        self.start_move()
        self.loop_functions.update({self.loop_shoot: False})  
        self.app.map.prepare_after(1500, self.loop_shoot)
        self.loop_functions.update({self.loop_shoot: True})

    def loop_canon_rotation(self):
        self.loop_functions.update({self.loop_canon_rotation: False})  
        do_next_loop = True
        if self.target == None or not self.target.active:
            l = [i for i in self.app.map.active_tanks if type(i) == self.target_type and self.active]
            if len(l) > 0:
                self.target = l[0]
            else:
                do_next_loop = False
        if do_next_loop:
            self.rotate_canon_from_event(self.target.pos)
            if self.active:
                self.app.map.prepare_after(self.rotation_canon_interval, self.loop_canon_rotation)
                self.loop_functions.update({self.loop_canon_rotation: True})

    def start_move(self):
        self.random_angle = randrange(360/self.random_angle_step)*self.random_angle_step
        self.random_remaining_loops = randrange(self.maximum_random_remaining_loops-self.minimum_random_remaining_loops) + self.minimum_random_remaining_loops
        self.loop_move()

    def loop_move(self):
        if self.active:
            self.random_remaining_loops += -1
            self.loop_functions.update({self.loop_move: False})  
            self.old_pos = Point(self.pos.x, self.pos.y)
            self.move_at(self.random_angle)
            if (~self.pos == ~self.old_pos and self.debug_move_loop_count < 100) or self.random_remaining_loops == 0:
                self.debug_move_loop_count += 1
                self.start_move()
            else:
                self.debug_move_loop_count = 0
                self.app.map.prepare_after(self.move_interval, self.loop_move)
                self.loop_functions.update({self.loop_move: True})

    def loop_shoot(self):
        if self.active and self.target != None and self.target.active:
            self.loop_functions.update({self.loop_shoot: False})  
            if abs(self.canon_rotation % 90) <= 30:
                pass
            else: 
                self.shoot()
            delay = randrange((self.maximum_shoot_delay-self.minimum_shoot_delay)/self.shoot_delay_step+1)*self.shoot_delay_step+self.minimum_shoot_delay
            self.app.map.prepare_after(delay, self.loop_shoot)
            self.loop_functions.update({self.loop_shoot: True})
            
    def desactivate(self):
        super(__class__, self).desactivate()
        i = 0
        while self != self.app.map.active_bots[i] and i < 10000:
            i += 1
        if i < len(self.app.map.active_bots):
            del self.app.map.active_bots[i]
        self.app.map.check_endgame()
            


class Projectile(MapObject):

    def __init__(self, app):
        super(__class__, self).__init__(app) #Va chercher sa classe parente
        self.profile = ProjectileProfile()
        self.map = app.map
        self.pos = None
        self.shooter = None
        self.remaining_rebounds = None
        self.done_loops = None
        self.vect = None
        self.real_vect = None
        self.rotation = None
        self.interval = 100
        self.pillow_image = None
        self.tk_image = None
        self.app.map.projectiles += [self]

    def __repr__(self):
        import math
        pos = tuple((math.trunc(i*100)/100 for i in ~self.pos))
        vect = tuple((math.trunc(i*100)/100 for i in ~self.vect))
        return 'Projectile at' + repr(pos) + ' moving toward ' + repr(vect)
    
    def activate(self):
        super(__class__, self).activate()
        self.active = True
        if self.app.use_images:
            import PIL
            self.pillow_image = PIL.Image.open(self.profile.graphics.image_adress)
            self.pillow_image.putdata(opacify(self.pillow_image.getdata(), (255, 0, 128, 255), 0))
            self.tk_pillow_image = ImageTk.PhotoImage(self.pillow_image, master=self.app.root)
            self.tag = self.app.canv.create_image(*~self.pos, image=self.tk_image)
        else:
            self.tag = self.app.canv.create_polygon(0,0, 0,0, 0,0, 0,0, 0,0, fill=self.shooter.profile.graphics.base_color)
        self.app.map.active_projectiles += [self]
        self.remaining_rebounds = self.profile.max_rebound 
        self.done_loops = 0

    def actualize_extern_points(self):
        m_sup = Point(
            self.pos.x - (self.profile.graphics.height/2)*cos(radians(self.rotation+90)),
            self.pos.y - (self.profile.graphics.height/2)*sin(radians(self.rotation+90)),
            )
        m_inf = Point(
            self.pos.x - (self.profile.graphics.height/2)*cos(radians(self.rotation-90)),
            self.pos.y - (self.profile.graphics.height/2)*sin(radians(self.rotation-90)),
            )
        self.extern_points = [
            Point(
                m_sup.x - (self.profile.graphics.width/2)*cos(radians(self.rotation)),
                m_sup.y - (self.profile.graphics.width/2)*sin(radians(self.rotation)),
                ),
            Point(
                m_inf.x - (self.profile.graphics.width/2)*cos(radians(self.rotation)),
                m_inf.y - (self.profile.graphics.width/2)*sin(radians(self.rotation)),
                ),
            Point(
                m_inf.x + (self.profile.graphics.width/2+self.profile.graphics.point_width)*cos(radians(self.rotation)),
                m_inf.y + (self.profile.graphics.width/2+self.profile.graphics.point_width)*sin(radians(self.rotation)),
                ),
            Point(
                m_sup.x + (self.profile.graphics.width/2+self.profile.graphics.point_width)*cos(radians(self.rotation)),
                m_sup.y + (self.profile.graphics.width/2+self.profile.graphics.point_width)*sin(radians(self.rotation)),
                ),
            ]
        self.extern_radius = self.profile.graphics.width/2+self.profile.graphics.point_width
          
    def draw(self):
        if self.active:
            if self.app.use_images:
                import PIL
                self.pillow_image = PIL.Image.open(self.profile.graphics.image_adress)
                self.pillow_image.putdata(opacify(self.pillow_image.getdata(), (255, 0, 128, 255), 0))
                self.pillow_image = self.pillow_image.rotate(-self.rotation+270, expand=True)
                self.tk_image = ImageTk.PhotoImage(self.pillow_image, master=self.app.root)
                self.app.canv.itemconfigure(self.tag, image=self.tk_image)
                self.app.canv.coords(self.tag, *~self.pos)
            else:
                self.actualize_extern_points()
                self.app.canv.coords(self.tag,
                    *~self.extern_points[0],
                    *~self.extern_points[1],
                    *~Point(
                        self.extern_points[2].x - self.profile.graphics.point_width*cos(radians(self.rotation)),
                        self.extern_points[2].y - self.profile.graphics.point_width*sin(radians(self.rotation)),
                        ),
                    (self.extern_points[2].x+self.extern_points[3].x)/2, (self.extern_points[2].y+self.extern_points[3].y)/2,
                    *~Point(
                        self.extern_points[3].x - self.profile.graphics.point_width*cos(radians(self.rotation)),
                        self.extern_points[3].y - self.profile.graphics.point_width*sin(radians(self.rotation)),
                        ),                                 
                    )

    def start(self):
        self.rotation = point_to_degree_angle(*~self.vect) % 360
        distance = self.profile.physics.max_speed*self.interval / 1000
        self.real_vect = Vect(distance*cos(radians(self.rotation)), distance*sin(radians(self.rotation)))
        self.actualize_extern_points()
        self.loop()

    def loop(self):
        if self.active:
            self.loop_functions.update({self.loop: False})  
            #mesure du temps de départ
            start_time = time()
            #initialisation de do_next_loop qui sera attribuée à False en cas d'intéraction amenant à la contination de la progression du projectile
            do_next_loop = True
            #vérification que le projectile n'a pas accidentellement traversé un mur et ne poursuit pas inifniment sa course
            if self.done_loops > 100000:
                self.desactivate()
                do_next_loop = False
            #calcul des nouvelles positions
            new_pos = Point(self.pos.x+self.real_vect.x, self.pos.y+self.real_vect.y)
            new_extern_points = [Point(point.x+self.real_vect.x, point.y+self.real_vect.y) for point in self.extern_points]
            new_head_point = Point((new_extern_points[2].x+new_extern_points[3].x)/2, (new_extern_points[2].y+new_extern_points[3].y)/2)
            params = ()
            for point in new_extern_points:
                params += ~point
            #vérification intersection avec un tank ou un projectile actif
            for obj in self.app.map.active_tanks + self.app.map.active_projectiles:
                if type(obj) != Projectile or type(self.shooter) != type(obj.shooter):
                    check_intersection = new_head_point.in_circle(*~obj.pos, obj.extern_radius)
                    if not check_intersection:
                        for point in self.extern_points:
                            if point.in_circle(*~obj.pos, obj.extern_radius):
                                check_intersection = True
                    if check_intersection:
                        if self.intersect_with(obj):
                            obj.interact_with(self)
                            do_next_loop = True
                            break
            #vérification intersection avec un item actif
            for item in self.app.map.active_items:
                for point in [new_head_point] + new_extern_points:
                    if item.corners.left < point.x < item.corners.right and item.corners.top < point.y < item.corners.bottom:
                        item.interact_with(self)
                        do_next_loop = False
                        break
            #changemnent de la position
            if do_next_loop and self.tag:
                self.pos = Point(*~new_pos)
                self.actualize_extern_points() 
                self.draw()
                self.done_loops += 1
                self.app.map.prepare_after(self.interval, self.loop)
                self.loop_functions.update({self.loop: True})
            end_time = time()
            self.history += [end_time-start_time]

    def interact_with(self, obj):
        super(__class__, self).interact_with(obj)
        if issubclass(type(obj), Tank):
            if type(self.shooter) != type(obj):
                self.desactivate()
                obj.desactivate()
        if issubclass(type(obj), Projectile):
            if type(self.shooter) != type(obj.shooter):
                self.desactivate()
                obj.desactivate()
            
	
    def desactivate(self, eleanor=None):
        if self.active:
            self.active = False
            for i in self.app.map.active_objects:
                if self == i:
                    del self.app.map.active_objects[self.app.map.active_objects.index(i)]
            for i in self.app.map.active_movable_items:
                if self == i:
                    del self.app.map.active_movable_items[self.app.map.active_movable_items.index(i)]
            for i in self.app.map.active_projectiles:
                if self == i:
                    del self.app.map.active_projectiles[self.app.map.active_projectiles.index(i)]
            self.app.canv.delete(self.tag)
            self.tag = None
            self.shooter.remaining_ammo += 1
            if self.shooter.remaining_ammo > self.shooter.profile.ammo_max:
                self.shooter.remaining_ammo = self.shooter.profile.ammo_max

def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()
else:
    warn('main.py is being imported')
    main()
