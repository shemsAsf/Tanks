def activate(self):
    super(Bot, self).activate()
    self.app.map.active_bots += [self]
    self.loop_canon_rotation()
    #self.start_move()
    #self.loop_shoot()
def move_to(self, x, y):
    start = time()
    old_pos = Point(*~self.pos)
    self.pos = Point(x, y)
    self.actualize_extern_points()
    do_move = True
    contact_point_indexes = -1
    contact_objs = None
    for obj in self.app.map.active_objects:
        if issubclass(type(obj), MapItem):
            for i in range(len(self.extern_points)): 
                if self.extern_points[i] in obj.corners:
                    contact_point_index = i
                    contact_obj = obj
                    do_move = False
                    break
        elif obj != self:
            for i in range(len(self.extern_points)):                    
                if self.extern_points[i].in_circle(obj.pos.x, obj.pos.y, obj.extern_radius):
                    contact_point_index = i
                    contact_obj = obj
                    do_move = False
                    break
            if self.intersect_with(obj):
                do_move = False
                break
    if not do_move:
        self.pos = Point(*~old_pos)
        self.actualize_extern_points()
        if contact_point_index > -1:
            old_contact_point = Point(*~self.extern_points[contact_point_index])
            new_contact_point = Point(*~self.extern_points[contact_point_index])
            if issubclass(type(contact_obj), MapItem):
                i = 0
                d = -3
                small_corners = Corners(contact_obj.corners.left+d, contact_obj.corners.top+d, contact_obj.corners.right-d, contact_obj.corners.bottom-d)
                while new_contact_point not in small_corners and i < 100:
                    new_contact_point.x += self.move_vect.x/2
                    new_contact_point.y += self.move_vect.y/2
                    i += 1
                if self.app.show_debug_graphics:
                    self.app.canv.create_line(small_corners.left, small_corners.top, small_corners.left, small_corners.bottom, fill='green')
                    self.app.canv.create_line(small_corners.left, small_corners.bottom, small_corners.right, small_corners.bottom, fill='green')
                    self.app.canv.create_line(small_corners.right, small_corners.bottom, small_corners.right, small_corners.top, fill='green')
                    self.app.canv.create_line(small_corners.right, small_corners.top, small_corners.left, small_corners.top, fill='green')
                if self.app.show_debug_graphics:
                    self.app.canv.create_polygon(new_contact_point.x-d, new_contact_point.y-d, new_contact_point.x-d, new_contact_point.y+d, new_contact_point.x+d, new_contact_point.y+d, new_contact_point.x+d, new_contact_point.y-d,fill='yellow')
                    self.app.canv.create_polygon(old_contact_point.x-d, old_contact_point.y-d, old_contact_point.x-d, old_contact_point.y+d, old_contact_point.x+d, old_contact_point.y+d, old_contact_point.x+d, old_contact_point.y-d, fill='blue')
                if True and ~old_contact_point != ~new_contact_point:
                    self.pos = Point(self.pos.x+new_contact_point.x-old_contact_point.x, self.pos.y+new_contact_point.y-old_contact_point.y)
                    self.actualize_extern_points()
                    self.draw()
    else:
        self.draw()
    self.history += [time()-start]
    print(time()-start)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __invert__(self):
        return (self.x, self.y)
    def in_circle(self, x, y, r):
        return (x-self.x)**2+(y-self.y)**2 <= r**2

if False:
    tks.Bot.activate = activate
    tks.Tank.move_to = move_to
