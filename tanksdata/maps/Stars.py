import os



bg_adress = 'tanksdata|images|bg_Stars1'.replace('|', SEP)

if os.path.exists(bg_adress):
    flag = 'wb'
else:
    flag = 'xb'
with open(bg_adress, flag) as f:
    f.write(bg_bytes)



sdp_false_walll_adress = 'tanksdata|images|Stars_sdp_false_walll.png'.replace('|', SEP)
sdp_false_walll_bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\x00\x00 \x08\x06\x00\x00\x00szz\xf4\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x0e\xc2\x00\x00\x0e\xc2\x01\x15(J\x80\x00\x00\x007IDATXG\xed\xce\xa1\x11\x00 \x10\x04\xb1\x03\xc3\x0c}\xd0\x7f\x89\xbc\xa1\x87\x17d\xcd\xda\x8c\xb5\xcfMc\xf3\xbd-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xdf\x01I\x01\x87u\x01u\x154\xf2`\x00\x00\x00\x00IEND\xaeB`\x82'

import os
if os.path.exists(sdp_false_walll_adress):
    flag = 'wb'
else:
    flag = 'xb'
with open(sdp_false_walll_adress, flag) as f:
    f.write(sdp_false_walll_bytes)

aux_wall_profile2 = WallProfile({
    'graphics': WallGraphicProfile({
        'image_adress': sdp_false_walll_adress,
        'opacity': 0.70,
        }),
    'solid_for_projectiles': False,
    })



low_resistance_wall_adress = 'tanksdata|images|Stars_low_resistance_walll.png'.replace('|', SEP)
low_resistance_wall_bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\x00\x00 \x08\x06\x00\x00\x00szz\xf4\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x0e\xc4\x00\x00\x0e\xc4\x01\x95+\x0e\x1b\x00\x00\x01wIDATXG\xc5\x94\xd1\x16\xc20\x08C\xa7?\xee\xfcr]\xea23\x84B\xeb9z_\xech\x80\x94u^\x1e\xcb\xfaX\xfeH3\xb0\xder\x0f\xeb\xfd\xb2\xaf\xb6\xf5\xa6\xb7\xcf\x1e\xd4\xe8\xbe\xc6\xb0\xbe\xb6\xa7\x0e\x10i3\x0f\xd5xZ\x1bSC\xc3\x13\x88Nc\xe9\xed\x11h\xd2\t\xf4\xa8\x18\xf7@c\x1al\x06\xf8\xf0\x0fJ\x13\x88\x0cf\xf1hB\x1a?\x0c if\x12#\xaf\xc1\xeb\xf16\xb0\x17\x9a1\x91\xe15f\xbf\xd7\x1d`\xf3\xc4\x84\x9e\xd6\xd3h\xa3\x93V\xd6\x96\x8f;\x90\x99\x88\x98\xd5\xbb\x97\xb0bB5V\xe7\x9d\x181/\xee\x1a\x00\x15\x13\x96\xa8\x89b\xf7\xd3\x7f\xc2\xect#\x06\tk 7\x9c\x00\x81828\xd3\xdc24\x01\xd5Eq\xd2\xdb\xd7\xbd\xf8\x0el"\x15F\x84\xd3\xd9\xe2\xdc\xeb\xd5:M\xa0\xd2P\x89\x9a{t\r\xec\xebFs.\xe2\xcc\xdc\xb7&\x0e\x03\xd5B^\x91\x11\x13@k\xb4;0Z\xc0\x12M\'B\xfb\xa5\x9f\xa1\x05\xc9\xdf\x1a\x06\xacq\xba\x033\x85+\xa7\x8f\xea"\xf7\xe3\x12\x92\x113(\xd4kB\xac\x06{\xa7W\x00\x01E\xad\xa8$\xcfbkZ\xba\xaf\x80\t6nif\x13\r\x08\rT\x1a\xb4\xdf@W5J\xd4H\xe9+`a\xef\x04\xa0\xda\x98@\xcf\x9c\xf2g\xa8&"##\xb0F\xd7\x806\xb2M=\x13\x88yq\x8fp\x02\xb6\x08\xd7\x1c\x1b\x13-\x1a?r\x8c\x19\xfb\x0c\xc2\xff\x81\xdf\xb0,O\x9eS\x18\xb9/\x9b\x96S\x00\x00\x00\x00IEND\xaeB`\x82'

import os
if os.path.exists(low_resistance_wall_adress):
    flag = 'wb'
else:
    flag = 'xb'
with open(low_resistance_wall_adress, flag) as f:
    f.write(low_resistance_wall_bytes)

aux_wall_profile1 = WallProfile({
    'graphics': WallGraphicProfile({
        'image_adress': low_resistance_wall_adress,
        }),
    'resistance': 0.5,
    })



