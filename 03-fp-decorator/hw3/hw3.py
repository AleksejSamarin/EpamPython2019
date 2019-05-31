def collatz_steps(n, calls=0):
    return collatz_steps(3 * n + 1 if n % 2 else int(n / 2), calls=calls + 1) if n != 1 else calls


assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152
