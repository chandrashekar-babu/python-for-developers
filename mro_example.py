class A:
    def method(self):
        print("Method from A")

class B(A):
    def method(self):
        print("Method from B")

class C(A):
    def method(self):
        print("Method from C")

class D(B, C):
    pass

# MRO for class D is:
# D -> B -> C -> A -> object
print(D.__mro__)

# When we call method() on a D instance:
d = D()
d.method()  # Prints "Method from B"
# Because B comes before C in the MRO
