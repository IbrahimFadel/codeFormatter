from ruamel.yaml import YAML 

yaml = YAML()

rawdata = open('config.yml', 'r').read()
data = yaml.load(rawdata)
curly = data['settings']['curly']
functionSpacing = data['settings']['functionSpacing']
filename = data['settings']['inputFile']
output = data['settings']['outputFile']

outputArray = []

def moveCurlyInline(i):
	with open(filename, 'r') as inputFile:
		data = [line.rstrip("\n") for line in inputFile]
		data[i - 1] += ' {'
		data[i] = ''
	with open(output, 'w') as outputFile:
		try:
			for i in range(len(data)):
				outputFile.write(data[i] + '\n')
		except:
			print("Error compiling")

def moveCurylyNewline(i):
	global amntRuns
	global outputArray
	global Is
	Is.append(i)
	with open(filename, "r") as inputFile:
		data = [line.rstrip('\n') for line in inputFile]
		pos = data[i].find('{')
		insertNL = data[i][:pos] + '\n{'
		outputArray.append(insertNL)
		data[i] = outputArray[amntRuns]
	with open(output, "w") as outputFile:
		try:
			for x in range(len(data)):
				if(data[x].count('function') > 0):
					outputFile.write(outputArray[amntRuns] + '\n')
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
Is = []
for i in range(len(lines)):	
	if curly == 'newline':
		if 'function' not in lines[i]:
			continue
		else:
			moveCurylyNewline(i)
			amntRuns += 1

	"""print(lines[i])
	if lines[i][0] == '{' and curly == 'inline':
		moveCurlyInline(i)

	elif lines[i].count('function') > 0 and lines[i].count('{') > 0 and curly == 'newline':
		#print(lines[i][0])
		moveCurylyNewline(i)"""

