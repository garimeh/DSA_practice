class Food:
    def __init__(self, foodrating, foodname):
        self.foodrating = foodrating
        self.foodname = foodname
    
    def __lt__(self, other):
        if self.foodrating == other.foodrating:
            return self.foodname < other.foodname
        return self.foodrating > other.foodrating
    

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating = {}
        self.food_cuisines = {}
        self.cuisine_food = defaultdict(list)

        for i in range(len(foods)):
            self.food_rating[foods[i]] = ratings[i]
            self.food_cuisines[foods[i]] = cuisines[i]
            heapq.heappush(self.cuisine_food[cuisines[i]], Food(ratings[i],foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating[food] = newRating
        cuisinename = self.food_cuisines[food]
        heapq.heappush(self.cuisine_food[cuisinename], Food(newRating, food))

    def highestRated(self, cuisine: str) -> str:
        highest = self.cuisine_food[cuisine][0]
        while self.food_rating[highest.foodname]!= highest.foodrating:
            heapq.heappop(self.cuisine_food[cuisine])
            highest = self.cuisine_food[cuisine][0]
        return highest.foodname


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)