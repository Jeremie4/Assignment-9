import turtle as t


class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True

    def draw_face(self):
        t.clear()
        self.__drawHead()
        self.__drawEyes()
        self.__drawMouth()
    
    def __drawHead(self):
        t.pu
        t.setpos(0,0)
        t.pd
        t.circle(100)

    def __drawEyes(self):
        t.pu
        t.setpos(25,100)
        t.pd
        t.circle(5)
        t.pu
        t.setpos(-25,100)
        t.pd
        t.circle(5)

    def __drawMouth(self):
        pass

    def isSmile(self):
        pass

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
    face = Face()
    face.draw_face()

    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" or "smile"
        emotion = "angry" or "happy"
        eyes = "blue" or "black"
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

    t.hidet()
    t.done()


main()