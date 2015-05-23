__author__ = 'Mateusz Jugowiec'

from game_core.manager import Manager

class State:
    def start(self):
        pass

    def stop(self):
        pass

    def resume(self):
        pass

    def pause(self):
        pass

class StateManager(Manager):
    def __init__(self):
        self.stack = []

    def push(self, state):
        if self.stack:
            self.stack[-1].pause()
        state.start()
        self.stack.append(state)
        state.resume()

    def pop(self):
        state = self.stack[-1]
        state.pause()
        self.stack.pop()
        state.stop()
        if self.stack:
            self.stack[-1].resume()
        return state

    def running(self):
        return bool(self.stack)

    def input(self, event):
        if self.stack:
            self.stack[-1].input(event)

    def update(self, event):
        if self.stack:
            self.stack[-1].update(event)

    def display(self, screen):
        if self.stack:
            self.stack[-1].display(screen)

state_manager = StateManager()

class StateSupervisor(Manager):
    def input(self, event):
        state_manager.input(event)

    def display(self, screen):
        state_manager.display(screen)

    def update(self, event):
        state_manager.update(event)

    def running(self):
        return state_manager.running()

