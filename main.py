import random

def draw_names(names):
    giver = names.copy()
    receiver = names.copy()
    random.shuffle(giver)
    random.shuffle(receiver)
    while not check_mappings_suitability(giver, receiver):
        random.shuffle(giver)
        random.shuffle(receiver)
    return list(zip(giver,receiver))

def check_mappings_suitability(giver,receiver):
    for i in range(len(giver)):
        if giver[i] == receiver[i]:
            return False
    return True

def print_list(list):
    for (a,b) in list:
        print(str(a) + " gives to " + str(b))

print_list(draw_names(["Adam","Bob","Charles","Dan","Emma","Forrest","Gandalf","Hobo"]))
