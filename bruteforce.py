
import csv
from itertools import combinations


def main():
    shares_list = read_csv()
    calculate_best_profit(shares_list)


def calculate_best_profit(shares):
    print("calculation in progress ... ")
    profit = 0
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

                if total_profit > profit:
                    profit = total_profit
                    best_combo = combo
    print(f"Meilleur investissement : {calc_cost(best_combo)}€")
    print(f"Meilleur profit : {profit}€")


def read_csv():
    with open("data/data_set.csv") as csvfile:
        shares_file = csv.reader(csvfile, delimiter=',')

        shares_list = []
        for row in shares_file:
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


main()
