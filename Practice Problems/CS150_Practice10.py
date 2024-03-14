'''
Practice Problems 10
Wednesday, Novemeber 20th

'''

#Write a fucntion without loops


def rec_in(a_list, item):
     """ Return True if item is contained in a_list, False otherwise """
     if len(a_list) == 0:
         return False
     else:
         if a_list[0] == item:
             return True
         else:
             return rec_in(a_list[1:], item)




#Write a docstring for this function


def mystery(a_list):
    """
     Check if list is sorted in ascending order
        
     Args:
         a_list: A list of comparable values
            
     Returns:
         True if listed is sorted in ascending order
     """
    if len(a_list) <= 1:
         return True
    else:
        return (a_list[0] <= a_list[1]) and mystery(a_list[1:])



#Write a fibbionacci sequence function

def fib(n):
    """ Calculates the nth Fibonacci number recursively """
    if (n == 1) or (n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)
        

        
        
        