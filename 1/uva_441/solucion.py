class sorted_permutation_iterator6:
    def __init__(self,numbers):
        self.numbers = numbers
        self.slack = len(numbers) - 6
        self.gaps = [0]*6
        self.done = False
        
    def __iter__(self):
        return(self)
        
    def permutation_subset(self):
        subset = []
        i = 0
        for gap in self.gaps:
            i += gap
            subset.append(self.numbers[i])
            i += 1
        return(subset)
            
    def __next__(self):
        temp = self.permutation_subset()
        if(self.slack > 0):
            self.gaps[5] += 1
            self.slack -= 1
            return(temp)
        else:
            for i in range(5,0,-1):
                if(not self.gaps[i] == 0):
                    self.gaps[i-1] += 1
                    self.slack = self.gaps[i] - 1
                    self.gaps[i] = 0
                    return(temp)
            if(self.done):
                raise(StopIteration())
            else:
                self.done = True
                return(temp)

string = input()
while(not string == '0'):
    for permutation in sorted_permutation_iterator6(string.split()[1:]):
        print(' '.join(permutation))   
    string = input()
    if(not string == '0'):
        print()