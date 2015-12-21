print "Enter the elements of array seperated with space"
s = raw_input()
numbers = map(int, s.split())
print numbers

k = input("Enter the size of subarray\n")
n = len(numbers )
sum = 0
start =0
if k < n:
    for j in range(0,k):
        sum += numbers[j]
    lowest = sum
    for i in range(k,n):
        sum += numbers[i] - numbers[i-k]
        if lowest>sum:
            lowest = sum
            start = i-k+1
    print "The bellow indices give the subarray of minimum average."
    print "Starting and ending index are: ", start, start + k - 1

else:
    print "The length of subarray should be less than length of array\n"
    exit()







