max_even_number = 100


def even_number_generator(max_val):
    for number in range(0, max_val, 2):
        yield number


if __name__ == "__main__":
    generated_even = even_number_generator(max_even_number)
    for even in generated_even:
        print(even)
