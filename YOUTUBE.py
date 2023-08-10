from pytube import Playlist
from pytube import YouTube

class YOUTUBE:

    def __init__(self, ui) -> None:
        self.ui = ui

    def parse(self, args: list) -> bool:
        options = self.__optparser(args)
        
        if options:

            if options['Type'] == 'File':
                return self.__Fileparser(options['File'])
            
            elif options['Type'] == 'URL':
                return self.__URLparser(options['URL'])

            else:
                self.ui.printerr('YouTube', 'YT001', 'Undefined type')
                return False
                        
        else:
            self.ui.printerr('YouTube', 'YT000', 'Undefined parameter type')
            return False

    def __Fileparser(self, filename: str) -> bool:
        try:
            file = open(filename, 'r')
            while True:
                URL = file.readline()
                if not URL:
                    break
                self.__URLparser(URL)           
            file.close()
            return True
        except:
            self.ui.printerr('YouTube', 'YT004', 'Fileparser exception')
            return False

    def __URLparser(self, URL: str) -> bool:
        if ('youtube' in URL) or ('yout.be' in URL):
            
            if ('list=' in URL):
                self.playlist(URL)
            
            elif ('watch?v=' in URL):
                self.video_downloader(URL)
            
            else:
                self.ui.print(URL)
                self.ui.printerr('YouTube', 'YT003', 'URL type mismatch')
                return False
        
        else:
            self.ui.print(URL)
            self.ui.printerr('YouTube', 'YT002', 'Invalid URL')
            return False

    def __optparser(self, args: list) -> dict:
        
        optdict = dict() 
        i = 0
        
        while i < len(args):
            
            if (args[i] == "-u") or (args[i] == "--url"):
                i += 1
                optdict["Type"] = "URL"
                optdict["URL"] = args[i]
            
            elif (args[i] == "-f") or (args[i] == "--file"):
                i += 1
                optdict["Type"] = "File"
                optdict["File"] = args[i]
            
            elif (args[i] == "-v") or (args[i] == "--video"):
                optdict["Video"] = True
            
            elif (args[i] == "-a") or (args[i] == "--audio"):
                optdict["Audio"] = True
            
            elif (args[i] == "-fe") or (args[i] == "--file-extension"):
                i += 1
                optdict["File Extension"] = args[i]
            
            elif (args[i] == "-o") or (args[i] == "--output"):
                i += 1
                optdict["Output"] = args[i]
            
            elif (args[i] == "-mt") or (args[i] == "--mime_type"):
                i += 1
                optdict["mime_type"] = args[i]
            
            elif (args[i] == "-abr") or (args[i] == "--abr"):
                i += 1
                optdict["abr"] = args[i]
            
            elif (args[i] == "-ac") or (args[i] == "--acodec"):
                i += 1
                optdict["acodec"] = args[i]
                
            elif (args[i] == "-ob") or (args[i] == "--order-by"):
                i += 1
                optdict["order_by"] = args[i]
            
            elif (args[i] == "-p") or (args[i] == "--progressive"):
                optdict["progressive"] = True
                
            else:
                return None
            
            i += 1
        return optdict

    def playlist(self, playlist_url: str) -> bool:
        p = Playlist(playlist_url)
        self.ui.print('\nTitle: '+ str(p.title))
        self.ui.print('Playlist contains ' + str(len(p.video_urls)) + ' videos\n')
        
        i = 0
        
        try:
            while i < len(p.video_urls):
                
                self.ui.print('[*] Downloading file '+ str(i+1) + '/' + str(len(p.video_urls)))
                try:
                    self.video_downloader(p.video_urls[i])
                except:
                    pass
                
                i += 1
                
            return True
        except:
            return False
            
    def video_downloader(self, url: str) -> bool:
        try:
            yt = YouTube(url)
            yt.register_on_progress_callback(self.yt_progress)
            self.ui.print('\nFilename: ' + str(yt.title))
            self.ui.print('URL: '+ str(url))

            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

            self.ui.print('\nDownload Complete')
            
            return True
        
        except:
            self.ui.printerr('YouTube', 'YT005', 'Unable to download \n')
            return False
    
    def yt_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining 
        
        perc = round((bytes_downloaded * 50) / (total_size))

        self.ui.print_end_exp('Downloading\t' + str(round(bytes_downloaded*100/total_size, 2)) + '%\t', endchar = '')

        for i in range(0,50):
            if i < perc:
                self.ui.print_end_exp('\x1b[38;2;242;75;75m▬', endchar = '')
            else:
                self.ui.print_end_exp('\x1b[38;2;115;14;41m▬', endchar = '')

        self.ui.print_end_exp('\x1b[0m', endchar = '\r')