x=111
def mul2(x):
    return x % 2 == 0
def mul3(x):
    return x % 3 == 0       
def mul5(x):
    return x % 5 == 0
lst =[]
def fnc(lst, *func):
    for i in lst:
        for f in func:
            print(f(i))
#fnc(lst, mul2, mul3, mul5)

class multifilter(): 

        def judge_half(pos, neg):
            # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
            if pos >= neg:
                return x

        def judge_any(pos, neg):
            # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
            if pos >= 1:
                return x

        def judge_all(pos, neg):
            # допускает элемент, если его допускают все функции (neg == 0)
            if neg == 0:
                return x
                
        def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
            self.iterable = iterable
            self.pos=0
            self.neg=0
            self.x=222          
            self.judge = judge
            
        def __iter__(self):
            # возвращает итератор по результирующей последовательности
            for x in self.iterable: 
                for y in mul2,mul3,mul5:
                    if y(x) == True: #(self.x)
                        self.pos +=1
                    else:
                        self.neg +=1 

                g=self.judge(self.pos,self.neg)
                if g != None:
                    yield x
                self.pos=self.neg=self.x=0

        def __next__(self):
            pass

                
a=[0,1,2,3,4,5,6,7,8,9,30]
#a = [i for i in range(31)] # [0, 1, 2, ... , 30]
print(list(multifilter(a, mul2, mul3, mul5)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half))) 
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))