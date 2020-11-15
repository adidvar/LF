import pygame


class Render:
    # (float,float,float) - > глубина в зад + висота + ширина
    renderqueue_obj: [((float, float, float), (float, float), any)] = []
    renderqueue_floor: [((float, float), (float, float), any)] = []

    PPO_z = 0.5
    PPO_x = 1.0
    PPO_y = 1.0

    def __init__(self):
        self.size = width, height = 1280, 720
        self.screen = pygame.display.set_mode(self.size)

    def draw_object(self, image: pygame.image, position: (float, float, float), size: (float, float)) -> None:
        self.renderqueue_obj.append((position, size, image))

    def draw_floor(self, image, position, size):
        self.renderqueue_floor.append((position, size, image))

    def display(self):

        self.screen.fill((0, 0, 0))

        self.renderqueue_obj.sort()
        self.renderqueue_floor.sort()

        for position, size, image in self.renderqueue_floor:
            old_x, old_y = size
            # маштабування розмірів
            size_after = (int(old_y * self.PPO_y), int(old_x * self.PPO_z))
            # маштабування позиції
            position_after = (int(position[1] * self.PPO_x - size_after[0] / 2),
                              int((self.size[1] - position[0] * self.PPO_z) - size_after[1] / 2))
            # малювання
            self.screen.blit(pygame.transform.scale(image, size_after), position_after)


        for position, size, image in self.renderqueue_obj:
            old_x, old_y = size

            size_after = (int(old_y * self.PPO_y),
                          int(old_x * self.PPO_x))

            self.screen.blit(pygame.transform.scale(image, size_after),
                             (int(position[2] * self.PPO_x - size_after[0] / 2),
                              int(self.size[1] - (position[0] * self.PPO_z + position[1] * self.PPO_y) - size_after[1])))

        pygame.display.flip()

        self.renderqueue_obj.clear()
        self.renderqueue_floor.clear()
