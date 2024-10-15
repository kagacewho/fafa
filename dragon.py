input_data = open('input.txt', 'r')
n = int(input_data.read())
count = 1
if n <= 4:
    ans = n
else:
    while n > 4:
        count *= 3
        n -= 3
    else:
        ans = count * n
output_data = open('output.txt', 'w')
output_data.write(str(ans))
input_data.close()
output_data.close()