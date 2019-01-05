"""

888888b.             8888888 888                       888      d8b                   8888888888               888          888 
888  "88b              888   888                       888      Y8P                   888                      888          888 
888  .88P              888   888                       888                            888                      888          888 
8888888K.  888  888    888   88888b.  888d888  8888b.  88888b.  888 88888b.d88b.      8888888     8888b.   .d88888  .d88b.  888 
888  "Y88b 888  888    888   888 "88b 888P"       "88b 888 "88b 888 888 "888 "88b     888            "88b d88" 888 d8P  Y8b 888 
888    888 888  88     888   888  888 888     .d888888 888  888 888 888  888  888     888        .d888888 888  888 88888888 888 
888   d88P Y88b 888    888   888 d88P 888     888  888 888  888 888 888  888  888     888        888  888 Y88b 888 Y8b.     888 
8888888P"   "Y88888  8888888 88888P"  888     "Y888888 888  888 888 888  888  888     888        "Y888888  "Y88888  "Y8888  888 
                888                                                                                                                    
           Y8b d88P                                                                                                                    
            "Y88P"                                                                                                                     

"""
from ruamel.yaml import YAML 

yaml = YAML()

rawdata = open('config.yml', 'r').read()
data = yaml.load(rawdata)
curly = data['settings']['curly']
functionSpacing = data['settings']['functionSpacing']
filename = data['settings']['inputFile']
output = data['settings']['outputFile']

nlOutputArray = []
ilOutputArray = []

def moveCurlyInline(i):
	global amntRuns
	global ilOutputArray
	with open(filename, "r") as inputFile:
		data = [line.rstrip('\n') for line in inputFile]
		pos = data[i].find('{')
		removeNL = data[i - 1] + data[i][:pos + 1] + '\b\b'
		removeCurly = data[i].rstrip('{')
		data[i] = removeCurly
		ilOutputArray.append(removeNL)
		data[i - 1] = ilOutputArray[amntRuns]
	with open(output, "w") as outputFile:
		for x in range(len(data)):
			if(data[x].count('{') > 0):
				outputFile.write(ilOutputArray[amntRuns])
			else:
				print(data[x])
				outputFile.write(data[x] + '\n')

def moveCurylyNewline(i):
	global amntRuns
	global nlOutputArray
	with open(filename, "r") as inputFile:
		data = [line.rstrip('\n') for line in inputFile]
		pos = data[i].find('{')
		insertNL = data[i][:pos] + '\n{'
		nlOutputArray.append(insertNL)
		data[i] = nlOutputArray[amntRuns]
	with open(output, "w") as outputFile:
		try:
			for x in range(len(data)):
				if(data[x].count('function') > 0):
					outputFile.write(nlOutputArray[amntRuns] + '\n')
				else:
					outputFile.write(data[x] + '\n')
		except:
			print("Error writing the compiled code")

file = open(filename, 'r')

i = 0
lines = []
for line in file.readlines():
	lines.append(line)
	i += 1

amntRuns = 0
for i in range(len(lines)):	
	if curly == 'newline':
		if 'function' not in lines[i]:
			continue
		else:
			moveCurylyNewline(i)
			amntRuns += 1
	elif curly == 'inline':
		if '{' not in lines[i]:
			continue
		else:
			moveCurlyInline(i)
			amntRuns += 1