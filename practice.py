# the step 1 is compute equation 1
def compute1(a,b,c,d,e,f):
    return ((a+(b/c))/(d+(e/f)))

ecu1 = compute1(1,2,3,4,5,6)
print("ecu1",ecu1)
# "the second step is compute equation 2"
def compute2(a,b,c,d):
    return (a-(b/(c-d)))
ecu2 = compute2(1,2,3,4)
print("ecu2",ecu2)
# "the third step is swap the variables"
ecu1,ecu2 = ecu2,ecu1
print("ahora ecu1 es",ecu1)
print("ahora ecu2 es",ecu2)
