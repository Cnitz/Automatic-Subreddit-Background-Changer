#!/usr/bin/python
import random
import sys

correct = 0
wrong = 0

hi = 1
low = 0


guess = 0

shownNum = 0
hiddenNum = 0

for num in range(0,2000000):
    
    #Number shown to user
    shownNum = random.random() * 2000000
    shownNum = round(shownNum)
    
    #Second number hidden from user
    hiddenNum = random.random() * 2000000
    hiddenNum = round(hiddenNum)
    
    if random.random() > 0.5:
        shownNum = shownNum * -1
    if random.random() > 0.5:
        guess = hi
    else:
        guess = low

    if hiddenNum > shownNum:
        if guess == hi:
            correct = correct +1
        else:
            wrong = wrong + 1

    if hiddenNum < shownNum:
        if guess == low:
            correct = correct +1
        else:
            wrong = wrong + 1

total = correct + wrong
percent = float(correct) / total

print "Percentage Correct with Pure Guessing: ", percent * 100, "%"



right=0
wrong=0
equal=0
i=0

while i<2000002:
    A = random.random() * 2000000
    A = round(A)
    if random.random() > 0.5:
        A = A * -1
    B = random.random() * 2000000
    B = round(B)
    if random.random() > 0.5:
        B = B * -1
    K = random.random() * 2000000
    K = round(K)
    if random.random() > 0.5:
        K = K * -1
    if A>K:
        if B<A:
            right+=1
        else:
            wrong+=1
    if A<K:
        if B>A:
            right+=1
        else:
            wrong+=1
    i+=1


total = right + wrong
percent = float(right) / total

print "Percentage Correct with Guessing Strategy: ", percent * 100, "%"


    

