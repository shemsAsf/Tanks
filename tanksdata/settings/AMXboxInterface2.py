class ArtificialKeySymEvent():
    def __init__(self, keysym):
        self.keysym = keysym


LIM = 10000
MAX = 32768


d = self.profile.interface.extern_events
i = 0
import inputs
while i < 10:
    for event in inputs.get_gamepad():
        if event.ev_type not in ('Sync', ):
            d.update({event.code: event})
    i += 1
l = []
for i in d:
    if d[i].ev_type == 'Absolute' and 'Z' not in d[i].code and abs(d[i].state) < LIM:
        l += [i]
    elif d[i].ev_type == 'Absolute' and 'Z' in d[i].code and d[i].state < 10:
        l += [i]
    elif d[i].ev_type == 'Key' and d[i].state == 0:
        l += [i]        
for i in l:
    del d[i]


x = 0
y = 0
b = False
for i in d:
    if d[i].code == 'ABS_X':
        b = True
        x += d[i].state/MAX
    if d[i].code == 'ABS_Y':
        b = True
        y += -d[i].state/MAX
if b:
    self.profile.interface.extern_data['move_position_x'] = x
    self.profile.interface.extern_data['move_position_y'] = y
    self.app.keypress(ArtificialEvent('ABS_X_Y'))
else:
    self.app.keyrelease(ArtificialEvent('ABS_X_Y'))


x = 0
y = 0
b = False
for i in d:
    if d[i].code == 'ABS_RX':
        x += d[i].state/MAX
        b = True
    if d[i].code == 'ABS_RY':
        y += d[i].state/MAX
        b = True
if b:
    self.profile.interface.extern_data['canon_position_x'] = x
    self.profile.interface.extern_data['canon_position_y'] = y
    self.app.keypress(ArtificialEvent('ABS_RX_RY'))
else:
    self.app.keyrelease(ArtificialEvent('ABS_RX_RY'))


for i in d:
    if d[i].code == 'ABS_RZ':
        if d[i].state > 130:
            self.app.keypress(ArtificialEvent('ABS_RZ'))
        else:
            self.app.keyrelease(ArtificialEvent('ABS_RZ'))
    if d[i].code == 'BTN_NORTH':
        self.app.run_again()
