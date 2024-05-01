from random import randint
import time

trials = 10000000

def knapsackmcmc(items, max_weight, trials): 
    n = len(items)
    b = max_weight
    a = items
    sols = {} # list of solutions for [0,b]
    for i in range(n, 0, -1):
        x = [0] * (n)
        b_i = min(b, sum(a[:(i)]))
        b_iminus1 = min(b, sum(a[:(i-1)]))
        countsols_biminus1 = 0 
        for j in range(trials): 
            coinflip = randint(0,1)
            rand_index = randint(0, n-1) 
            old_value = x[rand_index] 
            x[rand_index] = coinflip

            if sum(x) <= b_iminus1: 
                countsols_biminus1 += 1 
            if not sum(x) <= b_i: 
                x[rand_index] = old_value  
        sols[str(b_i) + "," + str(b_iminus1)] = [trials, countsols_biminus1]
    print("Ratios:", sols)
    total = 1
    for i in sols: 
        total *= sols[i][0]/(sols[i][1])
    return total

# for n=3, b=3, the solutions are as follows:
# b = 3: 111 
# b = 2: 110, 101, 011
# b = 1: 100, 010, 001
# b = 0 : 000 
# total 8 

answer = input("Would you like to run your own example? Otherwise, it run preset examples. Press 1 if yes: ")

if answer == '1': 
    user_list = input("Enter your items weight, separated by a comma. For example '1,2,3'. : ").split(',')
    item_input = sorted([int(i) for i in user_list])
    weight_input = int(input("What is the max weight of your Knapsack?: "))

    start_time = time.time()
    estimate = knapsackmcmc(item_input, weight_input, trials)
    end_time = time.time() 
    print("The estimate of total solutions of the Knapsack problem with items %s and max weight %d is %f" % (item_input, weight_input, estimate))
    print("Time to run: %f seconds" % (end_time-start_time))

answer2 = input("Would you like to see preset examples? If yes, press 1: ")

if answer2 == '1': 
    print("--- Example 1 ---") 
    ex1items = [1,1,1]
    ex1weight = 3
    print("Items: %s" % ex1items)
    print("Weight: %d" % ex1weight)

    start_time = time.time()
    estimate1 = knapsackmcmc(ex1items, ex1weight, trials)
    end_time = time.time() 
    print("The estimate of total solutions of the Knapsack problem with items %s and max weight %d is %f" % (ex1items, ex1weight, estimate1))
    print("Time to run: %f seconds" % (end_time-start_time))


    # Example 2
    print("--- Example 2 ---") 
    ex2items = [1,2,3,4,5]
    ex2weight = 11
    print("Items: %s" % ex2items)
    print("Weight: %d" % ex2weight)

    start_time = time.time()
    estimate2 = knapsackmcmc(ex2items, ex2weight, trials)
    end_time = time.time() 
    print("The estimate of total solutions of the Knapsack problem with items %s and max weight %d is %f" % (ex2items, ex2weight, estimate2))
    print("Time to run: %f seconds" % (end_time-start_time))

    # Example 3
    print("--- Example 3 ---") 
    items_input = [1,1,1,1,1,1,1,1,1,1]
    weight_input = 5
    print("Items: %s" % items_input)
    print("Weight: %d" % weight_input)

    start_time = time.time()
    estimate = knapsackmcmc(items_input, weight_input, trials)
    end_time = time.time() 
    print("The estimate of total solutions of the Knapsack problem with items %s and max weight %d is %f" % (items_input, weight_input, estimate))
    print("Time to run: %f seconds" % (end_time-start_time))

    # Example 4
    items_input = sorted([randint(1, 10) for i in range(10)])
    weight_input = randint(0,100)

    print("--- Example 4, Randomly Generated ---") 
    print("Items: %s" % items_input)
    print("Weight: %d" % weight_input)

    start_time = time.time()
    estimate = knapsackmcmc(items_input, weight_input, trials)
    end_time = time.time() 
    print("The estimate of total solutions of the Knapsack problem with items %s and max weight %d is %f" % (items_input, weight_input, estimate))
    print("Time to run: %f seconds" % (end_time-start_time))

