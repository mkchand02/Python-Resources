'''
Let us consider input list as:
l=[1,2,3,4,9,8,7,6,5,6,7,8,8,4,2,1]
'''
l=[1,2,3,4,9,8,7,6,5,6,7,8,8,4,2,1]
l.sort()
i=0
'''
After sorting, list becomes
l=[1,1,2,2,3,4,4,5,6,6,7,7,8,8,8,9]
Now, don't think about loops first hand. Create your program using bottom-up programming approach.
Clearly, using pen -paper, if we solve this problem, what we do is
1. Iterate over list. If the next number is same as current number, remove the next number(or current one) and append it to the list.
Ex.: [curr=1,next=1,2,2,3,4,4,5,6,6,7,7,8,8,8,9]
[curr=1,2,2,3,4,4,5,6,6,7,7,8,8,8,9]Removed:1
[curr=1,2,2,3,4,4,5,6,6,7,7,8,8,8,9,1]
If we go this way, with a single iteration, we can find our answer as:
[1,2,3,4,5,6,7,8,9,1,2,4,6,7,8,8]
But wait there is an issue:
The above answer is achieved only when we  stop at 9, i.e. the lst number of the original *sorted* list.
Ex. : [1,2,3,4,5,6,7,8,stop when you reach here :9,1,2,4,6,7,8,8]
If you think clearly for a little while, this gives out condition of how long should we go,i.e.,since we have sorted list, 
we should stop as soon as a small number follows a large number
Ex. : [1,2,3,4,5,6,7,8,large no.:9,small no.:1,2,4,6,7,8,8]
So, our code becomes
'''
i=0#index
length = len(l) 
while i<length and l[i]<=l[i+1]:#main condition is while curr no.<next no. , the other one is a security check for concurrent execution and code will execute without any errors without using that condition
    if l[i]==l[i+1]:
        l.append(l.pop(i+1))
    else:
        i+=1
print(l)
