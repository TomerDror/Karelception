import tkinter as tk
import time

SCREEN_SIZE = 600
MEMORY_HEIGHT = 8
MEMORY_WIDTH = 8
STACK_HEIGHT = 19
STACK_WIDTH = 5
COMMANDS_HEIGHT = 24
COMMANDS_WIDTH = 4


class Karel:
    def __init__(self, side):
        self.side = side
        self.world = [[0] * side for _ in range(side)]
        self.x = 0
        self.y = 0
        self.direction = "north"

    def turn_left(self):
        directions = ["north", "west", "south", "east"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index - 1) % 4]

    def move(self):
        if self.direction == "north" and self.y > 0:
            self.y -= 1
        elif self.direction == "south" and self.y < self.side - 1:
            self.y += 1
        elif self.direction == "west" and self.x > 0:
            self.x -= 1
        elif self.direction == "east" and self.x < self.side - 1:
            self.x += 1

    def put_beeper(self):
        self.world[self.y][self.x] += 1

    def pick_beeper(self):
        if self.world[self.y][self.x] > 0:
            self.world[self.y][self.x] -= 1

    def is_beeper(self):
        return self.world[self.y][self.x] > 0

    def front_is_clear(self):
        if self.direction == "north" and self.y > 0:
            return True
        elif self.direction == "south" and self.y < self.side - 1:
            return True
        elif self.direction == "west" and self.x > 0:
            return True
        elif self.direction == "east" and self.x < self.side - 1:
            return True
        return False

    def turn_off(self):
        print("Karel is turning off.")
        exit()


class KarelGUI(Karel):
    def __init__(self, side):
        super().__init__(side)
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=SCREEN_SIZE, height=SCREEN_SIZE)
        self.canvas.pack()
        self.render()
        self.root.after(100, self.mainloop)
        self.root.mainloop()

    def mainloop(self):
        # self.turn_off()
        pass

    def render(self):
        rect_size = SCREEN_SIZE // self.side
        # rect_size = 50
        for y in range(self.side):
            for x in range(self.side):
                self.canvas.create_rectangle(
                    x * rect_size, y * rect_size, (x + 1) * rect_size, (y + 1) * rect_size, fill="white"
                )
                if self.world[y][x] > 0:
                    self.canvas.create_oval(
                        x * rect_size + 10 / 50 * rect_size,
                        y * rect_size + 10 / 50 * rect_size,
                        (x + 1) * rect_size - 10 / 50 * rect_size,
                        (y + 1) * rect_size - 10 / 50 * rect_size,
                        fill="blue",
                    )
                    self.canvas.create_text(
                        x * rect_size + rect_size // 2,
                        y * rect_size + rect_size // 2,
                        text=str(self.world[y][x]),
                        fill="white"
                    )

        # Draw Karel as an arrow based on her direction
        karel_x = self.x * rect_size + 0.5 * rect_size
        karel_y = self.y * rect_size + 0.5 * rect_size
        if self.direction == "north":
            self.canvas.create_polygon(
                karel_x + (10 / 50) * rect_size, karel_y + (10 / 50) * rect_size,
                karel_x - (10 / 50) * rect_size, karel_y + (10 / 50) * rect_size,
                karel_x, karel_y - (20 / 50) * rect_size,
                fill="red"
            )
        elif self.direction == "south":
            self.canvas.create_polygon(
                karel_x + (10 / 50) * rect_size, karel_y - (10 / 50) * rect_size,
                karel_x - (10 / 50) * rect_size, karel_y - (10 / 50) * rect_size,
                karel_x, karel_y + (20 / 50) * rect_size,
                fill="red"
            )
        elif self.direction == "west":
            self.canvas.create_polygon(
                karel_x - 20 / 50 * rect_size, karel_y,
                karel_x + 10 / 50 * rect_size, karel_y - 10 / 50 * rect_size,
                karel_x + 10 / 50 * rect_size, karel_y + 10 / 50 * rect_size,
                fill="red"
            )
        elif self.direction == "east":
            self.canvas.create_polygon(
                karel_x + 20 / 50 * rect_size, karel_y,
                karel_x - 10 / 50 * rect_size, karel_y - 10 / 50 * rect_size,
                karel_x - 10 / 50 * rect_size, karel_y + 10 / 50 * rect_size,
                fill="red"
            )

    def turn_left(self):
        super().turn_left()
        self.canvas.delete("all")
        self.render()

    def move(self):
        super().move()
        self.canvas.delete("all")
        self.render()

    def turn_off(self):
        self.root.after(1000, super().turn_off())

    def put_beeper(self):
        super().put_beeper()
        self.canvas.delete("all")
        self.render()

    def pick_beeper(self):
        super().pick_beeper()
        self.canvas.delete("all")
        self.render()

    def facing_north(self):
        return self.direction == "north"

    def not_facing_north(self):
        return not self.facing_north()

    def facing_south(self):
        return self.direction == "south"

    def not_facing_south(self):
        return not self.facing_south()

    def facing_east(self):
        return self.direction == "east"

    def not_facing_east(self):
        return not self.facing_east()

    def facing_west(self):
        return self.direction == "west"

    def not_facing_west(self):
        return not self.facing_west()


