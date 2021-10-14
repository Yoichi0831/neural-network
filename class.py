def foo(x): #常规方法
    print("executing foo(%s)"%(x))

class A(object):
    #实例方法
    def foo(self,x):  #默认第一个参数为实例对象
        print("executing foo(%s,%s)"%(self,x))
        return x
    #类方法
    @classmethod
    def class_foo(cls,x):  #默认第一个参数为类对象
        print ("executing class_foo(%s,%s)"%(cls,x))
    #静态方法
    @staticmethod    #不需要绑定,调用注意
    def static_foo(x):
        print("executing static_foo(%s)"%x)


    def __call__(self):
        print('hello')    


    def __call__(self)    
a=A()
a.class_foo('beep')
#x = a('wooohooo')
#print('done' + x)
print(callable(a))