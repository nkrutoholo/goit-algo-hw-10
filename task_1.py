COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount: int) -> dict:
    result = {}
    for coin in COINS:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount = amount % coin
    return result


def find_min_coins(amount: int) -> dict:
    min_coins = [0] + [float('inf')] * amount
    last_coin = [0] * (amount + 1)

    for s in range(1, amount + 1):
        for coin in COINS:
            if coin <= s and min_coins[s - coin] + 1 < min_coins[s]:
                min_coins[s] = min_coins[s - coin] + 1
                last_coin[s] = coin
    result = {}
    s = amount
    while s > 0:
        coin = last_coin[s]
        result[coin] = result.get(coin, 0) + 1
        s -= coin
    return result



def compare_performance():
    import timeit

    print("\nПорівняння часу виконання (середнє по 100 запусках):")
    print(f"{'amount':>10} | {'greedy':>14} | {'dynamic':>14}")
    print("-" * 46)
    for amount in [100, 1_000, 10_000, 100_000]:
        t_greedy = timeit.timeit(lambda: find_coins_greedy(amount), number=100) / 100
        t_dp = timeit.timeit(lambda: find_min_coins(amount), number=100) / 100
        print(f"{amount:>10} | {t_greedy * 1000:>11.4f} ms | {t_dp * 1000:>11.4f} ms")


def main():
    amount = 113
    print("Amount: ", amount)
    print("Greedy: ", find_coins_greedy(amount))
    print("DP min: ", find_min_coins(amount))

    compare_performance()


if __name__ == "__main__":
    main()
