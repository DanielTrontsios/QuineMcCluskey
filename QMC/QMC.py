from operator import attrgetter
from itertools import combinations


class MinTerm:
    def __init__(self, number, binary):
        self.number = number
        self.binary = binary
        self.ones = self.binary.count('1')

    """
    MinTerm(number, fill) -> MinTerm(number = number,
                                     binary = bin(number),
                                     ones = number of ones in the binary)

    It takes as input a decimal number + the number of digits of the biggest number
    in the input list and converts it to it's binary and counts it's ones.
    """

    def __str__(self):
        return "{0}: {1}".format(self.number, self.binary)

    __repr__ = __str__


# Find the number of digits you need to print
def digit_filler(input_list):
    fill = len(str(bin(max(input_list))[2:]))
    """
    x = digit_filler(input_list) -> int

    Get the number of digits you need to use on every binary number (for presentation purposes).
    """
    return fill


def compare(minterm1, minterm2):
    number1 = minterm1.number
    number2 = minterm2.number
    binary1 = minterm1.binary
    binary2 = minterm2.binary
    position_of_differences = [i for i in range(len(binary1)) if binary1[i] != binary2[i]]
    number_of_differences = len(position_of_differences)
    o1 = minterm1.ones
    o2 = minterm2.ones
    new_minterm = None

    if o1 == (o2 - 1) and number_of_differences == 1:
        binary2 = list(binary2)
        for i in position_of_differences:
            binary2[i] = '-'
        binary2 = "".join(binary2)
        new_minterm = MinTerm("{0},{1}".format(number1, number2), binary2)
    """
    new_minterm = compare(minterm1, minterm2) -> MinTerm
    
    Change the names of the vars for easier usage.
    Get the position of the different digits between the 2 binary numbers,
    Save the number of the differences, calculated above, in a variable for easier usage,
    Change the names of the vars for easier usage,
    Create a new empty minterm,
    
    If the number of ones of minterm1 is less the number of ones of minterm2 by 1,
    and the 2 binary numbers have only 1 different bit,
    Make a list of the digits of the second bin number,
    Get the position of differences calculated before and switch the digits at those positions with -,
    Rejoin the list of digits to a normal number.
    Create the new minterm with the name being a combination of the decimal numbers used(str),
    and the "binary" number we created,
    """
    return new_minterm


def bt_maker(minterms):
    step = 0
    results = minterms
    while True:
        step += 1
        results.append([])

        for minterm1, minterm2 in combinations(results[step - 1], 2):
            new_minterm = compare(minterm1, minterm2)
            exists = False

            if new_minterm:
                for i in results[step]:
                    if i.binary == new_minterm.binary:
                        exists = True
                        break

                if not exists:
                    results[step].append(new_minterm)

        if not results[step]:
            del results[step]
            break

    return results


def main():
    tm = []
    dc = []
    input_list = []
    starting_minterms = []
    big_table = []
    pi_chart = [[]]
    tm_loops = 6
    dc_loops = 2

    # Take the input min terms
    for i in range(tm_loops):
        number = input("Give me the tm: ")
        tm.append(number)
        input_list.append(int(number))

    for i in range(dc_loops):
        number = input("Give me the dc: ")
        dc.append(number)
        input_list.append(int(number))

    filler = digit_filler(input_list)
    input_list.sort()

    # Create true min term list
    for number in input_list:
        starting_minterms.append(MinTerm(str(number), bin(number)[2:].zfill(filler)))

    starting_minterms.sort(key=attrgetter('ones')) # Sort true min term list with key the number of ones (of the binary)

    big_table.append(starting_minterms)

    big_table = bt_maker(big_table)

    for i in big_table[-1]:
        pi_chart[0].append(i.number)

    pi_chart.append(tm)
    pi_chart.append([])

    for matches in pi_chart[0]:
        for tms in pi_chart[1]:
            if tms in matches:
                pi_chart[2].append('x')
            else:
                pi_chart[2].append('-')

    # Debugging print
    for i in big_table:
        print(i)

    print(pi_chart)
    print("tms: ", tm)
    print("dcs: ", dc)


if __name__ == "__main__":
    main()
