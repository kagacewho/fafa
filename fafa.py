input_data = open('input.txt', 'r') 
data = input_data.read()
n = int(data)
f = int(data)
f = 1
for i in range (1, n+1):
    f = f * i
output_data = open('output.txt', 'w')
output_data.write(str(f))
input_data.close()
output_data.close()