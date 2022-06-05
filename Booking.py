class Booking():
    def __init__(self,package_name,customer_name,no_of_pax,cost_per_pax):
        self.package_name = package_name
        self.customer_name = customer_name
        self.no_of_pax = no_of_pax
        self.cost_per_pax = cost_per_pax
    
    def get_package_name(self):
        return self.package_name
    
    def get_customer_name(self):
        return self.customer_name
    
    def get_no_of_pax(self):
        return self.no_of_pax

    def get_cost_per_pax(self):
        return self.cost_per_pax
    
    def set_package_name(self,package_name):
        self.package_name = package_name
    
    def set_customer_name(self,customer_name):
        self.customer_name = customer_name
    
    def set_no_of_pax(self,no_of_pax):
        self.no_of_pax = no_of_pax
    
    def set_cost_per_pax(self,cost_per_pax):
        self.cost_per_pax = cost_per_pax
