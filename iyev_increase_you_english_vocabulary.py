import os
import random

def header():
    print("Developed by Douglas Bernardino.\nContact me: <dougl4s.viana@gmail.com>.\n")

def clear_screen():
    os.system("cls")

def list_to_str(l): #Receve list, retorn str.
    return str(l)
    
def ls_to_ll(l): #Recebe uma lista de string, retorna uma lista de lista.
    list_of_list = []
    N = len(l)
    for i in range(N):
        list_of_list.append(str_to_list(l[i]))
    return list_of_list

def str_to_list(word): #Recebe str, retorna list.
# -------------------------- Converte uma list "stringada", i.e., '[0, 0,..]' para um lista verdadeira.
# '[cat,gato]\n'
    word_aux2 = ['','']
    word_aux = word.split("\n")[0]
    N = len(word)
    last_char_index = N-1
    penultimate_char_index = last_char_index - 1
    second_char_index = 1
    
    if ',' not in word:
        print("Input error! Format input should be [arg1,arg2].")
        return 0
    elif " , " in word:
        word_aux2 = word_aux[second_char_index : penultimate_char_index].split(" , ")
    elif " ," in word:
        word_aux2 = word_aux[second_char_index : penultimate_char_index].split(" ,")
    elif ", " in word:
        word_aux2 = word_aux[second_char_index : penultimate_char_index].split(", ")
    else:
        word_aux2 = word_aux[second_char_index : penultimate_char_index].split(',')
        
    word_aux2[0] = nomarlize_word(word_aux2[0])
    word_aux2[1] = nomarlize_word(word_aux2[1])
    
    return word_aux2

def nomarlize_word(word): #Recebe str, retorna str.
    word_normalized_aux = word.lower()
    x = word_normalized_aux[0].upper()
    word_normalized = x + word_normalized_aux[1:]
    return word_normalized
    
def db_check(db_name):
    cwd = os.getcwd()
    archives = os.listdir(cwd)
    if db_name in archives:
        return 1
    else:
        return 0

def add_word(db_name, word): # type(word) == str
    word_to_add = word + '\n'
    var_database = open(db_name, 'r')
    l = var_database.readlines()
    var_database.close()
       
    # Se a palavra passada como parâmetro for nova, ela é escrita no banco de dados.
    var_database = open(db_name, 'a')
    
    if (word_to_add not in l):
        var_database.write(word_to_add)
        var_database.close()
    
def show_list(db_name):
    print("Current user\'s word list:\n")
    var_database = open(db_name, 'r')
    for s in var_database.readlines():
        print(s,end='')
    var_database.close()
    print("")
    
def get_word(message):
    word = input(message)
    return word
    
def delete_word(db_name, word): # type(word) == str
# Cria um banco de dados auxiliar temporário que irá conter o corrente menos a palavra deletada. Acho que salvou repetidamente, provavel que seja na função add_word.
   
    word_to_del = word + "\n"
    var_database = open(db_name, 'r')
    var_database_aux = open('database_aux', 'w')
    
    # Se a palavra a no banco de dados não for a que tem que ser deletada, então escreve-se esta no banco de dados auxiliar.
    for s in var_database.readlines():
        if (s != (word_to_del)):
            var_database_aux.write(s)
        else:
            pass
    var_database.close()
    var_database_aux.close()
    
    # Substitui o conteúdo do banco de dados corrente pelo do auxiliar.
    var_database = open(db_name, 'w')
    var_database_aux = open('database_aux', 'r')
    
    for s in var_database_aux.readlines():
        var_database.write(s)
    
    var_database_aux.close()
    var_database.close()
        
def play(db_name):
    var_database = open(db_name, 'r')
    list = ls_to_ll(var_database.readlines())
    N = len(list)
    seq = random.sample(range(N),N)
    clear_screen()
    for i in seq:
        answer = nomarlize_word(input("\n%s\nEnter answer: " %list[i][0]))
        if answer in list[i][1]:
            print("Right!\n")
        else:
            print("Incorrect!")
            return 0

def getch():
    q = 'x'
    while q =='x':
        q = input("Press any key...")

def select_menu():
    option = input("\n:: Choose a option ::\n\n 1. Play game\n 2. Add word\n 3. Delete word\n 4. Show current user word list\n E. Exit\n\n>> ")
    print("")
    if option in ['1','2','3','4', 'e', 'E']:
        return option
    else:
        print("\nInvalid input!\n")
    
def main(user):
    header()
    
    if (db_check(user) == 0):
        var_database = open(user, 'w')
        var_database.close()
        
    while True:
        clear_screen()
        option = select_menu()
          
        if option == '1': # Caso 1: Jogar
            play(user)
            
        elif option == '2': # Caso 2: Adicionar palavra
            while True:
                clear_screen()
                word_to_add = get_word("Enter the word in format [cat,gato]\nor press F to return to main menu:\n\n>> ")
                print('')
                if word_to_add not in ['f', 'F']:
                    add_word(user, word_to_add)
                else:
                    break
                    
        
        elif option == '3': # Caso 3: Apagar palavra
            while True:
                clear_screen()
                show_list(user)
                word_to_del = get_word("Enter the word to delete in format [cat,gato]\nor press F to return to main menu:\n\n>> ")
                if word_to_del not in ['f', 'F']:
                    delete_word(user, word_to_del)
                else:
                    break
        
        elif option == '4': # Caso 4: Mostrar lista de palavras
            clear_screen()
            show_list(user)
            getch()
            
        else: # Caso E/e: Sair
            clear_screen()
            print("Bye!")
            break
            return 1
header()        
user = nomarlize_word(str(input("User: ")))
print("\nHello, %s!\n" %user)
getch()

main(user)
