# required args
# def greet(name):
#     print('hello',name)
# greet("john")
# # greet()
# def greet1(name,msg):
#     print(name,msg)
# greet1('john','how are you')
# # keyword args
# def greet2(name,msg):
#     print(f'name is{name},message is {msg}')
# greet2(msg='hy',name='john')
# variable length args
def sum(*args):
    total=0
    for n in args:
        total+=n
    return total
print(sum(5,8,3,9))
print(sum(4,2))
#keyword variable length args
def greet3(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')
greet3(name='john')
greet3(name='john',age=30)

