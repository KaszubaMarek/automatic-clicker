import time
from pynput import mouse, keyboard

#  Todo make class Automat for doing various automated activities
# class Automat:
#     def __init__(self):
#         self.mouse = mouse.Controller()
#         self.keyboard = keyboard.Controller()


class Mouse:
    def __init__(self):
        self.mouse = mouse.Controller()

    def move_to_point(self, x, y):
        self.mouse.position = (x, y)
        print('moved mouse')

    def click_button(self, button):
        self.mouse.press(button)
        self.mouse.release(button)
        print('clicked left button')


class Keyboard:
    def __init__(self):
        self.keyboard = keyboard.Controller()

    def write(self, text):
        for sign in text:
            self.keyboard.press(sign)
            self.keyboard.release(sign)
            time.sleep(0.1)
            print('write text')

    def pres_key(self, key):
        self.keyboard.press(key)
        time.sleep(0.2)
        self.keyboard.release(key)
        time.sleep(0.2)
        print(f'pressed key {key}')

    def paste_text(self, text):
        self.keyboard.type(text)


class OpenFile:
    def __init__(self, path):
        self.path = path

    def open_txt_file(self):
        with open(self.path, 'r') as file:
            text = file.read()

        return text

    def open_json_file(self):
        ...


mouse_action = Mouse()
keyboard_action = Keyboard()
mouse_action.move_to_point(x=30, y=1050)
time.sleep(0.5)
mouse_action.click_button(mouse.Button.left)
time.sleep(3)
mouse_action.move_to_point(x=193, y=138)
mouse_action.click_button(mouse.Button.left)
time.sleep(0.5)
keyboard_action.write('koszubamarek82@gmail.com')
for _ in range(2):
    keyboard_action.pres_key(keyboard.Key.tab)
keyboard_action.write('Prawie Walentynki')
keyboard_action.pres_key(keyboard.Key.tab)

open_file = OpenFile('message.txt')
read_text = open_file.open_txt_file()
keyboard_action.paste_text(read_text)
mouse_action.move_to_point(x=37, y=110)
time.sleep(0.5)
mouse_action.click_button(mouse.Button.left)










