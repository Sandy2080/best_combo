from tqdm import tqdm

import csv
import sys
import time
from itertools import combinations

start_time = time.time()
MAX_INVEST = 500


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

    best_combo = knapSack(max_invest, cost, profit, shares_total, shares_list)
    display_results(best_combo)
    return 0

# optimize
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# W => capacity
# wt => weight
# val


def knapSack(max_invest, cost, profit, shares_total, shares_list):
    """Initialize the matrix (ks) for 0-1 knapsack problem
     Get best shares combination

     @param shares_list: shares data (list)
     @return: best possible combination (list)
    """

    # TABLE with actions list and max investissement
    ks = [[0 for x in range(max_invest + 1)] for x in range(shares_total + 1)]

    # looping thru the actions to find optimal profit
    for i in tqdm(range(1, shares_total + 1)):

        for w in range(1, max_invest + 1):
            # while cost < W or max invest, add action to table or knapsack
            if cost[i-1] <= w:
                # Get max profit bet.
                # 1- if weight not exceeding the max invest (max capacity)
                # 2- return max profit from previous object
                ks[i][w] = max(ks[i-1][w], ks[i-1][w-cost[i-1]] + profit[i-1])
            else:
                # if no better max profit is found, returns previous max profit
                ks[i][w] = ks[i-1][w]

    # Retrieve combination of shares from optimal profit
    # 1- retrieve max and best profit in the table
    best_combo = []

    while max_invest >= 0 and shares_total >= 0:

        if ks[shares_total][max_invest] == \
                ks[shares_total-1][max_invest - cost[shares_total-1]] + profit[shares_total-1]:

            best_combo.append(shares_list[shares_total-1])
            max_invest -= cost[shares_total-1]

        shares_total -= 1

    return best_combo


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
    """Sum of current share combo profit
    @param combo: list of shared combo
    @return: total costs
    """

    costs = []
    for el in combo:
        costs.append(el[1] / 100)

    return sum(costs)

# calcul retour sur investissement


def calc_profit(combo):
    """Sum of current share combo profit
    @param combo: list of shared combo
    @return: total profits
    """

    profits = []
    for el in combo:
        profits.append(el[2])

    return sum(profits)


def display_results(best_combo):
    """Display best combination results with costs, profits and time elapsed
    @param best_combo: most profitable shares combination
    """
    print(f"\nMost profitable investment ({len(best_combo)} shares) :\n")
    for item in best_combo:
        print(f"{item[0]} | {item[1] / 100} € | +{item[2]} €")

    print("\nTotal cost : ", calc_cost(best_combo), "€")
    print("Profit after 2 years : +", calc_profit(best_combo), "€")
    print("\nTime elapsed : ", time.time() - start_time, "seconds\n")


main()
