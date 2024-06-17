Created a Secure Key Exchange API using Django and Django Rest Framework.
Defined a Channel model with the required fields.
Implemented a ChannelViewSet to handle the creation, acceptance, and listing of channels.
Created views (SecretExchangeView and KeyGenerationView) to exchange secrets and generate keys securely.
Wrote HTML templates to display channel lists.
Wrote tests to verify the API functionalities.




Run the Server and Test
Run the Django development server:
python manage.py runserver



Access the API and templates:

Channels list: Visit http://localhost:8000/api/channels/ to see the JSON response.
HTML view: Visit http://localhost:8000/api/channels/list/ to see the HTML view of the channels list.


Run the tests:
python manage.py test




