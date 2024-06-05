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
    
app.root.bind('<Button-2>', lambda event: exec('b1.active=False'))
app.root.bind('<Button-3>', lambda event: g())
app.root.bind('<Double-3>', f)
