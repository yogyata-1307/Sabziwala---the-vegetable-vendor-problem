def print_result(purchased):
    print("Items Brought: ", [item[0] for item in purchased])
    print("Profit: Rs. ", sum([item[2] for item in purchased]))
    
def max_profit(items, max_weight):
    
    items.sort(reverse=True, key=lambda item: item[2]/item[1])
    
    purchased = []
    while max_weight!=0:
        can_carry = [item for item in items if item[1]<max_weight]
        
        if(len(can_carry)==0): break
    
        purchased.append(can_carry[0])
        max_weight -= purchased[-1][1]
        
    print_result(purchased)
    
def main():
    items = [
        ('Potato',2,4),
        ('Black pepper',3,5),
        ('Banana',1,3),
        ('Watermelon',4,7)
    ]
    max_weight = 5
    max_profit(items, max_weight)