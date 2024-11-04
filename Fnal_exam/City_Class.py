import random
from tkinter.font import names

from File import Json

class City:
    def __init__(self,name,population):
        self.name =name
        self.population=population
        self.population_dict = {}
        self.costume_shops = []
        self.data=Json()

    def add_shop(self, shop_name=None):
        shop = {
            "city_name": self.name,
            "shop": shop_name
        }
        self.costume_shops.append(shop)


    def simulate_demand(self):
        my_list=[]
        costume_list=[]
        for x in (self.costume_shops):
            different_costumes=len(x)-2

            for y in range(different_costumes):
                costume=(x[f"costume{y+1}"]["costume_name"])
                costume_list.append(costume)

            my_list.append(different_costumes)
        diff_costum=sum(my_list)
        try:
            numbers = [random.randint(0, diff_costum) for _ in range(diff_costum - 1)]
            numbers.sort()
            percentage = [numbers[0]] + [numbers[i] - numbers[i - 1] for i in range(1, diff_costum - 1)] + [100 - numbers[-1]]
        except:
            percentage=[100]

        for x in range(len(costume_list)):
            self.population_dict[costume_list[x]] = (percentage[x])


        for x in (self.costume_shops):
            different_costumes=len(x)-2
            for y in range(different_costumes):
                differences = self.population_dict[x[f"costume{y+1}"]["costume_name"]]
                if differences >= 0 and differences <= 30:
                    costume_price = (30)
                elif differences > 30 and differences <= 60:
                    costume_price = (60)
                else:
                    costume_price = (100)
                (x[f"costume{y+1}"]["costume_price"])=costume_price
        self.data.save_info(self.costume_shops)
        self.data.population_save_info(self.population_dict)
        print("Demand for scostumes in percentages", self.population_dict)


    def city_report(self):
        print("city_report")
        for info in self.costume_shops:
            for kay,value in info.items():
                print(kay,value)



