# 21st AM
import scraperwiki
import lxml.html
# import brings in a library
#
# # Read in a page
html = scraperwiki.scrape("http://uk.soccerway.com/teams/netherlands/fortuna-sittard/")
print html
# if you didn't 'print html' you could still get the results you just wouldn't be able to see it
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']") - original text but replaced by us with the line below 
tds = root.cssselect('td')
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
