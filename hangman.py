class Hangobj(object):
    def __init__(self, word):
        
        self.secretword = word
        self.disguisedWord = ['_']*len(self.secretword)
        self.lettersGuessed = []
        self.guessesLeft = 8
        self.wordNotGuessed = True

    def isWordGuessed(self):
        if self.secretword == ''.join(self.disguisedWord):
            self.wordNotGuessed = False

    def isGuessCorrect(self,guess):
        if guess in self.secretword:
            for i in range(0, len(self.secretword)):
                if self.secretword[i] == guess:
                    self.disguisedWord[i] = guess
            return True
        else:
            return False

def getSecretWord():
    secWord = raw_input('please enter the secret word: ')
    return secWord

def getGuess():
    choice = raw_input('Enter 1 to guess word or 2 to guess a letter: ')
   
    if int(choice) ==1:
        return raw_input('guess a word: ')        

    elif int(choice) == 2:
        return raw_input('Please enter a letter: ')

def checkGuess(hangman, guess):
    hangman.guessesLeft -= 1

    if len(guess) == 1:
        if guess in hangman.lettersGuessed:
            return 'you already guessed that letter! Still counts as a guess..'
        else:
            hangman.lettersGuessed.append(guess)
            if hangman.isGuessCorrect(guess):
                return 'You guessed correctly'
            else:
                return 'You guessed wrong'
    else:
        if guess == hangman.secretword:
            hangman.wordNotGuessed = False
            return 'wait a minute...'

def hangman():
    hangman = Hangobj(getSecretWord())

    while hangman.guessesLeft > 0 and hangman.wordNotGuessed: 
        print ''.join(hangman.disguisedWord)
        print 'letters guessed already: ' , ','.join(hangman.lettersGuessed)
        print 'you have', hangman.guessesLeft, 'guesses remaining' 
        
        print checkGuess(hangman, getGuess())
        hangman.isWordGuessed()

    if hangman.wordNotGuessed == True:
        print 'sorry you have lost. The word was: ' , hangman.secretword
    else:
        print ('you have won!')

hangman()    
