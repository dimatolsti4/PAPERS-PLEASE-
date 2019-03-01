import time
import random
list_name_male = ['Fracois', 'Tzukan', 'Arron', 'Claude', 'Peter',
                  'Alin', 'Michael', 'Nikita', 'Gregory', 'Eugen',
                  'Tomas', 'Bjorn', 'John', 'Simon', 'Vince', 'Danic',
                  'Kordon', 'Messof', 'Mikhail', 'Nathan', 'Filipe']

list_name_female = ['Inessa', 'Alana', 'Goncalina', 'Riffka', 'Stepheni',
                    'Danika', 'Katherine', 'Marie', 'Shae', 'Elisa']

list_surname = ['Degryse', 'Tzukan', 'Hopcraft', 'Mothias', 'Cizadlo',
                'Ingebret', 'Lopes', 'Dragomir', 'Desjardins',
                'Ramsdinska', 'Beilstein', 'Hoffman', 'Graire', 'Kudeuske',
                'Davok', 'Eriksson', 'Blovska']

list_countries = ['Antegria', 'Impor', 'Obristan', 'Kolechia', 'Republia']

list_mistakes = ['incor_date', 'incor_sex', 'over_date', 'incor_country',
                 'wr_country', 'incor_name', 'incor_surname']

list_incor_date = ['incor_day', 'incor_month', 'incor_year']

list_incor_country = ['Antagria', 'Impar', 'Obriсtan', 'Kojechia', 'Republїa']

list_incor_name_male = ['Fracoиs', 'Tcukan', 'Arran', 'Claudy', 'Pettr',
                        'Alan', 'Mikhael', 'Niktta', 'Gregori', 'Eygen',
                        'Tomos', 'Biorn', 'Jonn', 'Symkn', 'Vinci', 'Danik',
                        'Kardon', 'Mescof', 'Michail', 'Nathon', '`Filipэ']

list_incor_surname = ['Digruse', 'Tsukan', 'Hopcratt', 'Modhias', 'Cizatlo',
                      'Ingabret', 'Lapes', 'Dragamir', 'Desjadins',
                      'Ramddinska', 'Beilstain', 'Hotfman', 'Craire',
                      'Kudeyske', 'Dovok', 'Errikson', 'Blovsta']

list_incor_name_female = ['Innesia', 'Aluna', 'Gancalina', 'Rifkka',
                          'Stephhen', 'Daneka', 'Katterine', 'Marre',
                          'Shoe', 'Eliza']

money = 100
son = 1
daughter = 1
wife = 1
mother_in_law = 1
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
bribe_taken = 0
money_notfair = 0

print('БУМАГИ, ПОЖАЛУЙСТА!')
print('Нажмите "0" для вывода правил')
print('Нажмите "1" для начала игры')
while dec != 1:
    try:
        dec = int(input())
    except ValueError:
        print('Нажмите "0" для вывода правил')
        print('Нажмите "1" для начала игры')
    if dec == 0:
        print('Добро пожаловать!')
        print('Вы находитесь в авторитарной стране Арстотцка')
        print('Вы работаете на границе, Ваша задача - проверять паспорта')
        print('Если вы видите несовпадение паспорта' /
              'и информации о посетителе, Вы должны отказать в пропуске')
        print('Проверяйте совпадение имён, корректность' /
              'даты рождения, соответсвие пола, совпадение страны')
        print('Паспорт не должен быть просрочен(EXPIRATION-DATE)')
        print('Если Вам кажется, что никаких проблем нет, то пропускайте')
        print('Ваша задача - проверять как можно больше' /
              'человек каждый день и заработать 1000$ для' /
              'выезда из страны с семьёй')
        print('Если Вы не успеете сделать это за 15 дней, то' /
              'на Вас сфабрикуют рапорт и посадят в тюрьму')
        print('Кроме того, Вы должны заботиться о своей семье')
        print('Удачи и слава Арстотцке!')

