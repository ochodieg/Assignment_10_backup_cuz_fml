def get_generations() -> list:
    """returns a list of generations"""
    generation_lst = ["Greatest (1901-1924)",
                      "Traditionalists (1925-1945)",
                      "Baby Boomers (1946-1964)",
                      "Gen X (1965-1980)",
                      "Millennials (1981-1996)",
                      "iGen (1997-2010)",
                      "Gen Alpha (2011-Present)"]
    return generation_lst



def get_generation_idx(year: int) -> int:
    """accepts a year and returns an
    index value"""
    ndx = -1
    if 1901 <= year <= 1924:
        ndx = 0
    elif 1925 <= year <= 1945:
        ndx = 1
    elif 1946 <= year <= 1964:
        ndx = 2
    elif 1965 <= year <= 1980:
        ndx = 3
    elif 1981 <= year <= 1996:
        ndx = 4
    elif 1997 <= year <= 2010:
        ndx = 5
    elif 2011 <= year <= 2021:
        ndx = 6

    return ndx


def get_year_tuples(yrs: list) -> list:
    """accepts list of years and returns a list of
    tuples in the format: (year, generation_index based
    on the get_generation_idx() function"""
    year_list = []

    for year in yrs:
        year_ndx = get_generation_idx(year)
        tuple_pair = (year, year_ndx)
        year_list.append(tuple_pair)
    return year_list

listt = get_year_tuples([1965, 1934, 1976, 1985, 2021])
# listt = get_year_tuples([2005, 1934, 1976, 1985, 1990])

print("the list is: " + str(listt))

def get_table(tple_lst: list) -> str:
    accumulator = 0
    gen_list = get_generations()
    accumulated = ""
    yrz = ""
    description = ""
    liststr = ""
    table2 = []
    stringlist = ""

    for itm in range(len(tple_lst)):

        accumulator += 1
        description = gen_list[tple_lst[itm][1]]
        yrz = str(tple_lst[itm][0])
        accumulated = str(accumulator)

        # stringlist += (str(accumulated) + "\t" + yrz + "\t" + description) + "\n"
        stringlist += "{}\t{}\t{}\n".format(str(accumulated), yrz, description)

    table = "{}\t{}\t{}\n{}".format("#", "Year", "Generation", stringlist)

    return table

print(get_table(listt))

def get_average(tuple_lst:list) -> int:

    divisor = 0
    accumulated = 0
    for itm in tuple_lst:
        accumulated += itm[0]
        divisor += 1

    avrg = round(accumulated/divisor)

    return avrg

print("get_average returns an average year of: " + str(get_average(listt)))


def get_newest(tuple_lst:list) -> int:

    accumulator = -1
    order_lst = []
    for itm in tuple_lst:
        accumulator += 1
        order_lst.append(itm[0])
        order_lst.sort()
    highest = order_lst[accumulator]

    return highest


print("get_newest returns the highest year in the list of tuples: " + str(get_newest(listt)))


def get_oldest(tuple_lst:list) -> int:

    accumulator = -1
    order_lst = []
    for itm in tuple_lst:
        accumulator += 1
        order_lst.append(itm[0])
        order_lst.sort()
    order_lst.reverse()
    lowest = order_lst[accumulator]
    return lowest


print("get_oldest returns the oldest year in the list of tuples: " + str(get_oldest(listt)))

