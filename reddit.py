import sqlite3

import praw
import time
import feedparser
import os
import urlparse

#These are your variables that don't change between restarting the program
feed = 'http://modmyi.com/cydia/rsscat.php?category=Tweaks'
done = []
# Things that only need to be done once don't need to be in a function

print 'Connecting'
r = praw.Reddit(user_agent='newcydia tweaks rss bot by /u/') #put your username here to make it more unique
print 'Starting to log in!'
sub = 'newcydiatweaks'
password = ''
r.login('newcydiatweaks', password)
print 'Completed log in!'

sql = sqlite3.connect('sql.db')
log.info('Loaded SQL Database')
cur = sql.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS submitted(ID TEXT)')
sql.commit()

def parseFeed():
    f = feedparser.parse(feed)
    for post in f.entries:
        bundleid = f.link.replace('http://modmyi.com/cydia/', '')

        cur.execute('SELECT * FROM submitted WHERE ID=?', [bundleid])
        if not cur.fetchone():
            tweakName = f.title.replace('Tweaks: ', '')
            link = 'http://cydia.saurik.com/package/' + bundleid
            desc = f.description



            cur.execute("INSERT INTO submitted VALUES(?)", bundleid)
            sql.commit()

while True:
    parseFeed()
    time.sleep(120)
