# 21st AM
# import brings in a library
import scraperwiki
import lxml.html
#
html = scraperwiki.scrape("http://uk.soccerway.com/teams/netherlands/fortuna-sittard/")
# if you don't 'print html' you  still get the results you just won't see the result.  We are using scraperwiki library for the function scrape and performing it on the soccerway webpage.
#
# The line below uses the function fromstring from the lxml library on our variable html.  It turns it from html into a language that cssselect can use.
root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']") - original text but replaced by us with the line 2 below
# the line below uses cssselect on variable root to grab the table cell i.e. 'td' and put in variable 'tds'.
tds = root.cssselect('td')
#
#The function fromstring changed it so that the lxml library could read it so we  need to change it back to something that we can read.
# for td in tds:
#   print lxml.html.tostring(td)
#   print td.text
# the above can be adpated as below so that we know where to look out for the bit you are interested in among the result.
# for td in tds:
#   print "???" - it is in his slide but I did no manage to finish it
#   print lxml.html.tostring(td)
#   print "HTML text"
#   print td.text
#
# A dictionary is a series of pairs of data e.g. Age: 25 and they are in curly brackets e.g. {Name: Mo; Height: 178}
#
#for td in tds:
#  record = {"cell" : td.text}
#  print record
#  scraperwiki.sqlite.save(["cell"], record)
# The above contained null records which caused it a problem but we can change it to allow for null values as below
indexno = 0
for td in tds:
  indexno = indexno + 1
  record = {"cell" : td.text, "index" : indexno}
  print record
  scraperwiki.sqlite.save(["index"], record)
#
# You don't have to do things with the ScraperWiki and lxml libraries.  You can use whatever libraries you want: 
# https://morph.io/documentation/python All that matters is that your final data is written to an SQLite database called 
# "data.sqlite" in the current working directory which has at least a table called "data".
