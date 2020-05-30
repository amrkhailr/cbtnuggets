#my_list = [1,2,3,4]
#my_list[2] = 45
#A = my_list *3
#print(A)

#my_list = [1024, 3, True, 6.5]
#my_list.append(False)
#print(my_list)

import datetime

def greet():
    dt = datetime.datetime.now()

    if dt.hour <= 11 :
        greeting = 'morning'
    elif dt.hour <= 17:
        greeting = 'afternoon'
    else:
        greeting = 'night'
    print("Hello, good",greeting)
greet()
