from random import randint
import time


"""Classes for melon orders."""

class AbstractMelonOrder(object):
    """HALLO"""

    def __init__(self, species, qty, order_type=None, tax=0):
        """HALLO 2 """
        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type


    def get_base_price(self):
        """calculates SPLURGE pricing"""

        week_day = time.strftime("%a", time.localtime())
        current_time = time.strftime("%H", time.localtime())

        if week_day not in ['Sat', 'Sun'] and current_time in range(8, 11):

            base_price = randint(5, 9) + 4
        else:

            base_price = randint(5, 9)

        return base_price


    def get_total(self):

        base_price = self.get_base_price()

        if "christmas melon" in self.species.lower():
            base_price *= 1.5

        return (1 + self.tax) * self.qty * base_price #total!



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super(DomesticMelonOrder, self).__init__(species, qty, order_type="domestic", tax=.08)

    def get_total(self):
        """Calculate price, including tax."""
        return super(DomesticMelonOrder, self).get_total()


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super(InternationalMelonOrder, self).__init__(species, qty, order_type="international", tax=.17)

        self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""

        total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            return total + 3

        else:
            return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovermentOrder(AbstractMelonOrder):
    """ government order for melons """

    def __init__(self, species, qty):
        """ Initialize melon order attributes for govts"""
        super(GovermentOrder, self).__init__(species, qty, order_type='goverment order', tax=0)

        self.passed_inspection = False

    def inspection_passed(self):
        """ Inspection status """

        self.passed_inspection = True
        #return self.passed_inspection


order0 = InternationalMelonOrder('christmas MELONSSSSSSSSSSS', 6, 'KAZAKHSTANDYYYY')
# if order0.inspection_passed() is False:
#     print "yippeeeeeeeeee"
print order0.get_total()
