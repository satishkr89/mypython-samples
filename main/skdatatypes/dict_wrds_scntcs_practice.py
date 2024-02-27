from pprint import pprint
# -------------------------------
# create an empty dictionary. this dictionary will save the number of occurrences of each word in any sentence.
wrd_counter = {}
# You would need to use word as key and the number of occurrences as values
# Task1: Ask the user to enter any sentence
try:
    print("Welcome to word counter. This app will count number of occurrences of each word in any sentence.")
    # test : sam was playing sam scored goal goal was winner for sam playing game is sam's passion
    while(True):
        in_sentence = input("Enter scentence : ")
        if in_sentence == "stop":
            print("quitting word counter")
            break
        else:
            word_list = in_sentence.split(" ")
            word_set=set(word_list)
            unique_word_list = list(word_set)
            print(f" unique_word_list {unique_word_list}<....")
            for word in unique_word_list:
                #print(f" checking.......>{word}<....")
                if word in wrd_counter.keys():
                    print(f"{word} ___ already counted, skip adding to dict")
                else:
                    wrd_counter[word.strip("")]= word_list.count(word)
        print(f"In scentence {in_sentence}")
        pprint(f"Occurrences of each word are : {wrd_counter}")
except:
    print("Exception....")



# Task2: Remove the full stops from the sentence.

# in_sentence = input("Enter scentence : ")
# print(f" we have removed all full stops from this scentence: ")
# modified_in_sentence = in_sentence.replace(".","")
# print(modified_in_sentence)


# Task3: Split the sentence with respect to spaces

# in_sentence = input("Enter scentence : ")
# print(f" we have split this scentence based on spaces: ")
# modified_in_sentence =  in_sentence.split(" ")
# print(modified_in_sentence)


# Task4: Use a loop over the splitted sentence
# in_sentence = input("Enter scentence : ")
# word_list = in_sentence.split(" ")
# for word in word_list:
#     print(f" words---->{word}<-")

# Task5: inside the loop check if the word is not present in the dictionary then
#        save the word with the count of 1

new_wrd_counter = {}
# in_sentence = input("Enter scentence : ")
# word_list = in_sentence.split(" ")
# for word in word_list:
#     print(f" words---->{word}<-")
#     if word in new_wrd_counter.keys():
#         print(f"{word} ___ already counted, skip adding to dict")
#     else:
#         new_wrd_counter[word.strip("")]=1
# print(f"final dictionary form scentence is: {new_wrd_counter} ")

# Task6: if the word is already present in the dictionary then
#        increment the word count by 1

# Task7: Outside of the loop show the dictionary 
# Let say if you enter the sentence:
# I am a student and I am working. 
# The dictionary should look like this:
# {'I':2, 'am':2, 'a':1, 'student':1, 'working':1}

# in_sentence = input("Enter scentence : ")
# word_list = in_sentence.split(" ")
# for word in word_list:
#     print(f" words---->{word}<-")
#     if word in new_wrd_counter.keys():
#         print(f"{word} ___ already added, incrementing count")
#         new_wrd_counter[word.strip("")] = new_wrd_counter[word.strip("")] + 1
#     else:
#         new_wrd_counter[word.strip("")]=1
# print(f"final dictionary form scentence is: {new_wrd_counter} ")



# Task8: Check how many words were there in the compelete sentence
# in_sentence = input("Enter scentence : ")
# word_list = in_sentence.split(" ")
# print(f" words---in scentence are: {len(word_list)}")

# -------------------------------
