from tkinter import messagebox


class Tutorial():
    def __init__(self):
        messagebox.showinfo(title="Welcome To The Flappy bird Game",
                                message=
                                    "This game was built fully with Python, so it can be a little bit slow.\n\n"
                                    "Game Tutorial:\n"
                                    "1. If you touch the left or right edges, you're going to die.\n"
                                    "2. If you go to the top too much, your bird will die because there is no oxygen.\n"
                                    "3. If you go to the bottom, the net man or his dog will catch you.\n\n"
                                    "4. If you touch any evil bird, your bird gonna die."
                                    "How To Play:\n"
                                    "• Up key to move to the top\n"
                                    "• Left key to move to the left\n"
                                    "• Right key to move to the right"
                                )


    # showing message if the player touch the left or right edges
    def edges_is_touched(self):
        messagebox.showinfo(title="Edges directed", message="Ooops! You lost; make sure not to touch the edges next time.")

    def top_is_touched(self):
        messagebox.showinfo(title="Extremely high", message="Euuh! I'm dying from a lack of oxygen.")

    def bird_catcher_message(self):
        messagebox.showinfo(title="Catched by net man", message="Ooooh Yeah! It's going to cook now.")

    def hunting_dog_message(self):
        messagebox.showinfo(title="Catched by hunting dog", message="rawr! rawr! rawr! rawr!")

