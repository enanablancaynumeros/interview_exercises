class Robot:
    def move(self):
        """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """

    def turnLeft(self):
        """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

    def turnRight(self):
        """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

    def clean(self):
        """
       Clean the current cell.
       :rtype void
       """


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        current_position = (0, 0)
        status = 1
        robot.clean()
        self.process(robot, status, visited, current_position)

    def process(self, robot, status, visited, current_position):
        visited.add(current_position)
        for i in range(4):
            next_position = self.get_next_position(status, current_position)
            if next_position not in visited and robot.move():
                robot.clean()
                self.process(robot, status, visited, next_position)
                status = self.turn_left(status, robot)
                status = self.turn_left(status, robot)
                robot.move()
                status = self.turn_left(status, robot)
                status = self.turn_left(status, robot)
            status = self.turn_right(status, robot)

    def get_next_position(self, status, last_position):
        if status == 0:
            return last_position[0] - 1, last_position[1]
        elif status == 1:
            return last_position[0], last_position[1] + 1
        elif status == 2:
            return last_position[0] + 1, last_position[1]
        elif status == 3:
            return last_position[0], last_position[1] - 1

    def turn_right(self, status, robot):
        status = (status + 1) % 4
        robot.turnRight()
        return status

    def turn_left(self, status, robot):
        status = (status - 1) % 4
        robot.turnLeft()
        return status
