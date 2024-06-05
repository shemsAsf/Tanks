"""
1.0: Fonctions importées de la bibliothèque personnelle d'AM.
1.1: Ajout des classes Point et Corners.
1.2: Ajout de la classe SuperDict.
1.3: Ajout de la vérification de l'adresse pour les backups (évite de planter si le dossier demandé n'existe pas, lance seulement un averissement).
1.4: Déplacement des classes utiles (par opposition aux outils de développement qui ne seront pas présents dans la version finale).
1.5: Ajout de la surcharge de l'opératur d'inversion '-' de Babckup pour désactiver les avertissements. Ajout de la classe Tabify et de tabify.
2.0.0: Récupération du code de la version finale de Tanks1 (version fonctionnelle basique).
2.0.1: Import de builtins dans Backup pour prévenir d'un opverwrite de builtins.open
"""

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

if __name__ == '__main__':
    pass
elif 'VERSION' in globals():
    print(__name__ + str().join([' ' for i in range(30-len(__name__))]) + ' ' + VERSION + ' successfully imported')  
    del VERSION
