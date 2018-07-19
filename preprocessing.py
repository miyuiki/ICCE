import pandas as pd
import numpy as np
import csv

class Student():
	"""docstring for Student"""
	def __init__(self, name):
		super(Student, self).__init__()
		self.name = name
	PAGE_JUMP = 0
	marker = 0
	memo = 0
	bookmark = 0
	nextc = 0
	prevc = 0
	read_page = 0
		

if __name__ == '__main__':
	student_num = 0
	student_id = []
	student_set = []
	student = []
	data = pd.read_csv('data1_clickstream.csv',sep = ',')
	for row in range(0,data.shape[0]):
		student_id.append(data['userid'][row])
	for i in student_id:
		if i not in student_set:
			student_set.append(i)
	for uid in student_set:
		student.append(Student(uid))
	
	for s in range(0,len(student_set)):
		for i in range(0, len(student_id)):
			if(student[s].name == student_id[i] and data['operationname'][i] == 'PAGE_JUMP' ):
				student[s].PAGE_JUMP += 1
			elif(student[s].name == student_id[i] and data['operationname'][i] == 'ADD MARKER' ):
				student[s].marker += 1
			elif(student[s].name == student_id[i] and data['operationname'][i] == 'ADD BOOKMARK' ):
				student[s].bookmark += 1
			elif(student[s].name == student_id[i] and data['operationname'][i] == 'ADD MEMO' ):
				student[s].memo += 1
			elif(student[s].name == student_id[i] and data['operationname'][i] == 'NEXT' ):
				student[s].nextc += 1
			elif(student[s].name == student_id[i] and data['operationname'][i] == 'NEXT' ):
				student[s].prevc += 1
		student[s].read_page = student[s].nextc - student[s].prevc + 1
	# for s in range(0,len(student_set)):
	# 	print("{} PAGE_JUMP:{} MARKERC:{} BOOKMARKC:{} MEMOC:{} read_page:{}"
	# 		.format(student[s].name,student[s].PAGE_JUMP,student[s].marker
	# 		,student[s].bookmark,student[s].memo,student[s].read_page))
	with open('features.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['userid','PageJumpC','MarkerC','bookmarkC',' MemoC','Readpages'])
		for s in range(0,len(student_set)):
			writer.writerow([student[s].name,student[s].PAGE_JUMP,student[s].marker,
				student[s].bookmark,student[s].memo,student[s].read_page])





	
		