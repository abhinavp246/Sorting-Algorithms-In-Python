
from numpy.random import rand                     
import pandas                                    
import numpy as np                               
import timeit                                     
import os, sys                                  

def numGen(number_count):
    '''This Function is used to create 5 files of different sizes (10, 100, 1000, 10000, 100000) with random numbers.'''
    f = open(str(number_count)+".txt", 'w') #Create a file with the appropriate name.
    for i in range (number_count): #Add random float values into the list based on the size of the file specified. 
        x = rand()*1000
        f.write(str(x) + " ") 

def file_opener():
    '''This function is used to open the files with random numbers, convert them to lists of floats, then load them into the sorting functions.'''
    with open('10.txt', 'r') as f: #Open the files and convert the contents into an unsorted list.
        l1 = f.read().split(' ')
        del l1[-1]

    with open('100.txt', 'r') as f:
        l2 = f.read().split(' ')
        del l2[-1]

    with open('1000.txt', 'r') as f:
        l3 = f.read().split(' ')
        del l3[-1]

    with open('10000.txt', 'r') as f:
        l4 = f.read().split(' ')
        del l4[-1]

    with open('100000.txt', 'r') as f:
        l5 = f.read().split(' ')
        del l5[-1]

    list10 = [float (i) for i in l1] #Convert the elements of the lists into floating point integers.
    list100 = [float (i) for i in l2]
    list1000 = [float (i) for i in l3]
    list10000 = [float (i) for i in l4]
    list100000 = [float (i) for i in l5]
    fileList = [list10, list100, list1000, list10000, list100000] #Create a list of all of the above lists.
    mergeSort_timer(fileList)  #Load the lists into the sorting functions.
    insertionSort_timer(fileList)
    selectionSort_timer(fileList)

def mergeSort_timer(fileList): 
    '''This function is used to determine the time cost of mergeSort on various input sizes.'''
    print ("************* Merge Sort **************")
    print("Input Size (# of Numbers):                   Time Cost(s)")
    for i in range (len(fileList)): #Find the time cost of sorting different size lists. 
        start = timeit.default_timer()
        mergeSort(fileList[i])
        stop = timeit.default_timer()
        writeProcessed(mergeSort(fileList[i]), str(len(fileList[i])), "mergeSort")
        print (len(fileList[i]), "               ", stop - start)

def insertionSort_timer(fileList):
    '''This function is used to determine the time cost of insertionSort on various input sizes.'''
    print ("************* Insertion Sort **************")
    print("Input Size (# of Numbers):                    Time Cost(s)")
    for i in range (len(fileList)):
        start = timeit.default_timer()
        insertionSort(fileList[i])
        stop = timeit.default_timer()
        writeProcessed(insertionSort(fileList[i]), str(len(fileList[i])), "insertionSort")
        print (len(fileList[i]), "               ", stop - start)

def selectionSort_timer(fileList):
    '''This function is used to determine the time cost of selectionSort on various input sizes.'''
    print ("************* Selection Sort **************")
    print("Input Size (# of Numbers):                    Time Cost(s)")
    for i in range (len(fileList)):
        start = timeit.default_timer()
        selectionSort(fileList[i])
        stop = timeit.default_timer()
        writeProcessed(selectionSort(fileList[i]), str(len(fileList[i])), "selectionSort")
        print (len(fileList[i]), "               ", stop - start)

def writeProcessed(data, outfile, prefix):
    '''Helper function used to write the sorted output into a file with the appropriate name format.'''
    np.savetxt(prefix + outfile +".txt", data, fmt='%f', delimiter=',')

def fileDeleter(x,y):
    '''This function is used to delete either the sorted output files or the random number files (or both) based on the user's choice.'''
    name_list = ['mergeSort', 'selectionSort', 'insertionSort'] #Creating a list with all of the sorting function names. 
    size_list = ['10','100','1000','10000','100000'] #Creating a list with all of the file sizes.
    if x == 'y' or x == 'Y':
        for i in range (len(name_list)): #Looping through the different name-size combinations, and deleting all relevant files.
            for j in range (len(size_list)):
                os.remove(name_list[i]+size_list[j]+'.txt')
    else:
        print("Sorted files saved to directory.")

    if y == 'Y' or y == 'y':
        for i in range (len(size_list)): #Looping through the various input sizes and deleting all relevant files. 
            os.remove(size_list[i]+'.txt')
    else: 
        print("Unsorted number files saved to directory")

def mergeSort(arr):
    '''Merge sort implementation in python.'''
    sort_list = []  #Base case for recursion. 
    if len(arr) <= 1:
        return arr

    else:
        mid_partition = int(len(arr)/2) # Determining the middle point for partitioning. 
        left = mergeSort(arr[:mid_partition]) # Recursively dividing the original array into smaller sub-arrays until the base-case has been reached. 
        right = mergeSort(arr[mid_partition:])

        i = 0
        j = 0 
        while i < len(left) and j < len(right): # Sorting the elements by comparison. 
            if left[i] < right[j]:
                sort_list.append(left[i])
                i += 1
            else: 
                sort_list.append(right[j])
                j += 1
        sort_list += left[i:] # Merging the sorted lists. 
        sort_list += right[j:]
        return sort_list

def insertionSort(arr):
    '''Insertion sort implementation in python.'''
    for i in range( 1, len(arr)): #Iterating through the list.
        val = arr[i]
        k = i
        while k > 0 and val < arr[k - 1]: #Checking if the current value is less than the preceding value. 
            arr[k] = arr[k - 1] # Inserting the value into the correct position.
            k -= 1
        arr[k] = val
    return arr

def selectionSort (arr):
    for i in range(len(arr)):
        smallest = i
        for k in range (i + 1, len(arr)):
            if arr[k] < arr[smallest]:
                smallest = k
        val = arr[smallest]
        arr[smallest] = arr[i]
        arr[i] = val
    return arr

def driver():
    file_size = 10 
    while file_size <= 100000:
        numGen(file_size)
        file_size=file_size*10
    file_opener()
    delete_sorted_output = input("Do you want to delete the sorted output files? Type 'Y' for yes and 'N' for no.")
    delete_number_files = input("Do you want to delete the random number files? Type 'Y' for yes and 'N' for no.")
    fileDeleter(delete_sorted_output, delete_number_files)
    return "End of processing!"

    
if __name__ == "__main__":
    driver()
#print (insertionSort(list1))

