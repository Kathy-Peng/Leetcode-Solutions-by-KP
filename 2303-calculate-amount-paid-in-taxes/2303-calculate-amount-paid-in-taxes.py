class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        total_tax = 0
        prev_upper = 0
        for item in brackets:
            upper = item[0]
            percent = item[1]
            if income > upper:
                total_tax += (upper - prev_upper)*percent/100
                prev_upper = upper
            else:
                total_tax += (income - prev_upper)*percent/100
                break
        return total_tax
                