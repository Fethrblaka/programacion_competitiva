def share_numbers(a,b):
    for x in a:
        if(x in b):
            return(True)
    return(False)
    
def repeats_numbers(a):
    is_number_in_a = [False]*10
    for x in a:
        if(is_number_in_a[int(x)] == False):
            is_number_in_a[int(x)] = True
        else:
            return(True)
    return(False)

def checkQuotient(quotient, divisor):
    no_solution = True
    correct_divisors = []
    remaining_numbers = []
    for number in ['0','1','2','3','4','5','6','7','8','9']:
        if(number not in divisor):
            remaining_numbers.append(number)
    for number in remaining_numbers:
        dividend = str(int(number+divisor)*quotient)
        if(len(dividend) <= 5):
            dividend = dividend[-len(number+divisor):]
            if(not share_numbers(dividend,number+divisor) and not repeats_numbers(dividend)):
                if(len(dividend) == 5 and len(number+divisor) == 5):
                    correct_divisors.append(int(number+divisor))
                else:
                    correct_divisors.extend(checkQuotient(quotient,number+divisor))
    return(correct_divisors)

quotient = int(input())
while(quotient != 0):
    solutions = checkQuotient(quotient,'')
    if(len(solutions) == 0):
        print("There are no solutions for",str(quotient)+'.')
    else:
        solutions.sort()
        for solution in solutions:
            print(solution*quotient,'/',('0'+str(solution))[-5:],'=',quotient)
    quotient = int(input())
    if(quotient != 0):
        print()