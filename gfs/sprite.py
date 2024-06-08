import pygame


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, animations, frame_duration):
        super(AnimatedSprite, self).__init__()

        # animation is a dict of images merged in one image
        self.rect = pygame.Rect(x, y, width, height)
        self.animations = animations

        self.current_animation = None
        self.next_animation = None
        self.current_frame = 0
        self.count_frame = frame_duration

        self.frame_duration = frame_duration

        self.image = pygame.Surface((width, height))

    def animate(self, animation, next_animation=None):
        if self.current_animation != animation:
            self.current_animation = animation
            self.current_frame = 0
            self.next_animation = next_animation

    def update(self):
        if self.current_animation is not None and self.count_frame >= self.frame_duration:
            self.current_frame += 1
            current_animation = self.animations[self.current_animation]
            # an animation is a duet : (number of frames, image)
            if self.current_frame >= current_animation[0]:
                if self.next_animation is not None:
                    self.current_animation = self.next_animation
                self.current_frame = 0

            # knowing the number of frames and the size of the total animation we can calculate the sub image
            width = current_animation[1].get_width() // current_animation[0]
            height = current_animation[1].get_height()

            self.image = current_animation[1].subsurface(width * self.current_frame, 0, width, height)
            self.count_frame = 0

        self.count_frame += 1
