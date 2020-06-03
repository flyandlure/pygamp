import pygamp

# https://developers.google.com/analytics/solutions/crm-mp-integration

"""
To send CRM data to Google Analytics using the Measurement Protocol you should send it as a non-interactive event. 
This prevents the data inflating pageview or other metrics on the site. To connect the data on a user to an existing
site user, you need to provide the user's client ID. This can be parsed from the Google Analytics cookie or accessed
using a JavaScript function and then needs to be stored in the database and associated with the user upon login. 
"""

from pygamp.custom_definitions import custom_dimension


custom_dimension('123456789', 'UA-18841631-1', '5', 'RFM 555')
