def find_missing(array1,array2):
    #method to create missing number

    if array1 == array2:

        return 0

    elif array1 != array2:

        a = set(array1)

        b = set(array2)

        c = a^b

        return list(c)[0]
       
