# put your code here
def print_restaurant_ratings(filename):
    """Restaurant rating lister."""

    file = open(filename)
    restaurant_dic = {}
    
    # create dictionary with restaurant as key and score as value
    for line in file:
        stripped_input = line.rstrip()
        name,rating = stripped_input.split(":")
        restaurant_dic[name] = rating
    
    # create list of restaurant names
    # li = list(restaurant_dic.keys())
    # li.sort()
    li = sorted(restaurant_dic)

    # step through restaurant names and print message
    for restaurant in li:
        print("{} is rated at {}.".format(restaurant,restaurant_dic[restaurant]))

print_restaurant_ratings("scores.txt")