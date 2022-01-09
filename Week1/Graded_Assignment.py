# Q1 -------------------------------------
def fun(s):
    p = 0
    s.lower()
    for i in range (len(s)):
        if s[i] not in s[:i]:
            p += 1
    return p

#print(fun("Ashutosh")) # gives total number of distinct letters in string s

# Q2 -------------------------------------
#print(foo("check")) # calling function before declaration would raise NameError

def foo(s):
    return 5

# if variable is used without defining the same would raise NameError
# if built-in function is mispelled it would raise NameError

# Q3 -------------------------------------
def f(n):
    s = 0
    for i in range(2, n):
        if n%i == 0 and  i%2 == 1:
            s = s + 1
    return(s)

#print(f(60) - f(59)) # 3

# Q4 -------------------------------------
x = 1
while True:
    if x%5 == 0:
        break
    print(x, end=' ')
    x += 1

print("\n")

# Q5 -------------------------------------
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, ', self.name)

p = Person('Good morning')
#p.say_hi() # Hello,  Good morning

# Q6 -------------------------------------
a = [1, 2, 3]
try:
    print("Second element = %d" %(a[1]))
    print("Fourth element = %d" %(a[3]))
except:
    print("An error occured")

#Second element = 2
#An error occured

# Q7 -------------------------------------
def special3Bad(L):
    print(L)
    try:
        if L[0] % L[1] == 0 and L[1] != 0:
            if L[0] / (L[1] ** 2 - L[2]) == 0:
                return True
        return False
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except:
        print('Some other exception occured')
    else:
        print('Noexception occured')

#special3Bad([48,6,36]) #[4,2,4] [8,4,16] [48,6,36]

# Q8 -------------------------------------
def isSymetricBad(L):
    print(L)
    try:
        while len(L) > 0:
            if L.pop(0) != L.pop(-1):
                return False
        return True
    except IndexError:
        print('IndexError')
    except:
        print('Some other exception occured')
    else:
        print('No exception occured')

#isSymetricBad([2, 4, 6]) # [1, 2, 3, 4, 3, 2, 1] [1, 1, 1, 1, 1, 1, 1] [8]

# Q9 -------------------------------------
c=0
def gcd(m, n):
    global c
    (a,b) = (max(m,n), min(m,n))
    if a%b == 0:
        return(b)
    else:
        c = c+1
        return(gcd(b, a%b))

#print(gcd(24, 130))
#print(c) # 3

# Q10 -------------------------------------
class Enrollment:
    count = 0
    def __init__(self,n,c):
        self.name = n
        self.course = c
        Enrollment.count += 1
    
    def display(self):
        print(self.name)
        print(self.course)

# name and course are object variables, and count is a class variable
# count represents the number of objects created for class Enrollment