#!/usr/bin/env python
""" A Simple python script that reads rss feeds from both Kenyan Standard and Nation Newspapers and presents them on your terminal"""

import feedparser 

#Function that captures RSS feeds from Nation & Standard Kenyan Newspapers 

def rssFeeds():
    standard_local ="https://www.standardmedia.co.ke/rss/kenya.php"
    nation_local="https://www.nation.co.ke/1148-2613630-view-asFeed-iahce3/index.xml"
    feed_standard = feedparser.parse(standard_local, nation_local)
    feed_nation = feedparser.parse(nation_local)
    posts_standard = feed_standard.entries
    posts_nation = feed_nation.entries

    #rss feeds from Standard newspaper
    print ' '
    print 'STANDARD NEWSPAPER RSS FEEDS'
    print '----------------------------'
    for value, post in enumerate(posts_standard, 1):
        print value, post.title +"||" + post.link
    
    #rss feeds from Nation newspaper
    print ' '
    print 'NATION NEWSPAPER RSS FEEDS'
    print '----------------------------'
    for value, post in enumerate(posts_nation, 1):
        print value, post.title + '||' + post.link

rssFeeds()








