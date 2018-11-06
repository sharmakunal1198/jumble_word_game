# This package is import for using random value.
import random
#An empty List
word = ""
#points of player 1
pts1=0
#points for player 2
pts2=0

#function will return the jumble word
def jumble():
        #some predefined Words in list.
        WORDS=['python','reactjs','java','golang','priyansh ','guarav','vaibhav','hemant','sachin','umang','shikhar','yagyesh','devansh']
        global word
        # select an any arbitatry word from predefined words.
        word = random.choice(WORDS)
        # jumble[] List in which we get alphabets.
        jumble = []
        # new jumble is string in which we get new jumble word.
        new_jumble = ""
        #number[] is to jumble the alphabet using indexing
        number = []
        # we append each number into the number[] and shuffle that indexes. 
        for i in range(0,len(word)):
            number.append(i)
            random.shuffle(number)
       # Append word at index     
        for i in number:
                jumble.append(str(word[i]))     

        new_jumble = new_jumble.join(jumble)         
        return new_jumble
        
# function return userinput
 def user_input():
    user_answer = input("enter the answer :-  ")
    return user_answer     


i=1
while i > 0:
    print("do you want to play press yes/no")
    # Taking user input in Answer1
    answer1 = input()
 
    if answer1 == 'yes':
        
        if(i%2==0):
            print("player 2 chance")
            # getting a jummble word
            jumble_word = jumble() 
            print("jumble word for player 2 is:-",jumble_word)
            # getting user 2 answer    
            player2_answer = user_input()
            # if answer is right than increasing the point of user 2
            if player2_answer == word:
                pts2 = pts2+1
        else:
            print("player 1 chance")
            # getting a jummble word
            jumble_word = jumble() 
            print("jumble Word for player 1 is :-",jumble_word)
            # getting user 2 answer    
            player1_answer = user_input()
            # if answer is right than increasing the point of user 2

            if player1_answer == word:
                pts1 = pts1+1        
        
    else:
        print("Player 1 point is :-",pts1)
        print("player 2 point is :-",pts2)
        exit()
    i=i+1
