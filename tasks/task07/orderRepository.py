class Good:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Order:
    def __init__(self, order_id, order_date, client_id, goods, price):
        self.order_id = order_id
        self.order_date = order_date
        self.client_id = client_id
        self.goods = goods
        self.price = price


OrderRepository = []


def add(order):
    OrderRepository.append(order)


def get(order_id):
    for i in OrderRepository:
        if i.order_id == order_id:
            return i
        else:
            print('There is no such order!')


first = Order(11, '12.12', 1, 'bread', 200)
add(first)
print(OrderRepository)
