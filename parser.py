from ruamel.yaml import YAML

yaml = YAML()

rawdata = open('config.yml', 'r').read()
data = yaml.load(rawdata)
curly = data['settings']['curly']
functionSpacing = data['settings']['functionSpacing']
file = data['settings']['file']

def moveCurlyInline(line, i):
	#f = open(file, 'w')
	with open('test.js', 'r') as linesdata:
		lines = linesdata.readlines()
	lines[i] = ''
	with open('test.js', 'a') as test:
		lines[i - 1] += ' {'
		#test.write(lines[i - 1])
	print(lines[i])

	with open('test.js', 'w') as file:
		file.writelines(lines)

file = open(file, 'r')

i = 0
lines = []
for line in file.readlines():
	lines.append(line)
	i += 1

for i in range(len(lines)):
	#print(lines[i])
	if lines[i][0] == '{' and curly == 'inline':
		#print("BAD SYNTAX!")
		moveCurlyInline(lines[i], i)

