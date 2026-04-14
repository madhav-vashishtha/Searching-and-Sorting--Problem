def minimumTotalDistance(robot, factory):
        robot.sort()
        factory.sort()

        n = len(robot)
        dp = [-1] * (n + 1)
        dp[0] = 0

        for pos, cap in factory:
            prev = dp[:]

            for i in range(n + 1):
                if prev[i] == -1:
                    break

                cost = prev[i]

                for k in range(1, cap + 1):
                    if i + k > n:
                        break

                    cost += abs(robot[i + k - 1] - pos)

                    if dp[i + k] == -1 or cost < dp[i + k]:
                        dp[i + k] = cost

        return dp[n]

robot = [0,4,6]
factory = [[2,2],[6,2]]

print(minimumTotalDistance(robot, factory))

robot = [1,-1]
factory = [[-2,1],[2,1]]

print(minimumTotalDistance(robot, factory))


