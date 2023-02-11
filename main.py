import json
import time
from pynput import mouse, keyboard


class Mouse:
    def __init__(self):
        self.mouse = mouse.Controller()

    def move_to_point(self, x, y):
        self.mouse.position = (x, y)
        time.sleep(0.5)
        print(f'moved mouse to point {self.mouse.position}')

    def click_button(self, button, sleep):
        self.mouse.press(button)
        self.mouse.release(button)
        time.sleep(sleep)
        print('clicked left button')


class Keyboard:
    def __init__(self):
        self.keyboard = keyboard.Controller()

    def write(self, text):
        for sign in text:
            self.keyboard.press(sign)
            self.keyboard.release(sign)
            time.sleep(0.2)
        print('write text')

    def pres_key(self, key, number_of_clicks):
        for _ in range(number_of_clicks):
            self.keyboard.press(key)
            time.sleep(0.2)
            self.keyboard.release(key)
            time.sleep(0.2)
            print(f'pressed key {key}')

    def paste_text(self, text):
        self.keyboard.type(text)
        time.sleep(1.5)


class File:
    def __init__(self, path):
        self.path = path

    def open_txt_file(self):
        with open(self.path, 'r') as file:
            text = file.read()

        return text

    def open_json_file(self):
        with open(self.path) as json_file:
            data = json.load(json_file)

        return data


class Process:
    def __init__(self, mouse_action, keyboard_action, txt_file):
        self.mouse_action = mouse_action
        self.keyboard_action = keyboard_action
        self.txt_file = txt_file

        self.options = {
            'Move to': self.mouse_action.move_to_point,
            "Click mouse button": lambda button, sleep: self.mouse_action.click_button(getattr(mouse.Button, button),
                                                                                       sleep),
            "Write text": self.keyboard_action.write,
            "Press key": lambda key, clicks: self.keyboard_action.pres_key(getattr(keyboard.Key, key),
                                                                           clicks),
            "Past text": lambda text: self.keyboard_action.paste_text(eval(text))
        }
        self.steps = []

    def load_json(self):
        json_file = File('action.json')
        self.steps = json_file.open_json_file()['steps']

    def start(self):
        for step in self.steps:
            for name, value in step.items():
                self.options[name](**value)


def main():
    mouse_action = Mouse()
    keyboard_action = Keyboard()
    text_file = File('message.txt')
    process = Process(mouse_action, keyboard_action, text_file)
    process.load_json()
    process.start()


if __name__ == "__main__":
    main()
