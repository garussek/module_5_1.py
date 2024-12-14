class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        if 0 < new_floor <= self.number_of_floors:
            for i in range(1, new_floor +1):        # значения от 1 до new_floor(включительно)
                print(i)
            else:
                print("Тфкого этажа не существует")

h1 = House("ЖК Горский", 12)
h2 = House("ЖК Домик в деревне", 2)

h1.go_to(5)
h2.go_to(10)



