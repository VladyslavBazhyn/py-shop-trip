from __future__ import annotations

from app.shop import Shop


class Customer:

    def __init__(
            self,
            customer: dict
    ) -> None:

        self._name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car = customer["car"]

    def _find_distance(
            self,
            shop: Shop
    ) -> float:

        x_distance = abs(self.location[0] - shop.location[0])
        y_distance = abs(self.location[1] - shop.location[1])

        return round(((x_distance ** 2) + (y_distance ** 2)) ** (1 / 2), 2)

    def chose_shop(
            self,
            shop_list: list[Shop],
            fuel_price: float
    ) -> None:
        print(f"{self._name} has {self.money} dollars")

        chipest_shop = None
        chipest_shop_price = None

        for shop in shop_list:

            road_cost = (
                    fuel_price
                    * self._find_distance(shop)
                    * self.car["fuel_consumption"]
            )

            product_cost = 0
            for product in self.product_cart:
                product_cost += (shop.products[product] * self.product_cart[product])

            trip_cost = round(road_cost + product_cost, 2)

            print(f"{self._name}'s trip to the {shop._name} costs {trip_cost}")

            if not chipest_shop_price:
                chipest_shop_price = trip_cost
                chipest_shop = shop
            if chipest_shop_price > trip_cost:
                chipest_shop_price = trip_cost
                chipest_shop = shop

        if self.money > chipest_shop_price:
            chipest_shop.customer_buying(customer=self)
            self.money -= trip_cost
            print(f"{self._name} rides to {chipest_shop._name}")
        else:
            print(f"{self._name} doesn't have enough money to make a purchase in any shop")

    def driving_home(self) -> None:
        print(
            f"{self._name} rides home\n"
            f"{self._name} now has {round(self.money, 2)} dollars"
        )
