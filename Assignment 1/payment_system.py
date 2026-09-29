from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def get_details(self):
        pass
    @abstractmethod
    def pay(self, amount):
        pass

class RazorpayCardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number
    def get_details(self):
        return "Razorpay Card: " + self.card_numbe
    def pay(self, amount):
        print("Payment of ₹", amount, "made using Razorpay Card")
        return True

class RazorpayUPIPayment(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id
    def get_details(self):
        return "Razorpay UPI: " + self.upi_id
    def pay(self, amount):
        print("Payment of ₹", amount, "made using Razorpay UPI")
        return True

class StripeCardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number
    def get_details(self):
        return "Stripe Card: " + self.card_number
    def pay(self, amount):
        print("Payment of ₹", amount, "made using Stripe Card")
        return True

class StripeUPIPayment(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id
    def get_details(self):
        return "Stripe UPI: " + self.upi_id
    def pay(self, amount):
        print("Payment of ₹", amount, "made using Stripe UPI")
        return True

class FactoryPaymentMethod(ABC):
    factory = {}
    @classmethod
    def get_payment_object(cls, method_type, **kwargs):
        if method_type not in cls.factory:
            raise ValueError("Invalid payment method")
        return cls.factory[method_type](**kwargs)

class RazorpayFactory(FactoryPaymentMethod):
    factory = {"card": RazorpayCardPayment, "upi": RazorpayUPIPayment}

class StripeFactory(FactoryPaymentMethod):
    factory = {"card": StripeCardPayment, "upi": StripeUPIPayment}

class Aggregator(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def call_get_payment_object(self, method_type, amount, **kwargs):
        pass

class RazorpayAggregator(Aggregator):
    def __init__(self):
        super().__init__("Razorpay")
        self.processing_fee = 2.0
    def call_get_payment_object(self, method_type, amount, **kwargs):
        payment = RazorpayFactory.get_payment_object(method_type, **kwargs)
        print("Processing Fee:", amount * self.processing_fee / 100)
        return payment.pay(amount)

class StripeAggregator(Aggregator):
    def __init__(self):
        super().__init__("Stripe")
        self.processing_fee = 2.9
    def call_get_payment_object(self, method_type, amount, **kwargs):
        payment = StripeFactory.get_payment_object(method_type, **kwargs)
        print("Processing Fee:", amount * self.processing_fee / 100)
        return payment.pay(amount)

class AggregatorFactory:
    factory = {"stripe": StripeAggregator, "razorpay": RazorpayAggregator}
    @classmethod
    def get_aggregator_object(cls, aggregator_name):
        if aggregator_name not in cls.factory:
            raise ValueError("Invalid aggregator")
        return cls.factory[aggregator_name]()

def main():
    print("--------Payment Processing System--------")
    aggregator_name = input("Enter aggregator (stripe/razorpay): ").lower()
    method_type = input("Enter payment method (card/upi): ").lower()
    try:
        amount = float(input("Enter amount: "))
        if method_type == "card":
            card_number = input("Enter card number: ")
            aggregator = AggregatorFactory.get_aggregator_object(aggregator_name)
            aggregator.call_get_payment_object(method_type,amount,card_number=card_number)
        elif method_type == "upi":
            upi_id = input("Enter UPI ID: ")
            aggregator = AggregatorFactory.get_aggregator_object(aggregator_name)
            aggregator.call_get_payment_object(method_type,amount,upi_id=upi_id)
        else:
            print("Invalid payment method")
    except ValueError as e:
        print("Error:", e)
if __name__ == "__main__":
    main()