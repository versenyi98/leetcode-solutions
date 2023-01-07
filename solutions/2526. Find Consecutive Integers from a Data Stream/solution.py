class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.number_of_consec_values = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.number_of_consec_values += 1
        else:
            self.number_of_consec_values = 0
        return self.number_of_consec_values >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)