"""
1.?.? Evolution des principales classes tout le long du développement de la version fonctionnelle.
2.0.0: Récupération du code de la version finale de Tanks1 (version fonctionnelle basique).
2.0.1: Passage au nouveau format des versions
2.1.0: Passage au nouveau format des profils (suppressions des objets profils par défaut)
2.1.1: Correction de l'erreur dans Player.check_interface_specs (utilisation de l'ancienne constante VERSION)
2.1.2: Ajout de la méthode Tank.actualize_graphics.
2.2.0: Ajout de toutes les méthodes et attributs de MapObject.
2.2.1: Ajout de constantes de debug
2.3.0: Changement des algorithmes de Tank.move_to.
2.4.0: Changement des algorithmes de Projectile.loop et de Projectile.draw.
2.4.1: Ajout de la méthode "check_endgame" à App.
2.4.2: Ajout des méthodes des méthodes "interact_with" dans les descendants de MapObject.
2.4.3: Ajout des méthodes des méthodes "desactivate" dans les descendants de MapObject.
2.5.0: Modification des interface des Player.
2.5.1: Adapatation aux interfaces externes des Player.
2.5.2: Ajout de la méthode Tank.rotate_canon_to et adaptation de Tank.rotate_from_event.
2.5.3: Ajout des méthodes App.run_again et App.destroy.
2.5.4: Ajout de la classe App.ApDebugParameters (utilsée pour accéder plus facilement aux paramètre de débugage et adaptation des paramètres pré-existants.
2.5.5: Modification de la méthode App.check_endgame, App.run_again et App.destroy (proposition pour rejouer la partie).
2.5.6: Ajout de la ckasse App.AppPersonnalSettings et tentative d'execution des scripts importés dans main (infuctueuse jusque là).
2.5.7: Ajout de conditions de sécurité dans Bot pour l'empêcher de boucler à l'infini (dû au manque de définition actuel de MapObject.intersect_with) et dans Projectile pour que le nombbre de projectiles ne dépasse pas le nombre maximum défini dans le profil du Bot.
2.5.8: Ajout de la méthode Player.unload_interface.
2.5.9: Ajout de des méthdoes App.motion et App.buttons puis modifications de Player.load_interface et Player.unload_interface et délais avant que le bot ne commence à tirer.
2.6.0: Premières modifications liées à l'utilisation d'images (ajout de l'attribut App.use_images et réorientation de Wall.draw) ainsi que le dessin du fond de la carte et dessin des wall (basique, sans utilisation du chemin décrit dans le profil).
2.6.1: Utilisation complète d'images.
2.6.2: Déplacement de la méthode App.check_endgame vers Map.check_endgame.
2.6.3: Déplacement de la méthode "opacify" de tanksmain.py vers tanksutils.py.
2.6.4: Passage au méthodes optimissées de after (à savoir prepare_after et do_after).
2.6.5: Retour à la méthode after classique par redirection de prepare_after.
2.7.0: Ajout de la fonction pause et des dictionnaires de fonctions loops (fonction pause bindée sur <p>).
2.7.1: Verrouillage de la taille de la fenêtre.
2.7.2: Ajout de la barre de menu et du bouton pause.
3.0.0: Menus codés à la barbare.
3.0.1: Ajout de l'idle et redirection modification de App.run_again.
3.0.2: Amélioration du placement des composants dans les menus.
3.0.3: Correction du App.run_again.
3.0.4: Ajout de conditions supplémentatires dans les pauses.
3.0.5: Ajout des images des bouttons sur l'écran d'accueil.
3.1.0: Ajout de l'écran de sélection des interfaces
3.1.1: Changement de l'écran de sélection des interfaces vers un écran de sélection des profils.
3.1.2: Correction bug stratégie bot (un plus à la place d'un moins)
3.2.0: Ajout menu aide.
3.2.1: Recification interface
3.2.2: Tentative de vérification intersect_with (échec)
"""


from tkinter import *
from tanksmodules import *
from math import sqrt, cos, sin, acos, asin, atan, degrees, radians
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


        
if __name__ == '__main__':
    from main import *