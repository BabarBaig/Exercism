def steps(number: int) -> int:
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    step_count = 0
    while number > 1:
        # Perform integer division below -- far more efficient than float division
        number = number // 2 if number % 2 == 0 else number * 3 + 1
        step_count += 1
    return step_count
