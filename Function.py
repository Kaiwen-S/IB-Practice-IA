def LinearSearch(arr,x):
    Found=False
    for i in arr:
        if i==x:
            Found=True
    print(Found)

def BinarySearch(arr,x):
    SelectionSortA(arr)
    Found=False
    while len(arr)>=1:
        if arr[len(arr)//2]==x:
            Found=True
            break
        elif arr[len(arr)//2]<x:
            del arr[:len(arr)//2]
        elif arr[len(arr)//2]>x:
            del arr[len(arr)//2:]
        if len(arr)==1:
            break
    print(Found)

def Search(arr,x,Method):
    if Method=='Linear':
        LinearSearch(arr,x)
    elif Method=='Binary':
        BinarySearch(arr,x)

# Make sure to type 'from Funcion import *' to import all the functions defined in this file

def sorting_alphabet(movies_arr):
    for i in range(len(movies_arr)):
        m=movies_arr[i]
        for j in range(i+1,len(movies_arr)):
            if m>movies_arr[j]:
                m=movies_arr[j]
                max_index=j
                movies_arr[i],movies_arr[j]=movies_arr[j],movies_arr[i]
    for i in range(len(movies_arr)):
        print(movies_arr[i])

def FileIntoList(x):
    file=open(x)
    file_string=file.read()
    file_array=file_string.split('\n')
    return file_array

def StringInsideString(a,ls):
    Result=[]
    Found=False
    for i in ls:
        if a in i:
            Result.append(i)
            Found=True
    if Found==True:
        print(Result)
    else:
        print('Not Found!')
    return Found

def OutPut(x):
    doc=open("yout_movie_list.txt","w")
    for i in x:
        print(i)
        print(i,file=doc)
    doc.close()
    
    

