import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--start', type=int)
parser.add_argument('--end', type=int)

args = parser.parse_args()


def validate(password):
    # Will error out if I'm feeding in non 6 digit integers outside of the range
    assert isinstance(password, int)  # It is an integer
    assert len(str(password)) == 6  # It is 6 digits
    assert start <= password <= end  # It is in the range

    digit_list = [int(digit) for digit in str(password)]

    is_identical = False  # Has 2 adjacent identical digits
    is_increasing = True  # Digits increase or stay the same
    digits_strict_identical = set()  # For part 2
    digits_strict_not_identical = set()  # Digits that are 3 identical in a row

    for x in range(0, len(digit_list) - 1):
        if digit_list[x] == digit_list[x + 1]:
            is_identical = True
            digits_strict_identical.add(digit_list[x])
            if x + 2 < len(digit_list) and digit_list[x] == digit_list[x + 1] == digit_list[x + 2]:
                digits_strict_not_identical.add(digit_list[x])
        elif digit_list[x] > digit_list[x + 1]:
            is_increasing = False

    # Both must be true
    return is_identical and is_increasing, \
    len(digits_strict_identical.difference(digits_strict_not_identical)) > 0 and is_increasing


if __name__ == "__main__":
    start = args.start
    end = args.end
    valid_count = 0
    valid_count_strict = 0

    for password_candidate in range(start, end + 1):
        valid, valid_strict = validate(password_candidate)
        if valid:
            valid_count += 1
        if valid_strict:
            valid_count_strict += 1

    print(f"Part One {valid_count}")
    print(f"Part Two {valid_count_strict}")