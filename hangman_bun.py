tries = 0
max_tries = 1200
word = ""
guess = ""
alphabet = "IETRALCUĂNOSMPDFGȚȘVZBHÂÎJXKYWQ"

with open('cuvinte.csv', 'r', encoding='utf-8') as file:
    cuvinte = file.read()

with open('dictionar_cu_toate_cuv.csv', 'r', encoding='utf-8') as file:
    dictionar = file.read()


rows = cuvinte.strip().split("\n")
cuvinte_dictionar = [item.upper() for item in dictionar.strip().split("\n")]

for row in rows:
    index_alpha = 0
    number, masked_word, full_word = row.split(";")
    word = full_word
    guess = masked_word

    possible_words = [w for w in cuvinte_dictionar if len(w) == len(word)]
    #iteram prin dict si cautam cuvinte cu aceeasi lungime ca a cuvantului la care ne aflam


    possible_words = [w for w in possible_words if all(
        guess[i] == "*" or guess[i] == w[i] for i in range(len(guess))
    )]

    tries1=0
    while word != guess:
        print(f"Cuvant: {guess}, Litera: {alphabet[index_alpha]}, Incercari: {tries1}")

        if len(possible_words) == 1:
            guess = possible_words[0]
            tries1 += 1
            print(f"Am ghicit cuvantul: {guess} in {tries1} incercari.\n")
            break


        if alphabet[index_alpha] in guess:
            print(f"Litera {alphabet[index_alpha]} este deja in cuvant.")
            index_alpha += 1
            tries += 1
            continue


        possible_words = [w for w in possible_words if all(
            guess[i] == "*" or guess[i] == w[i] for i in range(len(guess))
        )]

        # check if the letter is in any possible word
        found = any(alphabet[index_alpha] in w for w in possible_words)

        if not found:
            tries1 += 1
            print(f"{alphabet[index_alpha]} is not in the word ")
            index_alpha += 1
            continue


        for i in range(len(word)):
            if guess[i] == "*":
                if word[i] == alphabet[index_alpha]:
                    tries1 += 1
                    guess = guess[:i] + alphabet[index_alpha] + guess[i + 1:]
                    print(f"Letter: {alphabet[index_alpha]} has been added, tries for this word: {tries1}")

        index_alpha += 1
    tries = tries + tries1

print(f"\nIncercari totale: {tries}, maximul admis {max_tries}")
