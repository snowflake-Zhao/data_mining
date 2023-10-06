import math


def cal_entropy(prob_distribution):
    rlt = 0
    for i in prob_distribution:
        rlt = rlt - (i * math.log2(i))
    return rlt

# print(4/7 * cal_entropy([1/4,3/4]))
# print(2/7 * cal_entropy([1/2,1/2]))

# print(4/7 * cal_entropy([1/4,3/4]))
#
# print(3/5*cal_entropy([1/3,2/3]))
print(cal_entropy([1/5,4/5]))
#
# print(4/7 * cal_entropy([1/4,3/4]))


# print(3/12 * cal_entropy([1/3,2/3]) + 9/12 * cal_entropy([1/3,2/3]))
#
# print(2/12 * cal_entropy([1/2,1/2]) + 10/12 * cal_entropy([2/5,3/5]))
#
# print(8/12 * cal_entropy([2/8,6/8]) + 4/12 * cal_entropy([3/4,1/4]))
#
# print(10/12 * cal_entropy([3/10,7/10]))


