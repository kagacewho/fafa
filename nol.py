input_data = open('input.txt', 'r')
data = input_data.read()
counter = 0 
ans = 0
for i in data:
    if i == '0':
        counter += 1
    else:
        if counter > ans:
            ans = counter
            counter = 0
        else:
            counter = 0
output_data = open('output.txt', 'w')
output_data.write(str(ans))
input_data.close()
output_data.close()