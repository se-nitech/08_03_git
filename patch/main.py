

def calculate_weighted_diff(x, y):
    z = 2 * x - y
    return z


def apply_to_adjacent_pairs(a):
    for i in range(len(a) - 1):
        calculate_weighted_diff(a[i], a[i + 1])

def apply_to_adjacent_pairs_extended(a):
    for i in range(len(a) - 1):
        calculate_weighted_diff(a[i], a[i + 1])


def main():
    a = [1, 2, 3, 4, 5]
    for _ in range(100):
        apply_to_adjacent_pairs(a)
    for _ in range(300):
        apply_to_adjacent_pairs_extended(a)


if __name__ == '__main__':
    main()
