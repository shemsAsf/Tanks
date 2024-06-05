"""
1.0: Classes utiles présentes dans la version finale: Point, Corners et SuperDict
1.1: Déplacement des modules vers le dossier tanksmodules
1.2: Ajout de la classe Vect. Surcharge de l'opérateur "~" pour Point, et Corners. Ajout de la classe Version.
1.3: Surcharge de l'opérateur "in" de Corners
2.0.0: Récupération du code de la version finale de Tanks1 (version fonctionnelle basique).
2.0.1: Nouvelle gestion des versions plus propre par Version et new_version
2.0.2: Importation totale de os
2.0.3: Ajout de Point.in_circle
2.0.4: Redéfinition de open depuis os.open vers builtin.open après l'importation totale de os.
2.0.5: Ajout de méthodes à SuperDict.
2.1.0: Ajout des classes ArtificialKeySymEvent et ArtificialNumEvent.
2.1.1: Ajout de la focntion new.
2.1.2: Ajotu de la fonction opacify.
"""

from tanksmodules.tankstoolbox import *
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

exec(-backup-'AM'>>'D:\\Backups')

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
