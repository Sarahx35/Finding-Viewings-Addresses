file = open('Sat_3_Viewings.txt')
print(file)
yucky_lines = file.readlines()
clean_lines = []
for line in yucky_lines:
    clean_lines.append(line.strip())
while '' in clean_lines:
    clean_lines.remove('')

line_number = 0
for line in clean_lines:
    if line.startswith('Address:'):
        print(line,clean_lines[line_number+1])
    line_number = line_number + 1
   