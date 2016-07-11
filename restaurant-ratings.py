# your code goes here
def print_restaurant_rating(filename):
    """returns sorted list of restaurants and their ratings"""

    the_file = open(filename)
    all_restaurant = {} 
    restaurant_info =[]

    #for loop to create dictionary with restaurants and ratings
    for line in the_file:
        restaurant_info = line.rstrip().split(":")
        all_restaurant[restaurant_info[0]] = restaurant_info[1]

    sorted_all_restaurant = sorted(all_restaurant)

    #for loop to loop over new list and call on value from dictionary. 
    #Returns both in string. 
    for restaurant in sorted_all_restaurant:
        print "{} is rated at {}.".format(restaurant,all_restaurant[restaurant])

print_restaurant_rating("scores.txt")