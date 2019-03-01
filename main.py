import time, random

list_name_male = ['Fracois', 'Tzukan', 'Arron', 'Claude', 'Peter', 'Alin', 'Michael', 'Nikita', 'Gregory', 'Eugen', 'Tomas', 'Bjorn', 'John', 'Simon', 'Vince', 'Danic', 'Kordon', 'Messof', 'Mikhail', 'Nathan', 'Filipe']
list_name_female = ['Inessa', 'Alana', 'Goncalina', 'Riffka', 'Stepheni', 'Danika', 'Katherine', 'Marie', 'Shae', 'Elisa']
list_surname = ['Degryse', 'Tzukan', 'Hopcraft', 'Mothias', 'Cizadlo', 'Ingebret', 'Lopes', 'Dragomir', 'Desjardins', 'Ramsdinska', 'Beilstein', 'Hoffman', 'Graire', 'Kudeuske', 'Davok', 'Eriksson', 'Blovska']
list_countries = ['Antegria', 'Impor', 'Obristan', 'Kolechia', 'Republia']
list_mistakes = ['incor_date', 'incor_sex','over_date', 'incor_country', 'wr_country', 'incor_name', 'incor_surname']
list_incor_date = ['incor_day', 'incor_month', 'incor_year']
list_incor_country=['Antagria', 'Impar', 'Obriсtan', 'Kojechia', 'Republїa']
list_incor_name_male=['Fracoиs', 'Tcukan', 'Arran', 'Claudy', 'Pettr', 'Alan', 'Mikhael', 'Niktta', 'Gregori', 'Eygen', 'Tomos', 'Biorn', 'Jonn', 'Symkn', 'Vinci', 'Danik', 'Kardon', 'Mescof', 'Michail', 'Nathon', '`Filipэ']
list_incor_surname=['Digruse', 'Tsukan', 'Hopcratt', 'Modhias', 'Cizatlo', 'Ingabret', 'Lapes', 'Dragamir', 'Desjadins', 'Ramddinska', 'Beilstain', 'Hotfman', 'Craire', 'Kudeyske', 'Dovok', 'Errikson', 'Blovsta']
list_incor_name_female=['Innesia', 'Aluna', 'Gancalina', 'Rifkka', 'Stephhen', 'Daneka', 'Katterine', 'Marre', 'Shoe', 'Eliza']

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
bribe_taken = 0
money_notfair = 0

print('PAPERS, PLEASE!')
print('Press "0" to read rules')
print('Press "1" to start game')
while dec != 1:
    try:
        dec = int(input())
    except ValueError:
        print('Press "0" to read rules')
        print('Press "1" to start game')
    if dec == 0:
        print('rules')

