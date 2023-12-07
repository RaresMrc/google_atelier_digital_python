cuvant = "onomatopee".lower()

cuvant_de_ghicit = list(cuvant)
print(cuvant_de_ghicit)

# for i, val in enumerate(cuvant_de_ghicit)
for i in range(1, len(cuvant_de_ghicit) - 1):
    if (cuvant_de_ghicit[i] != cuvant_de_ghicit[0] and cuvant_de_ghicit[i] != cuvant_de_ghicit[-1]):
        cuvant_de_ghicit[i] = "_"

print(cuvant_de_ghicit)


# ''.join(string_cuvant_de_ghicit) ar fi fost alternativa pentru asta
string_cuvant_de_ghicit = ""

for i in cuvant_de_ghicit:
    string_cuvant_de_ghicit += i


string_cuvant_de_ghicit = list(string_cuvant_de_ghicit)
print(string_cuvant_de_ghicit)

vieti = 7
litere_incercate = list("")

while vieti != 0 and '_' in string_cuvant_de_ghicit:
    # take the user input
    litera = input("Choose a letter: ").lower()
    while (not litera.isalpha() or len(litera) != 1):
        litera = input("Choose a letter: ").lower()
    # check if the letter has been tried already, if not, save it
    if litera not in litere_incercate:
        litere_incercate.append(litera)

    if litera in cuvant:
        for i, val in enumerate(cuvant):
            if val == litera:
                string_cuvant_de_ghicit[i] = litera
        print(''.join(string_cuvant_de_ghicit))
        if '_' not in string_cuvant_de_ghicit:
            print("You won")
    else:
        vieti -= 1
        print(f"You have {vieti} lives left, the letters you tried are: {' '.join(litere_incercate)}")
        if vieti == 0:
            print(f"You lost, the word was {cuvant}\n")