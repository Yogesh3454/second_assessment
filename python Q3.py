def print_door_mat(N, M):
    # Upper Part
    for i in range(N // 2):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(M, '-'))

    # Middle Part
    print("WELCOME".center(M, '-'))

    # Lower Part
    for i in reversed(range(N // 2)):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(M, '-'))

# Example usage
N = 7  # Number of rows
M = 21  # Number of columns (3 times N)
print_door_mat(N, M)