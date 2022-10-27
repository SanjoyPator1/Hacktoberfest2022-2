# You are given a number with duplicate digits your task is to remove the immediate duplicate digits and print the result
a=input()   #taking a string input
b=""        # an empty string
i=0
while(i<len(a)):             
    if (i==len(a)-1):
        b=b+a[i]                #for the last element of the string
    elif(a[i]==a[i+1]):         
        i=i+1                   # skip the element
    else:
        b=b+a[i]
    i+=1
if(len(b)==0):                  # if no such elements are found print -1
  print("-1")
else: 
  print(b)
