# This is a sample Python script.
cars_list = []

def cars(arg1, arg2, arg3, arg4, arg5):
    global cars_list

    cars_list = []

    i = {"id": arg1, "brand": arg2, "model": arg3, "hp": arg4, "price": arg5}

    #i_copy = i.copy()

    #return i, cars_list.append(i)
    cars_list.append(i)


    return cars_list

print(cars(1, "Hyunday", "Santa Fe", 189, 30000))
#print(cars_list)
print(cars(2, "Kia", "Sorento", 140, 20000))
print(cars_list)