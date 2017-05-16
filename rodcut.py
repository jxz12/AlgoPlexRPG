# rod cut:
# V_n = max_i(V_n-i + p_i)
# where n is length, p is price

# rpg:
# V_n = max_i(e_i(V_n-c_i))
# where n is points, e is effect, c is cost

attrs = [
    {'cost': 2, 'effect': lambda x: x+2, 'name': 'bigger sword'},
    {'cost': 3, 'effect': lambda x: x+3, 'name': 'flaming sword'},
    {'cost': 3, 'effect': lambda x: x*3, 'name': 'pet lion'}
]

# attrs = [
#     {'cost': 1, 'effect': lambda x: x+1, 'name': '1'},
#     {'cost': 2, 'effect': lambda x: x+5, 'name': '2'},
#     {'cost': 3, 'effect': lambda x: x+8, 'name': '3'},
#     {'cost': 4, 'effect': lambda x: x+2, 'name': '4'},
#     {'cost': 5, 'effect': lambda x: x+10, 'name': '5'},
#     {'cost': 6, 'effect': lambda x: x+17, 'name': '6'},
#     {'cost': 7, 'effect': lambda x: x+17, 'name': '7'},
#     {'cost': 8, 'effect': lambda x: x+20, 'name': '8'},
# ]

memo = {0:0}
choices = {}

def rodcut(w):
    if w < 0:
        return -999

    if w not in memo:
        # initialise to 0
        memo[w] = 0
        for attr in attrs:
            # if you don't know lambdas, they are simply variables you can treat like functions
            attack = attr['effect'](rodcut(w - attr['cost']))
            # keep track of the max
            if attack > memo[w]:
                memo[w] = attack
                choices[w] = attr['name']

    return memo[w]


rodcut(8)
print(memo)
print(choices)