class Solution(object):
    def calculate_score(self, player):
        score = 0
        last_two = [0, 0]
        for i in range(len(player)):
            if 10 in last_two:
                score += 2 * player[i]
            else:
                score += player[i]
            last_two[0] = last_two[1]
            last_two[1] = player[i]
        return score

    def isWinner(self, player1, player2):
        """
        :type player1: List[int]
        :type player2: List[int]
        :rtype: int
        """
        score1 = self.calculate_score(player1)
        score2 = self.calculate_score(player2)
        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        else:
            return 0


if __name__ == '__main__':
    print(Solution().calculate_score([3,8,4,5]))
