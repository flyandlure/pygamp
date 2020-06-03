from .transport import send


def refund_transaction(cid, property_id: str, transaction_id: str):
    """Create a Google Analytics transaction refund using the Measurement Protocol API.
    :param cid: Client ID
    :param property_id: Universal Analytics property ID, i.e. UA-123456-1
    :param transaction_id: Transaction ID
    :return: HTTP response status
    """

    payload = {
        'cid': cid,
        'ti': transaction_id,
        't': 'event',
        'ec': 'Ecommerce',
        'ea': 'Refund transaction',
        'ni': 1,
        'pa': 'refund'
    }
    send(payload, property_id)


def refund_items(cid, property_id: str, transaction_id: str, item_code: str, item_quantity: int):
    """Create a Google Analytics item refund using the Measurement Protocol API.

    :param cid: Client ID
    :param property_id: Universal Analytics property ID, i.e. UA-123456-1
    :param transaction_id: Transaction ID
    :param item_code: Item code, i.e. ABC1
    :param item_quantity: Quantity of units to refund, i.e. 3
    :return: HTTP response status
    """

    payload = {
        'cid': cid,
        'ti': transaction_id,
        'pr1id': item_code,
        'pr1qt': item_quantity,
        't': 'event',
        'ec': 'Ecommerce',
        'ea': 'Refund transaction',
        'ni': 1,
        'pa': 'refund'
    }
    send(payload, property_id)


def promotion_impression(cid,
                         property_id: str,
                         document_hostname: str,
                         document_path: str,
                         document_title: str,
                         promotion_index: int,
                         promotion_id: str,
                         promotion_name: str,
                         promotion_creative: str,
                         promotion_position: str):
    """Create a Google Analytics promotion impression using the Measurement Protocol API.

    :param cid: Client ID
    :param property_id: Universal Analytics property ID, i.e. UA-123456-1
    :param document_hostname: Document hostname, i.e. example.com
    :param document_path: Document path, i.e. /about
    :param document_title: Document title, i.e. About us
    :param promotion_index: Promotion index slot (integer between 1 and 200)
    :param promotion_id: Promotion ID, i.e. PROMO_123
    :param promotion_name: Promotion name, i.e. Summer sale
    :param promotion_creative: Promotion creative, i.e. Summer sale banner
    :param promotion_position: Promotion position, i.e. Top left slot
    :return: HTTP response status
    """

    payload = {
        'cid': cid,
        't': 'pageview',
        'dh': document_hostname,
        'dp': document_path,
        'dt': document_title,
        'promo' + str(promotion_index) + 'id': promotion_id,
        'promo' + str(promotion_index) + 'nm': promotion_name,
        'promo' + str(promotion_index) + 'cr': promotion_creative,
        'promo' + str(promotion_index) + 'ps': promotion_position,
    }
    send(payload, property_id)


def promotion_click(cid,
                    property_id: str,
                    promotion_index: int,
                    promotion_id: str,
                    promotion_name: str,
                    promotion_creative: str,
                    promotion_position: str):
    """Create a Google Analytics promotion click using the Measurement Protocol API.

    :param cid: Client ID
    :param property_id: Universal Analytics property ID, i.e. UA-123456-1
    :param promotion_index: Promotion index slot (integer between 1 and 200)
    :param promotion_id: Promotion ID, i.e. PROMO_123
    :param promotion_name: Promotion name, i.e. Summer sale
    :param promotion_creative: Promotion creative, i.e. Summer sale banner
    :param promotion_position: Promotion position, i.e. Top left slot
    :return: HTTP response status
    """

    payload = {
        'cid': cid,
        't': 'event',
        'ec': 'Internal promotions',
        'ea': 'Click',
        'el': promotion_name,
        'promoa': 'click',
        'promo' + str(promotion_index) + 'id': promotion_id,
        'promo' + str(promotion_index) + 'nm': promotion_name,
        'promo' + str(promotion_index) + 'cr': promotion_creative,
        'promo' + str(promotion_index) + 'ps': promotion_position,
    }
    send(payload, property_id)


def checkout_option(cid, property_id: str, transaction_id: str, checkout_step_number: int, checkout_option_label: str):
    """Record a Google Analytics checkout option using the Measurement Protocol API.

    :param cid: Client ID
    :param property_id: Universal Analytics property ID, i.e. UA-123456-1
    :param transaction_id: Transaction ID
    :param checkout_step_number: Checkout step number, i.e. 2
    :param checkout_option_label: Checkout option label, i.e. FedEx
    :return: HTTP response status
    """
    payload = {
        'cid': cid,
        'ti': transaction_id,
        't': 'event',
        'ec': 'Checkout',
        'ea': 'Option',
        'pa': 'checkout_option',
        'cos': checkout_step_number,
        'col': checkout_option_label,
    }
    send(payload, property_id)


