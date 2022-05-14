###########
# IMPORTS #
###########

import webscraping as ws
import costants


#############
# FUNCTIONS #
#############

def dict_list_find_by(dict_list, item, key):
    """
    Search in the whole dict if "item" under "key" exist

    :param dict_list: dict in which search
    :type dict_list: dict

    :param item: key value to search
    :type item: str

    :param key: key that contains the item
    :type key: str

    :return: item position or -1 if not found
    """

    for index in range(len(dict_list)):
        if item in dict_list[index][key]:
            return index

    return -1  # Not found case


def dict_list_clean(dict_list, keylist):
    """
    Remove from a dict all the selected keys

    :param dict_list: dict to clean
    :type dict_list: dict

    :param keylist: List of keys to remove
    :type keylist: list

    :return: Cleaned dict
    """

    for index in range(len(dict_list)):
        for key in keylist:
            try:
                dict_list[index].pop(key)
            except KeyError:
                continue

    return dict_list


def print_dict(dict_var):
    """
    Simply print a given dict in a better way

    :param dict_var: dict to print
    :type dict_var: dict
    """

    for key, value in dict_var.items():
        print(f"{key}: {value}")


########
# MAIN #
########

if __name__ == "__main__":
    print("\n\n")

    # Scraping infos
    cryptos_temp = ws.extract_json(costants.API)['coins']

    # Remove useless informations
    cryptos = dict_list_clean(cryptos_temp, costants.REMOVE_PARAMS)

    print_str = []
    maxlen = 0
    for i in range(len(cryptos)):
        print_str.append(f"{cryptos[i]['symbol']}: ${round(cryptos[i]['price'], 7)}")
        if len(print_str[i]) > maxlen:
            maxlen = len(print_str[i])

    # Count some more chars to avoid "collisions" between columns
    maxlen += 2

    # Ordinated string printing
    for i in range(len(print_str)):
        if i % costants.COLUMNS < costants.COLUMNS-1:
            print(print_str[i], end="")

            # Add some spaces to align columns
            for x in range(maxlen - len(print_str[i])):
                print(" ", end="")
        else:
            print(print_str[i])

    # Find the index of a specific symbol
    idx = dict_list_find_by(cryptos, input("\n\n\nSelect a crypto for more information: "), 'symbol')

    # Print the informations about a selected crypto
    print_dict(cryptos[idx])
