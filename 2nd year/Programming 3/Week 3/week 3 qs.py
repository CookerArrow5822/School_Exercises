#q1

#O(n) linear

""" There is only one loop which keeps this programs
linearity"""

#q2

""" It is O(logn) due to the fact it cuts the workload into 2 each time
which correlates to the time complexity of O(logn)"""

#q3

#O(n) linear

""" the loops are not nested which calculates to O(2n) which simplifies down
to basic linear time complexity"""

#q4

# O{log n)

"""i which is the counter or n is halved each time causing the time complexity
to be O(log n) as there is only logarithmic growth in terms of time complexity"""

#q5

#O(n^2)

""" there is a nested loop with an unknown making the time complexity
equate to o(n^2)"""

#q6

"""it is due to the fibonacci call being recursive which produces a recursion tree
making it exponential"""

#q7
import math
def log2(n):
    return math.log(n) / math.log(2)

for n in [1, 2, 4, 8, 16, 32, 100]:
    my_answer = log2(n)
    mathlog2 = math.log2(n)

    print (my_answer == math.log2(n))


#q8

def has_duplicate_pairs(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return True
        seen.add(number)

    return False

print (has_duplicate_pairs([1,2,3,4,5]))
print (has_duplicate_pairs([1,2,3,2]))
print (has_duplicate_pairs([7,7,7,7]))