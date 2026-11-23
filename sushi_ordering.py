from tkinter import *
from tkinter import ttk


class SushiOrdering:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1250x600+1+1')
        self.root.title('Sushi Restaurant Ordering System')
        self.root.configure(background='silver')
        self.root.resizable(False, False)

        title = Label(self.root, text='[Sushi Restaurant Ordering System]',
                      bg='yellow', fg='black', font=('monospace', 14))
        title.pack(fill=X)

        self.customer_id_var = StringVar()
        self.customer_name_var = StringVar()
        self.table_var = StringVar()

        self.food_id_var = StringVar()
        self.food_name_var = StringVar()
        self.food_type_var = StringVar()
        self.price_var = StringVar()
        self.availability_var = StringVar()
        self.search_var = StringVar()

        self.order_id_var = StringVar()
        self.order_customer_var = StringVar()
        self.order_food_var = StringVar()
        self.quantity_var = StringVar()
        self.bill_var = StringVar()
        self.gift_var = StringVar()

        # Customer and seating information
        customer_frame = Frame(self.root, bg='white')
        customer_frame.place(x=20, y=45, width=390, height=535)

        customer_title = Label(customer_frame, text='Customer and Seating',
                               bg='#1AA', fg='white', font=('monospace', 14))
        customer_title.pack(fill=X)

        customer_id_label = Label(customer_frame, text='Customer ID', bg='white')
        customer_id_label.pack()
        customer_id_entry = Entry(customer_frame, textvariable=self.customer_id_var,
                                  justify='center', bd=2)
        customer_id_entry.pack()

        customer_name_label = Label(customer_frame, text='Customer Name', bg='white')
        customer_name_label.pack()
        customer_name_entry = Entry(customer_frame, textvariable=self.customer_name_var,
                                    justify='center', bd=2)
        customer_name_entry.pack()

        table_label = Label(customer_frame, text='Table Number', bg='white')
        table_label.pack()
        table_entry = Entry(customer_frame, textvariable=self.table_var,
                            justify='center', bd=2)
        table_entry.pack()

        register_btn = Button(customer_frame, text='Register Customer', bg='orange')
        register_btn.place(x=120, y=200, width=150, height=33)

        # Food and menu information
        food_frame = Frame(self.root, bg='white')
        food_frame.place(x=430, y=45, width=390, height=535)

        food_title = Label(food_frame, text='Food and Menu',
                           bg='#1AA', fg='white', font=('monospace', 14))
        food_title.pack(fill=X)

        food_id_label = Label(food_frame, text='Food ID', bg='white')
        food_id_label.pack()
        food_id_entry = Entry(food_frame, textvariable=self.food_id_var,
                              justify='center', bd=2)
        food_id_entry.pack()

        food_name_label = Label(food_frame, text='Food Name', bg='white')
        food_name_label.pack()
        food_name_entry = Entry(food_frame, textvariable=self.food_name_var,
                                justify='center', bd=2)
        food_name_entry.pack()

        food_type_label = Label(food_frame, text='Sushi Type', bg='white')
        food_type_label.pack()
        food_type_entry = Entry(food_frame, textvariable=self.food_type_var,
                                justify='center', bd=2)
        food_type_entry.pack()

        price_label = Label(food_frame, text='Price', bg='white')
        price_label.pack()
        price_entry = Entry(food_frame, textvariable=self.price_var,
                            justify='center', bd=2)
        price_entry.pack()

        availability_label = Label(food_frame, text='Availability', bg='white')
        availability_label.pack()
        availability_combo = ttk.Combobox(food_frame, textvariable=self.availability_var)
        availability_combo['values'] = ('Available', 'Unavailable')
        availability_combo.pack()

        search_label = Label(food_frame, text='Search Food Name or Type', bg='white')
        search_label.pack()
        search_entry = Entry(food_frame, textvariable=self.search_var,
                             justify='center', bd=2)
        search_entry.pack()

        add_food_btn = Button(food_frame, text='Add Food', bg='orange')
        add_food_btn.place(x=120, y=330, width=150, height=33)
        update_food_btn = Button(food_frame, text='Update Food', bg='purple', fg='white')
        update_food_btn.place(x=120, y=370, width=150, height=33)
        search_food_btn = Button(food_frame, text='Search Food', bg='blue', fg='white')
        search_food_btn.place(x=120, y=410, width=150, height=33)

        # Order, bill, and gift information
        order_frame = Frame(self.root, bg='white')
        order_frame.place(x=840, y=45, width=390, height=535)

        order_title = Label(order_frame, text='Order and Report',
                            bg='#1AA', fg='white', font=('monospace', 14))
        order_title.pack(fill=X)

        order_id_label = Label(order_frame, text='Order ID', bg='white')
        order_id_label.pack()
        order_id_entry = Entry(order_frame, textvariable=self.order_id_var,
                               justify='center', bd=2)
        order_id_entry.pack()

        order_customer_label = Label(order_frame, text='Customer ID', bg='white')
        order_customer_label.pack()
        order_customer_entry = Entry(order_frame, textvariable=self.order_customer_var,
                                     justify='center', bd=2)
        order_customer_entry.pack()

        order_food_label = Label(order_frame, text='Food ID', bg='white')
        order_food_label.pack()
        order_food_entry = Entry(order_frame, textvariable=self.order_food_var,
                                 justify='center', bd=2)
        order_food_entry.pack()

        quantity_label = Label(order_frame, text='Quantity', bg='white')
        quantity_label.pack()
        quantity_entry = Entry(order_frame, textvariable=self.quantity_var,
                               justify='center', bd=2)
        quantity_entry.pack()

        bill_label = Label(order_frame, text='Bill Total', bg='white')
        bill_label.pack()
        bill_entry = Entry(order_frame, textvariable=self.bill_var,
                           justify='center', bd=2)
        bill_entry.pack()

        gift_label = Label(order_frame, text='Gift', bg='white')
        gift_label.pack()
        gift_entry = Entry(order_frame, textvariable=self.gift_var,
                           justify='center', bd=2)
        gift_entry.pack()

        order_btn = Button(order_frame, text='Place Order', bg='orange')
        order_btn.place(x=120, y=330, width=150, height=33)
        report_btn = Button(order_frame, text='Bill and Gift Report', bg='blue', fg='white')
        report_btn.place(x=120, y=370, width=150, height=33)


root = Tk()
app = SushiOrdering(root)
root.mainloop()
