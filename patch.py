import os

SEP = os.path.sep
tanksmain_path = 'tanksmodules|tanksmain.py'.replace('|', SEP)
compact_path = 'Tanks3Compact.py'

if os.path.exists(tanksmain_path):
    try:
        file = ''
        with open(tanksmain_path, 'r') as f:
            for i in f:
                file += i
        file = file.replace(
            'self.app.canv.config(bg=self.profile.background_image_adress)',
            'self.app.canv.config(bg=self.profile.background_color)'
            )
        with open(tanksmain_path, 'w') as f:
            f.write(file)
    except:
        print('frist_except')
else:
    print('first else')
if os.path.exists(compact_path):
    try:
        file = ''
        with open(compact_path, 'r') as f:
            for i in f:
                file += i
        file = file.replace(
            'self.app.canv.config(bg=self.profile.background_image_adress)',
            'self.app.canv.config(bg=self.profile.background_color)'
            )
        with open(compact_path, 'w') as f:
            f.write(file)
    except:
        pass
