"""Imagine you have a large text file that contains information about customer orders. 
   You want to extract information about each order, such as the order number, the customer name, and the items in the order.

Sample output:
{'Order Number': 123, 'Customer': 'John Doe', 'Items': {'Item 1': 2, 'Item 2': 1, 'Item 3': 3}}"""

import re

class OrderDetails:
    def __init__(self,filepath: str):
        self.file = filepath
        self.order_details = dict.fromkeys(['Order Number','Customer','Items'],0)
    
    # append the order deatils to a list from file
    def get_order_list(self):
        try:
            order_list = []
            with open(self.file, 'rt') as data:
                for line in data:
                    if line.startswith("Order Number"):
                        order_list.append(line)
            return order_list
                
        except:
            print("The file path not existed")
    
    # using the order details list get the details
    def get_order_details(self,data_list):
        for line in data_list:
            # print(line)
            print(re.search(r'.\*Customer',line))
            # self.order_details.setdefault("Order Number",)



object_a = OrderDetails(r"E:\Pavan Learnings\Braineest\week_04\Task\Task-02\shopfile.txt")
order_data = object_a.get_order_list()
object_a.get_order_details(order_data)

