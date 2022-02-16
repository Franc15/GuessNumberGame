class GuessNumber:
    def __init__(self, num, min=0, max=100):
        self.number = num
        self.min = min
        self.max = max
        self.guesses = 0

    def get_guess(self):
        guess = input(f'Guess a number between {self.min} - {self.max}: ')

        if self.valid_number(guess):
            return int(guess)
        else:
            print('Enter a valid number')
            return self.get_guess()

    def valid_number(self, strnum):
        try:
            num = int(strnum)
        except:
            return False
        return self.min <= num <= self.max\

    def play(self):
        while True:
            guess = self.get_guess()
            self.guesses += 1

            if guess < self.number:
                print('your guess was under')
            elif guess > self.number:
                print('your guess was above')
            else:
                print(f'you guessed right in {self.guesses} guesses!')
                break

game = GuessNumber(45)
game.play()