#The merge sort algorithm mainly performs three actions:

#Divide an unsorted sequence of items into sub-parts
#Sort the items in the sub-parts
#Merge the sorted sub-parts
#The above happens recursively until the sub-parts are merged into the complete sorted sequence. Let's start by #dividing the sequence.


def merge_sort(array):
#Before testing the merge_sort() function, you need to create a base case that stops the function execution #when the length of array is less than or equal to 1. Serve para parar com a recursividade
    if len(array) <= 1:
        return

    middle_point = len(array) // 2 #Divide o array na metade
    left_part = array[:middle_point] #Guarda numa lista a metade esquerda do array
    right_part = array[middle_point:] #Guarda numa lista a metade direita do array
    
    merge_sort(left_side)#Recursividade para dividir as listas até apenas existir 1 elemento em cada lista
    merge_sort(right_part) #Recursividade para dividir as listas até apenas existir 1 elemento em cada lista

#Now it's time to sort and merge the lists (left_part and right_part) into the original array.

#You can do this by comparing elements on both lists, and merging the smaller element to the main list. You are #going to do this comparison for all the indexes in left_part and right_part.

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index]= (left_part[left_array_index])
            left_array_index += 1
#When the if condition evaluates to True, it means that the element in the left_part list is smaller than the #element it is being compared to in the right_part list. Assim sendo, adiciona no array sorted esse elemento
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1
#se um dos arrays estiver vazio, a comparação entre o left e o right não consegues ser feita. Assim faz-se um
#while para colocar os restantes na lista
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
   
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


#You can use the __name__ variable to determine if a Python script is being run as the main program or if it is #being imported as a module (code written in another Python file).
#If the value of __name__ is set to '__main__', it implies that the current script is the main program, and not #a module.

if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: '+str(numbers))