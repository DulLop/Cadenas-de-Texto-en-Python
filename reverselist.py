"""list = ["hello world","Hello Python","1 2 3 4 5 6 7 8"]

def reverse (list):
    reverse_list = list[::-1]
    print(reverse_list)

if __name__ == "__main__":
    reverse(list)"""

"""def magic_function(list_a):
    list_output = []
    for a in list_a:
       list_output.append(a[::-1])
    return list_output 

A = ["hello world","Hello Python","1 2 3 4 5 6 7 8"]
B = magic_function(A)
print(B)"""

def magic_function(list_input):
    list_output = [a[::-1] for a in list_input]
    return list_output


A = ["hello world","Hello Python","1 2 3 4 5 6 7 8"]
B = magic_function(A)
print (B)