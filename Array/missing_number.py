my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10 ,12 ,13 ,14 ,15]
def find_missing(lst, n):
    sum1 = n * (n+1) / 2
    sum2 = sum(lst)
    print (sum1 - sum2)

find_missing(my_list,15)