

def amount_of_possible_numbers(start_number: int, number_of_moves: int):

    if not isinstance(start_number, int):
        raise TypeError("The start_number can only be of type int")

    if not isinstance(number_of_moves, int):
        raise TypeError("The number_of_moves can only be of type int")

    if not start_number in range(0, 9):
        raise TypeError("The start number needs to be in range 0-9")

    if  number_of_moves < 0:
        raise TypeError("The number of moves can't be negative")

    ecken = 0
    rand_kann_null = 0
    rand = 0
    null_taste = 0



    if start_number in (1, 3, 7, 9):
        ecken += 1

    if start_number in (4, 6):
        rand_kann_null += 1

    if start_number in (2, 8):
        rand += 1

    if start_number == 0:
        null_taste += 1

    if start_number == 5:
        if number_of_moves == 0:
            return 1
        else:
            return 0


    for _ in range(number_of_moves):
            new_ecken = rand_kann_null * 2 + rand * 2
            new_rand_kann_null = ecken + null_taste  * 2
            new_rand = ecken
            new_null = rand_kann_null
            ecken = new_ecken
            rand_kann_null = new_rand_kann_null
            rand = new_rand
            null_taste = new_null

    possible_numbers = ecken + rand_kann_null + rand + null_taste
    

    
    return possible_numbers


def main():

    number_of_moves = int(input("Geben sie die Anzahl der Züge ein : "))
    start_number = int(input("Geben sie die Startzahl ein : "))

    ergebnis = amount_of_possible_numbers(start_number, number_of_moves)

    print(f'die Anzahl der möglichen Zahlen in {number_of_moves} Zügen ist : {ergebnis} !')




if __name__ == '__main__':
    main()
