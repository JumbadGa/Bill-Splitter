# write your code here
import random

party_members = {}
number_peoples = int(input("Enter the number of friends joining (including you):\n"))
if number_peoples > 0:
    print("\nEnter the name of every friend (including you), each on a new line: ")
    for i in range(number_peoples):
        name = input()
        party_members.update({name: 0})
    print('\n')
    print("Enter the total bill value:")
    bill = int(input())

    print('\n')
    print('Do you want to use "Who is lucky?" feature? Write Yes/No: ')
    consent = input()

    if consent == "Yes":
        luck_list = list(party_members.keys())
        lucky = random.choice(luck_list)
        print("\n" + lucky + " is the lucky one\n")
        del party_members[lucky]
        per_head = round((bill / len(party_members)), 2)
        party_members = dict.fromkeys(party_members, per_head)
        print(party_members)
    else:
        print("\nNo one is going to be lucky\n")
        per_head = round((bill / len(party_members)), 2)
        party_members = dict.fromkeys(party_members, per_head)
        print(party_members)
else:
    print("No one is joining for the party")
