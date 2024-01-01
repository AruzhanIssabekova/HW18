class Main:
    def __init__(self, text=''):
        self.text = text

    def new_text(self, text_new=''):
        self.text = text_new

    def display(self):
        print(self.text)
class Sub(Main):
    def __init__(self, text='', numeric=0):
        super().__init__(text)
        self.numeric = numeric

    def display(self):
        super().display()
        print(self.numeric)

def info(n):
    return n.display()

base = Main("Hello")

d = Sub("World", 42)

print(info(base), info(d))