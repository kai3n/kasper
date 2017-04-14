# Let's assume that we have 10 customers
class Customer:
    def __init__(self, d, bid):
        self.d = d  # days that this person wishes to rent one room
        self.bid = bid  # money that this person is willing to pay for the entire stay

# Assign a random value d and bid to each customer
customer1 = Customer(4,10)
customer2 = Customer(5,10)
customer3 = Customer(8,30)
customer4 = Customer(3,10)
customer5 = Customer(7,20)
customer6 = Customer(5,10)
customer7 = Customer(8,15)
customer8 = Customer(2,13)
customer9 = Customer(4,17)
customer10 = Customer(7,9)

# A period of days
D = 15

# Make a group
customers = [0, customer1, customer2, customer3, customer4, customer5,
             customer6, customer7, customer8, customer9, customer10]

# Initialize opt 3-D array
opt = [[[0 for _ in range(D+1)] for _ in range(D+1)] for _ in range(len(customers))]

# Your solution
for i in range(len(customers)):
    for d1 in range(D+1):
        for d2 in range(D+1):
            # initial condition1: OPT(d1, d2, 0) = 0
            if i == 0:
                opt[i][d1][d2] = 0
            elif d1 < customers[i].d and d2 < customers[i].d:
                '''initial condition2: OPT(d1,d2,i) = -∞ if d1 < d[i] or d2 < d[i]
                    Since there is some problems with your initial condition2, I modified "or" to "and"
                    and then added other cases that "if d1 > d[i] and d2 < d[i]" and "if d1 < d[i] and d2 > d[i]"
                    Otherwise, your recurrence is not going to work properly'''
                opt[i][d1][d2] = -9999999
            else:
                if d1 < customers[i].d:
                    # 10 + 1 1 0
                    opt[i][d1][d2] = max(customers[i].bid + opt[i-1][d1][d2-customers[i].d], opt[i-1][d1][d2])
                elif d2 < customers[i].d:
                    opt[i][d1][d2] = max(customers[i].bid + opt[i-1][d1-customers[i].d][d2], opt[i-1][d1][d2])
                else:
                    opt[i][d1][d2] = max(customers[i].bid + opt[i-1][d1-customers[i].d][d2],
                                         customers[i].bid + opt[i-1][d1][d2-customers[i].d],
                                         opt[i-1][d1][d2])
                print("i:{} d1:{} d2:{} profit:{}".format(i, d1, d2, opt[i][d1][d2]))  # test

print("The maximum profit is {}".format(opt[len(customers)-1][D][D]))


# My solution

# Initialize opt 3-D array
opt = [[[[0 for _ in range(D+1)] for _ in range(D+1)] for _ in range(D+1)] for _ in range(len(customers))]
r = [D, D]  # define room1, room2
# opt[i, d, r[r1, r2]]
for i in range(len(customers)):
    for r1 in range(r[0]+1):
        for r2 in range(r[1]+1):
            # initial condition1: OPT(d1, d2, 0) = 0
            if i == 0:
                opt[i][r1][r2] = 0
            elif r1 < customers[i].d and r2 < customers[i].d:
                opt[i][r1][r2] = -9999999
            else:
                if r1 < customers[i].d:
                    opt[i][r1][r2] = max(customers[i].bid + opt[i - 1][r1][r2 - customers[i].d], opt[i - 1][r1][r2])
                elif r2 < customers[i].d:
                    opt[i][r1][r2] = max(customers[i].bid + opt[i - 1][r1 - customers[i].d][r2], opt[i - 1][r1][r2])
                else:
                    opt[i][r1][r2] = max(customers[i].bid + opt[i - 1][r1 - customers[i].d][r2],
                                         customers[i].bid + opt[i - 1][r1][r2 - customers[i].d],
                                         opt[i - 1][r1][r2])
                print("i:{} r1:{} r2:{} profit:{}".format(i, r1, r2, opt[i][r1][r2]))  # test

print("The maximum profit is {}".format(opt[len(customers)-1][r[0]][r[0]]))