def checkout_step(cid,
                  property_id: str,
                  transaction_id: str,
                  document_hostname: str,
                  document_path: str,
                  document_title: str,
                  checkout_step_number: int,
                  checkout_step_label: str):
    """Record a Google Analytics checkout step using the Measurement Protocol API.

    :param cid: Client ID
    :param property_id: Universal Analytics property ID, i.e. UA-123456-1
    :param transaction_id: Transaction ID
    :param document_hostname: Document hostname, i.e. example.com
    :param document_path: Document path, i.e. /payment
    :param document_title: Document title, i.e. Checkout complete
    :param checkout_step_number: Checkout step number, i.e. 5
    :param checkout_step_label: Checkout step label, i.e. Checkout complete
    :return:
    """
    payload = {
        'cid': cid,
        'ti': transaction_id,
        't': 'pageview',
        'dh': document_hostname,
        'dp': document_path,
        'dt': document_title,
        'ec': 'Checkout',
        'ea': 'Option',
        'pa': 'checkout',
        'cos': checkout_step_number,
        'col': checkout_step_label,
    }
    send(payload, property_id)


def enhanced_transaction(cid,
                         property_id: str,
                         document_hostname: str,
                         document_path: str,
                         document_title: str,
                         transaction_id: str,
                         transaction_revenue: float,
                         transaction_tax: float,
                         transaction_shipping: float,
                         transaction_coupon: str,
                         items: dict):
    """Record a Google Analytics enhanced ecommerce transaction step using the Measurement Protocol API.
    This function takes core parameters for a transaction and a nested Python dictionary of items and then
    formats and merges the payloads before passing them to the API.

    :param cid: Client ID
    :param property_id: Universal Analytics property ID, i.e. UA-123456-1
    :param document_hostname: Document hostname, i.e. example.com
    :param document_path: Document path, i.e. /payment
    :param document_title: Document title, i.e. Checkout complete
    :param transaction_id: Transaction ID, i.e. 12345
    :param transaction_revenue: Transaction revenue, i.e. 199.99
    :param transaction_tax: Transaction tax, i.e. 49.99
    :param transaction_shipping: Transaction shipping, i.e. 0
    :param transaction_coupon: Transaction coupon code, i.e. WELCOME
    :param items: Python dictionary of item level data
    :return: HTTP Status
    """
    payload = {
        'cid': cid,
        't': 'pageview',
        'pa': 'purchase',
        'dh': document_hostname,
        'dp': document_path,
        'dt': document_title,
        'ti': transaction_id,
        'tr': transaction_revenue,
        'tt': transaction_tax,
        'ts': transaction_shipping,
        'tcc': transaction_coupon,
    }

    payload = {**payload, **enhanced_transaction_items(items)}
    send(payload, property_id)


def enhanced_transaction_items(items: dict):
    """Return a formatted payload of items for a Google Analytics enhanced ecommerce transaction.

    :param items: Nested Python dictionary containing item data.
    :return: Formatted payload of items matching the below format.
    :example:

    items = {
    1: {'product_id': 'ABC1',
        'product_name': 'Product 1',
        'product_price': 19.99,
        'product_quantity': 1,
        'product_brand': 'Apple',
        'product_category': 'Phones',
        'product_variant': '256GB',
        },
    2: {'product_id': 'ABC2',
        'product_name': 'Product 2',
        'product_price': 20.99,
        'product_quantity': 2,
        'product_brand': 'Apple',
        'product_category': 'Phones',
        'product_variant': '500GB',
        },
    }
    """

    items_payload = {}

    for item in items:
        prefix = 'pr{0}'.format(item)
        payload_item = {}

        if 'product_id' in items[item]:
            payload_item[prefix + 'id'] = items[item]['product_id']

        if 'product_name' in items[item]:
            payload_item[prefix + 'nm'] = items[item]['product_name']

        if 'product_price' in items[item]:
            payload_item[prefix + 'pr'] = items[item]['product_price']

        if 'product_quantity' in items[item]:
            payload_item[prefix + 'qt'] = items[item]['product_quantity']

        if 'product_brand' in items[item]:
            payload_item[prefix + 'br'] = items[item]['product_brand']

        if 'product_category' in items[item]:
            payload_item[prefix + 'ca'] = items[item]['product_category']

        if 'product_variant' in items[item]:
            payload_item[prefix + 'va'] = items[item]['product_variant']

        items_payload = {**items_payload, **payload_item}

    return items_payload
