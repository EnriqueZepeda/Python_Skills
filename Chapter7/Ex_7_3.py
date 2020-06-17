file = input('Enter a file name:')

# Easter egg, verify file exists
try:
    fileHandle = open(file)
except:
    if file == 'na na boo boo':
        print(file.upper(), 'TO YOU - You have been punk\'d!')
    else:
        print('Error: file', file, 'no found')
    exit()

count = 0
totValue = 0

for lines in fileHandle:
    lines = lines.rstrip()
    if not lines.startswith('X-DSPAM-Confidence:'):
        continue
    length = len('X-DSPAM-Confidence:')
    strValue = lines[(length):]
    try:
        value = float(strValue)
    except:
        continue
    totValue = totValue + value
    count = count + 1;

print('Average spam confidence:', totValue/count)
