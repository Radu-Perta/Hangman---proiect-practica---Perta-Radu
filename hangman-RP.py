alfabet = "AĂÂBCDEFGHIÎJKLMNOPRSTUȘȚVZ"
# initializam o variabila care pentru moment contine toate literele din alfabetul romanesc
def read_masked_words(filename):
    masked_full_pairs = [] # initializam o lista goala, care mai tarziu va contine cuvintele incomplete si cele complete
    with open(filename, mode='r', encoding='utf-8-sig') as file:
        data = file.read() # ii atribuim lui data cuvintele citite din fisier
        rows = data.strip().split("\n") # separam cuvintele intre ele la fiecare "new line"
        for row in rows:
            number, masked_word, full_word = row.split(";") # separam si toate elementele de pe o linie
            masked_full_pairs.append((masked_word, full_word)) # adaugam in lista noastra goala doar cuvintele mascate si cele complete
    return masked_full_pairs

def update_guess(full_word, guess, letter):
    updated_guess = list(guess) # convertim str intr-o lista
    matched = False # initilizam variabila cu fals
    for i in range(len(full_word)):
        if guess[i] == "*" and full_word[i] == letter:
            # verificam daca litera/* de pe pozitia i este * si litera curenta corespunde cu litera cuvantului intreg de pe pozitia i
            updated_guess[i] = letter # daca corespunde if-ului plasam litera pe pozitia i in "updated_guess"
            matched = True
    return "".join(updated_guess), matched


def needed_letters(masked_word, full_word):
    return set(full_word[i] for i in range(len(full_word)) if masked_word[i] == '*')
# returnam un set de litere pe exact pozitia in care fiecare are "*" in cuvantul incomplet

def reorder_alphabet(masked_word, needed_letters):
    ordered_letters = [masked_word[i] if masked_word[i] != '*' else None for i in range(len(masked_word))]
# cream o lista care va contine literele deja ghicite si "None" pentru cele pe care inca trebuie sa le ghicim

    final_order = [] # cream o lista goala pentru ordinea finala a literelor
    for letter in needed_letters:
        if letter in alfabet:
            final_order.append(letter)
# verificam daca litera este in alfabet, daca este o adaugam in lista finala
    return ''.join(final_order) # returnam noul str cu litere necesare din alfabet

def main(filename):
    masked_full_pairs = read_masked_words(filename) # citim doar cuv complete si incomplete cu ajutorul functiei de mai sus
    tries = 0  # initilizam un counter pentru a putea tine cont de try-uri

    for masked_word, full_word in masked_full_pairs: # iteram prin toate cuvintele...
        guess = masked_word # incepem ghicitul de la cuvantul incomplet

        letters_needed = needed_letters(masked_word, full_word) # luam literele necesare pentru a completa cuv incomplet
        reordered_alphabet = reorder_alphabet(masked_word, letters_needed) # reodornam alfabetul in functie de litere avem nevoie pt cuv

        print(f"\nToate litere necesare pentru '{masked_word}' sunt: {reordered_alphabet}")

        for letter in reordered_alphabet: # iteram prin toat alfabetul
            guess, matched = update_guess(full_word, guess, letter)
# updatam guess-ul dupa fiecare litera ghicita, la fel si cu matched-ul in true

            if matched:
                tries += 1 # daca litera se potriveste, adaugam +1 la counterul de try-uri
                print(f"Cuvant updatat: {guess}, Incercari pana in momentul actual: {tries}")

            if guess == full_word:
                tries += 1 # verificam daca am ajuns la cuvantul complet si mai adaugam un try
                print(f"Cuvant complet: {guess} in {tries} tries")
                break

    print(f"\nIncercari totale: {tries} ; Incercari maxime admise: 1200")


if __name__ == "__main__":
    filename = 'cuvinte.csv'
    main(filename)
