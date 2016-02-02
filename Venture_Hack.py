#!/usr/bin/python
def all_combinations(string):
    a=[''] # Initialising with empty string to account for single alphabet strings
    for i in string:
        temp=[]
        for j in a:
            temp.append(j+i)
        a.extend(temp)
    return a[1:] # Removing Empty String
def index(string):
    p=[0]*26
    for i in string:
        p[ord(i)-ord('a')]+=1
    return tuple(p)
def init():
    print '...Processing List Of Legal Words Started...'
    File=open('wordsEn.txt','r') # Opening File in read mode
    words=map(lambda x:x.strip(),File.readlines())
    bag={}
    for i in words:
        if not i.isalpha(): # Check for strings containg non-alphabet characters
            continue
        ind=index(i)
        if bag.has_key(ind):
            bag[ind].append(i)
        else:
            bag[ind]=[i]
    print '...Processing List Of Legal Words Done...'
    return bag
def solution(hash_table):
    while True:
        print 'Enter input string (Only letters, 2<=length<=7): ',
        inp=raw_input()
        if inp.isalpha() and 2<=len(inp)<=7:
            break
        if not inp.isalpha():
            print 'The input string should be letters only.'
        else:
            print 'The string length should be no less than 2 letters and no more than 7 letters.'
    a=all_combinations(inp)
    result=[]
    for i in a:
        t=index(i)
        if hash_table.has_key(t):
            result.extend(hash_table[t])
    result=list(set(result)) # Removing Duplicates
    result.sort()
    print '...Answer...'
    for i in result:
        print i
    print '...Done...'
if __name__=='__main__':
    hash_table=init() # Processing list of legal words
    while True:
        solution(hash_table)
        choice=raw_input('Another Input(y/n): ')
        if choice.lower() == 'n':
            break
