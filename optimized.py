# algo du sac à dos
import csv
import sys
import time
from itertools import combinations

start_time = time.time()
MAX_INVEST = 500


def main():
    brute_force()  # à remplacer avec knapsack
    shares_list = read_csv()
    max_invest = int(MAX_INVEST * 100)  # max_invest - W
    shares_total = len(shares_list)  # les actions - n
    costs = [int(i[1] * 100) for i in shares_list]   # weights
    profits = [int(i[2] * 100) for i in shares_list]  # values
    # knap_sack(max_invest, costs, profits, shares_total)
    kSack(max_invest, costs, profits)


def kSack(W, wt, val):
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif wt[i-1] <= j:
                table[i][j] = max(val[i-1]
                                  + table[i-1][j-wt[i-1]],  table[i-1][j])
            else:
                table[i][j] = table[i-1][j]

    print(table[n][W])


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


def read_csv():
    file = sys.argv[1] if len(sys.argv) > 1 else "data/data_set_2.csv"
    with open(file) as csvfile:
        shares_file = csv.reader(csvfile, delimiter=',')

        shares_list = []
        for row in shares_file:
            if float(row[1]) > 0:  # vérif si coût > 0E
                shares_list.append(
                    (row[0], float(row[1]), float(row[2]))
                )

        return shares_list

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

# optimize
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# W => capacity
# wt => weight
# val


def knap_sack(max_invest, costs, profits, shares_total):

    # Base Case
    # on vérifie que la capacité ou nombre actions ne soit pas égale à 0
    if shares_total == 0 or max_invest == 0:
        return 0

    # If weight (coût) of the nth item is
    # more than Knapsack of capacity (max_invest),
    # then this item cannot be included
    # in the optimal solution (profit)

    # on vérifie si 1 valeur (cost) ne soit pas supérieur à la capacité max_invest
    # ici W == 500
    if (costs[shares_total-1] > max_invest):
        return knap_sack(max_invest, costs, profits, shares_total-1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        try:
            return max(
                profits[shares_total-1] + knap_sack(
                    max_invest-costs[shares_total-1], costs, profits, shares_total-1),
                knap_sack(max_invest, costs, profits, shares_total-1))
        except Exception:
            breakpoint()


def display_results(best_combo):
    """Display best combination results
    @param best_combo: most profitable shares combination (list)
    """
    print(f"Best investment : {calc_cost(best_combo)}€")

    print("\nTotal cost : ", calc_cost(best_combo), "€")
    print("Profit after 2 years : +", calc_profit(best_combo), "€")
    print("=======================================")
    print("\nTime elapsed : ", time.time() - start_time, "seconds\n")


main()
