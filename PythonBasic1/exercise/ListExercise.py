# using this list, 
from queue import PriorityQueue
import this


basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# 1. Remove the Banana from the list
first_list = basket.remove('Banana')
print(basket)
# 2. Remove "Blueberries" from the list.
second_list = basket.pop(2)
print(basket)
# 3. Put "Kiwi" at the end of the list.
third_list = basket.append('Kiwi')
print(basket)
# 4. Add "Apples" at the beginning of the list
basket.insert(0,'Apples')
print(basket)
# 5. Count how many apples in the basket
print(basket.count('Apples'))
# 6. empty the basket
basket.clear()
print(basket)
