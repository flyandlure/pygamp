from .transport import send


def transaction(cid,
                property_id: str,
                transaction_id: str,
                transaction_revenue: float,
                transaction_tax: float,
                transaction_shipping: float,
                transaction_currency: str,
                transaction_affiliation: str = None,
                transaction_coupon: str = None,
                ):
    """Create a Google Analytics transaction using the Measurement Protocol API.
    This should be used in conjunction with individual item hits containing each SKU,
    and Google Analytics will link them together using the common transaction_id.

    :param cid: Client ID
    :param property_id: Universal Analytics property ID, i.e. UA-123456-1
    :param transaction_coupon: Transaction coupon used
    :param transaction_shipping: Transaction shipping charge
    :param transaction_tax: Transaction tax charge
    :param transaction_revenue: Transaction revenue
    :param transaction_id: Transaction ID
    :param transaction_affiliation: Affiliation, i.e. Website
    :param transaction_currency: Transaction currency code, i.e. GBP
    :return: HTTP response status
    """

    payload = {'cid': cid,
               't': 'transaction',
               'ti': transaction_id,
               'ta': transaction_affiliation,
               'tr': transaction_revenue,
               'tt': transaction_tax,
               'ts': transaction_shipping,
               'tcc': transaction_coupon,
               'cu': transaction_currency,
               }
    send(payload, property_id)


def item(cid,
         property_id: str,
         transaction_id: str,
         item_name: str,
         item_price: float,
         item_quantity: int,
         item_code: str,
         item_currency: str,
         item_variation: str = None,
         ):
    """Create a Google Analytics transaction using the Measurement Protocol API.
    This should be used in conjunction with individual item hits containing each SKU,
    and Google Analytics will link them together using the common transaction_id.

    :param cid: Client ID
    :param property_id: Universal Analytics property ID, i.e. UA-123456-1
    :param transaction_id: Transaction ID
    :param item_variation: Item variation or category, i.e. Widgets
    :param item_currency: Item currency code, i.e. GBP
    :param item_code: Item code, i.e. ABC1234
    :param item_quantity: Item quantity, i.e. 5
    :param item_price: Item unit price, i.e. 1.99
    :param item_name: Item name, i.e. Purple Widget
    :return: HTTP response status
    """

    payload = {'cid': cid,
               't': 'transaction',
               'ti': transaction_id,
               'in': item_name,
               'ip': item_price,
               'iq': item_quantity,
               'ic': item_code,
               'iv': item_variation,
               'cu': item_currency,
               }
    send(payload, property_id)
