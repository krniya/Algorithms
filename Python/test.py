class Player:
    teamName = 'Liverpool' # class variables
    def __init__(self, name):
        self.name = name # creating instance variables

    @staticmethod
    def demo():
        print("I am a static method.")

p1 = Player("lol")
p1.demo()
Player.demo()

