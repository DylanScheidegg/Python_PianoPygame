from settings import *
from Buttons import Button

pygame.init()
width = 1500
height = 400
window = pygame.display.set_mode((width, height))
pygame.mixer.init()
pygame.mixer.pre_init(22050, -16, 2, 1024)


class Pyano(object):
    def __init__(self):
        self.C_Left = Button((255, 255, 255), 0, height - 200, 100, 200, 60, 'C')
        self.D_Left = Button((255, 255, 255), 100, height - 200, 100, 200, 60, 'D')
        self.E_Left = Button((255, 255, 255), 200, height - 200, 100, 200, 60, 'E')
        self.F_Left = Button((255, 255, 255), 300, height - 200, 100, 200, 60, 'F')
        self.G_Left = Button((255, 255, 255), 400, height - 200, 100, 200, 60, 'G')
        self.A_Left = Button((255, 255, 255), 500, height - 200, 100, 200, 60, 'A')
        self.B_Left = Button((255, 255, 255), 600, height - 200, 100, 200, 60, 'B')

        self.C_Right = Button((255, 255, 255), 700, height - 200, 100, 200, 60, 'C')
        self.D_Right = Button((255, 255, 255), 800, height - 200, 100, 200, 60, 'D')
        self.E_Right = Button((255, 255, 255), 900, height - 200, 100, 200, 60, 'E')
        self.F_Right = Button((255, 255, 255), 1000, height - 200, 100, 200, 60, 'F')
        self.G_Right = Button((255, 255, 255), 1100, height - 200, 100, 200, 60, 'G')
        self.A_Right = Button((255, 255, 255), 1200, height - 200, 100, 200, 60, 'A')
        self.B_Right = Button((255, 255, 255), 1300, height - 200, 100, 200, 60, 'B')
        self.C_Right_Right = Button((255, 255, 255), 1400, height - 200, 100, 200, 60, 'C')

        self.Db_Left = Button((255, 10, 10), 75, height - 200, 50, 100, 60, 'Db')
        self.Eb_Left = Button((255, 10, 10), 175, height - 200, 50, 100, 60, 'Eb')
        self.Gb_Left = Button((255, 10, 10), 375, height - 200, 50, 100, 60, 'Gb')
        self.Ab_Left = Button((255, 10, 10), 475, height - 200, 50, 100, 60, 'Ab')
        self.Bb_Left = Button((255, 10, 10), 575, height - 200, 50, 100, 60, 'Bb')

        self.Db_Right = Button((255, 10, 10), 775, height - 200, 50, 100, 60, 'Db')
        self.Eb_Right = Button((255, 10, 10), 875, height - 200, 50, 100, 60, 'Eb')
        self.Gb_Right = Button((255, 10, 10), 1075, height - 200, 50, 100, 60, 'Gb')
        self.Ab_Right = Button((255, 10, 10), 1175, height - 200, 50, 100, 60, 'Ab')
        self.Bb_Right = Button((255, 10, 10), 1275, height - 200, 50, 100, 60, 'Bb')

        self.play_sheet = Button((200, 100, 0), width//2 - 200, height//2 - 175, 400, 100, 60, 'Play Sheet Music')

    def handle(self):
        self.C_Left.draw(window, (255, 255, 255))
        self.D_Left.draw(window, (255, 255, 255))
        self.E_Left.draw(window, (255, 255, 255))
        self.F_Left.draw(window, (255, 255, 255))
        self.G_Left.draw(window, (255, 255, 255))
        self.A_Left.draw(window, (255, 255, 255))
        self.B_Left.draw(window, (255, 255, 255))

        self.C_Right.draw(window, (255, 255, 255))
        self.D_Right.draw(window, (255, 255, 255))
        self.E_Right.draw(window, (255, 255, 255))
        self.F_Right.draw(window, (255, 255, 255))
        self.G_Right.draw(window, (255, 255, 255))
        self.A_Right.draw(window, (255, 255, 255))
        self.B_Right.draw(window, (255, 255, 255))
        self.C_Right_Right.draw(window, (255, 255, 255))

        self.Db_Left.draw(window, (255, 255, 255))
        self.Eb_Left.draw(window, (255, 255, 255))
        self.Gb_Left.draw(window, (255, 255, 255))
        self.Ab_Left.draw(window, (255, 255, 255))
        self.Bb_Left.draw(window, (255, 255, 255))

        self.Db_Right.draw(window, (255, 255, 255))
        self.Eb_Right.draw(window, (255, 255, 255))
        self.Gb_Right.draw(window, (255, 255, 255))
        self.Ab_Right.draw(window, (255, 255, 255))
        self.Bb_Right.draw(window, (255, 255, 255))

        self.play_sheet.draw(window, (255, 255, 255))


pyano = Pyano()
piano = True
while piano:
    pyano.handle()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if pressed[pygame.K_a] or pyano.C_Left.isOver(pos):
            print("C")
            pygame.mixer.music.load("music/lc.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_q]:
            print("Db")
            pygame.mixer.music.load("music/n1.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_s]:
            print("D")
            pygame.mixer.music.load("music/ld.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_w]:
            print("Eb")
            pygame.mixer.music.load("music/n2.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_d]:
            print("E")
            pygame.mixer.music.load("music/le.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_z]:
            print("F")
            pygame.mixer.music.load("music/lf.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_e]:
            print("Gb")
            pygame.mixer.music.load("music/n3.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_x]:
            print("G")
            pygame.mixer.music.load("music/lg.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_r]:
            print("Ab")
            pygame.mixer.music.load("music/n4.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_c]:
            print("A")
            pygame.mixer.music.load("music/la.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_t]:
            print("Bb")
            pygame.mixer.music.load("music/n5.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_f]:
            print("B")
            pygame.mixer.music.load("music/lb.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()

        elif pressed[pygame.K_h]:
            print("C")
            pygame.mixer.music.load("music/rc.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_y]:
            print("Db")
            pygame.mixer.music.load("music/n6.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_j]:
            print("D")
            pygame.mixer.music.load("music/rd.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_u]:
            print("Eb")
            pygame.mixer.music.load("music/n7.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_d]:
            print("E")
            pygame.mixer.music.load("music/re.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_k]:
            print("F")
            pygame.mixer.music.load("music/rf.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_i]:
            print("Gb")
            pygame.mixer.music.load("music/n8.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_b]:
            print("G")
            pygame.mixer.music.load("music/rg.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_o]:
            print("Ab")
            pygame.mixer.music.load("music/n9.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_n]:
            print("A")
            pygame.mixer.music.load("music/ra.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_t]:
            print("Bb")
            pygame.mixer.music.load("music/n10.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_m]:
            print("B")
            pygame.mixer.music.load("music/rb.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()
        elif pressed[pygame.K_p]:
            print("C")
            pygame.mixer.music.load("music/rrc.wav")
            pygame.mixer.music.play(1, 0.0)
            pygame.mixer.stop()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pyano.play_sheet.isOver(pos):
                # 1421 notes
                # 5580 bps
                # 1421 / 5580 = 0.2546595 pause on wait

                for row in pyano_sheet:
                    for note in row:
                        if note == '-':
                            time.sleep(0.2546595)
                        elif note == 'a' or note == 'b' or note == 'c' or note == 'd' or note == 'e' or note == 'f' or note == 'g':
                            print(note)
                            pygame.mixer.music.load("music/r" + str(note) + ".wav")
                            pygame.mixer.music.play(1, 0.0)
                        else:
                            continue

    pygame.display.update()