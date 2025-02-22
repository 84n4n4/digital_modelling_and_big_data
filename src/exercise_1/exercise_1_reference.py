"""
Exercise 1
Perform the tasks detailed in the Todo's
Do not change the methods names and signature (unless explicitely asked to do so in the todo)
You can use main() function at the bottom to test your functions and your code, this main function is called when
you press the play button in your ide or run `python exercise_1.py` from a shell.
DO NOT ADD any code to the global scope of this file.
You are free to add new functions as long as they do not shadow existing function names.
"""



# Todo: fill the function below to calculate and return c using pythagoras theorem
def pythagoras(a, b):
    return (a**2 + b**2)**0.5


# Todo: fill the function below so that all spaces in the text are repalaced with '-' dashes and return the text
def replace_space_with_dash(text):
    return text.replace(' ', '-')


# Todo: fill the function below so that it removes all duplicated values in the list and return a new list(!)
def remove_duplicates(list_of_numbers):
    return list(set(list_of_numbers))


# Todo: rewrite the function signature so that a has a default value of 5
def square_a(a=5):
    return a**2


# Todo: rewrite the function below that it returns the integer value of a string of numbers, e.g. '123' becomes 123
def make_integer(some_string):
    return int(some_string)


# Todo: create a function that return the fibonacci sequence up to a certain value (so all numbers in the sequence smaller than limit)
def make_fibonacci(limit):
    fib_sequence = [0, 1]
    if limit < 0:
        return []
    if limit == 0:
        return [0]
    while True:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        if next_value > limit:
            break
        fib_sequence.append(next_value)
    return fib_sequence


# Todo: sort the given list and return it
def sort_list_of_numbers(list_of_numbers):
    return sorted(list_of_numbers)


# Todo: create a function that takes as input a csv formated text, e.g.
"""
x_value,y_value
1,3
2,4
"""
# and create a two dimensional array based on 'list' type with this values (as 'int') in the following orientation.
"""
[[1,3],
 [2,4]]
"""
def read_a_two_dimensional_list_from_a_csv_string(csv_string):
    lines = csv_string.strip().splitlines()
    table = []
    for l in lines[1:]:
        row = []
        for c in l.split(','):
            row.append(int(c))
        table.append(row)
    return table


# Todo: create a function that takes as input a csv formated text, e.g.
"""
Name,PhoneNumber,Age
Tom,12345,22
Jack,3456,24
"""
# and create a dictionary with name as key and value again being a dict with 'phone_number' and 'age' as respective keys.
# age in the output dict is to be of type 'int' and the phone number is to be of type 'string'.
"""
{'Tom': {'phone_number': '12345', 'age': 22}, 'Jack': {'phone_number': '3456', 'age': 24}}
"""
def read_phone_book_from_a_csv_string(csv_string):
    lines = csv_string.strip().splitlines()
    phone_book = {}
    for l in lines[1:]:
        name = l.split(',')[0]
        phone = l.split(',')[1]
        age = l.split(',')[2]
        phone_book.update({name: {'phone_number': phone, 'age': int(age)}})
    return phone_book



# Todo: create a sine wave (as values in a list) given a start and end value and given step size:
# e.g. create_sine_wave(0, math.pi, 0.5) -> [0., 0.47942554, 0.84147098, 0.99749499, 0.90929743, 0.59847214, 0.14112001]
def create_sine_wave(start, stop, step_size):
    import math
    sine_wave = []
    while True:
        sine_wave.append(math.sin(start))
        start += step_size
        if start > stop:
            break
    return sine_wave


def main():
    # Todo: test your functions here:
    print(pythagoras(1, 2))


if __name__ == "__main__":
    main()
