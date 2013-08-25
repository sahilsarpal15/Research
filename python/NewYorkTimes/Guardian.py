# !/usr/bin/env python
# -*- coding: UTF-8  -*-
# Scraping The Guardian using Python
# 20120421@ Canberra
# chengjun wang


import json
import urllib2

'''
 http://content.guardianapis.com/search?q=occupy+wall+street&from-date=2011-09-01&to-date=2012-02-14&page=2
 &page-size=3&format=json&show-fields=all&use-date=newspaper-edition&api-key=mudfuj8durd693pwm3g33gzq
'''

'''step 1: input query information'''
apiUrl='http://content.guardianapis.com/search?q=occupy+wall+street' # set the query word here
apiDate='from-date=2011-09-01&to-date=2011-10-09'                     # set the date here
apiPage='page=2'      # set the page
apiNum=10             # set the number of articles in one page
apiPageSize=''.join(['page-size=',str(apiNum)])                
fields='format=json&show-fields=all&use-date=newspaper-edition'
key='api-key=mudfuj8durd693pwm3g33gzq'  # input your key here

'''step 2: get the number of offset/pages'''
link=[apiUrl, apiDate, apiPage, apiPageSize, fields, key]
ReqUrl='&'.join(link)
jstr = urllib2.urlopen(ReqUrl).read()  # t = jstr.strip('()')
ts = json.loads( jstr )
number=ts['response']['total'] #  the number of queries  # query=ts['tokens'] # result=ts['results']
print number
seq=range(number/(apiNum-1) )  # this is not a good way
print seq

'''step 3: crawl the data and dump into csv'''
import csv
addressForSavingData= "D:/Research/Dropbox/tweets/wapor_assessing online opinion/News coverage of ows/guardian2.csv"    
file = open(addressForSavingData,'wb') # save to csv file
for i in seq:
    nums=str(i+1)
    apiPages=''.join(['page=', nums]) # I made error here, and print is a good way to test
    links= [apiUrl, apiDate, apiPages, apiPageSize, fields, key]
    ReqUrls='&'.join(links)
    print "*_____________*", ReqUrls
    jstrs = urllib2.urlopen(ReqUrls).read()
    t = jstrs.strip('()')
    tss= json.loads( t )  
    result = tss['response']['results']
    for ob in result:
        title=ob['webTitle'].encode('utf-8')  # body=ob['body']   # body,url,title,date,des_facet,desk_facet,byline
        print title
        section=ob["sectionName"].encode('utf-8')
        url=ob['webUrl']
        date=ob['fields']['newspaperEditionDate'] # date=ob['webPublicationDate']  # byline=ob['fields']['byline'] 
        w = csv.writer(file,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        w.writerow((date, title, section, url)) # write it out		
file.close()
pass



