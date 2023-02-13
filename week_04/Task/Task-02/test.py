# read the file into a list of lines
with open(r"E:\Pavan Learnings\Braineest\week_04\Task\Task-02\shopfile.txt") as file:
    lines = file.readlines()

# create a list to store the order information
orders = []

# loop through each line in the file
for line in lines:
    # split the line into separate values
    order_info = line.strip().split(' and ')
    order_number = int(order_info[0].split()[2])
    customer_name = ' '.join(order_info[1].split()[4:])
    items = {}

    # get the items purchased
    items_raw = order_info[2].split(', ')
    print(items_raw)
    for item in items_raw:
        item_info = item.split()
        item_name = ' '.join(item_info[:-1])
        item_quantity = int(item_info[-1])
        items[item_name] = item_quantity

    # add the order information to the orders list as a dictionary
    orders.append({
        'Order Number': order_number,
        'Customer': customer_name,
        'Items': items
    })

# print the orders list
for order in orders:
    print(order)
