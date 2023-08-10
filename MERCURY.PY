import UIElements
import Parser
import ModuleManager
from time import sleep

class Mercury:
    def __init__(self) -> None:
        self.ui = UIElements.UIElements()
        self.parse = Parser.Parser()
        self.manager = ModuleManager.ModuleManager(self.ui)

    def initialize(self):
        print('Checking file integrity...')
        #chkint
        print('Initializing UI...')
        self.ui.initialize()
        sleep(1)
        self.ui.clearscreen()
        self.ui.view_mercury_logo()

    def mercuryterm(self):
        while True:
            parsedata = self.parse.parser(self.ui.getInput())
            if not self.manager.findmodule(parsedata):
                exit()

if __name__ == '__main__':
    mercury = Mercury()
    mercury.initialize()
    mercury.mercuryterm()