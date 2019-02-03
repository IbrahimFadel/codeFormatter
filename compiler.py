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
inputFileName = data['settings']['inputFile']
outputFileName = data['settings']['outputFile']

lines = []

def moveNewLine(i):
	if(lines[i].find('//') == -1):
		pos = lines[i].find('{')
		newline = lines[i][:pos] + '\n' + lines[i][pos:]
		lines[i] = newline
		print(lines[i])
		with open(outputFileName, 'w') as outputFile:
			for x in range(len(lines)):
				outputFile.write(lines[x])

def moveInline(i):
	noNew = lines[i - 1].rstrip('\n')
	noNew = noNew.rstrip('\t')
	newline = noNew + ' ' + lines[i]
	lines[i - 1] = newline
	lines[i] = ''
	print(newline)

	with open(outputFileName, 'w') as outputFile:
		for x in range(len(lines)):
			outputFile.write(lines[x])

with open(inputFileName, 'r') as inputFile:
	for line in inputFile.readlines():
		lines.append(line);

for i in range(len(lines)):
	if curly == 'newline':
		if 'function' not in lines[i]:
			continue
		else:
			moveNewLine(i)
	elif curly == 'inline':
		if '{' not in lines[i]:
			continue
		else:
			moveInline(i)

