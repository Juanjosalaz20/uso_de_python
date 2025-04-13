class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.available = True

    def sale(self):
        if self.available:
            self.available = False
            print(f'El carro marca {self.brand} modelo {self.model} ha sido vendido')
        else:
            print(f'El carro marca {self.brand} modelo {self.model} no esta disponible para la venta')
    
    def purchase(self):
        self. available = True
        print(f'El carro marca {self.brand} modelo {self.model} ha sido adquirido nuevamente')

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.sales_car = []
    
    def sale_car(self, car):
        if car.available:
            car.sale()
            self.sales_car.append(car)
        else:
            print(f'El carro marca {car.brand} modelo {car.model} no esta disponible para la venta')

    def purchase_car(self, car):
        if car in self.sales_car:
            car.purchase()
            self.sales_car.remove(car)
        else:
            print(f'El carro marca {car.brand} modelo {car.model} no esta en su poder')

class Concessionaire:
    def __init__(self):
        self.cars = []
        self.users = []

    def add_car(self, car):
        self.cars.append(car)
        print(f'El carro marca {car.brand} modelo {car.model} ha sido agregado')

    def register_user(self, user):
        self.users.append(user) 
        print(f'El cliente {user.name} con ID {user.id} ha sido registrado')

    def show_cars(self):
        print(f'Autos disponibles:')
        for car in self.cars:
            if car.available:
                print(f'{car.brand} modelo {car.model}. Precio: {car.price}')

car1 = Car('Toyota', '2019', '80.000.000' )
car2 = Car('Mazda', '2017', '66.000.000')

user1 = User('Juan', '001')

concessionaire = Concessionaire()

concessionaire.add_car(car1)

concessionaire.add_car(car2)

concessionaire.register_user(user1)

concessionaire.show_cars()

user1.sale_car(car2)

concessionaire.show_cars()

user1.purchase_car(car2)

concessionaire.show_cars()