normal_walll_adress = 'tanksdata|images|Stars_normal_walll.png'.replace('|', SEP)
normal_walll_bytes = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\x00\x00 \x08\x06\x00\x00\x00szz\xf4\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x0e\xc4\x00\x00\x0e\xc4\x01\x95+\x0e\x1b\x00\x00\x00gIDATXGc\xfc\xcf\xd0\xf0\x9f\x01\x08\xf8E\xe7\x83(0\xf8\xf8:\x11\xca\xa2.\xc0f\x07\x13\x98\x1c@\xc0\xc8'*\x0f\x0e\x81\x81\x02\x03\x1e\x02\x03\x1f\x05\xd8\x12\xe1\xcf\xaflP\x16u\x01;\xf7/(k\x10%\xc2Q\x07\x8c:`\xd4\x01\xa3\x0e\x18u\xc0\xa8\x03F\x1d0\xea\x80Q\x07\x8c:`\xb4c2\xf0Q0\xc2{\xc7\x0c\x0c\x00\x1b\xde\x1c8$\r\x96Y\x00\x00\x00\x00IEND\xaeB`\x82"

import os
if os.path.exists(normal_walll_adress):
    flag = 'wb'
else:
    flag = 'xb'
with open(normal_walll_adress, flag) as f:
    f.write(normal_walll_bytes)

aux_wall_profile3 = WallProfile({
    'graphics': WallGraphicProfile({
        'image_adress': normal_walll_adress,
        }),
    })

data = {
    'grid_size': Point(29, 20),
    'title': 'Stars1',
    'border_profile': aux_wall_profile3,
    'background_image_adress': bg_adress,
    'player_list': [
        (Point(2, 2), PlayerProfile()),
        (Point(2, 4), PlayerProfile()),
        (Point(2, 7), PlayerProfile()),
        (Point(4, 2), PlayerProfile()),
        ],
    'bot_list': [
        (Point(8, 17), BotProfile()),
        (Point(16, 14), BotProfile()),
        (Point(21, 8), BotProfile()),
        ],
    'wall_list': {
        Corners(4, 4, 5, 5): aux_wall_profile3,
        Corners(4, 8, 9, 9): aux_wall_profile3,
        Corners(4, 11, 5, 13): aux_wall_profile2,
        Corners(4, 15, 8, 16): aux_wall_profile3,
        Corners(5, 4, 6, 5): aux_wall_profile1,
        Corners(5, 11, 6, 13): aux_wall_profile2,
        Corners(6, 4, 7, 5): aux_wall_profile3,
        Corners(6, 5, 7, 7): aux_wall_profile1,
        Corners(6, 16, 7, 19): aux_wall_profile2,
        Corners(7, 4, 8, 5): aux_wall_profile1,
        Corners(8, 4, 9, 5): aux_wall_profile3,
        Corners(8, 6, 9, 8): aux_wall_profile1,
        Corners(8, 9, 9, 13): aux_wall_profile3,
        Corners(8, 15, 10, 16): aux_wall_profile2,
        Corners(9, 4, 10, 5): aux_wall_profile2,
        Corners(9, 10, 11, 11): aux_wall_profile1,
        Corners(10, 4, 11, 5): aux_wall_profile3,
        Corners(10, 5, 11, 7): aux_wall_profile1,
        Corners(10, 8, 12, 9): aux_wall_profile1,
        Corners(10, 12, 12, 13): aux_wall_profile1,
        Corners(10, 15, 14, 16): aux_wall_profile3,
        Corners(11, 4, 12, 5): aux_wall_profile2,
        Corners(11, 16, 12, 19): aux_wall_profile2,
        Corners(12, 4, 13, 5): aux_wall_profile3,
        Corners(12, 5, 13, 6): aux_wall_profile1,
        Corners(12, 6, 13, 7): aux_wall_profile3,
        Corners(12, 7, 13, 8): aux_wall_profile1,
        Corners(12, 8, 13, 9): aux_wall_profile3,
        Corners(12, 9, 13, 10): aux_wall_profile2,
        Corners(12, 10, 13, 11): aux_wall_profile3,
        Corners(12, 11, 13, 12): aux_wall_profile2,
        Corners(12, 12, 13, 13): aux_wall_profile3,
        Corners(13, 4, 16, 13): aux_wall_profile2,
        Corners(14, 1, 15, 4): aux_wall_profile1,
        Corners(15, 1, 16, 4): aux_wall_profile1,
        Corners(18, 4, 19, 5): aux_wall_profile1,
        Corners(18, 12, 19, 13): aux_wall_profile1,
        Corners(19, 4, 20, 7): aux_wall_profile3,
        Corners(19, 10, 20, 13): aux_wall_profile3,
        Corners(19, 15, 23, 16): aux_wall_profile3,
        Corners(20, 6, 21, 7): aux_wall_profile1,
        Corners(20, 10, 21, 11): aux_wall_profile1,
        Corners(22, 1, 23, 4): aux_wall_profile1,
        Corners(22, 13, 23, 15): aux_wall_profile1,
        Corners(22, 16, 23, 17): aux_wall_profile3,
        Corners(23, 3, 25, 4): aux_wall_profile1,
        Corners(23, 10, 24, 13): aux_wall_profile3,
        Corners(23, 13, 24, 15): aux_wall_profile1,
        Corners(24, 12, 25, 13): aux_wall_profile3,
        },
    }


if True:
    def PATCH_Map_load(self):
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
            self.app.canv.config(bg=self.profile.background_color)
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
        if 'border_profile' in dir(self.profile):
            for wall in [wall1, wall2, wall3, wall4]:
                wall.profile = self.profile.border_profile
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
        import tkinter.messagebox as messagebox
        for i in range(len(self.profile.bot_list)):
            newbot = Bot(self.app)
            newbot.spawn_order = i
            old_spawn = self.profile.bot_list[i][0]
            newbot.spawn = Point(old_spawn.x*self.app.scale, old_spawn.y*self.app.scale)
            newbot.pos = newbot.spawn
            newbot.profile = self.profile.bot_list[i][1]
        for corners_coords in self.profile.wall_list:
            if type(corners_coords) == tuple:
                newwall = Wall(self.app, Corners(*(i*scale for i in corners_coords)))
            else:
                newwall = Wall(self.app, Corners(*(i*scale for i in ~corners_coords)))                
            newwall.profile = self.profile.wall_list[corners_coords]
    Map.load = PATCH_Map_load

if True:
    def PATCH_Wall_draw_image(self):
        if self.active:
            import PIL
            self.canvas_tag = []
            image = PIL.Image.open(self.profile.graphics.image_adress)
            if 'opacity' in dir(self.profile.graphics):
                image.putdata(list([(i, j, k, round(255*self.profile.graphics.opacity)) for i, j, k, l in image.getdata()]))
            else:
                image.putdata(opacify(image.getdata(), (255, 0, 128, 255), 0))
            self.pillow_image = ImageTk.PhotoImage(image, master=self.app.root)
            for x in range(round(self.corners.left/self.app.scale), round(self.corners.right/self.app.scale)):
                for y in range(round(self.corners.top/self.app.scale), round(self.corners.bottom/self.app.scale)):
                    params = (x*self.app.scale+self.app.scale/2, y*self.app.scale+self.app.scale/2)
                    #self.app.canv.create_rectangle(params[0]-2, params[1]-2, params[0]+2, params[1]+2, fill='green')
                    new_tag = self.app.canv.create_image(*params, image=self.pillow_image )
                    self.canvas_tag += [new_tag]
    Wall.draw_image = PATCH_Wall_draw_image
    
if True:
    def PATCH_Wall_interact_with(self, obj):
        super(Wall, self).interact_with(obj)
        if issubclass(type(obj), Projectile):
            if not self.profile.solid_for_projectiles:
                obj.pos = Point(obj.pos.x+obj.real_vect.x, obj.pos.y+obj.real_vect.y)
                obj.actualize_extern_points() 
                obj.draw()
                obj.done_loops += 1
                obj.app.map.prepare_after(obj.interval, obj.loop)
                obj.loop_functions.update({obj.loop: True})
            elif obj.remaining_rebounds > 0:
                if obj.profile.destruction_power >= self.profile.resistance:
                    self.desactivate()
                    obj.desactivate()
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
    Wall.interact_with = PATCH_Wall_interact_with

if True:
    def PATCH_Wall_desactivate(self):
        if self.active:
            self.active = False
            to_del = -1
            for i in range(len(self.app.map.active_items)):
                if self.app.map.active_items[i] == self:
                    to_del = i
            if to_del > -1:
                del self.app.map.active_items[to_del]
            to_del = -1
            for i in range(len(self.app.map.active_static_items)):
                if self.app.map.active_static_items[i] == self:
                    to_del = i
            if to_del > -1:
                del self.app.map.active_static_items[to_del]
            to_del = -1
            for i in range(len(self.app.map.active_objects)):
                if self.app.map.active_objects[i] == self:
                    to_del = i
            if to_del > -1:
                del self.app.map.active_objects[to_del]
                
            for i in self.canvas_tag:
                self.app.canv.delete(i)   
            self.canvas_tag = None
    Wall.desactivate = PATCH_Wall_desactivate

if True:
    def PATCH_Projectile_loop(self):
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
                if not do_next_loop:
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
    Projectile.loop = PATCH_Projectile_loop