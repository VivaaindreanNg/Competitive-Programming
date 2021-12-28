def solve(input_str: str, adjacent_num: int) -> int:
    input_str_list = input_str.rstrip().lstrip().split()
    greatest_prod = 0
    tmp = None


    for row in input_str_list:
        # Use sliding-window technique
        for idx, _ in enumerate(row):
            start_idx = idx 
            end_idx = start_idx+adjacent_num
            total = 1

            if end_idx <= len(row):
                window_str = row[start_idx:end_idx]
                for i in window_str:
                    total *= int(i)

                if total > greatest_prod:
                    greatest_prod = total
                    tmp = window_str

    print(f"Adjacent digits: {tmp}")

    return greatest_prod
