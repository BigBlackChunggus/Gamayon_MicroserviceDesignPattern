# Gamayon_MicroserviceDesignPattern
Microservice Design Pattern - Gamayon (Activity)


In this example, I produced 3 services: User, Account, and Gateway service. User and Account service are
responsible for retrieving data about users and accounts. Gateway on the otherhand acts as a proxy between the client
and other services.

Each service has its own Flask app that listens on a different port, and uses the requests library to communicate
with other services. The Gateway service combines data from the User service and the Account service and returns it to
the client as a single JSON response.

In effect, the files have their own individual functionality and responsibility to operate the program independently.

This is a basic example of a microservice design pattern, which allows us to break down large applications to smaller,
more manageable services that can be developed, deployed, and scaled independently.
