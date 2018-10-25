class network:
    def __init__(self, E):
        self.employes = E
        self.friends  = [[]]*E
        
    def add_friends(self, friends_list, employe_index):
        self.friends[employe_index] = friends_list
        
    def get_boom_list(self, source_employe_index):
        if(len(self.friends[source_employe_index]) > 0):
            employe_is_aware = [False]*self.employes
            employe_is_aware[source_employe_index] = True
            nextday = [source_employe_index]
            boom_list = [0]
            while(len(nextday) > 0):
                today = nextday
                nextday = []
                for employe in today:
                    for friend in self.friends[employe]:
                        if(not employe_is_aware[friend]):
                            nextday.append(friend)
                            employe_is_aware[friend] = True
                boom_list.append(len(nextday))
            return(boom_list)
        else:
            return([0])


        
employes = int(input())
case = network(employes)
for employe in range(employes):
    case.add_friends(list(map(int, input().split()[1:])), employe)
tests = int(input())
for test in range(tests):
    boom_list = case.get_boom_list(int(input()))
    biggest_boom = max(boom_list)
    print(biggest_boom,end='')
    if(biggest_boom > 0):
        print(' ' + str(boom_list.index(biggest_boom)))
    else:
        print()      
        