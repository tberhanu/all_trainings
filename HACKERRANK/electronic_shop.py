# """ Failed some tests ..."""
# def getMoneySpent(keyboards, drives, b):
#     arr = []
#     for i in range(len(keyboards)):
#         e = keyboards[i] + drives[0]
#         biggest = e
#         small = b - e if e <= b else -1
#         for j in range(len(drives)):
#             e2 = keyboards[i] + drives[j]
#             diff2 = b - e2 if e2 <= b else -1
#             if diff2 != -1 and diff2 < small:
#                 small = diff2
#                 biggest = e2
#         arr.append(biggest)
#
#     return max(arr)
#
# 
# a = [3, 1]
# b = [5, 2, 8]
# c = 10
# print(getMoneySpent(a, b, c))