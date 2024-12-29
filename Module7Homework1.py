class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        prods_str = str(f'{self.name}, {self.weight}, {self.category}')
        return prods_str


class Shop:
    def __init__(self):
        self.__file_name = open('products.txt', 'a')
        self.__file_name.close()

    def get_products(self):
        get_file = open('products.txt', 'r')
        name_prod = get_file.read()
        get_file.close()
        return name_prod

    def add(self, *products):
        for product in products:
            with open('products.txt', 'r') as file:
                lines = file.readlines()
            is_in_file = False
            for line in lines:
                if product.name in line and product.category in line:
                    is_in_file = True
                    product_weight = float(line.split(', ')[1])
                    product_weight += product.weight
                    with open('products.txt', 'w') as file:
                        for line in lines:
                            if product.name in line and product.category in line:
                                file.write(f'{product.name}, {product_weight}, {product.category}\n')
                            else:
                                file.write(line)
                    print(f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {product_weight}')
            if not is_in_file:
                with open('products.txt', 'a+') as file:
                    file.write(f'{str(product)}\n')
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())