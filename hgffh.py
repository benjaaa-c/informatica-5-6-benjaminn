database = {
      "apple": [["calories", 130], ["sugars", 25], ["proteins", 1]],
      "avocado": [["calories", 50], ["sugars", 0], ["proteins", 1]],
      "banana": [["calories", 110], ["sugars", 19], ["proteins", 1]],
      "orange": [["calories", 80], ["sugars", 14], ["proteins", 1]],
      "peach": [["calories", 60], ["sugars", 13], ["proteins", 1]]
  }

fruit = input("Item: ")
def show_nutrition(fruit):
      if fruit in database:
            print(f"\n{fruit.capitalize()}nutrition facts")
            for item in database[fruit]:
                  print(f"{item[0]}: {item[1]}")
      else:
            print("fruit not found in database.")

# main program loop
while True:
    user_input = input("\nitem (press enter to stop): ").lower()

    if user_input == "":
        print("program stopped by the user.")
        break
    show_nutrition(user_input)

             
       