import random

word = ""
pts1=0
pts2=0

def jumble():
        WORDS=['python','reactjs','java','golang','priyansh ','guarav','vaibhav','hemant','sachin','umang','shikhar','yagyesh','devansh']
        global word
        word = random.choice(WORDS)
        jumble = []
        new_jumble = ""
        number = []
        for i in range(0,len(word)):
            number.append(i)
            random.shuffle(number)
            
        for i in number:
                jumble.append(str(word[i]))     

        new_jumble = new_jumble.join(jumble)         
        return new_jumble
        
def user_input():
    user_answer = input("enter the answer :-  ")
    return user_answer     


i=1
while i > 0:
    print("do you want to play press yes/no")
    answer1 = input()
    if answer1 == 'yes':
        if(i%2==0):
            print("player 2 chance")
            jumble_word = jumble() 
            print("jumble word for player 2 is:-",jumble_word)
            player1_answer = user_input()
            if player1_answer == word:
                pts2 = pts2+1
        else:
            print("player 1 chance")
            jumble_word = jumble() 
            print("jumble Word for player 1 is :-",jumble_word)
            player1_answer = user_input()
            if player1_answer == word:
                pts1 = pts1+1        
        
    else:
        print("Player 1 point is :-",pts1)
        print("player 2 point is :-",pts2)
        exit()
    i=i+1