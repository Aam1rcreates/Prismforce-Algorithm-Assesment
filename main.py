def can_abhinanyu_cross_chakravyuha(k, p, a, b):
    n = len(k)
    i = 0  # Start at the innermost circle

    while i < n:
        # Skip the battle if he has the option and enough skips left
        if a > 0:
            a -= 1
            i += 1
            continue

        # Recharge if needed and available
        if b > 0 and p <= k[i]:
            p += k[i]
            b -= 1
            continue

        # Battle with the enemy
        if p > k[i]:
            p -= k[i]
            i += 1
        else:
            return False

        # Check if enemy k3 or k7 can regenerate
        if i == 3 or i == 7:
            regenerated_power = k[i-1] // 2
            if i + 1 < n:
                if p > regenerated_power:
                    p -= regenerated_power
                else:
                    return False

    return True


# Test cases
test_cases = [
    # (k, p, a, b, expected_output)
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 15, 2, 1, True),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 10, 1, 1, False),
]

for idx, (k, p, a, b, expected) in enumerate(test_cases):
    result = can_abhinanyu_cross_chakravyuha(k, p, a, b)
    print(f"Test Case {idx + 1}: {'Passed' if result == expected else 'Failed'}")