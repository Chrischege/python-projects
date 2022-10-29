class budget:
    #budget_amount=int(input())
    #print(str(budget_amount) +' ' + 'is your intended budget')
    def __init__(self,name,budget_amt):
        self.name=name
        self.budget_amt=budget_amt

    
budget_1=budget("chege",50000)
print(budget_1.budget_amt)

class food(budget):
    def __init__(self,name,budget_amt,food_amount):
        super().__init__(name,budget_amt)
        self.food_amount=food_amount

    def diff_amt(self):
        diff=self.budget_amt-self.food_amount
        return diff
    def percent_usage(self):
        percent_use=(self.food_amount/self.budget_amt)*100
        return print(str(percent_use) + "%" )
        
food_budget=food('david',40000,30000)
print(food_budget.diff_amt())
print(food_budget.percent_usage())