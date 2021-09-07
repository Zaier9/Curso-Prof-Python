import random
HANGMAN_IMAGES = [
'''
       +---+
       |   |
           |
           |
           |
        
 ========='''
 '''
       +---+
       |   |
       O   |
           |
           |
        
 ========='''
 '''
       +---+
       |   |
       O   |
       |   |
           |
        
 ========='''
 '''
       +---+
       |   |
       O   |
      /|   |
           |
        
 ========='''
 '''
       +---+
       |   |
       O   |
      /|\  |
           |
        
 ========='''
 '''
       +---+
       |   |
       O   |
      /|\  |
      /    |
        
 ========='''
'''
       +---+
       |   |
       O   |
      /|\  |
      / \  |
       |
 =========''']

words = ('hormiga, babuino, tejon, murcielago, oso, castor, camello, gato, almeja, cobra, pantera, coyote, cuervo, ciervo, perro, burro, pato, aguila, huron, zorro, rana, cabra, ganso, halcon, leon, lagarto, llama, topo, mono, alce, raton, mula, salamandra, nutria, buho, panda, loro, paloma, piton, conejo, carnero, rata, cuervo, rinoceronte, salmon, foca, tiburon, oveja, mofeta, perezoso, serpiente, araña, cigüeña, cisne, tigre, sapo, trucha, pavo, tortuga, comadreja, ballena, lobo, wombat, cebra').split()

def get_random_word(wordsList):
#Esta funcion devuelve una cadena al azar de una cadera pasada como argumento
    index_of_words = random.randint(0, len(wordsList) - 1)
    return wordsList[index_of_words]

def show_board(HANGMAN_IMAGES, wrong_letters, correct_letters, secret_word):
    print(HANGMAN_IMAGES[len(wrong_letters)])
    print()

    print('Letras incorrectas:', end=' ')
    for letter in wrong_letters:
        print(letter, end=' ')
    print()

    empty_spaces = '-' * len(secret_word)

    #completar los espacios vacios con las letras adivinadas
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            empty_spaces = empty_spaces[:i] + secret_word[i] + empty_spaces[i+1:]
        
    #mostrar la palabra secreta con espacios entre cada letra
    for letter in empty_spaces:
        print(letter, end=' ')
    print()


def get_attempts(letters_tested):
#Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado solo una letra, y no otra cosa.
    while True:
        print('Adivina una letra')
        attempt = input()
        attempt = attempt.lower()
        if len(attempt) != 1:
            print('Por favor, introduce una letra.')
        elif attempt in letters_tested:
            print('Ya has probado esa letra, prueba con otra.')
        elif attempt not in 'abcdefghijklmnñopqrstuvwxyz,':
            print('Por favor ingresa una LETRA.')
        else:
            return attempt

def play_again():
#Esta funcion devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
    print('Quieres jugar de nuevo? (yes o no)')
    return input().lower().startswith('y')

print('A H O R A D O')
wrong_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
finished = False

while True:
    show_board(HANGMAN_IMAGES, wrong_letters, correct_letters, secret_word)
    #Permite al jugador escribir una letra.
    attempt = get_attempts(wrong_letters + correct_letters)

    if attempt in secret_word:
        correct_letters = correct_letters + attempt

        #Verifica si el jugador ha ganado.
        find_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                find_all_letters = False
                break
        if find_all_letters:
            print('SI! La palabra secreta es "' + secret_word + '"! HAS GANADO!!!')
            finished = True
    else:
        wrong_letters = wrong_letters + attempt

        #Comprobar si el jugador ha agotado sus intentos y ha perdido.
        if len(wrong_letters) == len(HANGMAN_IMAGES) - 1:
            show_board(HANGMAN_IMAGES, wrong_letters, correct_letters, secret_word)
            print('Te has quedado sin intentos! \nDespues de ' + str(len(wrong_letters)) + 'intentos fallidos y ' + str(len(correct_letters)) + 'aciertos, la palabra era "' + secret_word + '"')
            finished = True

    if finished:
        if play_again():
            wrong_letters = ''
            correct_letters = ''
            finished = False
            secret_word = get_random_word(words)
        else:
            break