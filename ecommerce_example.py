import uuid
from pygamp.ecommerce import transaction, item
from pygamp.enhanced_ecommerce import refund_items, refund_transaction
from pygamp.enhanced_ecommerce import promotion_impression, promotion_click
from pygamp.enhanced_ecommerce import checkout_option, checkout_step
from pygamp.enhanced_ecommerce import enhanced_transaction

client_id = str(uuid.uuid4())

# Transaction
#transaction(client_id, '90890', 19.90, 5.00, 0.00, 'GBP', 'Website', 'COUPON1')
#item(client_id, '90890', 'Test item', 1.99, 10, 'ABC1', 'GBP', 'Widgets')

# Enhanced ecommerce - Refunds
#refund_items(client_id, '12345', 'ABC1', 1)
#refund_transaction(client_id, '12345')

# Enhanced ecommerce - Internal promotions
#promotion_impression(client_id, 'example.com', 'about-us', 'About us', 2, 'PROMO1', 'Summer sale', 'Summer', 'Slot 1')
#promotion_click(client_id, 2, 'PROMO1', 'Summer sale', 'Summer', 'Slot 1')

# Enhanced ecommerce - Checkout option
#checkout_option(client_id, '12345', 1, 'DHL')
#checkout_step(client_id, '12345', 'example.com', '/order', 'Order complete', 5, 'Checkout complete')

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
    3: {'product_id': 'ABC3',
        'product_name': 'Product 3',
        'product_price': 39.99,
        'product_quantity': 3,
        'product_brand': 'Apple',
        'product_category': 'Phones',
        },
}

# Enhanced ecommerce - Transaction
enhanced_transaction(client_id, 'example.com', '/order', 'Order complete', '12345', 199.99, 40.00, 0.00, '', items)

#  https://developers.google.com/analytics/solutions/crm-mp-integration

