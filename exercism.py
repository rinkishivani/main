# abstract base class work
# from abc import ABC, abstractmethod
 
 
# class Animal(ABC):
 
#     def move(self):
#         pass
 
# class Human(Animal):
 
#     def move(self):
#         print("I can walk and run")
 
# class Snake(Animal):
 
#     def move(self):
#         print("I can crawl")
 
# class Dog(Animal):
 
#     def move(self):
#         print("I can bark")
 
# class Lion(Animal):
 
#     def move(self):
#         print("I can roar")
 
# # Driver code
# R = Human()
# R.move()
 
# K = Snake()
# K.move()
 
# R = Dog()
# R.move()
 
# K = Lion()
# K.move()

# """Functions for creating, transforming, and adding prefixes to strings."""
# isbn_valid_char = "0123456789X"
# def is_valid(isbn):
#     for digit in isbn:
#         isbn_no = ""
#         if digit.isnumeric():
#             isbn_no += digit
    

# is_valid("3-598-21508-8")

# def add_prefix_un(word):
#     """Take the given word and add the 'un' prefix. """

#     word = "un" + word
#     return word

# add_prefix_un("happy")
# def make_word_groups(vocab_words):
#     """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended. """
#     word_groups =  "word_groups[0]"
#     for i in range(1,len(vocab_words)):
#         word_groups += " :: " + vocab_words[0] + vocab_words[i]
#     return word_groups

# make_word_groups(['auto', 'didactic', 'graph', 'mate', 'chrome', 'centric', 'complete',
#               'echolalia', 'encoder'])
# def remove_suffix_ness(word):
#     """Remove the suffix from the word while keeping spelling in mind.

#     :param word: str - of word to remove suffix from.
#     :return: str - of word with suffix removed & spelling adjusted.

#     For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
#     """
#     word = word.removesuffix("ness")
#     print(word[:-1] + "y")
# # remove_suffix_ness("happiness")

# def adjective_to_verb(sentence, index):
#     """Change the adjective within the sentence to a verb.

#     :param sentence: str - that uses the word in sentence.
#     :param index: int - index of the word to remove and transform.
#     :return: str - word that changes the extracted adjective to a verb.

#     For example, ("It got dark as the sun set.", 2) becomes "darken".
#     """

#     extracted = ""
#     for i in range(len(index)):
        
#         s = sentence[i].split()
#         # s.replace(".","")
#         i = (index[i])
#         extracted += (s[i]+ "en ")
#         extracted = extracted.replace(".","")
#     print(extracted.split())

# input_data = ['Look at the bright sky.',
#               'His expression went dark.',
#               'The bread got hard after sitting out.',
#               'The butter got soft in the sun.',
#               'Her eyes were light blue.',
#               'The morning fog made everything damp with mist.',
#               'He cut the fence pickets short by mistake.',
#               'Charles made weak crying noises.',
#               'The black oil got on the white dog.']
# index_data = [-2, -1, 3, 3, -2, -3, 5, 2, 1]
# adjective_to_verb(input_data, index_data)
# adjective_to_verb(input_data, index_data)
#  --------------- Pig latin ---------------

# def translate(text):
#     vowel = 'aeiou'
#     if text[0] in vowel or text[0:2] == "xr" or text[0:2] == "yt":
#         text += "ay"
#     else:
#         ytext = text[1:]
#         if "y" in ytext:
#             i_of_y = text.find("y")
#             text = text[i_of_y:] + text[0:i_of_y] + "ay"

#         elif text[1:3] == "qu":
#             text_move = text[0:3]
#             text = text[3:] + text_move + "ay"
#         else:  
#             text_move = text[0:2]
#             text = text[2:] + text_move + "ay"
#     return text
# translate("rhythm")

#  --------------- Hey Bob ---------------
#  def response(hey_bob):
#     hey_bob = strip(hey_bob)
#     print(hey_bob)
#     if hey_bob.isupper() and hey_bob.endswith("?"):
#         answer = "Calm down, I know what I'm doing!" 
#     elif hey_bob.endswith("?"):
#         answer = "Sure."
#     elif hey_bob.isupper():
#         answer = "Whoa, chill out!"
#     elif not hey_bob or hey_bob.isspace():
#         answer = "Fine. Be that way!"
#     else:
#         answer = "Whatever."
#     return answer


#  --------------- Armstrong Number ---------------
# def is_armstrong_number(number):
#     '''To determine whether number is an Armstrong number '''
#     digits = len(str(number))
#     # print(type(digits))
     
#     armstrong_num = 0

#     for num in str(number):
#         # print(num)
#         armstrong_num += int(num)**digits
#         print(armstrong_num)
#     if number == armstrong_num:
#         return 
# is_armstrong_number(153)