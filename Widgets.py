import pygame

class Button:

    def __init__(self, color, x, y, width, height, text = ""):

        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline = None):

        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != "":

            font = None #pygame.font.SysFont("comicsans",60) 
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
   
    def isOverlapping(self, pos):

        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

class Text:
    
    def __init__(self, text, pos, **options):

        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 50
        self.fontcolor = (0,0,0)
        self.set_font()
        self.render()

    def set_font(self):

        self.font = pygame.font.Font(self.fontname, self.fontsize)
    
    def render(self):

        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos #pos = top left
    
    def draw(self, win):
        
        win.blit(self.img, self.rect)

        




        


