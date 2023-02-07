import time
from pynput.mouse import Controller
import tkinter


class Move:
    def __init__(self, destination):
        # coordinates of "Pliki" folder shortcut
        self.destination = destination
        self.mouse = Controller()
        self.root = tkinter.Tk()

    def screen_size(self):
        self.root.withdraw()
        width, height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        return width, height

    def move_mouse(self):

        screen_size = self.screen_size()
        actual_position = self.mouse.position
        print(f'actual position{actual_position}')
        print(f'destination position {self.destination}')
        print(f'screen size{screen_size}')
        step = []
        for actual, destination, size in zip(actual_position, self.destination, screen_size):
            print(actual - destination)

        # while True:
        #     step_x, step_y = step
        #     print(step_x, step_y)
        #     self.mouse.move(step_x, step_y)
        #     actual_position = self.mouse.position
        #     print(actual_position)
        #     time.sleep(0.005)
        #     for destination, actual in zip(self.destination, actual_position):
        #         if destination == actual:
        #             print(self.mouse.position)
        #             break



move = Move(destination=(900, 500))

move.move_mouse()








