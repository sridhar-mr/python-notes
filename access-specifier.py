# #there are three access specifier
# #---> Public
# #---> Protected  --> _
# #---> Private  --> __   # we can't access from child  class  # same to stanger class
#
#
#
# class order:
#
#     def __init__(self,customer_name,items,total_amount,discount):
#         self.customer_name = customer_name,
#         self.items = items,
#         self.__total_amount = total_amount,
#         self.__discount = discount
#
#     def __finalCalculation(self):  #Private
#         return self.__total_amount - self.__discount
#
#     def _get_admin_view(self): #protect
#         return{
#             "customer_name":self.customer_name,
#             "items":self.items,
#             "total_amount":self.__total_amount,
#             "discount":self.__discount,
#             "Final Bill": self.__finalCalculation()
#         }
#
#
#     def get_customer_view(self):  #public
#         return{
#             "customer_name":self.customer_name,
#             "items":self.items,
#             "Final Bill": self.__finalCalculation()
#
#         }
#
# class Admin_view:
#     def show_order(self,order):
#         return order._get_admin_view()
#
# class Customer_view:
#     def show_order(self,order):
#         return order.get_customer_view()
#
#
# order = order("sridhar", ["egg rice","chicken rice"], 800,150)
#
# admin = Admin_view()
# customer = Customer_view()
#
#
# print(admin.show_order(order))
# print(customer.show_order(order))