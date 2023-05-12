import turtle as t


class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True

    def __drawHead(self):
        t.setpos(0,0)
        t.circle(100)

    def __drawEyes(self):
        t.setpos(-50,0)
        t.circle(5)
        t.setpos(50,0)
        t.circle(5)

    def __drawMouth(self):
        t.setpos(-50,-75)
        t.circle(50, 180)

    def draw_face(self):
        t.clear()
        self.__drawHead()
        self.__drawEyes()
        self.__drawMouth()

    def isSmile(self):
        drawsmile = True if self.__smile else False

    def isHappy(self):
        pass

    def isDarkEyes(self):
        pass

    def changeMouth(self):
        pass
        self.draw_face()

    def changeEmotion(self):
        pass
        self.draw_face()

    def changeEyes(self):
        pass
        self.draw_face()


def main():
    face = True
    face.denominator

    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" + ", " + "smile"
        emotion = "angry" + ", " + "happy"
        eyes = "blue" + ", " + "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            pass
        elif menu == 2:
            pass
        elif menu == 3:
            pass
        else:
            break

    print("Thanks for Playing")

    t.hideturtle()
    t.done()


main()