while endgame == 2:
    print('DAY: ', day)
    print('You have: ', money, '$')
    if son == 1:
        print('Son is alive')
    if wife == 1:
        print('Wife is alive')
    if daughter == 1:
        print('Daughter is alive')
    if granny == 1:
        print('Granny is alive')
    if day > 0:
        print('You paid 15$ for your rent')
    print('You can buy food for 20$')
    print('Press "1" to buy food or "0" to not')
    try:
        buy_food = int(input())
    except ValueError:
        print('Press "1" to buy food or "0" to not')
    while buy_food != 1 and buy_food != 0:
        try:
            buy_food = int(input())
        except ValueError:
            print('Press "1" to buy food or "0" to not')
    if buy_food == 1:
        money = money - 25
        food = 1
    else:
        food = 0
    print('You can buy medicines for 10$')
    print('Press "1" to buy medicines or "0" to not')
    try:
        buy_med = int(input())
    except ValueError:
        print('Press "1" to buy medicines or "0" to not')
    while buy_med != 1 and buy_med != 0:
        try:
            buy_med = int(input())
        except ValueError:
            print('Press "1" to buy medicines or "0" to not')
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
        print('Visitor number: ', vis_num)
        true_answer = random.randint(0,1)
        sex = random.randint(0,1)
        ans=''
                
        if true_answer == 0:
            mistake = list_mistakes[random.randint(0,6)]
            if sex == 1:
                name = list_name_male[random.randint(0,20)]
                sex = 'MALE'
                passport = open("passportmale.txt").read()
            else:
                name = list_name_female[random.randint(0,8)]
                sex = 'FEMALE'
                passport = open("passportfemale.txt").read()

            if mistake == 'incor_date':
                type_of_mistake = list_incor_date[random.randint(0,2)]
                if type_of_mistake == 0:
                    birth_day = str(random.randint(32,33))
                    birth_month = str(random.randint(1,12))
                    birth_year = str(random.randint(1950,2004))
                elif type_of_mistake == 1:
                    birth_day = str(random.randint(1,28))
                    birth_month = '13'
                    birth_year = str(random.randint(1950,2004))
                else:
                    birth_day = str(random.randint(1,28))
                    birth_month = str(random.randint(1,12))
                    birth_year = str(random.randint(1850,1920))
                surname = list_surname[random.randint(0,16)]
                country = list_countries[random.randint(0,4)]
                birth_date = birth_day + '.' + birth_month + '.' + birth_year
                name = surname + ',' + name
                ex_day = str(random.randint(1,28))
                ex_month = str(random.randint(1,12))
                ex_year = str(random.randint(2019,2025))
                ex_date = ex_day + '.' + ex_month + '.' + ex_year
                name1 = 'NAME: ' + name + ' ' * (44 - len(name))
                passport = passport.replace('NAME:                                             ', name1)
                birth_date1 = 'DATE-OF-BIRTH: ' + birth_date + ' ' * (35 - len(birth_date))
                passport = passport.replace('DATE-OF-BIRTH:                                    ', birth_date1)
                sex1 = 'SEX: ' + sex + ' ' * (45 - len(sex))
                passport = passport.replace('SEX:                                              ', sex1)
                country1 = 'COUNTRY: ' + country + ' ' * (41 - len(country))
                passport = passport.replace('COUNTRY:                                          ', country1)
                ex_date1 = 'EXPIRATION-DATE: ' + ex_date + ' ' * (33 - len(ex_date))
                passport = passport.replace('EXPIRATION-DATE:                                  ', ex_date1)
            elif mistake == 'incor_sex':
                if sex == 1:
                    sex1 = 'FEMALE'
                else:
                    sex1 = 'MALE'
                surname = list_surname[random.randint(0,16)]
                country = list_countries[random.randint(0,4)]
                birth_day = str(random.randint(1,28))
                birth_month = str(random.randint(1,12))
                birth_year = str(random.randint(1950,2004))
                birth_date = birth_day + '.' + birth_month + '.' + birth_year
                name = surname + ',' + name
                ex_day = str(random.randint(1,28))
                ex_month = str(random.randint(1,12))
                ex_year = str(random.randint(2019,2025))
                ex_date = ex_day + '.' + ex_month + '.' + ex_year
                name1 = 'NAME: ' + name + ' ' * (44 - len(name))
                passport = passport.replace('NAME:                                             ', name1)
                birth_date1 = 'DATE-OF-BIRTH: ' + birth_date + ' ' * (35 - len(birth_date))
                passport = passport.replace('DATE-OF-BIRTH:                                    ', birth_date1)
                sex1 = 'SEX: ' + sex1 + ' ' * (45 - len(sex))
                passport = passport.replace('SEX:                                              ', sex1)
                country1 = 'COUNTRY: ' + country + ' ' * (41 - len(country))
                passport = passport.replace('COUNTRY:                                          ', country1)
                ex_date1 = 'EXPIRATION-DATE: ' + ex_date + ' ' * (33 - len(ex_date))
                passport = passport.replace('EXPIRATION-DATE:                                  ', ex_date1)
            elif mistake == 'over_date':
                surname = list_surname[random.randint(0,16)]
                country = list_countries[random.randint(0,4)]
                birth_day = str(random.randint(1,28))
                birth_month = str(random.randint(1,12))
                birth_year = str(random.randint(1950,2004))
                birth_date = birth_day + '.' + birth_month + '.' + birth_year
                name = surname + ',' + name
                ex_day = str(random.randint(1,28))
                ex_month = str(random.randint(1,12))
                ex_year = str(random.randint(2012,2018))
                ex_date = ex_day + '.' + ex_month + '.' + ex_year
                name1 = 'NAME: ' + name + ' ' * (44 - len(name))
                passport = passport.replace('NAME:                                             ', name1)
                birth_date1 = 'DATE-OF-BIRTH: ' + birth_date + ' ' * (35 - len(birth_date))
                passport = passport.replace('DATE-OF-BIRTH:                                    ', birth_date1)
                sex1 = 'SEX: ' + sex + ' ' * (45 - len(sex))
                passport = passport.replace('SEX:                                              ', sex1)
                country1 = 'COUNTRY: ' + country + ' ' * (41 - len(country))
                passport = passport.replace('COUNTRY:                                          ', country1)
                ex_date1 = 'EXPIRATION-DATE: ' + ex_date + ' ' * (33 - len(ex_date))
                passport = passport.replace('EXPIRATION-DATE:                                  ', ex_date1)
            elif mistake == 'incor_country':
                surname = list_surname[random.randint(0,16)]
                country = list_countries[random.randint(0,4)]
                birth_day = str(random.randint(1,28))
                birth_month = str(random.randint(1,12))
                birth_year = str(random.randint(1950,2004))
                birth_date = birth_day + '.' + birth_month + '.' + birth_year
                name = surname + ',' + name
                ex_day = str(random.randint(1,28))
                ex_month = str(random.randint(1,12))
                ex_year = str(random.randint(2019,2025))
                ex_date = ex_day + '.' + ex_month + '.' + ex_year
                name1 = 'NAME: ' + name + ' ' * (44 - len(name))
                passport = passport.replace('NAME:                                             ', name1)
                birth_date1 = 'DATE-OF-BIRTH: ' + birth_date + ' ' * (35 - len(birth_date))
                passport = passport.replace('DATE-OF-BIRTH:                                    ', birth_date1)
                sex1 = 'SEX: ' + sex + ' ' * (45 - len(sex))
                passport = passport.replace('SEX:                                              ', sex1)
                country1 = 'COUNTRY: ' + country + ' ' * (41 - len(country))
                passport = passport.replace('COUNTRY:                                          ', country1)
                ex_date1 = 'EXPIRATION-DATE: ' + ex_date + ' ' * (33 - len(ex_date))
                passport = passport.replace('EXPIRATION-DATE:                                  ', ex_date1)
                country2 = country
                while country2 == country:
                    country = list_countries[random.randint(0,4)]
            elif mistake == 'wr_country':
                country_num = random.randint(0,4)
                country1 = list_incor_country[country_num]
                country = list_countries[country_num]
                surname = list_surname[random.randint(0,16)]
                birth_day = str(random.randint(1,28))
                birth_month = str(random.randint(1,12))
                birth_year = str(random.randint(1950,2004))
                birth_date = birth_day + '.' + birth_month + '.' + birth_year
                name = surname + ',' + name
                ex_day = str(random.randint(1,28))
                ex_month = str(random.randint(4,12))
                ex_year = str(random.randint(2019,2025))
                ex_date = ex_day + '.' + ex_month + '.' + ex_year
                name1 = 'NAME: ' + name + ' ' * (44 - len(name))
                passport = passport.replace('NAME:                                             ', name1)
                birth_date1 = 'DATE-OF-BIRTH: ' + birth_date + ' ' * (35 - len(birth_date))
                passport = passport.replace('DATE-OF-BIRTH:                                    ', birth_date1)
                sex1 = 'SEX: ' + sex + ' ' * (45 - len(sex))
                passport = passport.replace('SEX:                                              ', sex1)
                country1 = 'COUNTRY: ' + country1 + ' ' * (41 - len(country1))
                passport = passport.replace('COUNTRY:                                          ', country1)
                ex_date1 = 'EXPIRATION-DATE: ' + ex_date + ' ' * (33 - len(ex_date))
                passport = passport.replace('EXPIRATION-DATE:                                  ', ex_date1)
            elif mistake == 'incor_name':
                if sex == 1:
                    name_num = random.randint(0,20)
                    name = list_name_male[name_num]
                    name1 = list_incor_name_male[name_num]
                else:
                    name_num = random.randint(0,8)
                    name = list_name_female[name_num]
                    name1 = list_incor_name_female[name_num]
                surname = list_surname[random.randint(0,16)]
                country = list_countries[random.randint(0,4)]
                birth_day = str(random.randint(1,28))
                birth_month = str(random.randint(1,12))
                birth_year = str(random.randint(1950,2004))
                birth_date = birth_day + '.' + birth_month + '.' + birth_year
                name1 = surname + ',' + name1
                name = surname + ',' + name
                ex_day = str(random.randint(1,28))
                ex_month = str(random.randint(4,12))
                ex_year = str(random.randint(2019,2025))
                ex_date = ex_day + '.' + ex_month + '.' + ex_year
                name1 = 'NAME: ' + name1 + ' ' * (44 - len(name))
                passport = passport.replace('NAME:                                             ', name1)
                birth_date1 = 'DATE-OF-BIRTH: ' + birth_date + ' ' * (35 - len(birth_date))
                passport = passport.replace('DATE-OF-BIRTH:                                    ', birth_date1)
                sex1 = 'SEX: ' + sex + ' ' * (45 - len(sex))
                passport = passport.replace('SEX:                                              ', sex1)
                country1 = 'COUNTRY: ' + country + ' ' * (41 - len(country))
                passport = passport.replace('COUNTRY:                                          ', country1)
                ex_date1 = 'EXPIRATION-DATE: ' + ex_date + ' ' * (33 - len(ex_date))
                passport = passport.replace('EXPIRATION-DATE:                                  ', ex_date1)
            else:
                if sex == 1:
                    name = list_name_male[random.randint(0,20)]
                    sex = 'MALE'
                    passport = open("passportmale.txt").read()
                else:
                    name = list_name_female[random.randint(0,8)]
                    sex = 'FEMALE'
                    passport = open("passportfemale.txt").read()
                surname_num = random.randint(0,16)
                surname = list_surname[surname_num]
                surname1 = list_incor_surname[surname_num]
                country = list_countries[random.randint(0,4)]
                birth_day = str(random.randint(1,28))
                birth_month = str(random.randint(1,12))
                birth_year = str(random.randint(1950,2004))
                birth_date = birth_day + '.' + birth_month + '.' + birth_year
                name1 = surname1 + ',' + name
                name = surname + ',' + name
                ex_day = str(random.randint(1,28))
                ex_month = str(random.randint(4,12))
                ex_year = str(random.randint(2019,2025))
                ex_date = ex_day + '.' + ex_month + '.' + ex_year
                name1 = 'NAME: ' + name1 + ' ' * (44 - len(name))
                passport = passport.replace('NAME:                                             ', name1)
                birth_date1 = 'DATE-OF-BIRTH: ' + birth_date + ' ' * (35 - len(birth_date))
                passport = passport.replace('DATE-OF-BIRTH:                                    ', birth_date1)
                sex1 = 'SEX: ' + sex + ' ' * (45 - len(sex))
                passport = passport.replace('SEX:                                              ', sex1)
                country1 = 'COUNTRY: ' + country + ' ' * (41 - len(country))
                passport = passport.replace('COUNTRY:                                          ', country1)
                ex_date1 = 'EXPIRATION-DATE: ' + ex_date + ' ' * (33 - len(ex_date))
                passport = passport.replace('EXPIRATION-DATE:                                  ', ex_date1)            
        if true_answer == 1:
            if sex == 1:
                name = list_name_male[random.randint(0,20)]
                sex = 'MALE'
                passport = open("passportmale.txt").read()
            else:
                name = list_name_female[random.randint(0,8)]
                sex = 'FEMALE'
                passport = open("passportfemale.txt").read()
            surname = list_surname[random.randint(0,16)]
            country = list_countries[random.randint(0,4)]
            birth_day = str(random.randint(1,28))
            birth_month = str(random.randint(1,12))
            birth_year = str(random.randint(1950,2004))
            birth_date = birth_day + '.' + birth_month + '.' + birth_year
            name = surname + ',' + name
            ex_day = str(random.randint(1,28))
            ex_month = str(random.randint(4,12))
            ex_year = str(random.randint(2019,2025))
            ex_date = ex_day + '.' + ex_month + '.' + ex_year
            name1 = 'NAME: ' + name + ' ' * (44 - len(name))
            passport = passport.replace('NAME:                                             ', name1)
            birth_date1 = 'DATE-OF-BIRTH: ' + birth_date + ' ' * (35 - len(birth_date))
            passport = passport.replace('DATE-OF-BIRTH:                                    ', birth_date1)
            sex1 = 'SEX: ' + sex + ' ' * (45 - len(sex))
            passport = passport.replace('SEX:                                              ', sex1)
            country1 = 'COUNTRY: ' + country + ' ' * (41 - len(country))
            passport = passport.replace('COUNTRY:                                          ', country1)
            ex_date1 = 'EXPIRATION-DATE: ' + ex_date + ' ' * (33 - len(ex_date))
            passport = passport.replace('EXPIRATION-DATE:                                  ', ex_date1)
        print(passport)
        print('VISITOR INFORMATION:')
        print('NAME: ', name)
        print('DATE OF BIRTH: ', birth_date)
        print('COUNTRY: ', country)
                
        print('Press "1" to let him pass or "0" to not')
        try:
            answer = int(input())
        except ValueError:
            print('Press "1" to let him pass or "0" to not')
        while answer != 1 and answer != 0:
            try:
                answer = int(input())
            except ValueError:
                print('Press "1" to let him pass or "0" to not')
        if answer == 1:
            print()
        else:
            print()
        if answer == true_answer:
            num_of_correct = num_of_correct + 1
        else:
            if true_answer < answer:
                num_of_incorrect = num_of_incorrect + 1
                print('INCORRECT!')
                print('PAY MORE ATTENTION!')
                print(mistake)
        if true_answer == 0 and answer == 0 :
            chance = (random.randint(0,100))
            bribe = (random.randint(30,100))
            if chance < 20:
                print('You are offered a bribe:',bribe,'$')
                print('1 To take a bribe or 0 to decline')
                ans=input()
                print('Successfuly!')
                print()
                if ans == '1':
                    money += bribe
                    money_notfair += bribe
                    bribe_taken += 1
                    
        inspect_chance = 7 + 2**bribe_taken
        if random.randint(1,100) < inspect_chance :
            print('You are surrounded by police')
            if bribe_taken == 0 :
                print('Your speech was so good that you dodged TerraLUl xd')
            elif random.randint(1,100) < 40 and bribe_taken != 0 :
                rnd = random.randint(2,6)
                print('You may pay off for:', money // rnd,'$')
                print('1 To pay off or 0 to decline')
                wow = input()
                if wow == '1':
                    money -= money // rnd
                elif wow == '0':
                    money -= (money_notfair // 3 + money // 6)
                bribe_taken = 0
            else:
                print('HANDS ON THE TABLE!!!!! GET DOWN !!!!! PAPSNAZ WORKS')
                print('У вас забрали', money_notfair // 2.5 + money // 3,'$')
                money -= (money_notfair //1.5 + money//3)
                bribe_taken = 0
            print()
        cur_time = time.time()
        money_notfair = 0
    income = (num_of_correct - num_of_incorrect) * 25
    if num_of_incorrect >= 3:
        income = 0
        print('YOU WILL NOT RECIVE MONEY FOR TODAY BECOUSE OF TOO MANY MISTAKES')
    print('You earned:', income + money_notfair)
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
        chance = random.randint(0,100)
        if chance < deathprob:
            son = 0
            print('Your son died')
    if daughter == 1:
        chance = random.randint(0,100)
        if chance < deathprob:
            daughter = 0
            print('Your daughter died')
    if wife == 1:
        chance = random.randint(0,100)
        if chance < deathprob:
            wife = 0
            print('Your wife died')
    if granny == 1:
        chance = random.randint(0,100)
        if chance < deathprob:
            granny = 0
            print('Your granny died')
    day = day + 1
    if son == 0 and daughter == 0 and wife == 0 and granny == 0:
        endgame = 3
    if day == 15:
        endgame = 4
    if money < 0:
        endgame = 5
    if money > 1000 :
        endgame = 1        
    
if endgame == 1:
    print('CONGRATULATIONS!')
    print('YOU WIN!')
    print('You managed to earn enough mouney to move away from this country with your famaly!')
elif endgame == 3:
    print('YOU LOST')
    print('All your family members are dead and now you have no reason too live...')
elif endgame == 4:
    print('YOU LOST')
    print('Police found out all bad staff about you and you are going too be in jail very soon...')
else:
    print('YOU LOST')
    print('You do not have money too pay for the rent and now your famaly is going to die...')
