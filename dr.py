input_data = open('input.txt', 'r') 
data = input_data.read()
inp = bin(int(data))
count = 0

for i in inp:
    if i == '1':
        count += 1
output_data = open('output.txt', 'w')
output_data.write(str(count))
input_data.close()
output_data.close()