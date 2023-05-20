
import csv
from itertools import combinations
import time
import copy
start_time = time.time()


def main():
    shares_list = read_csv()
    best_combo = calculate_best_profit(shares_list)
    best_combo = brute_force()
    display_results(best_combo)


def calculate_best_profit(shares):
    print("calculation in progress ... ")
    best_profit = 0
    best_combo = []
    for i in range(len(shares)):
        combos = combinations(shares, i+1)

        for combo in combos:
            # 1-j'achète des actions
            total_cost = calc_cost(combo)

            # 2-je vérifie que mes stocks <= 500E
            if total_cost <= 500:

                # 3-je calcule le meilleur retour sur investissement
                total_profit = calc_profit(combo)

                if total_profit > best_profit:
                    best_profit = total_profit
                    best_combo = combo
    return best_combo

# pour tester toutes les combinaisons possibles


def brute_force():

    # read csv
    shares_list = read_csv()
    best_profit = 0
    memory = 0
    best_combo = []
    # generate all combos
    for i in range(len(shares_list)):

        combos = combinations(shares_list, i+1)
        combos_copy = copy.copy(combos)

        # calcul complexité spatiale
        memory = memory + len(list(combos_copy))

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
    print("\nmemory space : ", str(memory))
    return best_combo


def read_csv():
    with open("data/data_set.csv") as csvfile:
        shares_file = csv.reader(csvfile, delimiter=',')

        shares_list = []
        for row in shares_file:
            shares_list.append(
                (row[0],  float(
                    row[1]), float(row[2])))

        return shares_list

# calcul coût investissement


def calc_cost(combo):
    costs = []
    for el in combo:
        costs.append(el[1])
    return sum(costs)

# calcul retour sur investissement


def calc_profit(combo):
    profits = []
    for el in combo:
        profits.append(el[1] * el[2] / 100)
    return sum(profits)


def display_results(best_combo):
    """Display best combination results
    @param best_combo: most profitable shares combination (list)
    """
    print("\nTotal cost : ", calc_cost(best_combo), "€")
    print(f"Best investment : {calc_profit(best_combo)}€")
    print("=======================================")
    print("\nTime elapsed : ", time.time() - start_time, "seconds\n")


main()
