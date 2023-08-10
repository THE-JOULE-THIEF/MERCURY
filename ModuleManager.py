class ModuleManager:
    
    def __init__(self, ui) -> None:
        self.ui = ui

    def findmodule(self, parsedata: dict) -> bool:
        if parsedata['module'] == 'remove-module':
            return True

        elif parsedata['module'] == 'add-module':
            return True

        elif parsedata['module'] == 'man':
            self.man(parsedata['args'])
            return True

        elif parsedata['module'] == 'exit':
            return False

        ###YOUTUBE###
        elif parsedata['module'] == 'youtube':
            try:
                import YOUTUBE
                null = YOUTUBE.YOUTUBE(self.ui).parse(parsedata['args'])
            except:
                self.ui.printerr('ModuleManager', 'MM001', 'Unexpected module error encountered ')
            return True
        ###ENDYOUTUBE###

        ##NEW_MODULE_FILES_START_HERE##

        else:
            self.ui.printerr('ModuleManager', 'MM000', 'No compatible modules found')
            return True
        
    def removemodule(self,args) -> None:
        pass
    
    def addmodule(self,args) -> None:
        pass

    def man(self,args) -> None:
        try:
            path = 'README\\'+args[0].upper()+'.md'
            self.ui.printmd(path)
        except:
            try:
                if not args:
                    self.ui.printerr('ModuleManager', 'MM002', 'Expected module name')
                    self.man([self.ui.input_message('[!] Enter module name:')])
            except:
                self.ui.printerr('ModuleManager', 'MM003', 'Unexpected error encountered')