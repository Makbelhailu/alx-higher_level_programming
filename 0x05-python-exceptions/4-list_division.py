#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    value = []
    for i in range(list_length):
        try:
            value.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            value.append(0)
        except ZeroDivisionError:
            print("division by 0")
            value.append(0)
        except IndexError:
            print("out of range")
            value.append(0)
        finally:
            return (value)
