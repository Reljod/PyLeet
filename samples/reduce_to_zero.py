class NumReducer:
    
    def __init__(self, initial_num) -> None:
        self.initial_num = initial_num
        self.current_num = initial_num
        self.reduce_times = 0
    
    def __str__(self) -> str:
        return f"Initial num: {self.initial_num}, current num: {self.current_num}, reduce times: {self.reduce_times}"
    
    def reduce_number_to_zero(self):
        if (self.current_num == 0):
            return
        
        self.reduce_times += 1
        # print(self) 
        is_even = self.current_num % 2 == 0
        
        if (is_even):
            self.current_num /= 2
            return self.reduce_number_to_zero()
        else:
            self.current_num -= 1
            return self.reduce_number_to_zero()
        
    def get_reduce_times(self):
        return self.reduce_times


def main():
    num_reducer = NumReducer(initial_num=23769)
    num_reducer.reduce_number_to_zero()
    
    print(f"Reduce times: {num_reducer.get_reduce_times()}")


if __name__ == '__main__':
    main()