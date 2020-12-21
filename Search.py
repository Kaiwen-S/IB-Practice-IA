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

# Make sure to type 'from Search import *' to import all the functions defined in this file
