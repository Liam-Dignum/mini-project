import pickle
import csv
#declare menu text and load lists from file
product_menu = "0.Exit program\n1.Print List\n2.Add to list\n3.Edit product in list\n4.Delete from list\n"
main_menu = "0.Exit Menu\n1.Product menu\n2.Order menu\n3.Courier menu\n"
order_menu = "0.Exit Menu\n1.Print orders\n2.add order\n3.edit delivery status\n4.edit order\n5.delete order\n"
courier_menu ="0.Exit Menu\n1.Print couriers\n2.Add courier\n3.Edit courier\n4.Delete courier\n"
#with open('products_data.csv', mode='w') as file:
#  # set the headers for the CSV
#  fieldnames = ['product_name', 'price']
#  writer = csv.DictWriter(file, fieldnames=fieldnames)
#  # instruct the writer to know to write the headers
#  writer.writeheader()
#  # instruct the writer to write the row
#  writer.writerow({
#    'product_name': 'Pepsi',
#    'price': '80'
#  })
#  writer.writerow({
#    'product_name': 'Coke',
#    'price': '100'
#  })
#  with open("orders_data.csv" ,"wb") as f:
#        writer = csv.DictWriter(f, fieldnames= orders[0].keys())
#        writer.writeheader()
#        writer.writerows(orders)
#    with open("couriers_data.csv" ,"wb") as f:
#        writer = csv.DictWriter(f, fieldnames= couriers[0].keys())
#        writer.writeheader()
#        writer.writerows(couriers)
try:
    with open (r"Data\products_data.csv","r") as f:
        reader = csv.DictReader(f)
        print(reader)
        products = list()
        for row in reader:
            products.append(row)
        print(products)
except:
     products = []

try:
    with open (r"Data\orders_data.csv","r") as f:
        reader = csv.DictReader(f)
        print(reader)
        orders = list()
        for row in reader:
            orders.append(row)
        print(orders)
except:
        orders = []
try:
    with open (r"Data\couriers_data.csv","r") as f:
        reader = csv.DictReader(f)
        print(reader)
        couriers = list()
        for row in reader:
            couriers.append(row)
        print(couriers)
except:
        couriers = []
#save lists to files and exit
def save_exit():
    with open(r"Data\products_data.csv" ,"w") as f:
        writer = csv.DictWriter(f, fieldnames= products[0].keys())
        writer.writeheader()
        writer.writerows(products)
    with open(r"Data\orders_data.csv" ,"w") as f:
        writer = csv.DictWriter(f, fieldnames= orders[0].keys())
        writer.writeheader()
        writer.writerows(orders)
    with open(r"Data\couriers_data.csv" ,"w") as f:
        writer = csv.DictWriter(f, fieldnames= couriers[0].keys())
        writer.writeheader()
        writer.writerows(couriers)
