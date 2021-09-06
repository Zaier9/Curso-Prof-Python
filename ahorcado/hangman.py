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

 words = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()

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

    for in in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            empty_spaces = empty_spaces[:i] + secret_word[i] + empty_spaces[i+1:]
        