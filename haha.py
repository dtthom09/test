import webbrowser   #module allows you to open webpages via python code
import time         #allows you to delay while loop so not consistently opening pages
import random

while True:     #run until kill via terminal
    websites = random.choice(['google.com', 'youtube.com', 'bing.com']) #list of websites
    visit = "http://{}".format(websites)    #formats website string.. yes, I did not want to write http multiple times
    webbrowser.open(visit)                  #pass the string to the webbrower open function which will randomly pick a site each time this loops
    seconds = random.randrange(10,30)       #give it a range of seonds from _ to _
    time.sleep(seconds)