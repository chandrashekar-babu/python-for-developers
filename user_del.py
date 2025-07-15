class User:
    def __init__(self):
        print(f"User {self} created")
    
    def __del__(self):
        print(f"User {self} is being destroyed.")

u1 = User()
u2 = u1
u3 = u2
u4 = u3

del u1
print("u1 deleted")

del u3
print("u3 deleted")

del u4
print("u4 deleted")

#del u2
#print("u2 deleted")

u2 = 100
print("u2 reassigned to 100")