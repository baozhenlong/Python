# coding : utf-8
import random
import sys
import pygame
from settings import *
import copy

#: 颜色定义
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)


def draw_block(surface, left, top, color):
    # pygame.draw.rect(surface, BACKGROUND_COLOR, pygame.Rect(
    #     left, top, BLOCK_WIDTH, BLOCK_HEIGHT))
    pygame.draw.rect(surface, color, pygame.Rect(
        left, top, BLOCK_WIDTH - 1, BLOCK_HEIGHT - 1))


class Tetris:

    def __init__(self):
        # self.form = random.choice(TETRIS)
        self.form = copy.deepcopy(random.choice(TETRIS))
        # self.form = TETRIS[0]

    def get_fills(self):
        return self.form[0]

    def get_color(self):
        return self.form[1]

    def set_fills(self, value):
        self.form[0] = value


class Chess:

    def __init__(self):
        self.size = (BLOCK_WIDTH * BLOCK_X_COUNT, BLOCK_HEIGHT * BLOCK_Y_COUNT)
        self.layout = self.generate_layout()

    def is_wall(self, x, y):
        return not (BLOCK_LEFT_WALL_COUNT - 1 < x < BLOCK_X_COUNT - BLOCK_RIGHT_WALL_COUNT and y < BLOCK_Y_COUNT - BLOCK_BOTTOM_WALL_COUNT)

    def generate_layout(self):
        return [
            [0 if not self.is_wall(x, y) else 1 for x in range(BLOCK_X_COUNT)] for y in range(BLOCK_Y_COUNT)
        ]

    def create_new_tetris(self):
        """
        创建新的积木,初始化位置为第 5,0 格, 速度为 4
        :return: 返回 False 无空间创建了
        """
        self.tetris = Tetris()
        self.tetris_left, self.tetris_top = 5, 0
        self.drop_speed = DROP_SPEED
        return self.check_tetris_touch_wall()

    @property
    def speed(self):
        return self.drop_speed

    def check_tetris_touch_wall(self, x_offset=0, y_offset=0):
        """
        是否已经触底/墙壁
        具体操作：
        判断最后一排的 1，是否在当前对应的位置是也是 1
        参数：
            x_offset: x 的偏移量  移动时可以传入 1/-1 来判断
            y_offset:  y的偏移量  正常下落时可以传入 1 来判断
        """
        fills = self.tetris.get_fills()
        for i in range(4, -1, -1):
            for j in range(5):
                if fills[i][j]:
                    if self.layout[i + self.tetris_top + y_offset][j + self.tetris_left + x_offset]:
                        # print("check_tetris_touch_wall true")
                        return True
        # print("check_tetris_touch_wall false")
        return False

    def move_tetris_left_right(self, x):
        """
        左右移动
        参数：
            x:  移动量 x_offset
        """
        # 移动时不能撞墙
        if not self.check_tetris_touch_wall(x_offset=x):
            self.tetris_left += x

    def drop_tetris(self):
        """ 自动下落 """
        self.tetris_top += 1

    def drop_tetris_quickly(self):
        """ 快速降落 """
        self.drop_speed = DROP_QUICKLY_SPEED

    def convert_tetris(self):
        """
        * 顺时针旋转
        具体操作：
        把第一竖排的倒序给第一横排的
        把第二竖排的倒序给第二横排的
        后面同理
        """
        new_fills = [[0 for i in range(5)] for j in range(5)]
        fills = self.tetris.get_fills()
        for i in range(5):
            for j in range(4, -1, -1):
                new_fills[i][j] = fills[4 - j][i]
        self.tetris.set_fills(new_fills)

    def clear_full_lines(self):
        """消除满行的所有行"""
        new_layout = self.generate_layout()
        row_len = BLOCK_X_COUNT - BLOCK_X_WALL_COUNT
        new_row = BLOCK_Y_COUNT - BLOCK_BOTTOM_WALL_COUNT - 1
        for cur_row in range(BLOCK_Y_COUNT - BLOCK_BOTTOM_WALL_COUNT - 1, 0, -1):
            if sum(self.layout[cur_row][2:BLOCK_X_COUNT - BLOCK_BOTTOM_WALL_COUNT]) < row_len:
                new_layout[new_row] = self.layout[cur_row]
                new_row -= 1
        # print("==============================")
        self.layout = new_layout

    def add_tetris_to_layout(self):
        """将积木放到棋盘里"""
        fills = self.tetris.get_fills()
        for i in range(4, -1, -1):
            for j in range(5):
                if fills[i][j]:
                    self.layout[i + self.tetris_top][j + self.tetris_left] = 1
        # 这里会调用消除函数
        self.clear_full_lines()

    def draw_tetris(self, surface):
        """
        显示积木
        """
        cur_left, cur_top = self.tetris_left * \
            BLOCK_WIDTH, self.tetris_top * BLOCK_HEIGHT
        fills = self.tetris.get_fills()
        color = self.tetris.get_color()
        for i in range(5):
            for j in range(5):
                # 只画积木实体，不管盒子本身
                if fills[j][i]:
                    draw_block(surface, cur_left + i * BLOCK_WIDTH,
                               cur_top + j * BLOCK_HEIGHT, color)

    def draw(self, surface):
        """
        显示棋盘
        """
        for x in range(BLOCK_X_COUNT):
            for y in range(BLOCK_Y_COUNT):
                if self.is_wall(x, y):
                    draw_block(surface, x * BLOCK_WIDTH,
                               y * BLOCK_HEIGHT, WALL_COLOR)
                elif self.layout[y][x] == 0:
                    draw_block(surface, x * BLOCK_WIDTH,
                               y * BLOCK_HEIGHT, BACKGROUND_COLOR)
                else:
                    draw_block(surface, x * BLOCK_WIDTH,
                               y * BLOCK_HEIGHT, BLOCK_COLOR)


