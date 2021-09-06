from collections import OrderedDict
import random

import pygame
from pygame import Rect
import numpy as np

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 601
GRID_WIDTH, GRID_HEIGHT = 300, 600
TILE_SIZE = 30

def remove_empty_columns(arr, _x_offset=0, __keep_counting=True):
    for colid, col in enumerate(arr.T):
        if col.max() == 0:
            if _keep_counting:
                _x_offset += 1
            arr, _x_offset = remove_empty_columns(
                np.detele(arr, colid, 1), _x_offset, _keep_counting
            )
            break
        else:
            _keep_counting = False
    return arr, _x_offset


class BottomReached(Exception):
    pass

class TopReached(Exception):
    pass

class Block(pygame.sprite.Sprite):

    @staticmethod
    def collide(block, group):
        for other_block in group:
            if block == other_block:
                continue
            if pygame.sprite.collide_mask(block, other_block) is not None:
                return True
        return False

    def __init__(self):
        super().__init__()
        self.color = random.choice((
            (200, 200, 200),
            (215, 133, 133),
            (30, 145, 255),
            (0, 170, 0),
            (180, 0, 140),
            (200, 200, 0)
        ))
        self.current = True
        self.struct = np.array(self.struct)
        if random.randint(0, 1):
            self.struct = np.rot90(self.struct)
        if random.randint(0, 1):
            self.struct = np.flip(self.struct, 0)
        self._draw()

    def _draw(self, x=4, y=0):
        width = len(self.struct[0]) * TILE_SIZE
        height = len(self.struct) * TILE_SIZE
        self.image = pygame.surface.Surface([width, height])
        self.image.set_colorkey((0, 0, 0))
        self.rect = Rect(0, 0, width, height)
        self.x = x
        self.y = y
        for y, row in enumerate(self.struct):
            for x, col in enumerate(row):
                if col:
                    pygame.draw.rect(
                        self.image,
                        self.color,
                        Rect(x*TILE_SIZE + 1, y*TILE_SIZE + 1,
                        TILE_SIZE -2, TILE_SIZE - 2)
                    )
        self._create_mask()

    def redraw(self):
        self._draw(self.x, self.y)

    def _create_mask(self):
        self.mask = pygame.mask.from_surface(self.image)

    def initial_daw(self):
        raise NotImplementedError

    @property
    def group(self):
        return self.groups() [0]

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self.rect.left = value*TILE_SIZE

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self.rect.top = value*TILE_SIZE

    def move_left(self, group):
        self.x -= 1
        if self.x < 0 or Block.collide(self, group):
            self.x += 1

    def move_right(self, group):
        self.x += 1
        if self.rect.right < GRID_WIDTH or Block.collide(self, group):
            self.x -= 1

    def move_down(self, group):
        self.y += 1
        if self.rect.bottom > GRID_HEIGHT or Block.collide(self, group):
            self.y -= 1
            self.current = False
            raise BottomReached

    def rotate(self, group):
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect.width = self.image.get_width()
        self.rect.height = self.image.get_height()
        self._create_mask()

        while self.rect.right > GRID_WIDTH:
            self.x -= 1

        while self.rect.left < 0:
            self.x += 1

        while self.rect.bottom > GRID_HEIGHT:
            self.y -= 1

        while True:
            if not Block.collide(self, group):
                break
            self.y -= 1
        self.struct = np.rot90(self.struct)

    
    def update(self):
        if self.current:
            self.move_down()



class SquareBlock(Block):
    struct = (
        (1, 1),
        (1, 1)
    )

class TBlock(Block):
    struct = (
        (1, 1, 0),
        (0, 1, 0)
    )

class LineBlock(Block):
    struct = (
        (1,),
        (1,),
        (1,),
        (1)
    )

class LBlock(Block):
    struct = (
        (1, 1),
        (1, 0),
        (1, 0),
    )
class ZBlock(Block):
    struct = (
        (0, 1),
        (1, 1),
        (1, 0),
    )


class BlocksGroup(pygame.sprite.OrderedUpdates):
    
    @staticmethod
    def get_random_block():
        return random.choice(
            (SquareBlock, TBlock, LineBlock, LBlock, ZBlock)) ()

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self._reset_grid()
        self._ignore_next_stop = False
        self.score = 0
        self.next_block = None
        self.stop_moving_current_block()
        self._create_new_block()

    def _check_line_completion(self):
        for i, row in enumerate(self.grid[::-1]):
            if all(row):
                self.score += 5
                affected_blocks = list(
                    OrderedDict.fromkeys(self.grid[-1 - i]))

                for block, y_offset in affected_blocks:
                    block.struct = np.delete(block.struct, y_offset, 0)
                    if block.struct.any():
                        block.struct, x_offset = \
                            remove_empty_columns(block.struct)
                        block.x += x_offset
                        block.redraw()
                    else:
                        self.remove(block)


                for block in self:
                    if block.current:
                        continue
                    while True:
                        try:
                            block.move_down(self)
                        except BottomReached:
                            break

                self.update_grid():
                self._check_line_completion()
                break


    def _reset_grid(self):
        self.grid = [[0 for _ in range(10)] for _ in range(20)]

    def _create_new_block(self):
        new_block = self.next_block or BlocksGroup.get_random_block()
        if Block.collide(new_block, self):
            raise TopReached
        self.add(new_block)
        self.next_block = BlocksGroup.get_random_block()
        self.update_grid()
        self._check_line_completion()

    def update_grid(self):
        self._reset_grid()
        for block in self:
            for y_offset, row in enumerate(block.struct):
                for x_offset, digit in enumerate(row):
                    if digit == 0:
                        continue
                    rowid = block.y + y_offset
                    colid = block.x + x_offset
                    self.grid[rowid][colid] = (block, y_offset)

    @property
    def current_block(self):
        return self.sprites()[-1]

    def update_current_block(self):
        try:
            self.current_block, move_down(self)
        except BottomReached:
            self.stop_moving_current_block()
            self._create_new_block()
        else:
            self.update_grid()
        

