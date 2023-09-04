import pygame
import sys
from Manager import Manager  # Importe a classe Manager aqui

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Interface:
    
    def __init__(self):
        pygame.init()

        self.window_size = (800, 600)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("WorkHive")

        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()

        self.button_create_user = pygame.Rect(300, 250, 200, 50)
        self.button_login = pygame.Rect(300, 320, 200, 50)
        self.button_exit = pygame.Rect(300, 390, 200, 50)

        self.manager = Manager()  
        

    def draw_text(self, text, x, y, color):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def main_menu(self):
        while True:
            self.screen.fill(WHITE)

            pygame.draw.rect(self.screen, BLACK, self.button_create_user)
            pygame.draw.rect(self.screen, BLACK, self.button_login)
            pygame.draw.rect(self.screen, BLACK, self.button_exit)

            self.draw_text("WorkHive", self.window_size[0] // 2, self.window_size[1] // 4, BLACK)
            self.draw_text("Create User", self.button_create_user.centerx, self.button_create_user.centery, WHITE)
            self.draw_text("Login", self.button_login.centerx, self.button_login.centery, WHITE)
            self.draw_text("Exit", self.button_exit.centerx, self.button_exit.centery, WHITE)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button_create_user.collidepoint(mouse_pos):
                        self.create_user_menu()  # Chama o método para o menu de criação de usuário
                    elif self.button_login.collidepoint(mouse_pos):
                        self.login_menu()  # Chama o método para o menu de login
                    elif self.button_exit.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

            self.clock.tick(30)

    def create_user_menu(self):
        username = ""
        cpf = ""
        password = ""
        
        while True:
            self.screen.fill(WHITE)

            pygame.draw.rect(self.screen, BLACK, self.button_create_user)
            pygame.draw.rect(self.screen, BLACK, self.button_login)
            pygame.draw.rect(self.screen, BLACK, self.button_exit)

            self.draw_text("WorkHive", self.window_size[0] // 2, self.window_size[1] // 4, BLACK)
            self.draw_text("Create User", self.button_create_user.centerx, self.button_create_user.centery, WHITE)
            self.draw_text("Login", self.button_login.centerx, self.button_login.centery, WHITE)
            self.draw_text("Exit", self.button_exit.centerx, self.button_exit.centery, WHITE)

            self.draw_text("Username:", 250, 450, BLACK)
            self.draw_text(username, 450, 450, BLACK)

            self.draw_text("CPF:", 280, 500, BLACK)
            self.draw_text(cpf, 450, 500, BLACK)

            self.draw_text("Password:", 240, 550, BLACK)
            self.draw_text(password, 450, 550, BLACK)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button_create_user.collidepoint(mouse_pos):
                        return username, cpf, password
                    elif self.button_login.collidepoint(mouse_pos):
                        self.login_menu()
                    elif self.button_exit.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.unicode.isalnum() or event.unicode == " ":
                        if len(username) < 20:
                            username += event.unicode
                    elif event.unicode.isnumeric():
                        if len(cpf) < 11:
                            cpf += event.unicode
                    elif event.unicode.isalnum() or event.unicode == " ":
                        if len(password) < 20:
                            password += event.unicode
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                        cpf = cpf[:-1]
                        password = password[:-1]

            self.clock.tick(30)

    def login_menu(self):
        # Implementação do menu de login
        pass

if __name__ == "__main__":
    interface = Interface()
    interface.main_menu()







