import past_deck as past
import present_deck as present
import future_deck as future
import love_deck as love
import random, time

answer = input("How many times do you want the deck shuffled? ")
print("Take some time to sit with the deck as you shuffle it")
time_answer = int(input("how long would you like to work with the deck (in seconds)? "))
keys_past = list(past.past_deck.keys())
keys_present = list(present.present_deck.keys())
keys_future = list(future.future_deck.keys())
keys_love = list(love.love_deck.keys())
time.sleep(time_answer)

key = "reversed"

for i in range(int(answer)):
    random.shuffle(keys_past)

for h in range(int(answer)):
    random.shuffle(keys_present)

for g in range(int(answer)):
    random.shuffle(keys_future)

print("\n")

question = input("What question will you ask the cards? ")

print("\n")

random_card_past = random.choice(list(past.past_deck.keys()))

random_int_1 = random.randint(0, 1)

print("you asked the cards: ", question, " ,and the cards said this about your past...\n")

if key in past.past_deck[random_card_past].keys():
    if random_int_1 == 1:
        print(random_card_past, "\n", past.past_deck[random_card_past]["title"], "\n",
              past.past_deck[random_card_past]["normal"])
    else:
        print(random_card_past, "reversed", "\n", past.past_deck[random_card_past]["title"], "\n",
              past.past_deck[random_card_past]["reversed"])
else:
    print(random_card_past, "\n", past.past_deck[random_card_past]["title"], "\n",
          past.past_deck[random_card_past]["normal"])

print("\n")

random_card_present = random.choice(list(present.present_deck.keys()))


while random_card_present == random_card_past:
    random_card_present = random.choice(list(present.present_deck.keys()))

random_int_2 = random.randint(0, 1)

print("you asked the cards: ", question, " ,and the cards said this about your present...\n")

if key in past.past_deck[random_card_present].keys():
    if random_int_2 == 1:
        print(random_card_present, "\n", present.present_deck[random_card_present]["title"], "\n",
              present.present_deck[random_card_present]["normal"])
    else:
        print(random_card_present, "reversed", "\n", present.present_deck[random_card_present]["title"], "\n",
              present.present_deck[random_card_present]["reversed"])
else:
    print(random_card_present, "\n", present.present_deck[random_card_present]["title"], "\n",
          present.present_deck[random_card_present]["normal"])

print("\n")

random_card_future = random.choice(list(future.future_deck.keys()))

while random_card_future == random_card_past or random_card_future == random_card_present:
    random_card_future = random.choice(list(future.future_deck.keys()))

random_int_3 = random.randint(0, 1)

print("you asked the cards: ", question, " ,and the cards said this about your future...\n")

if key in future.future_deck[random_card_future].keys():
    if random_int_3 == 1:
        print(random_card_future, "\n", future.future_deck[random_card_future]["title"], "\n",
              future.future_deck[random_card_future]["normal"])
    else:
        print(random_card_future, "reversed", "\n", future.future_deck[random_card_future]["title"], "\n",
              future.future_deck[random_card_future]["reversed"])
else:
    print(random_card_future, "\n", future.future_deck[random_card_future]["title"], "\n",
          future.future_deck[random_card_future]["normal"])

print("\n")

go_on = input("Would you like to draw for your romance reading? (y/n) ")
go_on = go_on.upper()
if go_on == "Y" or go_on == "YES":
    pass
else:
    print("\n")
    print("Go with peace for the foreknowledge you have gained may change your path for the better \n"
          "or the worse, but you will be prepared for what is to come")
    quit()

print("Now we will shuffle the deck one more time for your love reading")

print("\n")

print("you asked the cards: ", question, " ,and the cards said this about your love life...\n")

for f in range(int(answer)):
    random.shuffle(keys_love)

random_card_love = random.choice(list(love.love_deck.keys()))

random_int_4 = random.randint(0, 1)

if key in love.love_deck[random_card_love].keys():
    if random_int_4 == 1:
        print(random_card_love, "\n", love.love_deck[random_card_love]["title"], "\n",
              love.love_deck[random_card_love]["normal"])
    else:
        print(random_card_love, "reversed", "\n", love.love_deck[random_card_love]["title"], "\n",
              love.love_deck[random_card_love]["reversed"])
else:
    print(random_card_love, "\n", love.love_deck[random_card_love]["title"], "\n",
          love.love_deck[random_card_love]["normal"])

print("\n")
print("Go with peace for the foreknowledge you have gained may change your path for the better \n"
      "or the worse, but you will be prepared for what is to come")



"""

    https://tarot-explained.com/card-meanings/major-arcana/ 

marjor arcana has 22 cards both normal and reversed positions
the minor arcana has 56 cards just normal position

    https://tarot-explained.com/card-meanings/cups/ 
    https://tarot-explained.com/card-meanings/wands/ 
    https://tarot-explained.com/card-meanings/swords/ 
    https://tarot-explained.com/card-meanings/pentacles/ 

"""