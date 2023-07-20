"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(50) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False
        with pytest.raises(ValueError):
            assert product.check_quantity(-1) is ValueError

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(10)
        assert product.quantity == 990
        product.buy(990)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(1001) is ValueError


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, cart, product):
        cart.add_product(product)
        assert cart.products == {product: 1}

        cart.add_product(product, 999)
        assert cart.products == {product: 1000}

    # # Проверяем, что в корзину невозможно добавить продуктов больше, чем есть на складе
    # def test_add_product_error(self, cart, product):
    #     with pytest.raises(ValueError):
    #         assert cart.add_product(product, 1001) is ValueError

    def test_remove_product(self, cart, product):
        cart.add_product(product, 100)
        cart.remove_product(product, 100)
        assert cart.products == {}

        cart.add_product(product, 100)
        cart.remove_product(product, 50)
        assert cart.products == {product: 50}

        cart.remove_product(product)
        assert cart.products == {}

    def test_clear(self, cart, product):
        cart.add_product(product, 500)
        assert cart.products == {product: 500}

        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 999)

        cart.get_total_price()
        assert cart.get_total_price() == 99900

    def test_buy(self, cart, product):
        cart.add_product(product, 10)
        cart.buy()

        assert cart.buy() is None
        assert product.quantity == 990

    def test_buy_error(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()