def quit():
    pygame.quit()
    sys.quit()


is_pause = False
is_over = False
chess = None


def reset():
    global is_pause
    global is_over
    global chess
    is_pause = False
    is_over = False
    chess = Chess()
    chess.create_new_tetris()


def main():
    global is_pause
    global is_over
    global chess
    pygame.init()
    reset()
    font = pygame.font.Font(None, 80)
    pygame.display.set_caption('俄罗斯方块')
    screen = pygame.display.set_mode((chess.size), 0, 32)
    continue_text = font.render("Continue", True, COLOR_WHITE)
    quit_text = font.render("Quit", True, COLOR_WHITE)
    continue_text_rect = continue_text.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
    quit_text_rect = quit_text.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
    while True:
        while not is_over:
            # 处理游戏消息
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    quit()
                # 处理按键
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:
                        is_pause = not is_pause
                    if not is_pause:
                        if e.key == pygame.K_UP:
                            chess.convert_tetris()
                        if e.key == pygame.K_DOWN:
                            chess.drop_tetris_quickly()
                        if e.key == pygame.K_LEFT:
                            chess.move_tetris_left_right(-1)
                        if e.key == pygame.K_RIGHT:
                            chess.move_tetris_left_right(1)
            if not is_pause:
                # 是否碰触底部地面了，是 -> 融合背景   否 -> 继续下落
                if chess.check_tetris_touch_wall(y_offset=1):
                    chess.add_tetris_to_layout()
                    is_over = chess.create_new_tetris()
                    pass
                else:
                    chess.drop_tetris()
            # 绘制
            chess.draw(screen)
            chess.draw_tetris(screen)
            pygame.display.update()
            # 速度
            pygame.time.Clock().tick(chess.speed)

        if is_over:
            screen.blit(continue_text, continue_text_rect)
            screen.blit(quit_text, quit_text_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if continue_text_rect.collidepoint(event.pos):
                        screen.fill(BACKGROUND_COLOR, continue_text_rect)
                        screen.fill(BACKGROUND_COLOR, quit_text_rect)
                        pygame.display.update(continue_text_rect)
                        pygame.display.update(quit_text_rect)
                        reset()
                    elif quit_text_rect.collidepoint(event.pos):
                        quit()
            pygame.display.flip()


if __name__ == '__main__':
    main()
