import os

def remove_text(file_name,text):
	lines=[]
	new_lines=[]
	with open(file_name,'r') as text_file:
		lines=text_file.readlines()
	print (lines)

	for line in lines:
		if text not in line:
			new_lines.append(line)

	with open(file_name,'w') as text_file:
		for line in new_lines: 
		   text_file.write(line)


file_name=os.path.realpath(__file__).split('/')[-1]
#print(file_name)
fileindir=os.listdir('./')
fileindir.remove(file_name)
print(fileindir)

for file in fileindir:
	remove_text(file,"abc")