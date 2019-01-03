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
		print(data[i - 1])
		data[i] = ''
		print(data[i])
	with open(output, 'w') as outputFile:
		for i in range(len(data)):
			print(data[i])
			outputFile.write(data[i] + '\n')

file = open(filename, 'r')

i = 0
lines = []
for line in file.readlines():
	lines.append(line)
	i += 1

for i in range(len(lines)):
	if lines[i][0] == '{' and curly == 'inline':
		moveCurlyInline(i)

