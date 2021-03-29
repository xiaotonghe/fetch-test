from WebController import WebControl

global control
control = WebControl()


def partition_in_three(coins: list):
    """partition coins into 3 groups"""
    steps = len(coins) // 3
    index = 0
    gold_list = []
    for _ in range(3):
        gold_list.append(coins[index: index + steps])
        index += steps
    return gold_list


def weigh(leftSide: list, rightSide: list):
    """weigh coins and return the sign of weigh result"""
    control.fill_bowl(leftSide, "left")
    control.fill_bowl(rightSide, "right")
    control.click_weigh()
    result = control.get_result()
    control.click_reset()
    return result


def choose_side(coin_groups: list):
    """compared all coin groups by pairs and return the side with fake coin to continue"""
    for i in range(len(coin_groups)):
        for j in range(i + 1, len(coin_groups)):
            sign = weigh(coin_groups[i], coin_groups[j])
            if sign == "<":
                return coin_groups[i]
            elif sign == ">":
                return coin_groups[j]


def get_fake(coin: int):
    """put fake coin index to check result"""
    alert = control.click_fakebar(coin)
    weighs = control.get_weighing()
    if alert == "Yay! You find it!":
        print(f"the fake gold is {coin}")
    control.close_driver()
    return alert
