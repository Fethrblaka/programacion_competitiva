class fibonacci:
    def __init__(self, max_length):
        self.numbers = [1,1] + [None]*max_length
    
    def grow_to(self, number):
        for i in range(number + 1):
            if(self.numbers[i] == None):
                self.numbers[i] = sum(self.numbers[i-2:i])
    
    def get_number(self, number):
        if(self.numbers[number] == None):
            self.grow_to(number)
        return(self.numbers[number])
        
fib = fibonacci(50)

while(True):
    length = int(input())
    if(length == 0):
        exit(0)
    print(fib.get_number(length))