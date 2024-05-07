# in previous class
myName = "Niroj Kumar Naik\""

print(myName)  # Niroj Kumar Naik"

print(myName[5])

for x in myName:
    print(x)

print(len(myName))

print("ro" in myName)

# today study
# use of 'in' and 'not in'

print("ro " not in myName)  # True

if "Ni" in myName:
    print("'Ni' is present in myName variable")


if "Ni " not in myName:
    print("No, 'Ni ' is not in myName variable")

# ------------character slicing----------------

# the variable is: myName = "Niroj Kumar Naik\""

#                       -OutPut-        begin          ends
#                                     (include)     (exclude)
print(myName[2:8])      # roj Ku          2             8
print(myName[2:8:2])    # rjK             2             8
print(myName[2::2])     # rjKmrNi"        2             16
print(myName[::2])      # NrjKmrNi"       0             16
print(myName[-5:-1])    # Naik           -5          -1 or 16

# another way to use slicing
sliceOne = slice(3)
sliceTwo = slice(3, -1, 2)

#                            -OutPut-        begin          ends
#                                          (include)     (exclude)
print(myName[sliceOne])      # Nir            0              3
print(myName[sliceTwo])      # o ua ak        3           -1 or 16
