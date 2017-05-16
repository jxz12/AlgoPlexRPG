# knapsack
# C(v,i) = max(C(v,i-1), c_i + C(v-w_i, i-1))
# where v is capacity, i is item idx

attrs = [
    {'cost': 2, 'effect': lambda x: x+2, 'name': 'bigger sword'},
    {'cost': 3, 'effect': lambda x: x+3, 'name': 'flaming sword'},
    {'cost': 3, 'effect': lambda x: x*3, 'name': 'pet lion'},
]

# attrs = [
#     {'cost': 1, 'effect': lambda x: x+1},
#     {'cost': 2, 'effect': lambda x: x+6},
#     {'cost': 5, 'effect': lambda x: x+18},
#     {'cost': 6, 'effect': lambda x: x+22},
#     {'cost': 7, 'effect': lambda x: x+28},
# ]

memo = {}

def knapsack(w,i):
    if w < 0:
        return -999
    if i < 0:
        return 0

    if (w,i) not in memo:
        temp1 = knapsack(w,i-1)
        temp2 = attrs[i]['effect'](knapsack(w-attrs[i]['cost'], i-1))

        memo[(w,i)] = max(temp1, temp2)

    return memo[(w,i)]



def fullmemo(w,i):
    if w < 0:
        return -999
    if i < 0:
        return 0
    return memo[(w,i)]

def knapsack_bottomup(_w,_i):
    for w in range(_w+1):
        for i in range(_i+1):
            temp1 = fullmemo(w, i-1)
            temp2 = attrs[i]['effect'](fullmemo(w-attrs[i]['cost'], i-1))

            memo[(w,i)] = max(temp1, temp2)


w=8
i=2
knapsack(w,i)

from numpy import zeros
table = zeros((w+1,i+1))
for tup in memo:
    table[tup[0]][tup[1]] = memo[tup]

print(table)