while endgame == 2:
    print('День: ', day)
    print('Деньги: ', money, '$')
    if son == 1:
        print('Ваш сын жив')
    if wife == 1:
        print('Ваша жена жива')
    if daughter == 1:
        print('Ваша дочь жива')
    if mother_in_law == 1:
        print('Ваша тёща жива')
    if day > 0:
        print('Вы заплатили 15$ за квартиру')
    print('Вы можете купить еду для семьи за 20$')
    print('"1" - купить, "0" - не покупать')
    try:
        buy_food = int(input())
    except ValueError:
        print('"1" - купить, "0" - не покупать')
    while buy_food != 1 and buy_food != 0:
        try:
            buy_food = int(input())
        except ValueError:
            print('"1" - купить, "0" - не покупать')
    if buy_food == 1:
        money = money - 25
        food = 1
    else:
        food = 0
    print('Вы можете купить лекарства для семьи за 10$')
    print('"1" - купить, "0" - не покупать')
    try:
        buy_med = int(input())
    except ValueError:
        print('"1" - купить, "0" - не покупать')
    while buy_med != 1 and buy_med != 0:
        try:
            buy_med = int(input())
        except ValueError:
            print('"1" - купить, "0" - не покупать')
    if buy_med == 1:
        money = money - 10
        med = 1
    else:
        med = 0
    start_time = time.time()
    cur_time = time.time()
    num_of_correct = 0
    num_of_incorrect = 0
    vis_num = 0

    while start_time > cur_time - 30 and num_of_incorrect < 4:
        vis_num = vis_num + 1
        print('Посетитель номер: ', vis_num)
        true_answer = random.randint(0, 1)
        sex = random.randint(0, 1)
        ans = ''
        if sex == 1:
            name = list_name_male[random.randint(0, 20)]
            sex = 'МУЖ'
            passport = open("passportmale.txt").read()
        else:
            name = list_name_female[random.randint(0, 8)]
            sex = 'ЖЕН'
            passport = open("passportfemale.txt").read()
        surname = list_surname[random.randint(0, 16)]
        country = list_countries[random.randint(0, 4)]
        birth_day = str(random.randint(1, 28))
        birth_month = str(random.randint(1, 12))
        birth_year = str(random.randint(1950, 2004))
        birth_date = birth_day + '.' + birth_month + '.' + birth_year
        name = surname + ',' + name
        ex_day = str(random.randint(1, 28))
        ex_month = str(random.randint(4, 12))
        ex_year = str(random.randint(2019, 2025))
        ex_date = ex_day + '.' + ex_month + '.' + ex_year
        name1 = 'NAME: ' + name + ' ' * (44 - len(name))
        birth_date1 = 'DATE-OF-BIRTH: ' + birth_date + ' ' * (35 - len(birth_date))
        sex1 = 'SEX: ' + sex + ' ' * (45 - len(sex))
        country1 = 'COUNTRY: ' + country + ' ' * (41 - len(country))
        ex_date1 = 'EXPIRATION-DATE: ' + ex_date + ' ' * (33 - len(ex_date))

        if true_answer == 0:
            mistake = list_mistakes[random.randint(0, 6)]

            if mistake == 'incor_date':
                type_of_mistake = list_incor_date[random.randint(0, 2)]
                if type_of_mistake == 0:
                    birth_day = str(random.randint(32, 33))
                elif type_of_mistake == 1:
                    birth_month = '13'
                else:
                    birth_year = str(random.randint(1850, 1920))
                birth_date = birth_day + '.' + birth_month + '.' + birth_year
                birth_date1 = 'DATE-OF-BIRTH: ' + birth_date + ' ' * (35 - len(birth_date))

            elif mistake == 'incor_sex':
                if sex == 1:
                    sex_wr = 'ЖЕН'
                else:
                    sex_wr = 'МУЖ'
                sex1 = 'SEX: ' + sex_wr + ' ' * (45 - len(sex_wr))

            elif mistake == 'over_date':
                ex_year = str(random.randint(2012, 2018))
                ex_date = ex_day + '.' + ex_month + '.' + ex_year
                ex_date1 = 'EXPIRATION-DATE: ' + ex_date + ' ' * (33 - len(ex_date))

            elif mistake == 'incor_country':
                country_right = country
                while country_right == country:
                    country = list_countries[random.randint(0, 4)]

            elif mistake == 'wr_country':
                country_num = random.randint(0, 4)
                country_wr = list_incor_country[country_num]
                country = list_countries[country_num]
                country1 = 'COUNTRY: ' + country_wr + ' ' * (41 - len(country_wr))

            elif mistake == 'incor_name':
                if sex == 1:
                    name_num = random.randint(0, 20)
                    name = list_name_male[name_num]
                    name_wr = list_incor_name_male[name_num]
                else:
                    name_num = random.randint(0, 8)
                    name = list_name_female[name_num]
                    name_wr = list_incor_name_female[name_num]
                name_wr = surname + ',' + name_wr
                name = surname + ',' + name
                name1 = 'NAME: ' + name_wr + ' ' * (44 - len(name_wr))

            else:
                surname_num = random.randint(0, 16)
                surname = list_surname[surname_num]
                surname1 = list_incor_surname[surname_num]
                country = list_countries[random.randint(0, 4)]
                name_wr = surname_wr + ',' + name
                name = surname + ',' + name
                name1 = 'NAME: ' + name_wr + ' ' * (44 - len(name_wr))

        passport = passport.replace('NAME:                                             ', name1)
        passport = passport.replace('DATE-OF-BIRTH:                                    ', birth_date1)
        passport = passport.replace('SEX:                                              ', sex1)
        passport = passport.replace('COUNTRY:                                          ', country1)
        passport = passport.replace('EXPIRATION-DATE:              ' /
                                    '                   ', ex_date1)
        print(passport)
        print('VISITOR INFORMATION:')
        print('NAME: ', name)
        print('DATE OF BIRTH: ', birth_date)
        print('COUNTRY: ', country)

        print('"1" - пропустить, "0" - отклонить')
        try:
            answer = int(input())
        except ValueError:
            print('"1" - пропустить, "0" - отклонить')
        while answer != 1 and answer != 0:
            try:
                answer = int(input())
            except ValueError:
                print('"1" - пропустить, "0" - отклонить')
        if answer == 1:
            print()
        else:
            print()
        if answer == true_answer:
            num_of_correct = num_of_correct + 1
        else:
            if true_answer < answer:
                num_of_incorrect = num_of_incorrect + 1
                print('НЕВЕРНО!')
                print('ВНИМАТЕЛЬНЕЕ!')
        if true_answer == 0 and answer == 0:
            chance = (random.randint(0, 100))
            bribe = (random.randint(30, 100))
            if chance < 20:
                print('Вам предложили взятку:', bribe, '$')
                print('"1" - принять, "0" - отклонить')
                ans = input()
                print('Successfuly!')
                if ans == '1':
                    money += bribe
                    money_notfair += bribe
                    bribe_taken += 1

        inspect_chance = 7 + 2**bribe_taken
        if random.randint(1, 100) < inspect_chance:
            print('Вас окружила полиция!')
            if bribe_taken == 0:
                print('Каким-то чудом Вы смогли избежать наказания!')
            elif random.randint(1, 100) < 40 and bribe_taken != 0:
                rnd = random.randint(2, 6)
                print('Вы можете откупиться:', money // rnd, '$')
                print('"1" - откупиться, "0" - нет')
                wow = input()
                if wow == '1':
                    money -= money // rnd
                elif wow == '0':
                    money -= (money_notfair // 3 + money // 6)
                bribe_taken = 0
            else:
                print('ВАС ПОЙМАЛИ!!!')
                print('У вас забрали', money_notfair // 2.5 + money // 3, '$')
                money -= (money_notfair // 1.5 + money // 3)
                bribe_taken = 0
            print()
        cur_time = time.time()
        money_notfair = 0
    income = (num_of_correct - num_of_incorrect) * 25
    if income < 0:
        income = 0
    if num_of_incorrect >= 3:
        income = 0
        print('ВЫ НЕ ПЛОУЧИТЕ ДЕНЕГ ИЗ-ЗА МНОГОЧИСЛЕННЫХ ОШИБОК!')
    print('Вы заработали:', income + money_notfair)
    money = money + income
    money = money - 15
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
    deathprob = (3 ** day_wo_food + 2 ** day_wo_med) ** 1
    if son == 1:
        chance = random.randint(0, 100)
        if chance < deathprob:
            son = 0
            print('Ваш сын умер...')
    if daughter == 1:
        chance = random.randint(0, 100)
        if chance < deathprob:
            daughter = 0
            print('Ваша дочь умерла...')
    if wife == 1:
        chance = random.randint(0, 100)
        if chance < deathprob:
            wife = 0
            print('Ваша жена умерла...')
    if mother_in_law == 1:
        chance = random.randint(0, 100)
        if chance < deathprob:
            mother_in_law = 0
            print('Ваша тёща умерла...')
    day = day + 1
    if son == 0 and daughter == 0 and wife == 0 and granny == 0:
        endgame = 3
    if day == 15:
        endgame = 4
    if money < 0:
        endgame = 5
    if money > 1000:
        endgame = 1

if endgame == 1:
    print('ПОЗДРАВЛЯЕМ!')
    print('ВЫ ПОБЕДИЛИ!')
    print('Вы заработали достатачно денег и теперь можете уехать за границу!')
elif endgame == 3:
    print('ВЫ ПРОИГРАЛИ')
    print('Все члены вашей семьи погибли и теперь Вы не видите смысла жить...')
elif endgame == 4:
    print('ВЫ ПРОИГРАЛИ')
    print('На Вас донесли в полицию и совсем скоро вы окажетесь в тюрьме...')
else:
    print('ВЫ ПРОИГРАЛИ')
    print('У Вас больше нет денег на оплату жилья и теперь' /
          'Ваша семья погибнет на улице от морозов...')
