def character_counter (message, dictionary):
    for character in message:
        dictionary setdefault (character, 0)
        dictionary[character] += 1

    print(dictionary)
    
    print (sum(dictionary.values())))

    # Alternative 1
    values_list = list(dictionary.values())
    print(values_list)
    largest_number_index = values_list.index()


message = input("Write a message: ")
dictionary = {}
character_counter (message, dictionary)