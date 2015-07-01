file=open("abc.txt","r")
file_contents=file.read()
file_contents=file_contents.split()
x=[]
for line in file_contents:
	x.append(line)
file.close
all_integers = []
all_strings = []
for item in x:
	try:
		value = int(item)
		all_integers.append(value)
	except ValueError:
		all_strings.append(item)
print (all_integers)
print (all_strings)
length=len(all_integers)
for i in range(length):
    for j in range(length-1):
        if all_integers[j] > all_integers[j+1]:
           all_integers[j],all_integers[j+1]=all_integers[j+1],all_integers[j]
print(all_integers)
all_strings.sort()
print(all_strings)
f=open("def.txt","w")
for i in range(max(len(all_integers),len(all_strings))):
	if len(all_integers)>i and len(all_strings)>i:             
		f.write(str(all_integers[i])+"\t"+all_strings[i]+"\n")
	elif len(all_integers)<=i and len(all_strings)>i:
		f.write( "\t"+all_strings[i]+"\n")
	else:
		f.write( str(all_integers[i])+"\t"+"\n")
f.close()



