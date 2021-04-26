"""
first clear date : 2021-04-26
need to improve efficiency
"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        max_candy = max(candies)
    
        candy_list = []
        
        for candy in candies:
            having_candy = candy + extraCandies
            candy_list.append(having_candy)
            
        for candy in candy_list:
            if candy < max_candy:
                answer.append(False)
            else:
                answer.append(True)
                
        return answer
        
