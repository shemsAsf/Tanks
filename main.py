from tanksmodules.tanksmain import *
import tanksmodules.tanksmain as tks


def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()
else:
    warn('main.py is being imported')
    main()
