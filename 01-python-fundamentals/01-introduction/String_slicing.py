L="HELLO WORLD"
#[start:stop:step]
print(L[::1])
print(L[::2])
print(L[3:7:1]) #7th index will not be printed
print(L[::-1]) #reverse slicing
print(L[9:4:-1])