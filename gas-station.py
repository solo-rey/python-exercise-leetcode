class Solution:
    """
    There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

    Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

    Note:
    The solution is guaranteed to be unique.
    """
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    """
    take-away, whenever sum <= 0, clear it, the next stop may be the starting point
    """
    def canCompleteCircuit(self, gas, cost):
        sum_gas = 0
        total = 0
        res = -1
        for i in range(len(gas)):
            sum_gas += (gas[i] - cost[i])
            total += (gas[i] - cost[i])
            if sum_gas < 0:
                res = i
                sum_gas = 0
        if total >= 0:
            return res+1
        else:
            return -1