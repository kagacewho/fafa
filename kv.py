input_data = open('input.txt', 'r') 
data = input_data.read()
n = int(data[0])
p = int(data)
g = int(data)
p = 2
g = p**n
output_data = open('output.txt', 'w')
output_data.write(str(g))
input_data.close()
output_data.close()