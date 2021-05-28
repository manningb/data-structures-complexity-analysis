def linear_search(search_area, search_key):
    for i in range(len(search_area)):
        if search_area[i] == search_key:
            return i
    return -1


linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
