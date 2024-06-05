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
    if i == 'ABS_X' and abs(d[i].state) < LIM:
        l += [i]
        break
for i in d:
    if i == 'ABS_Y' and abs(d[i].state) < LIM:
        l += [i]
        break
for i in d:
    if i == 'ABS_RX' and abs(d[i].state) < LIM:
        l += [i]
        break
for i in d:
    if i == 'ABS_RY' and abs(d[i].state) < LIM:
        l += [i]
        break
for i in d:
    if d[i].ev_type == 'Key' and d[i].state == 0:
        l += [i]
        break  
for i in l:
    del d[i]

b = False
for i in d:
    if i == 'ABS_X':
        self.profile.interface.extern_data['move_position_x'] = d[i].state/MAX
        b = True
        break    
for i in d:
    if i == 'ABS_Y':
        self.profile.interface.extern_data['move_position_y'] = -d[i].state/MAX
        b = True
        break
if b:
    self.app.keypress(ArtificialKeySymEvent('ABS_X_Y'))
else:
    self.app.keyrelease(ArtificialKeySymEvent('ABS_X_Y'))

b = False
for i in d:
    if i == 'ABS_RX':
        self.profile.interface.extern_data['canon_position_x'] = d[i].state/MAX
        b = True
        break    
for i in d:
    if i == 'ABS_RY':
        self.profile.interface.extern_data['canon_position_y'] = d[i].state/MAX
        b = True
        break
if b:
    self.app.keypress(ArtificialKeySymEvent('ABS_RX_RY'))
else:
    self.app.keyrelease(ArtificialKeySymEvent('ABS_RX_RY'))

for i in d:
    if i == 'ABS_RZ':
        if d[i].state > 130:
            self.app.keypress(ArtificialKeySymEvent('ABS_RZ'))
        else:
            self.app.keyrelease(ArtificialKeySymEvent('ABS_RZ'))
        break

for i in d:
    if i == 'BTN_NORTH':
        self.app.run_again()
        break
