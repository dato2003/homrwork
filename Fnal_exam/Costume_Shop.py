import random
from File import Json

from City_Class import City




class CostumeShop(City):
    def __init__(self,name,population):
        super().__init__(name,population)
        self.costumes = {}
        self.price = {}
        self.demand = {}
        self.data = Json()




    def add_costume(self,city_name,shop_name,price=50):
        for x in (self.costume_shops):

                if city_name == x["city_name"] and shop_name == x["shop"]:
                    costumes = int(input(f"How much costume will you add in {x["shop"]}?"))
                    new_info={}
                    for y in range(costumes):
                        costume_name= input("enter costume name")
                        stock = int(input(" enter stock"))
                        new_info["costume_name"]= costume_name
                        new_info["costume_stock"] = stock
                        new_info["costume_price"]=price
                        x[f"costume{y+1}"]=new_info.copy()
                    self.data.save_info(self.costume_shops)


    def adjust_price(self, city_name,shop_name, costume_name,new_price):
        for x in (self.costume_shops):
                diff_costume = len(x)-2
                if city_name == x["city_name"] and shop_name == x["shop"]:
                    for y in range(diff_costume):
                        if x[f"costume{y+1}"]["costume_name"]== costume_name:
                            x[f"costume{y+1}"]["costume_price"]=new_price
                            print("The new price of the costume",  x[f"costume{y+1}"])

    def adjust_stock(self,city_name,shop_name,costume_name,new_stock):
        for x in (self.costume_shops):
                diff_costume = len(x)-2
                if city_name == x["city_name"] and shop_name == x["shop"]:
                    for y in range(diff_costume):
                        if x[f"costume{y+1}"]["costume_name"]== costume_name:
                            x[f"costume{y+1}"]["costume_stock"]=new_stock
                            print("The new price of the costume",x[f"costume{y+1}"])

    def adjust_deman(self,costume_name,population):
        self.costume_shops= self.data.read_info()
        self.population_dict = self.data.population_read_info()
        if costume_name in self.population_dict:
            self.population_dict.pop(costume_name)
            my_list = []
            costume_list = []
            for x in (self.costume_shops):
                different_costumes = len(x) - 2

                for y in range(different_costumes):
                    costume = (x[f"costume{y + 1}"]["costume_name"])
                    costume_list.append(costume)

                my_list.append(different_costumes)

            costume_list.remove(costume_name)
            w=sum(my_list)-1
            diff_costum = w

            try:
                total = 100 - population

                if total < 0:
                    raise ValueError("The value of z is too large; the sum must be non-negative.")
                numbers = [random.randint(0, total) for _ in range(diff_costum-1)]
                numbers.sort()
                differences = [numbers[0]] + [numbers[i] - numbers[i - 1] for i in range(1, diff_costum-1)] + [
                total - numbers[-1]]
            except:
                differences=[total]



            for x in range(len(costume_list)):
                self.population_dict[costume_list[x]] = (f"{differences[x]}%")

            self.population_dict[costume_name]=(f"{population}%")
            print("new Demand for costumes",self.population_dict)



    def sell_costume(self,shop_name,costume_name,quantity):
      self.costume_shops=self.data.read_info()
      for x in self.costume_shops:
          if x["shop"]==shop_name:
                costumes = len(x)-2
                for costume_number in range(costumes):
                    if  costume_name == x[f"costume{costume_number+1}"]["costume_name"]:
                        costume= x[f"costume{costume_number+1}"]
                        costume_stock = costume["costume_stock"]
                        if costume_stock >= quantity:
                            new_costume_stock=costume_stock-quantity
                            costume["costume_stock"]=new_costume_stock
                            x[f"costume{costume_number + 1}"]=costume
                            self.data.save_info(self.costume_shops)
                            print("Number of suits left in stock",costume["costume_name"],"costume stock" ,costume["costume_stock"])
                        else :
                            print("There is not enough stock in the shop ")


    def report_stock(self):
        print("report_stock")
        for x in self.costume_shops:

            costumes = len(x) - 2
            for costume_number in range(costumes):
                print(x[f"costume{costume_number+1}"])
        print("Demand for costumes",self.population_dict,"\n")






