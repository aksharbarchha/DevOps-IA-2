# Example of Microservices in Python


Overview
========

This is an example project which demonstrates the use of microservices for a fictional movie theater. 
The backend of this project is powered by 4 microservices, all of which happen to be written in Python using 
Flask.
 * Movie Service (Port: 5001) : Provides information like movie ratings, title, etc.
 * Show Times Service (Port: 5002) : Provides show times information.
 * Booking Service (Port: 5003) : Provides booking information. 
 * Users Service (Port: 5000) : Provides movie suggestions for users by communicating with other services.

Install
=======

The quick way is use the provided `make` file.

<code>
$ make install
</code>

Starting and Stopping Services
==============================

To launch the services:

<code>
$ make launch
</code>

To stop the services: 

<code>
$ make shutdown
</code>



