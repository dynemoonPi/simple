"""
The Birthday Paradox, also called the
Birthday Problem, is the surprisingly high
probability that two people will have the
same birthday even in a small group of people.
In a group of 70 people, there’s a 99.9 percent chance
of two people having a matching birthday. But even
in a group as small as 23 people, there’s a 50 percent
chance of a matching birthday. This program performs several probability experiments to determine
the percentages for groups of different sizes. We call these types of experiments,
in which we conduct multiple random trials to understand the
likely outcomes, Monte Carlo experiment
"""

import random
import datetime


class BirthdayParadox:

    MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


    def get_birthday(number_of_birthdays):
        birthdays = []

        for i in range(0,number_of_birthdays):

            start_year = datetime.date(2001, 1, 1)

            # get a random day
            random_day = datetime.timedelta(random.randint(0, 365))
            birthday = start_year + random_day
            birthdays.append(birthday)


        return birthdays

    def get_match(birthdays):
        """ return the date object that occurs more than once
            in the birthday list
        """
        global birthday_match
        birth_match = 0
        if len(birthdays) == len(set(birthdays)):
            return None
        # Compare each birthday to every other birthday:
        for i, birthday_element in enumerate(birthdays):
            for j, birth_element in enumerate(birthdays[i+1:]):
                if birthday_element == birth_element:
                    birthday_match = birthday_element
        return birthday_match

    print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
    The Birthday Paradox shows us that in a group of N people, the odds
    that two of them have matching birthdays is surprisingly large.
    This program does a Monte Carlo simulation (that is, repeated random
    simulations) to explore this concept. (It's not actually a paradox, it's just a surprising result.)
    ''')


    # while True :
    #     print("how many birthday shall i generate !!!")
    #     num = int(input(">>:"))

   # run 100_1000 as simuration

if __name__ == '__main__':

    while (True):

        num = int(input("how many birthdays shall generate: "))

        birthDays = BirthdayParadox.get_birthday(num)
        temp = 0

        for i, element in enumerate(birthDays):
            month = BirthdayParadox.MONTHS[element.month-1]
            date = "{} {}".format(month,element.day)
            print(date, end=';')

        # How many simulations had matching birthdays in them.
        for i in range(100_000):
            if i % 10_000 == 0:
                print(i, " simuration")
            birthDays = BirthdayParadox.get_birthday(num)
            match = BirthdayParadox.get_match(birthDays)

            if match != None:
                temp += 1
        probability = round(temp /100_000 * 100 , 2)


        print("probality:>>", probability)














