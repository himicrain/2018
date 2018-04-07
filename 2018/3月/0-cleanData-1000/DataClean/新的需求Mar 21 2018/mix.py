#! /usr/bin/env python2
#! coding=utf8
import os
import codecs
import csv
from collections import Counter

Fields =set(['birthday', 'PrimaryFirst','messageid','userid','message','updated_time','nchar','q1','q2','q3','q4','q5','SWL_taken','SWL','gender','age','relationship_status','interested_in','network_size'])
FileName = ''
Fields = set()
UserIds = set()


def loadOriginalFiles(dir):
	global FileName,Fields,UserIds
	allDatas = []
	filesPath = os.listdir(dir)
	for path in filesPath:
		with open(dir + os.sep + path,mode='r') as csv_f:
			reader = csv.DictReader(csv_f)
			Fields.update(set(reader.fieldnames))

			if '' in Fields :
				Fields.pop('')


			file_data = {}
			for line in reader:
				id = line['userid']
				UserIds.add(id)
				line.pop('userid')
				file_data[id] = line
			
			
			allDatas.append(file_data)
				
	#print UserIds

	if UserIds == ' ':
		print '--------------------------------------'
	
	
	return allDatas

def mix(allDatas):
	with open('./mix.csv','w') as csv_f:
		writer = csv.DictWriter(csv_f, fieldnames=Fields)
		writer.writeheader()
		for id in list(UserIds):
			temp = {}
			flag  = 1
			for part in allDatas:
				try:
					t = part[id]
				except :
					flag = 0
					break
				temp.update(t)
			if flag == 0:
				continue
			temp.update({'userid':id})
			writer.writerow(temp)

		  
		  
if __name__ == "__main__":
	all = loadOriginalFiles('./OriginalFiles')
	mix(all)


