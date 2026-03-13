

# today's new version
def calculate_weights(x, y):
    z = 2 * x - y * 0.99
    return z

## equation modified
# def calculate_weights(x, y):
#     z = 2 * x - y
#     return z

## # a simple mistake ...
## def calculate_weights(x, y):
##     z = 2 * x - y + 1
##     return z

## # # new version
## # def calculate_weights(x, y):
## #     z = 2 * x - z + 1
## #     return z

#### def calculate_weights(x, y):
####     z = 2 * x - y
####     return z


def apply_to_adjacent_pairs(a):
    for i in range(len(a) - 1):
        calculate_weights(a[i], a[i + 1])


def main():
    a = [1, 2, 3, 4, 5]
    apply_to_adjacent_pairs(a)


if __name__ == '__main__':
    main()
