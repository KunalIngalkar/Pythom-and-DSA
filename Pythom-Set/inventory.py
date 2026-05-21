'''
Scenario: An e-commerce company operates two regional warehouses (Warehouse
A and Warehouse B). During an audit, the inventory management system outputs
tuples of product IDs currently in stock at each warehouse. The operations team
needs to balance the stock. 

Using sets, write a program to answer the following operational questions:

Which products are stocked in only one of the warehouses, but not both? (Items that
might need to be shared).

Is Warehouse B's inventory entirely covered by Warehouse A? (Check if B is a subset
of A).

Update Warehouse A's system so it includes all the items from Warehouse B.

Mock Data:
warehouse_a = ("P101", "P102", "P103", "P104", "P105")
warehouse_b = ("P103", "P104", "P109")
'''


warehouse_a = {"P101", "P102", "P103", "P104", "P105"}
warehouse_b = {"P103", "P104", "P109"}

#1
stocked_prod = warehouse_a ^ warehouse_b
print(stocked_prod)

#2
for item in warehouse_b:
    if item in warehouse_a:
        print(item)


#3
warehouse_a.update(warehouse_b)
print(warehouse_a)