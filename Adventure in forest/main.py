from sprites import *
from config import *
import sys


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Adventure in Forest")

        self.screen = pygame.display.set_mode((width_screen, height_screen))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("fonts/pixel-anchor-jack_0.ttf", 32)
        self.run = True

        self.character_spritesheet = Spritesheet('images/Player/Walk.png')
        self.idle_spritesheet = Spritesheet('images/Player/Idle.png')

        self.terrain_spritesheet = Spritesheet('images/Outdoor.png')
        self.interrain_spritesheet = Spritesheet('images/indoor.png')
        self.grass_spritesheet = Spritesheet('images/Texture/TX Tileset Grass.png')

        self.enemy_spritesheet = Spritesheet('images/Zombie/Walk.png')

        self.intro_background = pygame.image.load("images/bg.png")
        self.MENU_background = pygame.image.load("images/bgMenu.png")
        # self.play_background = pygame.image.load("images/backg.png")

    def CreateTilemap(self):
        for i, row in enumerate(tilemap):
            for j, colum in enumerate(row):
                Ground(self, j, i)
                if colum == "#":
                    Block(self, j, i)
                if colum == "@":
                    Tree(self, j, i)
                if colum == "0":
                    Trope1(self, j, i)
                if colum == "P":
                    Player(self, j, i)
                if colum == "D":
                    Desks(self, j, i)
                if colum == "E":
                    Enemy(self, j, i)
                if colum == "O":
                    Trope(self, j, i)
                if colum == "A":
                    TropeA(self, j, i)
                if colum == "B":
                    TropeB(self, j, i)
                if colum == "C":
                    TropeC(self, j, i)
                if colum == "U":
                    TropeUP(self, j, i)
                if colum == "T":
                    TropeDW(self, j, i)
                if colum == "W":
                    Wall(self, j, i)
                if colum == "F":
                    Flower(self, j, i)

    def new(self):
        self.play = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.CreateTilemap()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False
                self.run = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(black)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.play:
            self.events()
            self.update()
            self.draw()
        self.run = False

    def game_over(self):
        pass

    def settings_screen(self):
        menu = True

        title = self.font.render("Settings", True, blue)
        title_rect = title.get_rect(x=200, y=10)

        title_soon = self.font.render("!Comming Soon!", True, blue)
        title_soon_rect = title.get_rect(x=130, y=200)

        ex_button = Button(270, 280, 97, 45, white, black, "Exit", 24)

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                    self.run = False

                mouse_pos = pygame.mouse.get_pos()
                mouse_pressed = pygame.mouse.get_pressed()

                if ex_button.pressed(mouse_pos, mouse_pressed):
                    menu = False
                    self.intro_screen()

            self.screen.blit(self.MENU_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(title_soon, title_soon_rect)
            self.screen.blit(ex_button.image, ex_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def intro_screen(self):
        intro = True

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        title = self.font.render("Adventure in Forest", True, blue)
        title_rect = title.get_rect(x=35, y=10)

        play_button = Button(215, 150, 220, 50, white, black, "START", 25)
        settings_button = Button(215, 210, 220, 50, white, black, "SETTINGS", 25)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.run = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.pressed(mouse_pos, mouse_pressed):
                intro = False

            if settings_button.pressed(mouse_pos, mouse_pressed):
                intro = False
                self.settings_screen()

            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(settings_button.image, settings_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()


g = Game()
g.intro_screen()
g.new()
while g.run:
    g.main()
    g.game_over()


pygame.quit()
sys.exit()
