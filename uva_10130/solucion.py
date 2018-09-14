class Basket:
    def __init__(self,value,weight,products_id):
        self.value = int(value)
        self.weight = int(weight)
        self.products_id = products_id
    def __lt__(self,other):
        if(type(other) != type(self)):
            raise(TypeError("'<' not supported between instances of '"+ self.__class__.__name__+ "' and '"+ other.__class__.__name__ +"'"))
        if(self.value/self.weight != other.value/other.weight):
            return(self.value/self.weight > other.value/other.weight)
        else:
            if(self.weight != other.weight):
                return(self.weight < other.weight)
            else:
                return(False)
    def __add__(self,other):
        if(isinstance(other,type(self))):
            return(Basket(self.value + other.value, self.weight + other.weight,self.products_id + other.products_id))
        else:
            raise(TypeError("'+' not supported between instances of","'"+self.__class__.__name__+"'","'"+other.__class__.__name__+"'"))
      
class Product(Basket):
    def __init__(self,value,weight,product_id):
        Basket.__init__(self,value,weight,[product_id]) 

def remove_repetitions_and_sort(numbers):
    unique_numbers = []
    repetitions = []
    previus_repetition = None
    for number in numbers:
        if(number == previus_repetition):
            repetitions[-1] += 1
        else:
            repetitions.append(1)
            unique_numbers.append(number)
            previus_repetition = number
    return([unique_numbers,repetitions])        

def solve(products,capacities):
    products.sort()
    capacities.reverse()
    solution_baskets = []
    if(len(products) == 1):
        solution_baskets.append([[]])
        for capacity in capacities:
            if(capacity >= products[0].weight):
                solution_baskets[0].append(products[0])
    for i in range(len(products),0,-1):
        solution_baskets.append([None]*i)
    for i in range(len(products)):
        for j in range(i):
            best_baskets = []
            for capacity,capacity_index in zip(capacities,range(len(capacities))):
                if((products[j].weight + products[i].weight <= capacity)):
                    best_basket = products[j] + products[i]
                elif(products[j].weight <= capacity and products[i].weight <= capacity):
                    if(products[j].value >= products[i].value):
                        best_basket = products[j]
                    else:
                        best_basket = products[i]
                elif(products[j].weight <= capacity):
                    best_basket = products[j]
                elif(products[i].weight <= capacity):
                    best_basket = products[i]
                else:
                    best_basket = Product(0,capacity,-1)
                for k in range(i - j - 1):
                    if(solution_baskets[k][j][capacity_index].weight + products[i].weight <= capacity):
                        if(solution_baskets[k][j][capacity_index].value + products[i].value > best_basket.value):
                            best_basket = solution_baskets[k][j][capacity_index] + products[i]
                    elif(solution_baskets[k][j][capacity_index].value < products[i].value):
                        best_basket = solution_baskets[k][j][capacity_index]
                    elif(best_basket.value < solution_baskets[k][j][capacity_index].value):
                        best_basket = solution_baskets[k][j][capacity_index]
                best_baskets.append(best_basket)
            solution_baskets[i - j][j] = best_baskets
    best_baskets = []
    for capacity_index in range(len(capacities)):
        best_basket = solution_baskets[-1][0][capacity_index]
        for solution_index in range(1,len(products)):
            if(solution_baskets[-solution_index][-1][capacity_index].value > best_basket.value):
                best_basket = solution_baskets[-solution_index][-1][capacity_index] 
        best_baskets.append(best_basket)
    return(best_baskets)


for i in range(int(input())):  
    input()
    products = []
    capacities = []
    string = input()
    while(len(string.split()) == 2):
        value, weight = string.split()
        products.append(Product(value, weight,len(products)))
        string = input()
    for capacity in range(int(string)):
        capacities.append(int(input()))
    products.sort()
    capacities,repetitions = remove_repetitions_and_sort(capacities)
    solutions = solve(products,capacities)
    print(sum(solution.value*repeats for solution,repeats in zip(solutions,repetitions)))