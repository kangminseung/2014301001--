from bs4 import BeautifulSoup as bs
import csv
import os

path_list = ['C:/Users/Administrator/Desktop/오랑우탄/final_project/경력취준생_QA', 'C:/Users/Administrator/Desktop/오랑우탄/final_project/경력취준생톡방',
             'C:/Users/Administrator/Desktop/오랑우탄/final_project/신입취준생_QA', 'C:/Users/Administrator/Desktop/오랑우탄/final_project/신입취준생톡방',
             'C:/Users/Administrator/Desktop/오랑우탄/final_project/고민', 'C:/Users/Administrator/Desktop/오랑우탄/final_project/스펙']

file_list_1 = os.listdir(path_list[0])  # 경력취준생_QA 폴더 csv 파일
file_list_2 = os.listdir(path_list[1])  # 경력취준생톡방 폴더 csv 파일
file_list_3 = os.listdir(path_list[2])  # 신입취준생_QA 폴더 csv 파일
file_list_4 = os.listdir(path_list[3])  # 신입취준생톡방 폴더 csv 파일
file_list_5 = os.listdir(path_list[4])  # 고민 폴더 csv 파일
file_list_6 = os.listdir(path_list[5])  # 스펙 폴더 csv 파일


path_str = 'C:/Users/Administrator/Desktop/오랑우탄/final_project/Result/'



year = [2014, 2015, 2016, 2017, 2018]

for i in range(5):  # year
    res  = open(path_str+'result'+ str(year[i]) + '.csv', 'w', encoding='cp949')
    for j in range(6):  # path
        f = open(path_list[j] + '/' + file_list_1[i], 'r', encoding='cp949')

        while True:
            line = f.readline()
            if not line: break
            res.write(line)
        f.close()
    res.close()

year_1 = [2015, 2016, 2018]
for i in range(3):  # year
    res  = open(path_str+'result'+ str(year_1[i]) + '.csv', 'a', encoding='cp949')
    f  = open(path_str+'result'+ str(year_1[i]) + '-2.csv', 'r', encoding='cp949')
    while True:
        line = f.readline()
        if not line: break
        res.write(line)
    f.close()
    res.close()
    

words = ['ㅜㅜ', 'ㅠㅠ']
words_count = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]



counting = open(path_str+'result.csv', 'w', encoding='cp949')
                
for i in range(5):
    res  = open(path_str+'result'+ str(year[i]) + '.csv', 'r', encoding='cp949')
    while True:
        line = res.readline()
        if not line: break

        for j in range(len(words)):
            if(line.find(words[j]) != -1):
                words_count[i][j] += 1

    
    res.close()

for [i,j] in words_count:
    counting.write(str(i+j))
    counting.write(',')
counting.write('\n')


counting.close()