while True:
    choice = input(main_menu)
    if choice.isdigit() ==False:
        print("Invalid input")

    elif int(choice) == 0: #exit program
        save_exit()
        break
  
    elif int(choice) == 1: #product menu
        choice = input(product_menu)
        if choice.isdigit() ==False:
            print("Invalid input")
        
        elif int(choice) == 0: #exit program
            save_exit()
            break
        
        elif int(choice) == 1: #print products list
            print(products)
        
        elif int(choice) == 2: #add product to list
            new_product = input("Enter name for new product\n")
            new_price = input("Enter price for new item")
            products.append({"product_name" : new_product,"price" : new_price})
            print(products)

        elif int(choice) == 3: # Edit
            if len(products) != 0:  
                for i,item in enumerate(products, start=0):
                    print(i,item)
                choice = input("Select product to edit\n")
                if choice.isdigit() == True and int(choice)<len(products):
                    New_name = input("Input new name for product\n")
                    products[int(choice)] = New_name
                    print(products)
                else:
                    print("Invalid input")
                
            else:
                print("No products to delete\n")

        elif int(choice) ==4: #delete
            if len(products) != 0:  
                for i,item in enumerate(products, start=0):
                    print(i,item)
                choice = input("Select product to delete\n")
                if choice.isdigit() == True and int(choice)<len(products):
                    
                    products.pop(int(choice))
                    print(products)
                else:
                    print("Invalid input")
            else:
                print("No products to delete\n")
   
    elif int(choice) == 2: #order menu
        choice = input(order_menu)
        if choice.isdigit() ==False:
            print("Invalid input")

        elif int(choice) == 0:
            save_exit()
            break

        elif int(choice) == 1: #print orders
            print(orders)

        elif int(choice) == 2: #add order
            name = input("Enter Name")
            address = input("Enter address")
            phone_number = input("Enter phone number")
            for i,item in enumerate(couriers, start=0):
                    print(i,item)
            choice = input("Select courier")
            if len(couriers) > int(choice):
                orders.append({"name" : name,"address" : address,"phone_number" : phone_number,"Order_status" :"Pending", "courier" : choice})
            else:
                orders.append({"name" : name,"address" : address,"phone_number" : phone_number,"Order_status" :"Pending","courier" : None})
            print(orders)

        elif int(choice) == 3: #edit delivery status
            if len(orders) != 0:   
                for (i, item) in enumerate(orders, start=0):
                    print(i, item)
                choice = input("Select order")
                if choice.isdigit() == True:
                    temp_input = input("Enter order status")
                    orders[int(choice)]["Order_status"] = temp_input
                    print(orders)
                else:
                    print("Invalid input")
            else:
                print("No orders to edit\n")

        elif int(choice) ==4:  #edit order
            if len(orders) != 0:    
                for (i, item) in enumerate(orders, start=0):
                    print(i, item)
                choice = input("Select order")
                if choice.isdigit() == True:
                    print(orders[int(choice)])
                    for key in orders[int(choice)]:
                        temp_input = input(f"Enter new value for {key}")
                        if temp_input != "":
                            orders[int(choice)][key]= temp_input
                    print(orders)
                else:
                    print("Invalid input")
                
            else:
                print("No orders to edit\n")
        
        elif int(choice) ==5: #delete order
            if len(orders) != 0:  
                for (i, item) in enumerate(orders, start=0):
                    print(i, item)
                    choice = int(input("Select order"))
                    orders.pop(int(choice))
                    print(choice) 
                else:
                    print("No orders to delete\n")
    elif int(choice) == 3: #courier menu
        choice = input(courier_menu)
        if choice.isdigit() ==False:
            print("Invalid input")
        
        elif int(choice) == 0: #exit program
            save_exit()
            break
        
        elif int(choice) == 1: #print courier list
            print(couriers)
        
        elif int(choice) == 2: #add courier to list
            New_courier = input("Enter name for new courier\n")
            New_courier_number = input("Enter phone number for new courier")
            couriers.append({"Name" : New_courier,"Number" : New_courier_number})
            print(couriers)

        elif int(choice) == 3: # Edit
            if len(couriers) != 0:    
                for (i, item) in enumerate(couriers, start=0):
                    print(i, item)
                choice = input("Select order")
                if choice.isdigit() == True and int(choice)<len(couriers):
                    print(couriers[int(choice)])
                    for key in couriers[int(choice)]:
                        temp_input = input(f"Enter new value for {key}")
                        if temp_input != "":
                            couriers[int(choice)][key]= temp_input
                    print(couriers)
                else:
                    print("Invalid input")
            else:
                print("No couriers to delete\n")

        elif int(choice) ==4: #delete
            if len(couriers) != 0:  
                for i,item in enumerate(couriers, start=0):
                    print(i,item)
                choice = int(input("Select courier to delete\n"))
                couriers.pop(choice)
                print(couriers)
            else:
                print("No couriers to delete\n")
   
#test









