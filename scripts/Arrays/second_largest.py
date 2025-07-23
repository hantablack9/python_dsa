from typing import  Optional

def two_large(nums: Optional[list[int | float]])-> Optional[int | float]:
    """
    Function to return the 2nd largest number form an input list of numbers.
    
    ECs: zero matrix,idem
    """
    try:
        if not nums or not len(set(nums))<2:
            return None
    except IndexError:
        return None
    
    try:
        largest = second_largest = float('-inf')
        unique_list = list(set(nums))
        for num in unique_list:
            if num > largest:
                second_largest, largest = largest, num 

            elif largest> num>second_largest:
                second_largest = num

        return second_largest
    
    except IndexError:
        return None

if __name__ == '__main__':
    print(two_large([10, 20, 30]))       # 20
    print(two_large([5, 5, 5]))          # None
    print(two_large([1]))               # None
    print(two_large([-2, -1, -3]))       # -2
    print(two_large([3.5, 3.5, 1.1]))    # 1.1
    print(two_large([]))                # None
    print(two_large([2, 2, 1, 1]))       # 1