
class Expr(object):
    pass
class Val(Expr):
    __slots__ = ['value']
    def __init__(self,value=0):
        self.value=value
    def __repr__(self):
        return f'Val({self.value})'
    def eval(self):
        return self.value

v=Val(1)
print(v)
assert v.eval() == 1

assert isinstance(v,Expr)
assert isinstance(v,Val)
assert isinstance(v,int)

class Add(Expr):
    __slots__=['left','right']
    def __init__(self,a,b):
        if not isinstance(a,Expr):
            a = Val(a)
        if not isinstance(b,Expr):
            a = Val(b)
        self.left = a
        self.right = b
    def eval(self):
        return self.left.eval() + self.right.eval()

e = Add(Val(1),Val(2))
print(e.eval())
assert e.eval() == 3
e = Add(Val(1),Add(Val(2),Val(3)))
print(e.eval())
assert e.eval() == 6
e = Add(1,Add(1,2))
print(e.eval())
assert e.eval() == 4







print()
print()