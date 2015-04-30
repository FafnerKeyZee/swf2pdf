import os
import re
import subprocess
import sys

words=[]
listfile=[]
cmd = subprocess.Popen("swfdump "+sys.argv[1],shell=True, stdout=subprocess.PIPE)

for line in cmd.stdout :
	if "SHOWFRAME" in line.decode() :
		match = re.search(r'(SHOWFRAME )\d+', line.decode())
		if match :
			words.append(match.group(0).split(" ")[1])

for word in words :
	p=subprocess.Popen("swfrender -r 240 -p "+word+" "+sys.argv[1]+" -o tmp_"+word, shell=True)
	p.wait()
	p=subprocess.Popen("convert tmp_"+word+" tmp_"+word+".pdf", shell=True)
	p.wait()
	p=subprocess.Popen("rm tmp_"+word,shell=True)
	p.wait()
	listfile.append("tmp_"+word+".pdf")

p=subprocess.Popen("pdfunite "+" ".join(listfile)+" "+sys.argv[1]+".pdf", shell=True)
p.wait()
p=subprocess.Popen("rm "+" ".join(listfile), shell=True)
p.wait
print ("Done")
