""" write a function to find the median of a list.

The median is the middle number in a sorted sequence of numbers.

Finding the median of [7, 12, 3, 1, 6] would first consist of
sorting the sequence into [1, 3, 6, 7, 12] and then locating
the middle value, which would be 6.

If you are given a sequence with an even number of elements,
you must average the two elements surrounding the middle.

For example, the median of the sequence [7, 3, 1, 4] is 3.5,
since the middle elements after sorting the list are 3 and 4
and (3 + 4) / (2.0) is 3.5.

You can sort the sequence using the sorted()


Write a function called median that takes a list as an input
and returns the median value of the list. For example: median([1, 1, 2])
should return 1.

The list can be of any size and the numbers are not guaranteed
to be in any particular order. Make sure to sort it!
If the list contains an even number of elements, your function
should return the average of the middle two.

"""
def median(int_list):
    new_list = []
    new_list = sorted(int_list)
    #print(new_list)
    #print(len(new_list))
    if len(new_list) % 2 is 1:
        print("Odd",new_list[int(len(new_list) / 2)])
        # should be 34
    else:
        num1 = int((len(new_list) / 2) - 1)
        print("Even1",new_list[num1])
        # should be 35
        num2 = int(len(new_list) / 2)
        print("Even2",new_list[num2])
        avg = (new_list[num1] + new_list[num2]) / 2.0
        print(avg)


#        print(new_list(average(len(new_list/2),(len(new_list/2)+1))))

odd_list = [1,47,2,56,34]
even_list = [4,5,5,4]

median(odd_list)  
median(even_list)
  
