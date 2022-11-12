import csv
import random

#Untitled_spreadsheet_-_Sheet1.csv
#Magic_Pauper_Randomizer_Thing.csv

file_name = input('Please enter the CSV name: ')
number_of_cards = input('How many cards to pick (24 or 36)? ')
chosen_rows = []

def file_line_count(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

with open(file_name) as file:
    file_reader = csv.reader(file)
    number_of_lines = file_line_count(file_name)
    for card_choice_number in range(0,int(number_of_cards)):
        random_int = random.randint(1, number_of_lines)
        chosen_rows.append(random_int)
    print('Deck')
    for count, value in enumerate(file_reader):
        if count in chosen_rows:
            print('4 ' + value[1])
