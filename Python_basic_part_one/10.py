a = int(input("Input an integer : "))
n1 = int("%s" % a)
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))
print(n1 + n2 + n3)

"""
Write a Python program that accepts an integer (n) and 
computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
"""
