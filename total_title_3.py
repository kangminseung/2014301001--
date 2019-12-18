from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import os, sys
import pandas as pd
import csv
from itertools import count


f_2018 = open('C:/Users/Administrator/Desktop/오랑우탄/final_project/신입취준생톡방/2018.csv', 'w', encoding='cp949', newline='')
f_2017 = open('C:/Users/Administrator/Desktop/오랑우탄/final_project/신입취준생톡방/2017.csv', 'w', encoding='cp949', newline='')
f_2016 = open('C:/Users/Administrator/Desktop/오랑우탄/final_project/신입취준생톡방/2016.csv', 'w', encoding='cp949', newline='')
f_2015 = open('C:/Users/Administrator/Desktop/오랑우탄/final_project/신입취준생톡방/2015.csv', 'w', encoding='cp949', newline='')
f_2014 = open('C:/Users/Administrator/Desktop/오랑우탄/final_project/신입취준생톡방/2014.csv', 'w', encoding='cp949', newline='')

driver = webdriver.Chrome()
time.sleep(2)

#================================================================

totalCount = 1

for page_idx in range(39):
    if(((page_idx+1)%10) == 1):
        totalCount += 150
    base_url = 'https://cafe.naver.com/breakjobnaver'

    url = '/ArticleList.nhn?search.clubid=20395059&search.menuid=1041&search.boardtype=L&search.totalCount=%d&search.page=%d' % (totalCount, page_idx+1)
    driver.get(base_url + url)

    driver.switch_to.frame('cafe_main')

    soup = bs(driver.page_source, 'html.parser')

    div = soup.find('div', attrs={'class':'article-board m-tcol-c'})
    tbody = div.find('tbody')

    tr_table = tbody.findAll('tr')
    for tr in tr_table:
        date = tr.find('td', attrs={'class':'view-count m-tcol-c'})
        
        if(str(date).find('2018') != -1):
            article_title = tr.find('span', attrs={'class':'aaa'})
            article_title = article_title.get_text().strip().replace(' ', '')
            d = article_title.split()

            print(d[0])
            
            f_2018.write(d[0])
            f_2018.write('\n')

        elif(str(date).find('2017') != -1):
            article_title = tr.find('span', attrs={'class':'aaa'})
            article_title = article_title.get_text().strip().replace(' ', '')
            d = article_title.split()

            print(d[0])
            
            f_2017.write(d[0])
            f_2017.write('\n')
            
        elif(str(date).find('2016') != -1):
            article_title = tr.find('span', attrs={'class':'aaa'})
            article_title = article_title.get_text().strip().replace(' ', '')
            d = article_title.split()

            print(d[0])
            
            f_2016.write(d[0])
            f_2016.write('\n')
            
        elif(str(date).find('2015') != -1):
            article_title = tr.find('span', attrs={'class':'aaa'})
            article_title = article_title.get_text().strip().replace(' ', '')
            d = article_title.split()

            print(d[0])
            
            f_2015.write(d[0])
            f_2015.write('\n')
            
        elif(str(date).find('2014') != -1):
            article_title = tr.find('span', attrs={'class':'aaa'})
            article_title = article_title.get_text().strip().replace(' ', '')
            d = article_title.split()

            print(d[0])
            
            f_2014.write(d[0])
            f_2014.write('\n')
        else:
            continue

#================================================================

driver.close()
f_2018.close()
f_2017.close()
f_2016.close()
f_2015.close()
f_2014.close()


