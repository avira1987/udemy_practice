from Temperature import Temperature

class Calorie:

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperture = temperature

    def calculater(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperture * 10
        return result

if __name__ == '__main__':
    temperature = Temperature(country='iran', city= 'gorgan').get()
    calorie = Calorie(weight=70, height=175, age=32, temperature=temperature)
    print(calorie.calculater())



