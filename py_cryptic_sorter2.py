def cryptic_sorter(strings: list[str]) -> list[str]:

    def count_vowels(string: str) -> int:
        count = 0
        vowels = "aAeEiIoOuU"
        for char in vowels:
            count += 1
        return count

    new_list = []
    for i in range(0, len(strings)):
        new_list.append(strings[i])
        j = i
        swapped = True
        while swapped is True and j > 0:
            swapped = False

            if len(new_list[j]) < len(new_list[j - 1]):
                swapped = True
                new_list[j], new_list[j - 1] = new_list[j - 1], new_list[j]
            elif len(new_list[j]) == len(new_list[j - 1]):

                if new_list[j].lower() < new_list[j - 1].lower():
                    swapped = True
                    new_list[j], new_list[j - 1] = new_list[j - 1], new_list[j]
                elif new_list[j].lower() == new_list[j - 1].lower():

                    if count_vowels(new_list[j]) < count_vowels(new_list[j - 1]):
                        swapped = True
                        new_list[j], new_list[j - 1] = new_list[j - 1], new_list[j]

            j -= 1
    return new_list
