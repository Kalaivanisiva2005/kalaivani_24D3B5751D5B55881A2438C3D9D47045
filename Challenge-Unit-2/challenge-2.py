class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Create objects and call the play method for each object
if __name__ == "__main__":
    player1 = Player()
    batsman1 = Batsman()
    bowler1 = Bowler()

    print("Player 1:")
    player1.play()

    print("\nBatsman 1:")
    batsman1.play()

    print("\nBowler 1:")
    bowler1.play()
