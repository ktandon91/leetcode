class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir_x, dir_y = 0, 1
        x, y = 0, 0
        for ins in instructions:
            if ins == "G":
                x, y = x+dir_x, y+dir_y
            elif ins == "L":
                dir_x, dir_y = -1*dir_y, dir_x
            else:
                dir_x, dir_y = dir_y, -1*dir_x
        return (x, y) == (0, 0) or (dir_x, dir_y) != (0, 1)
