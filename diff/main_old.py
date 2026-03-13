

def calculate_weights(x, y):
    z = 2 * x - y + 1
    return z


def apply_to_adjacent_pairs(a):
    for i in range(len(a) - 1):
        calculate_weights(a[i], a[i + 1])


def main():
    a = [1, 2, 3, 4, 5]
    apply_to_adjacent_pairs(a)


if __name__ == '__main__':
    main()
