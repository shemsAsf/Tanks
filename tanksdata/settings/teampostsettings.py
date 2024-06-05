p1.profile.projectiles.graphics.height = 6
p1.profile.projectiles.graphics.width = 12
p1.profile.projectiles.graphics.point_width = 8
b1.profile.projectiles.graphics.height = 6
b1.profile.projectiles.graphics.width = 24
b1.profile.projectiles.graphics.point_width = 8
def f(event=None):
    print('\n')
    for i in app.map.__dict__:
        if type(app.map.__dict__[i]) == list:
            print(i, ':', len(app.map.__dict__[i]))
        if i == 'static_items':
            print('')
def g(event=None):
    globals().update({'p2': Player(app)})
    p2.profile = PlayerProfile()
    p2.pos = Point(100, 100)
    p2.activate()
    p2.draw()
def h(event=None):
    global nbr
    nbr = []
    for i in app.map.active_objects:
        print(type(i), i.loop_functions)
        for j in i.loop_functions:
            if i.loop_functions[j]:
                nbr += [(i, j)]
        i.active = False
    print(nbr)
def m(event=None):
    for i in nbr:
        i[0].active = True
        i[1]()
app.root.bind('<Double-2>', lambda event: exec('b1.active=False'))
app.root.bind('<Button-2>', lambda event: m())
app.root.bind('<Button-3>', h)
