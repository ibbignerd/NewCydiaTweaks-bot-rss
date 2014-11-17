import praw
import time
import feedparser
import os

#What lies ahead is probably broken
print 'Connecting' 
r = praw.Reddit(user_agent='newcydia tweaks rss bot')
print 'Starting to log in!' 
r.login('newcydiatweaks', 'yosemite') 
print 'Completed log in!'
feed = 'http://modmyi.com/cydia/rsscat.php?category=Tweaks'
sub = 'newcydiatweaks'
done = []

f = feedparser.parse(feed)

while True:
    if d.entries[0]['link'] in done:
        pass

    else:
        try:
            link = f.entries[0]['link'] 
            title = f['entries'][0]['title'] 
			
			
            r.submit(sub, title, url=link).distinguish()
            print 'Submitted {0}'.format(title)
			
            done.append(link) #This is annoying because it will go if the program is quit. Not to self: maintain a list of post titles in a text file - db thingy
        except Exception, e:
            print e
    #print "i have done these links"
    #print done
    print e
    time.sleep(30)
