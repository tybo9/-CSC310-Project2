print("Find Min and Max of a list without sorting")
#Find min and max without sorting the list

def MinAndMax1(arr):
    #Consider first element of the list as min and max value
    min = arr[0]
    max = arr[0]
    for x in arr:
        if(x<min):      #if list value is less the min value, assign min as list value
            min = x
        if (x > max):   #if list value is greater the max value, assign max as list value
            max = x
    return max,min

a = [10, 39, 47, 1, 49,100]
max, min = MinAndMax1(a)
print("Maximum: ",max," Minimum: ",min)

print("Find Min and Max of a list with sorting")
#Find min and max by sorting the list
def MinAndMax2(arr):
    #Sort the list value in descending order
    for i in range(0,6):
        for j in range(0,6):
            if(arr[i] > arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr[0], arr[5]   #return the first element and last element of the list

a = [10, 39, 47, 1, 49,100]
max, min = MinAndMax2(a)
print("Maximum: ",max," Minimum: ",min)

print("Find Min and Max of a list using recursion")
def MinMaxRec(arr, min, max):
    if(len(arr) == 0):       #if length of the list is 0, return min and max
        return min, max
    if(arr[0]<min):         #find the minimum value between min and arr[0], assign it to min
        min = arr[0]
    if(arr[0]>max):         #find the maximum value between max and arr[0], assign it to max
        max = arr[0]
    return MinMaxRec(arr[1:],min,max)


a = [10, 39, 47, 1, 49,100]
min, max = MinMaxRec(a,a[0],a[0])
print("Maximum: ",max," Minimum: ",min)

print("Reverse a string using recursion")
def reverseString(S):
    if(len(S) == 0):    #if length of the string is 0, return string
        return S
    return reverseString(S[1:])+S[0]    #Strink the string and add the first element of the string to last
#Example
#Iteration 1                iteration 2             finally         After combining the return statements
#S = string                 S = trings              S = ""          S = gnirts
#return(tring)+s           return(ring)+t+s         return "",

S = input("Enter a string to reverse: ")
print("Reverse String: ",reverseString(S))