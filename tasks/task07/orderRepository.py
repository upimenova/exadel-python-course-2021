class Good:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class OrderRepository:
    def __init__(self):
        self.order_repository = []

    def add(self, order):
        self.order_repository.append(order)

    def get(self, order_id):
        for i in self.order_repository:
            if i.order_id == order_id:
                return i.__dict__
            else:
                print('There is no such order!')

    def list(self, n_latest):
        if n_latest is None:
            return self.order_repository
        else:
            return self.order_repository[:n_latest+1]

    def delete(self, order_id):
        for i in self.order_repository:
            if i.order_id == order_id:
                self.order_repository.remove(i)
            else:
                print('There is no such order!')


class Order(OrderRepository):
    def __init__(self, order_id, order_date, client_id, goods, price):
        self.order_id = order_id
        self.order_date = order_date
        self.client_id = client_id
        self.goods = goods
        self.price = price


repo = OrderRepository()
first = Order(11, '12.12.2020', 1, 'bread', 200)
second = Order(2, '01.08.2021', 3, 'cheese', 500)
repo.add(second)
# print(repo.get(2))
assert print(repo.get(2)) == {'order_id': 2, 'order_date': '01.08.2021', 'client_id': 3, 'goods': 'cheese', 'price': 500}, 'Get function is incorrect!'
# repo.delete(second)
# print(repo.get(2))
