"""
1.0: Premierères constantes DEFAULT_APP_SCALE, DEFAULT_TANK_BASE_ROTATION, DEFAULT_TANK_CANON_ROTATION.
1.1: Ajout constantees pour PlayerInterfaceProfile.
1.1.? Passage des constantes k1, k2, k3 pour le dessin du canon.
1.2.? Ajout de constantes.
2.0.0: Récupération de get_nicknames depuis main.py.
2.0.1: Passage au nouveau format des versions.
2.1.0: Ajout de show_versions.
2.2.0: Ajout de import_personnal_settings.
2.2.1: Meilleure gestion des paramètres dans import_personnal_settings (préfixes, ...).
2.2.2: Correction des légers imprévus dans import_personnal_settings (grosses bavures dans le cas d'un fichier vide, soyons honnêtes).
2.2.3: Correction dans import_personnal_settings par rapport au "warn".
2.2.4: Correction dans import_personnal_settings.
2.2.5: Ajout du paramètre show_if_empty dans import_personnal_settings.
2.2.6: Ajout du paramètre app dans import_personnal_settings pour ajouter des scripts au redémarrage de l'app. 
"""

from tanksmodules.tanksutils import *

globals().update(new_version('2.2.6', __name__))
    
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
