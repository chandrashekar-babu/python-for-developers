def combined_generators():
    yield from range(3)  # 0, 1, 2
    yield from "abc"     # 'a', 'b', 'c'
    yield from [7, 8, 9]  # 7, 8, 9

list(combined_generators())  # [0, 1, 2, 'a', 'b', 'c', 7, 8, 9]