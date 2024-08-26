"""
Strategy Pattern
Công dụng của Strategy Pattern:

Strategy Pattern (Mẫu chiến lược) là một design pattern thuộc nhóm hành vi (Behavioral Pattern).
Mục đích của nó là định nghĩa một họ các thuật toán, đóng gói từng thuật toán, và làm cho chúng có thể hoán đổi cho nhau.
Strategy pattern cho phép thuật toán thay đổi độc lập so với chương trình sử dụng chúng.

Khi nào nên sử dụng Strategy Pattern?

Khi bạn có nhiều cách thức thực hiện một công việc nào đó và muốn dễ dàng thay đổi hoặc mở rộng mà không ảnh hưởng đến code hiện tại.
Khi bạn muốn tránh việc sử dụng nhiều câu lệnh điều kiện (if-else, switch-case) để chọn thuật toán trong runtime.
Ví dụ minh họa:

Giả sử bạn đang xây dựng một ứng dụng tính toán chi phí vận chuyển cho một công ty logistics.
Công ty có nhiều phương thức vận chuyển khác nhau như: giao hàng đường bộ, giao hàng đường hàng không,
và giao hàng đường biển, mỗi phương thức sẽ có cách tính toán chi phí khác nhau.

Chúng ta sẽ sử dụng Strategy Pattern để dễ dàng thêm vào hoặc thay đổi phương thức tính toán chi phí mà không ảnh hưởng đến các phần khác của chương trình.
"""
from abc import ABC, abstractmethod


# Interface Strategy
class ShippingCostStrategy(ABC):
    @abstractmethod
    def calculate(self, weight):
        pass


class RoadShippingCost(ShippingCostStrategy):
    def calculate(self, weight):
        return weight * 1.5


class AirShippingCost(ShippingCostStrategy):
    def calculate(self, weight):
        return weight * 3.0


class SeaShippingCost(ShippingCostStrategy):
    def calculate(self, weight):
        return weight * 2.0



class ShippingOrder:
    def __init__(self, strategy: ShippingCostStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ShippingCostStrategy):
        self._strategy = strategy

    def calculate_cost(self, weight):
        return self._strategy.calculate(weight)


# Sử dụng Strategy Pattern
order = ShippingOrder(RoadShippingCost())
print("Chi phí giao hàng đường bộ:", order.calculate_cost(10))  # Output: 15.0

order_air = ShippingOrder(AirShippingCost())
print("Chi phí giao hàng đường hàng không:", order_air.calculate_cost(10))  # Output: 30.0

order.set_strategy(SeaShippingCost())
print("Chi phí giao hàng đường biển:", order.calculate_cost(10))  # Output: 20.0
