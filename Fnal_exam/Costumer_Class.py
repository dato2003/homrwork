from Costume_Shop import CostumeShop
from File import Json
import random


class Costumer(CostumeShop):
    def __init__(self,costumer_name = str,budget =float,name=None,population=None):
        self.costumer_name = costumer_name
        self.budget = budget
        self.shoping_list = []
        self.data= Json()
        self.sell = CostumeShop(name,population)
        super().__init__(name,population)


    def by_costume(self,costume_name,quantity):
        costume = False
        Data =self.data.read_info()
        for info in Data:
            diff_costum =len(info)-2
            for number in range(diff_costum):
                    costume_stock = info[f"costume{number+1}"]["costume_stock"]
                    if costume_name ==info[f"costume{number+1}"]["costume_name"] and self.budget >= info[f"costume{number+1}"]["costume_price"] and costume_stock >= quantity and costume == False:
                        self.sell.sell_costume(info["shop"],costume_name,quantity)
                        self.budget = self.budget-info[f"costume{number+1}"]["costume_price"]
                        self.shoping_list.append(costume_name)
                        population =random.randint(0,100)
                        CostumeShop.adjust_deman(self,costume_name,population)




    def check_budget(self,costume_name):

        Data=self.data.read_info()
        for x in Data:
            costum =len(x)-2
            for number in range(costum):
                if costume_name==x[f"costume{number+1}"]["costume_name"]:
                    if x[f"costume{number+1}"]["costume_price"] <= self.budget:
                        print(f"{self.name}you can buy {x[f"costume{number+1}"]["costume_name"]} costume from {x["shop"]} price {x[f"costume{number+1}"]["costume_price"]}$")
                    else:
                        print(f"{self.name}you can not buy a costume your budget  is {self.budget}$, costume price is {x[f"costume{number+1}"]["costume_price"]}$")



    def shop_report(self):
        print(f"shopping list {self.shoping_list}")
        print(self.budget,"\n")



city =CostumeShop("tbilisy",100000)
city.add_shop("shop1")
city.add_shop("shop2")
city.add_costume('tbilisy',"shop1")
city.add_costume('tbilisy',"shop2")
city.adjust_price("tbilisy","shop1","zombie",25)
#city.adjust_stock('tbilisy',"shop1","zombie",5)
city.simulate_demand()

city.adjust_deman("zombie",30)
city.city_report()
city.report_stock()

costumer1 = Costumer("dato",120)
costumer1.by_costume("hulk",4)
costumer1.check_budget("zombie")
costumer1.shop_report()

costumer=Costumer("romani",234)
costumer.by_costume("zombie",2)
costumer.by_costume("hulk",12)
costumer.check_budget("hulk")
costumer.shop_report()









