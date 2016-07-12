# your code goes here
def restaurant_dict_from_file(filename):
    """returns sorted list of restaurants and their ratings"""

    the_file = open(filename)
    restaurant_from_file = {} 
    restaurant_info =[]

    #for loop to create dictionary with restaurants and ratings
    for line in the_file:
        restaurant_info = line.rstrip().split(":")
        restaurant_from_file[restaurant_info[0]] = restaurant_info[1]

    the_file.close()

    return restaurant_from_file


def restaurant_dict_from_user_input():
    """While user wants to input restaurant name and rating, add inputs into dictionary"""
    
    input_again = None
    restaurant_from_user = {}

    while input_again != "no":
        restaurant_name = raw_input("Please input the name of the restaurant. >>>")
        restaurant_rating = int(raw_input("Please input the rating of this restaurant. >>>"))
        restaurant_from_user[restaurant_name] = restaurant_rating
        input_again = raw_input("Would you like to enter another restaurant? Enter yes or no.").lower()
    
    return restaurant_from_user


# print restaurant_dict_from_user_input()

def combine_and_sort():
    """Combines dictionary from file and dictionary from user, sorts and prints list."""
    
    complete_restaurant = {} #Empty dictionary to combine both into. 

    #Call function to get dictionary
    restaurant_file_dict = restaurant_dict_from_file("scores.txt") 
    restaurant_file_keys = restaurant_file_dict.keys() #Makes list of only keys in dict.

    #iterates over the key list and adds to complete dictionary all pairs. 
    for restaurant in restaurant_file_keys:
        complete_restaurant[restaurant] = int(restaurant_file_dict[restaurant])

    #Call function to initiate user input prompts.
    restaurant_input_dict = restaurant_dict_from_user_input()
    restaurant_input_keys = restaurant_input_dict.keys() #Takes user input & makes lists of keys

    #Iterates over the key list from user input and adds to complete dictionary all pairs. 
    for restaurant in restaurant_input_keys: 
        complete_restaurant[restaurant] = int(restaurant_input_dict[restaurant])

    #Sorts the keys of the complete dictionary. 
    sorted_complete_restaurant = sorted(complete_restaurant)

    #iterates over the sorted complete list of restaurants and prints key and value. 
    for restaurant in sorted_complete_restaurant:
        print "{} is rated at {}.".format(restaurant,complete_restaurant[restaurant])

combine_and_sort()
