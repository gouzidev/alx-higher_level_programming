import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
arr = ['hello', 'World']
lib.print_python_list_info(arr)
del arr[1]
lib.print_python_list_info(arr)
arr = arr + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
lib.print_python_list_info(arr)
arr = []
lib.print_python_list_info(arr)
arr.append(0)
lib.print_python_list_info(arr)
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
lib.print_python_list_info(arr)
arr.pop()
lib.print_python_list_info(arr)
