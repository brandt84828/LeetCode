class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = ord(coordinates[0]) - ord('a') + 1
        y = int(coordinates[1])

        if x % 2 == y % 2:
            return False

        return True