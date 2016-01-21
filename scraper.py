# 21st AM
# import brings in a library
import scraperwiki
import lxml.html
#
html = scraperwiki.scrape("http://uk.soccerway.com/teams/netherlands/fortuna-sittard/")
# if you didn't 'print html' you could still get the results you just wouldn't be able to see it.  We are using scraperwiki library for the function scrape and performing it on the soccerway webpage
print html
#
# The line below is us using the function fromstring for the lxml library on our variable html.  It turns it from html into a language that cssselect can use. [# Find something on the page using css selectors]
root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']") - original text but replaced by us with the line below
# the line below is us using cssselect on variable root to grab the table cell i.e. 'td' and put in variable 'tds'
tds = root.cssselect('td')
#
#
#
#
#
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
