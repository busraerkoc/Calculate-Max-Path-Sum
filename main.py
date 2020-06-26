def check_prime(num):
    num = num
    if num > 1:
        for i in range(2, num):
            if(num%i)==0:
                return 1  # not prime number 
        return 0 # prime number
    else:
        return 1  # not prime number

def remove_prime_number(num):
    if check_prime(num) == 0:
        return -1
    else:
        return num
        
f=open('second.txt',"r")
# Create 2 dimensional array from input file 
path = []
all_values = []
all_value = []
for i in f:
    line = []
    i = i.strip().split()
    line = [int(j) for j in i]
    all_values.append(line)

# Remove Prime Numbers

for i in range(len(all_values)):
    for j in range(len(all_values[i])):
        all_values[i][j] = remove_prime_number(all_values[i][j])

length = len(all_values)

#Downwards and diagonally
temp = all_values
col_index = 0
path = []
path.append(all_values[0][0])
for i in range(length-1):
    j=col_index
    current = temp[i][j]
    left = temp[i+1][j]
    right = temp[i+1][j+1]
    if check_prime(left) and check_prime(right):
        if left > right and left!=-1:
            col_index = j
            path.append(left) 
        elif right > left and right!=-1:
            col_index = j+1
            path.append(right)
        else:
            continue
                    
max_sum = 0
for i in path:
    max_sum+=i
print("Path:", path)
print(max_sum)
