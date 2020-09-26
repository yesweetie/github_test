import os

def alter(file, old_str, new_str):
	with open(file, 'r',  encoding='utf-8') as f1, open('%s.sql' % file, 'w', encoding='utf-8') as f2:
		for line in f1:
			f2.write(line)	
			if old_str in line:
				line=line.replace(old_str, new_str)
				f2.write(line)	

	new_file=file.replace(old_str, new_str)
	os.rename('%s.sql' % file, new_file) 


alter(r'HBAP_Create.sql', 'HBAP', 'HASE')



import os

path = os.getcwd()
files = os.listdir(path)

for file in files:
	if 'HBAP' in file:
		with open(file, 'r',  encoding='utf-8') as f1, open('%s.sql' % file, 'w', encoding='utf-8') as f2:
			for line in f1:
				
				line=line.replace('HBAP', 'HASE')
				f2.write(line)	

		new_file=file.replace('HBAP', 'HASE')
		
		os.rename('%s.sql' % file, new_file) 



import os
import sys

def operate(old_str, new_str):
	path = os.getcwd()
	files = os.listdir(path)

	for file in files:
		if old_str in file:
			with open(file, 'r',  encoding='utf-8') as f1, open('%s.sql' % file, 'w', encoding='utf-8') as f2:
				for line in f1:
					
					line=line.replace(old_str, new_str)
					f2.write(line)	

			new_file=file.replace(old_str, new_str)
			
			os.rename('%s.sql' % file, new_file) 

if __name__ == '__main__':
	old_str, new_str = sys.argv[1], sys.argv[2]
	operate(old_str, new_str)








