import timeit, random


# списки
list_name_male = [Fracois, ]
list_name_female = []
list_surname = []
list_countries = []
# начальные параметры
money = 100
son = 1
daughter = 1
wife = 1
granny = 1
food = 1
med = 1
day = 0
endgame = 2
buy_food = 0
buy_med = 0
dec = 0
answer = 2
day_wo_food = 0
day_wo_med = 0

# начать игру
print('')# приветсвие
print('')# правила
print('')# нажмите 1
while dec != 1:
try:
    dec = int(input())
except ValueError:
    print('')

while endgame == 2:
    
    print('')
    print('')
    print('')
    print('')
    print('')
    while buy_food != 1 or buyfood != 0:
        try:
            buy_food = int(input())
        except ValueError:
            print('')
    if buy_food == 1:
        money = money - food_cost
        food = 1
    else:
        food = 0
    while buy_med != 1 or buy_med != 0:
        try:
            buy_med = int(input())
        except ValueError:
            print('')
    if buy_med == 1:
        money = money - med_cost
        med = 1
    else:
        med = 0

    start_time = time.time()
    num_of_correct = 0
    num_of_incorrect = 0
    while start_time < cur_time + working_day_time or num_of_incorrect = 3:
        cur_time = time.time()
        true_answer = random.random()
        if true_answer == 0:
            
        else:
            
        print('')
        print('')
        while answer != 1 or answer != 0:
        try:
            answer = int(input())
        except ValueError:
            print('')
        if answer == 1:
            print()
        else:
            print()
        if answer == true_answer:
            num_of_correct = num_of_correct + 1
        else
            num_of_incorrect = num_of_incorrect + 1
            print('')

    income = num_of_correct * pay_for_correct
    money = money + income
    money = money - 10
    if food == 0:
        day_wo_food = day_wo_food + 1
    else:
        day_wo_food = 0
    if med == 0:
        day_wo_med = day_wo_med + 1
    else:
        day_wo_med = 0
    food = 0
    med = 0
    deathprob = ()
    if son == 1:
        chance = random.randint(0,100)
        if chance < deathprob:
            son = 0
            print('')
    if daughter == 1:
        chance = random.randint(0,100)
        if chance < deathprob:
            son = 0
            print('')
    if wife == 1:
        chance = random.randint(0,100)
        if chance < deathprob:
            son = 0
            print('')
    if granny == 1:
        chance = random.randint(0,100)
        if chance < deathprob:
            son = 0
            print('')
    if son == 0 and daughter == 0 and wife == 0 and granny == 0:
        endgame = 3
    if day = 15:
        endgame = 4
    if money < 0:
        endgame = 5
    if money > 250:
        print('')
        endgame = 1        
    
if endgame == 1:
    print()
elif endgame == 3:
    print()
elif endgame == 4:
    print()
else:
    print()
