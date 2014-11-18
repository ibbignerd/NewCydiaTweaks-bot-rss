import sqlite3

import praw
import time
import feedparser
import os
import urlparse

#What lies ahead is probably broken
def login():
    print 'Connecting'
    r = praw.Reddit(user_agent='newcydia tweaks rss bot')
    print 'Starting to log in!'
    sub = 'newcydiatweaks'
    password = ''
    r.login('newcydiatweaks', password)
    print 'Completed log in!'

#parses rss feed
def parseFeed():
    feed = 'http://modmyi.com/cydia/rsscat.php?category=Tweaks'
    done = []
    f = feedparser.parse(feed)
    link = f.entries[0]['link']
    title = f['entries'][0]['title']
parseFeed()

# This will get the cydia.saurik.com link
def linkConvert():
    newLink = link.split('/')
    conLink = newLink[4]
    saurikLink = 'http://cydia.saurik.com/package/' + conLink
linkConvert()
def post():
    r.submit(sub, title, url=saurikLink)
    link = f.entries[0]['link'] # N - should be using the cydia.saurik.com links using the bundle id
    linkConvert()
    title = f['entries'][0]['title'] # N - Title needs to be parsed for better formatting
    print saurikLink
    #r.submit(sub, title, url=saurikLink)
    print 'Submitted {0}'.format(title)

post()   

# N - All code before this comment will only be executed once.
# N - Migrate to using functions to make your code cleaner - def functionName(var1):
while True:

        if f.entries[0]['link'] in done:
            pass # N - Because this if statement if in your main function, if you use "pass", it will just skip everything including the wait.else:
            try:
                
                link = f.entries[0]['link'] # N - should be using the cydia.saurik.com links using the bundle id
                linkConvert()
                title = f['entries'][0]['title'] # N - Title needs to be parsed for better formatting
                print saurikLink
                r.submit(sub, title, url=saurikLink)
                print 'Submitted {0}'.format(title)

                done.append(link) #This is annoying because it will go if the program is quit. Not to self: maintain a list of post titles in a text file - db thingy
                # N - Look into using sqlite3 for saving your files. its really easy to use and is better on your resources
            except Exception, e:
                print e
        # N - This setup makes it so that you are only checking one entry every 30 seconds. I guess that can be okay, but it's possible that the feed gets more than one entry in a 30 second span and now you are behind. The only way you would be able to catch up is if there is a period of no new entries in the feed. I would suggest looping through all the feed and checking it against the saved links.
        time.sleep()


    
