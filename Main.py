import pickle
#declare menu text and load lists from file
product_menu = "0.Exit program\n1.Print List\n2.Add to list\n3.Edit product in list\n4.Delete from list\n"
main_menu = "0.Exit Menu\n1.Product menu\n2.Order menu\n3.Courier menu\n"
order_menu = "0.Exit Menu\n1.Print orders\n2.add order\n3.edit delivery status\n4.edit order\n5.delete order\n"
courier_menu ="0.Exit Menu\n1.Print couriers\n2.Add courier\n3.Edit courier\n5.Delete courier\n"
try:
    with open(r"Data\products_data.txt",'rb') as f:
    
        products = pickle.load(f)
except:
     products = []

try:
    with open(r"Data\orders_data.txt",'rb') as f:
    
        orders = pickle.load(f)
except:
        orders = []
try:
    with open(r"Data\courier_data.txt",'rb') as f:
    
        couriers = pickle.load(f)
except:
        couriers = []
#save lists to files and exit
def save_exit():
    with open(r"Data\products_data.txt",'wb') as f:
        pickle.dump(products,f)
    with open(r"Data\orders_data.txt",'wb') as f:
        pickle.dump(orders,f)
    with open(r"Data\courier_data.txt",'wb') as f:
        pickle.dump(couriers,f)

print(products,len(orders))
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
            New_product = input("Enter name for new product\n")
            products.append(New_product)
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
                if choice.isdigit == True and int(choice)<len(products):
                    
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
                if choice.isdigit == True:
                    print(orders[int(choice)])
                    for key in orders[choice]:
                        temp_input = input(f"Enter new value for {key}")
                        if temp_input != "":
                            orders[choice][key]= temp_input
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
                    orders.pop(choice)
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
        
        elif int(choice) == 1: #print products list
            print(couriers)
        
        elif int(choice) == 2: #add courier to list
            New_courier = input("Enter name for new courier\n")
            couriers.append(New_courier)
            print(couriers)

        elif int(choice) == 3: # Edit
            if len(couriers) != 0:  
                for i,item in enumerate(couriers, start=0):
                    print(i,item)
                choice = int(input("Select courier to edit\n"))
                New_name = input("Input new name for courier\n")
                couriers[choice] = New_name
                print(couriers)
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
   










