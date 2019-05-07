# coding: UTF-8
from threading import Thread
import time


class Elevator:
    current_floor = 1  # текущий этаж лифта
    print(f'Current floor is {current_floor}')
    calls = []  # массив с вызовами лифта
    is_moving = 0  # статус лифта: 0 - не движется, 1 - движется

    def start(self):
        run = Thread(target=self.waiting, name='waiting_thread')
        run.start()

    def waiting(self):  # постоянно проверяет массив с вызовами
        print('waiting')
        while True:
            if len(self.calls) > 0:
                call = self.calls.pop(0)
                if self.current_floor != call[1]:
                    self.move(call[0], call[1])
                else:
                    self.stop()

    def move(self, direction, stage):
        self.is_moving = 1
        print(f'Elevator is moving!')
        while self.current_floor != stage:
            time.sleep(2)
            if self.current_floor < stage:
                self.current_floor += 1
            elif self.current_floor > stage:
                self.current_floor -= 1
            print(self.current_floor)
            i = 0
            for call in self.calls:
                if direction == call[0] and self.current_floor == call[1]:
                    self.calls.pop(i)
                    self.stop()
                i += 1

        self.stop()

    def stop(self):
        print(f'Stopped on #{self.current_floor} floor')
        self.open_doors()
        floor = int(input('Type floor: '))
        if floor < self.current_floor:
            direction = 'down'
        elif floor > self.current_floor:
            direction = 'up'
        else:
            direction = None

        if direction is not None:
            self.call(direction, floor)
        self.close_doors()

    @staticmethod
    def open_doors():
        print('Opening the doors!')
        # time.sleep(5)

    @staticmethod
    def close_doors():
        print('Closing the doors!')

    def call(self, direction, stage):
        print(f'call from {stage}')
        self.calls.append([direction, stage])
        time.sleep(1)


instance = Elevator()
instance.start()
# print('pause')
time.sleep(2)

# while True:
dir = input('Type direction: ')
floor = int(input('Type floor: '))
instance.call(dir, floor)
time.sleep(5)
instance.call('down', 5)


