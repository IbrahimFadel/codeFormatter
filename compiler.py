from ruamel.yaml import YAML

yaml = YAML()

rawdata = open('config.yml', 'r').read()
data = yaml.load(rawdata)
curly = data['settings']['curly']
functionSpacing = data['settings']['functionSpacing']
filename = data['settings']['inputFile']
output = data['settings']['outputFile']

def moveCurlyInline(i):
	with open(filename, 'r') as inputFile:
		data = [line.rstrip("\n") for line in inputFile]
		data[i - 1] += ' {'
		data[i] = ''
	with open(output, 'w') as outputFile:
		for i in range(len(data)):
			outputFile.write(data[i] + '\n')

def moveCurylyNewline(i):
	with open(filename, 'r') as inputFile:
		data = [line.rstrip("\n") for line in inputFile]
		new = data[i].replace('{', '')
		data[i] = new
		new2 = '\n{'
	with open(output, 'w') as outputFile:
		outputFile.write(data[i])
		outputFile.write(new2)
		for i in range(len(data) - 1):
			print(len(data))
			print(i)
			if i < len(data):
				outputFile.write('\n' + data[i + 1])
			#else:
			#	outputFile.write('\n' + data[i] + '\n')
		print(new,new2)

file = open(filename, 'r')

i = 0
lines = []
for line in file.readlines():
	lines.append(line)
	i += 1

for i in range(len(lines)):
	if lines[i][0] == '{' and curly == 'inline':
		moveCurlyInline(i)
	elif lines[i].count('function') > 0 and lines[i].count('{') > 0 and curly == 'newline':
		moveCurylyNewline(i)