#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    tmp = 0
    for i in range(list_length):
        try:
            tmp = my_list_1[i] / my_list_2[i]
        except TypeError:
            tmp = 0
            print("wrong type")
        except IndexError:
            tmp = 0
            print("out of range")
        except ZeroDivisionError:
            tmp = 0
            print("division by 0")
        finally:
            pass
        result.append(tmp)
    return result
