#! /usr/bin/env python3
#! coding=utf8
import os
import codecs
import csv
from collections import Counter

Fields = []
FileName = ''

def loadOriginalFiles(dir):
    global FileName,Fields
    allDatas = []
    filesPath = os.listdir(dir)
    for path in filesPath:
        FileName = FileName + (path.split('.'))[0] + ' and '

        f = open(dir + os.sep + path,mode='r')
        csv_f = csv.reader(f)

        tempDict = {}
        Fields = next(csv_f)

        for line in csv_f:
            id = line[0].strip()
            if id not in tempDict.keys():
                tempDict[id] = [line]
            else:
                tempDict[id].append(line)

        allDatas.append(tempDict)
        tempDict = {}

    FileName = FileName[:-5] + '.csv'
    print FileName

    return allDatas



def statistic(allDatas):
    leng = len(allDatas)

    ids = []

    for file in allDatas:
        for k,v in file.items():
            ids.append(k)



    temp_statistic = Counter(ids)

    fitIds = []

    for id,v in temp_statistic.items():
        if v == leng:
            fitIds.append(id)

    return fitIds


def statisticByFitIds(allDatas,fitids):
    global FileName,Fields
    f = open(FileName,'w')
    wr = csv.writer(f)
    wr.writerow(Fields)

    for id  in fitids:
        for file in allDatas:
            temp = file[id]
            for line in temp:
                wr.writerow(line)

    f.close()



if __name__ == '__main__':
    '''
    把所有的原始的文件放在original文件夹下，就是把三个文件放在original csvs文件夹下
    '''

    all = loadOriginalFiles('./original_csvs')

    fitids = statistic(all)

    statisticByFitIds(all,fitids)


