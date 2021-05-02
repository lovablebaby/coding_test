class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth_list = []
        for customer in accounts:
            wealth_value = sum(customer)
            wealth_list.append(wealth_value)
        wealth = max(wealth_list)
        return wealth
