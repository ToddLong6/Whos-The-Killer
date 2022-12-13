from random import randint, choice
from tkinter import messagebox
from tkinter import *
from bs4 import BeautifulSoup
import requests

# Game testing code
# murder_dict = {1: [{'f_name': 'Tony', 'l_name': 'Ables', 'Years Active': '1970–1990', 'Victims': 4,
#                     'Note': 'Murdered robbery victim in 1970, and at least three women until 1990 in '
#                             'St. Petersburg, Florida'}],
#                2: [{'f_name': 'Edward James', 'l_name': 'Adams', 'Years Active': '1920–1921', 'Victims': 7,
#                     'Note': 'Murdered seven people, including three policemen'}]
#                }


# ---------------------------- Getting Data ------------------------------- #
response = requests.get("https://en.wikipedia.org/wiki/List_of_serial_killers_in_the_United_States")
wiki_web_page = response.text

soup = BeautifulSoup(wiki_web_page, 'html.parser')

table = soup.find(name='table')
table_rows = table.find_all(name='tr')
table_rows_list = []
listed_part = []
game_info_dict = {}
for item in table_rows:
    table_rows_list.append(item.text)
for num in range(len(table_rows_list)):
    listed_part.append(table_rows_list[num].split('\n'))
for num in range(len(table_rows_list)):
    game_info_dict[num] = [{listed_part[0][1]:listed_part[num][1], listed_part[0][2]:listed_part[num][3],
                            listed_part[0][3]:listed_part[num][5], listed_part[0][6]:listed_part[num][-4]}]

murder_dict = game_info_dict
print(murder_dict)

# ---------------------------- Starting Game ------------------------------- #
# Game List
selection_list = []
name_list = []

for item in range(4):
    random_selection = randint(1, len(murder_dict))
    names = murder_dict[random_selection][0]['Name']
    name_list.append(names)
    selection_list.append(random_selection)


def skip():
    global random_killer
    global victims
    global years
    global name
    global count

    count = 0
    selection_list.clear()
    name_list.clear()

    for i in range(4):
        random_selection = randint(1, len(murder_dict))
        names = murder_dict[random_selection][0]['Name']
        name_list.append(names)
        selection_list.append(random_selection)

    # Resetting game variables
    random_killer = choice(selection_list)
    name = murder_dict[random_killer][0]['Name']
    victims = murder_dict[random_killer][0]['Proven victims']
    years = murder_dict[random_killer][0]['Years active']
    game_note = murder_dict[random_killer][0]['Notes']
    killer_1.configure(text=name_list[0])
    killer_2.configure(text=name_list[1])
    killer_3.configure(text=name_list[2])
    killer_4.configure(text=name_list[3])
    note_label.configure(text=game_note)
    hint_1.configure(text='')
    hint_2.configure(text='')


# Game Variables
random_killer = choice(selection_list)
score = 0
count = 0
print(f'this is the current killer {random_killer}')
name = murder_dict[random_killer][0]['Name']
victims = murder_dict[random_killer][0]['Proven victims']
years = murder_dict[random_killer][0]['Years active']
game_note = murder_dict[random_killer][0]['Notes']


# ---------------------------- ANSWERING ------------------------------- #
def button_1():
    global score
    killers = killer_1.cget('text')
    print(killers)
    if killers == name:
        print('You know your killers')
        score += 1
    else:
        messagebox.showinfo(title="That's Wrong", message=f"The killer was {name}")
        print('Try Again')
    print(score)
    score_label.configure(text=f'Score: {score}')
    skip()


def button_2():
    global score
    killers = killer_2.cget('text')
    print(killers)
    if killers == name:
        print('You know your killers')
        score += 1
    else:
        messagebox.showinfo(title="That's Wrong", message=f"The killer was {name}")
        print('Try Again')
    print(score)
    score_label.configure(text=f'Score: {score}')
    skip()


def button_3():
    global score
    killers = killer_3.cget('text')
    print(killers)
    if killers == name:
        print('You know your killers')
        score += 1
    else:
        messagebox.showinfo(title="That's Wrong", message=f"The killer was {name}")
        print('Try Again')
    print(score)
    score_label.configure(text=f'Score: {score}')
    skip()


def button_4():
    global score
    killers = killer_4.cget('text')
    print(killers)
    if killers == name:
        print('You know your killers')
        score += 1
    else:
        messagebox.showinfo(title="That's Wrong", message=f"The killer was {name}")
        print('Try Again')
    print(score)
    score_label.configure(text=f'Score: {score}')
    skip()


# ---------------------------- ADD HINTS ------------------------------- #
def add_hint():
    global count
    count += 1
    if count == 1:
        hint_1.configure(text=f"Hint 1: Number of victims was {victims}")
    elif count == 2:
        hint_2.configure(text=f"Hint 2: The active years were {years}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Who's That Serial Killer")
window.config(padx=25, pady=25)

# Canvas
canvas = Frame(width=200, height=200, highlightbackground="blue", highlightthickness=3)
canvas.grid(column=0, row=2, columnspan=3, padx=20, pady=20)

# Label
note_label = Label(canvas, text=game_note)
note_label.grid(column=0, row=0, columnspan=3, sticky=W)
hint_1 = Label(canvas, text='')
hint_1.grid(column=0, row=1, columnspan=3, sticky=W)
hint_2 = Label(canvas, text='')
hint_2.grid(column=0, row=2, columnspan=3, sticky=W)
score_label = Label(text=f'Score: {score}')
score_label.grid(column=0, row=0, sticky=W)

# Button
killer_1 = Button(text=name_list[0], command=button_1)
killer_1.grid(column=0, row=3, sticky=E)
killer_2 = Button(text=name_list[1], command=button_2)
killer_2.grid(column=0, row=4, sticky=E)
killer_3 = Button(text=name_list[2], command=button_3)
killer_3.grid(column=2, row=3, sticky=W)
killer_4 = Button(text=name_list[3], command=button_4)
killer_4.grid(column=2, row=4, sticky=W)
hint_button = Button(text='Hint', command=add_hint)
hint_button.grid(column=2, row=0, sticky=E)
next_button = Button(text='Skip', command=skip)
next_button.grid(column=0, row=0, sticky=E)

window.mainloop()
