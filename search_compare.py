import time
import random

def get_me_random_list(n):
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def sequential_search(a_list,item):
    position = 0
    found = False
    stopped = False
    while position < len(a_list) and not found and not stopped:
        if a_list[position] == item:
            found = True     
        else:
            if a_list[position] > item:
                stopped = True
            else:
                position  = position+1   
    return found


def ordered_sequential_search(a_list,item):
    list_size = len(a_list) 
    for i in range(list_size): 
        if item == a_list[i]: 
            return i 
        elif a_list[i] > item: 
            return None 
    return None


def binary_search_iterative(a_list,item):
    min = 0
    max = len(a_list) - 1
    mid = 0
    while min <= max:
        mid = (max + min) // 2
        if a_list[mid] < item:
            min = mid + 1
        elif a_list[mid] > item:
            max = mid - 1
        else:
            return mid
    return None
    
    
def binary_search_recursive(a_list,item):
    mid = len(a_list) // 2
    if len(a_list) == 1:
        return mid if a_list[mid] == item else None
    elif a_list[mid] == item:
        return mid
    else:
        if a_list[mid] < item:
            callback_response = binary_search_recursive((a_list[mid:]), item)
            return mid + callback_response if callback_response is not None else None
        else:
            return binary_search_recursive((a_list[:mid]), item)


def main():

        list_sizes = [500, 1000, 5000]

        the_size = list_sizes[0]

        search_num = 99999999

        print(500)
        total_time = 0
        for i in range(100):
            mylist500 = get_me_random_list(the_size)
            start = time.time()
            sequential_search(mylist500, search_num)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        total_time = 0
        for i in range(100):
            mylist500 = get_me_random_list(the_size)
            start = time.time()
            ordered_sequential_search(mylist500, search_num)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Ordered Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        total_time = 0
        for i in range(100):
            mylist500 = get_me_random_list(the_size)
            start = time.time()
            binary_search_iterative(mylist500, search_num)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Binary Search Iterative took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        total_time = 0
        for i in range(100):
            mylist500 = get_me_random_list(the_size)
            start = time.time()
            binary_search_recursive(mylist500, search_num)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Binary Search Recursive took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        print(1000)
        the_size = list_sizes[1]
        total_time = 0
        for i in range(100):
            mylist1000 = get_me_random_list(the_size)
            start = time.time()
            sequential_search(mylist1000, search_num)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        total_time = 0
        for i in range(100):
            mylist1000 = get_me_random_list(the_size)
            start = time.time()
            ordered_sequential_search(mylist1000, search_num)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Ordered Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        total_time = 0
        for i in range(100):
            mylist1000 = get_me_random_list(the_size)
            start = time.time()
            binary_search_iterative(mylist1000, search_num)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Binary Search Iterative took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        total_time = 0
        for i in range(100):
            mylist1000 = get_me_random_list(the_size)
            start = time.time()
            binary_search_recursive(mylist1000, search_num)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Binary Search Recursive took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        print(5000)
        total_time = 0
        the_size = list_sizes[2]
        for i in range(100):
            mylist5000 = get_me_random_list(the_size)
            start = time.time()
            sequential_search(mylist5000, search_num)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        total_time = 0
        for i in range(100):
            mylist5000 = get_me_random_list(the_size)
            start = time.time()
            ordered_sequential_search(mylist5000, search_num)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Ordered Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        total_time = 0
        for i in range(100):
            mylist5000 = get_me_random_list(the_size)
            start = time.time()
            binary_search_iterative(mylist5000, search_num)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Binary Search Iterative took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        total_time = 0
        for i in range(100):
            mylist5000 = get_me_random_list(the_size)
            start = time.time()
            binary_search_recursive(mylist5000, search_num)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Binary Search Recursive took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")
"""    
    five_hundred_list = []
    thousand_list = []
    five_thousand_list = []
    search_num = 99999999

    for i in range(100):
        five_hundred_list.append(random.sample(range(1,1000),500))
        thousand_list.append(random.sample(range(1,2000),1000))
        five_thousand_list.append(random.sample(range(1,10000),5000))

    print("500")
    for each_list in five_hundred_list:

        begin = time.time()
        sequential_search(each_list,search_num)
        end = time.time()
        print(f"Sequential Search runtime: {end - begin}")

        begin = time.time()
        ordered_sequential_search(each_list,search_num)
        end = time.time()
        print(f"Ordered Sequential Search runtime: {end - begin}")

        begin = time.time()
        binary_search_iterative(each_list,search_num)
        end = time.time()
        print(f"Binary Search Iterative runtime: {end - begin}")

        begin = time.time()
        binary_search_recursive(each_list,search_num)
        end = time.time()
        print(f"Binary Search Recursive runtime: {end - begin}")

    print("1000")
    for each_list in thousand_list:

        begin = time.time()
        sequential_search(each_list,search_num)
        end = time.time()
        print(f"Sequential Search runtime: {end - begin}")

        begin = time.time()
        ordered_sequential_search(each_list,search_num)
        end = time.time()
        print(f"Ordered Sequential Search runtime: {end - begin}")

        begin = time.time()
        binary_search_iterative(each_list,search_num)
        end = time.time()
        print(f"Binary Search Iterative runtime: {end - begin}")

        begin = time.time()
        binary_search_recursive(each_list,search_num)
        end = time.time()
        print(f"Binary Search Recursive runtime: {end - begin}")  

    print("5000")
    for each_list in five_thousand_list:

        begin = time.time()
        sequential_search(each_list,search_num)
        end = time.time()
        print(f"Sequential Search runtime: {end - begin}")

        begin = time.time()
        ordered_sequential_search(each_list,search_num)
        end = time.time()
        print(f"Ordered Sequential Search runtime: {end - begin}")

        begin = time.time()
        binary_search_iterative(each_list,search_num)
        end = time.time()
        print(f"Binary Search Iterative runtime: {end - begin}")

        begin = time.time()
        binary_search_recursive(each_list,search_num)
        end = time.time()
        print(f"Binary Search Recursive runtime: {end - begin}")      

"""    

if __name__ == "__main__":
    main()
