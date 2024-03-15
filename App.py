from Controller import Controller
from View import View


class App:
    def __init__(self):
        self.controller = Controller()
        self.view = View(self.controller)
        self.controller.set_view(self.view)

    def main(self):
        self.view.main()


if __name__ == "__main__":
    app = App()
    app.main()
