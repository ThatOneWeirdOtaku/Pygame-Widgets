import pygame, threading

class Button:
    """
    A button that has a function to check if something is overlapping, typically a mouse.
    """
    
    def __init__(self, color, x, y, width, height, text = "", fontsize = 50):

        self.color = color
        self.preservedcolor = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.fontsize = fontsize
        self.fontname = None

    def draw(self, win, outline = None):
        """
        Draws onto the screen with blit.
        """

        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != "":

            font = pygame.font.Font(self.fontname, self.fontsize)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
   
    def isOverlapping(self, pos):
        """
        Takes in a double and checks if it's overlapping with itself.
        """

        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False
    
    def colorchanged(self):

        self.color = self.preservedcolor

    def clickBlip(self, clicked_color):
        """
        Changes and then changes the color back after .2 seconds after a click.
        """

        self.color = clicked_color
        Timer = threading.Timer(.2, self.colorchanged)
        Timer.start()



class Text:
    """
    A simple class that has all the control you'll need for text.
    """

    def __init__(self, text, pos, fontsize = 50, fontcolor = (0,0,0)):

        self.text = text
        self.pos = pos
        self.fontsize = fontsize
        self.fontcolor = fontcolor

        self.fontname = None
        self.set_font()
        self.render()

    def set_font(self):
        """
        Call after you've changed the text to update it.
        """
        
        self.font = pygame.font.Font(self.fontname, self.fontsize)
    
    def render(self):
        """
        Converts the text into an image. Call after update of text.
        """

        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
    
    def draw(self, win):
        """
        Draws onto the screen with blit.
        """
        
        win.blit(self.img, self.rect)

    def update(self, screen, updated_text = ""):
        """
        The best way to update the text, includes drawing.
        """
        self.text = updated_text
        self.render()
        self.draw(screen)


        




        


