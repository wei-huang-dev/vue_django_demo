>> pip install django

>> pip install djangorestframework

>> pip install django-cors-headers

---- Django project....

>> python manage.py makemigrations WarchestApp

>> python manage.py migrate WarchestApp

>>  python manage.py runserver

--- Check to see if SQLite created the table structure below


CREATE TABLE WarchestApp_warchestdata (
    Id            INTEGER      NOT NULL
                               PRIMARY KEY AUTOINCREMENT,
    Title         VARCHAR (50) NOT NULL,
    Field1        VARCHAR (50) NOT NULL,
    Field2        VARCHAR (50) NOT NULL,
    Field3        VARCHAR (50) NOT NULL,
    Field4        VARCHAR (50) NOT NULL,
    Field5        VARCHAR (50) NOT NULL,
    Date          DATE         NOT NULL,
    photoFileName VARCHAR (50) NOT NULL
);

---- Insert some records
insert into WarchestApp_warchestdata values(1,'ABC', 'a1', 'a2', 'a3', 'a4', 'a5', '2022-08-17', '');
insert into WarchestApp_warchestdata values(2, 'ABC', 'b1', 'b2', 'b3', 'b4', 'b5', '2022-08-18', '');
insert into WarchestApp_warchestdata values(3, 'DEF', 'd1', 'd2', 'd3', 'd4', 'd5', '2022-08-17', '');
insert into WarchestApp_warchestdata values(4, 'DEF', 'e1', 'e2', 'e3', 'e4', 'e5', '2022-08-18', '');
insert into WarchestApp_warchestdata values(5, 'GIJ', 'g1', 'g2', 'g3', 'g4', 'g5', '2022-08-17', '');
insert into WarchestApp_warchestdata values(6, 'GIJ', 'i1', 'i2', 'i3', 'i4', 'i5', '2022-08-18', '');
insert into WarchestApp_warchestdata values(7, 'KLM', 'k1', 'k2', 'k3', 'k4', 'k5', '2022-08-17', '');
insert into WarchestApp_warchestdata values(8, 'KLM', 'l1', 'l2', 'l3', 'l4', 'l5', '2022-08-18', '');


select * from warchestapp_warchestdata;


To check data
http://127.0.0.1:8000/admin
http://127.0.0.1:8000/warchest
http://127.0.0.1:8000/warchest/viewusers