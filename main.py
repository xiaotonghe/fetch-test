from implement import partition_in_three, choose_side, get_fake


def main(coins):
    while True:
        coin_groups = partition_in_three(coins)
        coins = choose_side(coin_groups)
        if len(coins) == 1:
            get_fake(coins[0])
            break


if __name__ == "__main__":
    # generate gold coins from 0 to 8
    coins = [i for i in range(9)]
    main(coins)
