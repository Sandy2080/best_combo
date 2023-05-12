from tqdm import tqdm

import csv
import sys
import time
from itertools import combinations

start_time = time.time()
MAX_INVEST = 5001


def main():
    """Check for filename input"""
    try:
        filename = "data/" + sys.argv[1] + ".csv"
    except IndexError:
        print("\nNo filename found. Please try again.\n")
        time.sleep(1)
        sys.exit()

    shares_list = read_csv(filename)

    print(
        f"\nProcessing '{sys.argv[1]}' ({len(shares_list)} valid shares) for {MAX_INVEST}€ :")

    max_invest = int(MAX_INVEST * 100)
    shares_total = len(shares_list)
    cost = []       # weights
    profit = []     # values

    for share in shares_list:
        cost.append(share[1])
        profit.append(share[2])

    knapSack(max_invest, cost, profit, shares_total, shares_list)

    return 0

# optimize
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# W => capacity
# wt => weight
# val


def knapSack(max_invest, cost, profit, shares_total, shares_list):
    """(ks) for 0-1 knapsack problem
     @param shares_list: max_invest (max capacity), cost (weight), profit (values), shares_total, shares_list
     @return: best combinaition and best return on investment
    """

    #
    # TABLE with actions list and max investissement
    ks = [[0 for x in range(max_invest + 1)] for x in range(shares_total + 1)]

    # looping thru the actions to find optimal profit
    for i in tqdm(range(1, shares_total + 1)):

        for w in range(1, max_invest + 1):
            # while cost < W or max invest, add action to table or knapsack
            if cost[i-1] <= w:
                # Get max profit bet.
                # 1- get max profit for every combo
                # 2- if cost not exceeding the max invest (max capacity)
                ks[i][w] = max(ks[i-1][w], ks[i-1][w-cost[i-1]] + profit[i-1])
            else:
                ks[i][w] = ks[i-1][w]

    print(f"\nBest investment : {ks[shares_total][max_invest]}€")
    print("\nTime elapsed : ", time.time() - start_time, "seconds\n")


# bruteforce


def brute_force():

    # read csv
    shares_list = read_csv()
    best_profit = 0
    best_combo = []
    # generate all combos
    for i in range(len(shares_list)):
        combos = combinations(shares_list, i+1)

        # combos = get_combos(shares_list)
        # filter combos - must be < 500E + calculate profits
        combos = [combo
                  for combo in combos if calc_cost(combo) <= 500]

        # return best profit
        for combo in combos:
            total_profit = calc_profit(combo)
            if total_profit > best_profit:
                best_profit = total_profit
                best_combo = combo
    display_results(best_combo)


def get_combos(shares):
    for i in range(len(shares)):
        combos = combinations(shares, i+1)
        return combos


# def best_combo_and_profit(combos):

def read_csv(filename):
    """read and load data from csv file
    @return: list of shares
    """
    try:
        with open(filename) as csvfile:
            shares_file = csv.reader(csvfile, delimiter=',')

            if filename != "data/test_shares.csv":
                next(csvfile)       # skip first row in both datasets

            shares_list = []

            for row in shares_file:
                if float(row[1]) <= 0 or float(row[2]) <= 0:
                    pass
                else:
                    share = (
                        row[0],
                        int(float(row[1])*100),
                        float(float(row[1]) * float(row[2]) / 100)
                    )
                    shares_list.append(share)

            return shares_list

    except FileNotFoundError:
        print(f"\nFile '{filename}' does not exist. Please try again.\n")
        time.sleep(1)
        sys.exit()
# calcul coût investissement


def calc_cost(combo):

    prices = []
    for el in combo:
        prices.append(el[1])

    return sum(prices)

# calcul retour sur investissement


def calc_profit(combo):
    profits = []
    for el in combo:
        profits.append(el[1] * el[2] / 100)

    return sum(profits)


def display_results(best_combo):
    print(f"Best investment : {calc_profit(best_combo)}€")
    print("=======================================")
    print("\nTime elapsed : ", time.time() - start_time, "seconds\n")


main()
