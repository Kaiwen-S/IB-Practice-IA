movies_arr=['avatar','matrix','star wars','mission impossible','iron man']

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

sorting_alphabet(movies_arr)

