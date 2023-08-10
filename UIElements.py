import re

class UIElements:
    
    def __init__(self) -> None:
        self.retcode = ''
        self.modcol = ''
        self.errcol = ''
        self.mercury = ''
        self.colorstat = False

    def initialize(self):
        params = self.__readconfig()
        if not params:
            print('[-] UI Initialization failed !!')
            print('[*] Reverting to normal state')
            return False
        if self.__setcols(params):
            print('[+] UI Initialization success !!')
            return True
        
    def __setcols(self, params: dict) -> bool:
        try:
            if params['TERMINAL_COLOR'] == 'TRUE':
                self.mercury = '\x1b[38;2;' + params['MERCURY_FOREGROUND_COLOR'] + 'm' + '\x1b[48;2;' + params['MERCURY_BACKGROUND_COLOR'] + 'm'
                self.retcode = '\x1b[' + params['TERMINAL_RETURN_CODE']
                self.modcol = '\x1b[38;2;' + params['MODULE_FOREGROUND_COLOR'] + 'm' + '\x1b[48;2;' + params['MODULE_BACKGROUND_COLOR'] + 'm'
                self.errcol = '\x1b[38;2;' + params['ERROR_FOREGROUNG_COLOR'] + 'm' + '\x1b[48;2;' + params['ERROR_BACKGROUNG_COLOR'] + 'm'
                self.colorstat = True
                return True
            elif params['TERMINAL_COLOR'] == 'FALSE':
                self.colorstat = False
                return True
            else:
                return False
        except:
            return False
            
    def __readconfig(self) -> dict:
        try:
            params = dict()
            config = open('CONFIG\\UICONFIG.MERC','rt')
            while True:
                line = config.readline()
                if not line:
                    config.close()
                    return params
                if line == '\n':
                    continue
                if not line.startswith('#'):
                    line = line.split('=')
                    params[line[0].strip()] = line[1].strip()
        except:
            return None
    
    def view_mercury_logo(self):
        print("██████ ██  ██ ██▀▀█   █████████████████████████████████████████████ ",)
        print("  ██   ██▄▄██ ██▄▄                                                  ",)
        print("  ██   ██▀▀██ ██▀▀              VERSION : 1.00 BETA                 ",)
        print("  ██   ██  ██ ██▄▄█                                                 ",)
        print("            ▄███  ▄███████▄ ▄███ ██████ ██  ██ ▄█████▄   ▄████████▀ ",)
        print("           ▄█▀██ ██ ██      ██  ▀██  ██ ██  ██ ██  █ ██  ██▀        ",)
        print("          ▄█▀  ███▀ ████    ██   ██     ██  ██ ██    ▀████▀         ",)
        print("         ▄█▀        ██      ██   ██  ██ ██  ██ ██      ██           ",)
        print("▄█████████▀         ██████▀ ██   ██████ ██████ ██      ██           ",)
        print("                         ███ █ ████ █████ ███████ █████ ▄██████████ ",)
        print("  BY : THE_JOULE_THIEF   █████ ██   ██ ██    ██   ██▄   ██    ██    ",)
        print("                         ██    ██   ██ ██ ██ ██   ██▀   ██    ██    ",)
        print("███████████████████████  ██    █▀   █████ █████   █████ ▀███▀ ██    ",)
        
    def printerr(self, module: str, err_code: str, error_statement: str) -> None:
        print(self.modcol + ' ' + module + ' ' + self.errcol + ' ERR ' + err_code + ' ' + self.retcode + ' ' +  error_statement)
            
    ### INCOMPLETE MODULE
    def printmsg(self, module: str, message: str) -> None:
        print(module + ' ' + message)

    def iscolor(self) -> bool:
        return self.colorstat

    def print(self, message: str) -> None:
        print(message)

    def print_end_exp(self, message, endchar)-> None:
        print(message, end = endchar)

    def input(self):
        return input()

    def input_message(self,message: str):
        return input(message)

    def getInput(self) -> str:
        return input('\n' + self.mercury + ' MERCURY █' + self.retcode + ' ')
    
    def clearscreen(self):
        from os import system, name
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
    #INCOMPLETE FUNCTION
    def printmd(self, path: str) -> None:
        try:
            readme = open(path,'rt')
            while True:
                line = readme.readline()
                if not line:
                    readme.close()
                    return
                
                if line.startswith('#'):
                    line = line.replace('# ','\x1b[1;38;2;255;0;0m')

                bold = re.findall(r'\*\*[0-9A-Za-z]+\*\*',line)
                italic = re.findall(r'\_[0-9A-Za-z]+\_',line)
                strike = re.findall(r'\~\~[0-9A-Za-z]+\~\~',line)

                try:
                    #BOLD CODE
                    ansi_replacement = []
                    for i in bold:
                        i = i.replace('**','\x1b[1;38;2;255;255;0m',1)
                        i = i.replace('**','\x1b[0m',1)
                        ansi_replacement.append(i)

                    for i in range(len(bold)):
                        line = line.replace(bold[i], ansi_replacement[i])

                    #ITALIC
                    ansi_replacement = []
                    for i in italic:
                        i = i.replace('_','\x1b[3m',1)
                        i = i.replace('_','\x1b[0m',1)
                        ansi_replacement.append(i)

                    for i in range(len(italic)):
                        line = line.replace(italic[i], ansi_replacement[i])

                    #STRIKE
                    ansi_replacement = []
                    for i in strike:
                        i = i.replace('~~','\x1b[9m',1)
                        i = i.replace('~~','\x1b[0m',1)
                        ansi_replacement.append(i)

                    for i in range(len(strike)):
                        line = line.replace(strike[i], ansi_replacement[i])

                except:
                    pass

                print(line, end=self.retcode)
        except:
            self.printerr('UIElements', 'UI000', 'No markdown found')