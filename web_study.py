##import webbrowser
##
##url = 'http://localhost:6006'
##
##webbrowser.open(url)


##import os
##
##os.system('explorer http://blindfish.tistory.com')
##
##
##import webbrowser
##url = "http://localhost:6006"
##webbrowser.open_new(url)
import webbrowser

url = 'http://localhost:6006/'

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

webbrowser.get(chrome_path).open(url)
