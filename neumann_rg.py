#python test 1 - Neumann's random generator
samples_number = input()#number of samples
data_input = []     #initialize data input array as a list
data_output = []    #initialize data output array as a list
for index in range(0,int(samples_number)):
    tmp = input()
    data_input.append(int(tmp)) #insert every value

def loop_finder(int_value):
    data_tmp=[int_value] #initalize as a list
    print(type(data_tmp))
    while True:
        int_value = int_value*int_value #Same as value²
        int_value = int((int_value/100)%10000)#First Eliminate last two digits with the division, and % gets the other 4 digits needed
        if int_value in data_tmp:
            break
        else:
            data_tmp.append(int_value)#for a better performance, the value inserted must be int
            #print(int_value)
    return len(data_tmp) #gives the number of iterations until loop

for value in (data_input):
    data_output.append(loop_finder(value)) #find the value of repetitions until the loop and append to data_output

print("these are the iterations for every value")
print(data_output)
