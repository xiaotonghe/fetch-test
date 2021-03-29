from implement import partition_in_three, weigh, choose_side, get_fake


class TestFetchFakeCoins:
    def test_partition_in_three(self):
        assert partition_in_three([0, 1, 2, 3, 4, 5, 6, 7, 8]) == [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
        ]

        assert partition_in_three([0, 1, 2]) == [[0], [1], [2]]

    def test_weigh(self):
        assert weigh([1, 2, 3], [4, 5, 6]) in ["<", ">", "="]
        assert weigh([1], [2]) in ["<", ">", "="]

    def test_choose_side(self):
        # None means [1, 2, 3] = [4, 5, 6]
        assert choose_side([[1, 2, 3], [4, 5, 6]]) in [
            [1, 2, 3], [4, 5, 6], None]

    def test_getfake(self):
        assert get_fake(4) in ["Yay! You find it!", "Oops! Try Again!"]
