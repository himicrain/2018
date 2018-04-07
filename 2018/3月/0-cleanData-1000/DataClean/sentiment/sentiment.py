#!/usr/bin/env python2
# coding=utf-8

from textblob import TextBlob
import os
import csv


Statistic = {'Nutral': 0, 'Positive': 0, 'Negative': 0}

def statistic_sentiment(Dir,file):
	global Statistic
	i = 0


	with open(file.split(".")[0] + "_res.csv","w") as wf:
		wr = csv.writer(wf)
		with open(Dir+os.sep+file,'r+') as f:
			reader = csv.reader(f)
			Fields = next(reader)
			index = Fields.index("message")
			Fields.append("score")
			wr.writerow(["userid","messageid","message","score"])
			for datas in reader:
				line = datas[index].strip()
				line = line.decode('utf-8')
				p = TextBlob(line)
				pro,sub = p.sentiment
				datas.append(str(pro))
				
				new_data = []
				for x in ["userid","messageid","message","score"]:
					new_data.append(datas[Fields.index(x)])
				wr.writerow(new_data)
				if pro < 0 :
					Statistic['Negative'] += 1
				elif pro == 0:
					Statistic['Nutral'] += 1
				else:
					Statistic['Positive'] += 1
				print i, pro
				i += 1



if "__main__" == __name__:
	Dir = './csvs'
	
	dirs = os.listdir(Dir)
	for d in dirs:
		statistic_sentiment(Dir, d)
	print Statistic
	print "over "
