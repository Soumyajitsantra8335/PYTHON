#Mutable
#bytes 0-255
x = bytearray(b'A')
print(list(x))
print("Datatype = ",x)

#letter type
x[0]=75
print(x)
print(list(x))