class MyBasicKarel(KarelGUI):

    def turn_right(self):
        super().turn_left()
        super().turn_left()
        super().turn_left()

    def turn_south(self):
        while super().not_facing_south():
            super().turn_left()

    def turn_north(self):
        while super().not_facing_north():
            super().turn_left()

    def turn_east(self):
        while super().not_facing_east():
            super().turn_left()

    def turn_west(self):
        while super().not_facing_west():
            super().turn_left()

    def move_to_wall(self):
        while super().front_is_clear():
            super().move()

    def move_to_west_wall(self):
        self.turn_west()
        self.move_to_wall()

    def move_to_south_wall(self):
        self.turn_south()
        self.move_to_wall()

    def move_to_east_wall(self):
        self.turn_east()
        self.move_to_wall()

    def move_to_north_wall(self):
        self.turn_north()
        self.move_to_wall()

    def move_to_beeper(self):
        while not super().is_beeper():
            super().move()


class BasicCumputerKarel(MyBasicKarel):
    def mainloop(self):
        self.initialize_computer()

    def initialize_computer(self):
        self.start_memory()
        self.start_stack()
        self.start_commands()

    def move_to_start(self):
        super().move_to_west_wall()
        super().move_to_south_wall()

    def start_memory(self):
        self.move_to_start()
        super().turn_east()
        super().move()
        super().turn_north()
        for i in range(MEMORY_HEIGHT + 1):
            super().put_beeper()
            super().move()

        super().turn_east()
        for i in range(MEMORY_WIDTH + 1):
            super().put_beeper()
            super().move()

        super().turn_south()
        for i in range(MEMORY_HEIGHT + 1):
            super().put_beeper()
            super().move()
        super().put_beeper()

        self.declare_memory_empty()

    def declare_memory_empty(self):
        self.go_to_memory()
        super().turn_east()
        for i in range(int(MEMORY_WIDTH / 2)):
            super().move()
            super().turn_north()
            super().move()
            while not super().is_beeper():
                super().put_beeper()
                super().move()
            super().move_to_south_wall()
            super().turn_east()
            super().move()

    def go_to_memory(self):
        self.move_to_start()
        super().turn_east()
        super().move()

    def start_stack(self):
        self.go_to_stack()

        super().turn_north()
        for i in range(STACK_HEIGHT + 1):
            super().put_beeper()
            super().move()

        super().turn_east()
        for i in range(STACK_WIDTH + 1):
            super().put_beeper()
            super().move()

        super().turn_south()
        for i in range(STACK_HEIGHT + 1):
            super().put_beeper()
            super().move()
        super().put_beeper()
        
        self.go_to_stack()
        super().turn_east()
        super().move()
        self.turn_north()
        while not super().is_beeper():
            super().move()
        super().turn_south()
        super().move()
        super().put_beeper()

    def go_to_stack(self):
        self.go_to_memory()
        super().turn_east()
        for i in range(MEMORY_WIDTH + 2):
            super().move()

    def start_commands(self):
        self.go_to_commands()

        super().turn_north()
        for i in range(COMMANDS_HEIGHT + 1):
            super().put_beeper()
            super().move()

        super().turn_east()
        for i in range(COMMANDS_WIDTH + 1):
            super().put_beeper()
            super().move()

        super().turn_south()
        for i in range(COMMANDS_HEIGHT + 1):
            super().put_beeper()
            super().move()
        super().put_beeper()
        self.go_to_commands()
        super().turn_east()
        super().move()
        self.turn_north()
        while not super().is_beeper():
            super().move()
        super().turn_south()
        super().move()
        super().put_beeper()

    def go_to_commands(self):
        self.go_to_stack()
        super().turn_east()
        for i in range(STACK_WIDTH + 2):
            super().move()

    def clear_screen(self):
        self.move_to_start()
        super().turn_north()
        while super().front_is_clear():
            self.clear_line()
            super().move_to_west_wall()
            super().turn_north()
            super().move()
            print("a")
        self.clear_line()

    def clear_line(self):
        super().turn_east()
        while super().front_is_clear():
            print("c")
            while super().is_beeper():
                super().pick_beeper()
                print("b")
            super().move()
        while super().is_beeper():
            super().pick_beeper()


def main():
    side = 30  # Change the side length to the desired size
    karel_gui = BasicCumputerKarel(side)


if __name__ == '__main__':
    main()
