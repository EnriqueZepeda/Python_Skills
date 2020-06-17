file = input('Enter a file name:')

try:
    fileHandle = open(file)
except:
    print('Error: file', file, 'no found')
    quit()

count = 0

for lines in fileHandle:
    lines = lines.rstrip()
    print(lines.upper())
    count = count + 1;