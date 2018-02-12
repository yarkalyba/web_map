from collections import defaultdict
from location import get_loc


def intro():
    """
    Function gets the year for which the location of the films will be found
    and number of the locations
    (None) -> tuple(int, int)
    return: tuple of a year and number of locations
    """

    try:
        year = int(input("Enter a year: "))
        loc_num = int(input("Enter the number of "
                            "locations(best choice is 5-10): "))
        assert (loc_num >= 0)
        return year, loc_num
    except ValueError:
        return intro()
    except AssertionError:
        return intro()


year, loc_num = intro()


def read():
    """
    Function returns dictionary with keys as coordinates and
    values as names of the films filmed on that locations
    (None) -> dict
    return: dictionary(key - location, value - films)
    or string with the message that no films where found
    """

    dict_loc = defaultdict(set)
    with open("locations.list", encoding="utf-8", errors="ignore") as f:
        line = f.readline()
        while not line.startswith("="):
            line = f.readline()
            pass

        for line in f:
            if ("({0})").format(year) in line:
                line = line.strip()

                if line.endswith(")"):
                    line = line[:-((line[::-1]).index("(") + 1)].strip()

                key_loc = get_loc(line.split("\t")[-1].strip())
                dict_loc[key_loc].add(line.split('({})'.format(year))[0])
                print("Loading... {}/{}".format(len(dict_loc.keys()), loc_num))
                if len(dict_loc.keys()) >= loc_num:
                    break

    if len(dict_loc.keys()) == 0:
        print("No films found in this year")

    return dict_loc
