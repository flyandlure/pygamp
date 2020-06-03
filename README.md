# PyGAMP
#### Google Analytics Measurement Protocol for Python
PyGAMP is a simple implementation of the Google Analytics Measurement Protocol API, which provides a server-side means of passing data into GA, whether it's from a web application, mobile app or server-based application. 

#### Installation
PyGAMP can be installed via PyPi by issuing the command `pip3 install pygamp`.

#### Features
PyGAMP currently supports the following features of Google Analytics Measurement Protocol: 

* App screenviews
* Exceptions
* Pageviews
* Event tracking
* Social interactions
* Custom dimensions
* Custom metrics
* Ecommerce tracking
* Enhanced ecommerce tracking
    * Internal promotions
    * Item and transaction refunds
    * Checkout options
    * Checkout steps

#### Examples
##### Refunding an item
`refund_items(client_id, 'UA-123456-1', '12345', 'ABC1', 1)`

##### Refunding a transaction
`refund_transaction(client_id, 'UA-123456-1', '12345')`

##### Record a promotion impression
`promotion_impression(client_id, 'UA-123456-1', 'example.com', 'about-us', 'About us', 2, 'PROMO1', 'Summer sale', 'Summer', 'Slot 1')`

##### Record a promotion click
`promotion_click(client_id, 'UA-123456-1', 2, 'PROMO1', 'Summer sale', 'Summer', 'Slot 1')`

##### Assign a value to a custom dimension
`custom_dimension(client_id, 'UA-123456-1', '2', 'Analytics')`

##### Assign a value to a custom metric
`custom_metric(client_id, 'UA-123456-1', '1', '1234')`

##### Create an interactive event
`event(client_id, 'UA-123456-1',  'NI event', 'action', 'label', 10, 1)`

##### Create a non-interactive event
`event(client_id, 'UA-123456-1', 'I event', 'action', 'label', 10, 0)`

##### Record a pageview
`pageview(client_id, 'UA-123456-1', '/hello', 'example.com', 'Test')`

##### Record a social interaction
`social(client_id, 'UA-123456-1', 'like', 'facebook', '/home')`

##### Record an exception
`exception(client_id, 'UA-123456-1', 'Transaction not found', 1)`

##### Record an application view
`screenview(client_id, 'UA-123456-1', 'PyGAMP', '1.0.1', 'Example')`

##### Record an enhanced ecommerce transaction
To record a transaction using enhanced ecommerce, you first need to construct a nested dictionary of items to push to Google Analytics along with the transaction data. This should use the following format: 

```python
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
```

This is then passed to GA using the following method: 

```python
enhanced_transaction(client_id, 'UA-123456-1', 'example.com', '/order', 'Order complete', '12345', 199.99, 40.00, 0.00, '', items)
```

