import uuid
from pygamp.events import event
from pygamp.pageviews import pageview
from pygamp.custom_definitions import custom_dimension, custom_metric
from pygamp.social_interactions import social
from pygamp.exceptions import exception
from pygamp.app import screenview

client_id = str(uuid.uuid4())

# Custom dimension
custom_dimension(client_id, '2', 'Analytics')

# Custom dimension
custom_metric(client_id, '1', '1234')

# Non-interactive event
event(client_id, 'NI event', 'action', 'label', 10, 1)

# Interactive event
event(client_id, 'I event', 'action', 'label', 10, 0)

# Pageview
pageview(client_id, '/hello', 'example.com', 'Test')

# Social interactions
social(client_id, 'like', 'facebook', '/home')

# Exceptions
exception(client_id, 'Transaction not found', 1)

# Applications
screenview(client_id, 'PyGAMP', '1.0.1', 'Example')
