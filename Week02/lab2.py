elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "carbon"]
print("Elements: ", elements)
#  git add . && git commit -m "add elements array" && git push

# def funct_name():
#     return True
# def say_greeting(name, message="hi"):
#     print(f" {message}, {name}")
# say_greeting("Maziar")
# say_greeting("Maziar", "Hello")

def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(print))
        except ValueError:
            print("Error: Please enter a valid integer!")
            continue
            try:
                elements_selected = get_valid_int_input("Enter the index of the element you like")
            except Exception as e:
                print("")