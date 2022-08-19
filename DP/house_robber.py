# Top Down approach
def houseRobber(houses, currentIndex):
    dic = {}
    def helper(houses, currentIndex):
        if currentIndex >= len(houses):
            return 0
        else:
            stealFirstHouse = houses[currentIndex] + houseRobber(houses, currentIndex + 2)
            skipFirstHouse = houseRobber(houses, currentIndex+1)
            return max(stealFirstHouse, skipFirstHouse)
    return helper(houses, currentIndex)

houses = [6,7,1,30,8,2,4]
print(houseRobber(houses, 0))

# Bottom Up approach
def houseRobber(houses):
    res = [0] * (len(houses) + 2)
    for house in range(len(houses) -1, -1, -1):
        res[house] = max((houses[house] + res[house + 2]), res[house + 1])
    return res[0]
houses = [6,7,1,30,8,2,4]
print(houseRobber(houses))