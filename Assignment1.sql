CREATE DATABASE RRS;

USE RRS;
CREATE TABLE Train (
    TrainNum int NOT NULL UNIQUE,
    TrainName varchar(255) NOT NULL UNIQUE,
    Source varchar(255) NOT NULL,
    Dest varchar(255) NOT NULL,
    fareOfGeneral int NOT NULL,
    fareOfPremium int NOT NULL
);

CREATE TABLE trainStatus (
    TrainNum int NOT NULL,
    DOJ Date NOT NULL,
    seatsAvailable int NOT NULL,
    seatsOccupied int NOT NULL,
    CHECK (seatsOccupied <=20)
);

CREATE TABLE Passenger (
    firstName varchar(255) NOT NULL,
    lastName varchar(255) NOT NULL,
    Age int NOT NULL,
    Address varchar(255),
    status varchar(255) NOT NULL,
    TrainNum int NOT NULL,
    DOJ Date NOT NULL,
    category varchar(255)
);



INSERT INTO Train
VALUES (123, "CHNY", "Chicago","Newyork",30,80),
(456, "CHHY", "Chennai","Hyderabad",40,90),
(789, "NYCH", "Newyork","Chicago",50,100),
(111, "AUHO", "Austin","Houston",60,120),
(222, "SASA", "San Fransisco","San Jose",20,45);

INSERT INTO Passenger
VALUES("Sunil","Aleti",24,"Arlington","Confirmed",123,'2022-02-14',"General"),
("Sunil","Aleti",24,"Arlington","Confirmed",789,'2022-02-18',"Premium"),
("Harika","Aleti",18,"Hyderabad","Confirmed",456,'2022-02-19',"Premium"),
("Madhuri","Mittapali",24,"Arlington","Confirmed",123,'2022-02-14',"Premium");



select * from Passenger where lastName="Aleti" and firstName="Sunil";

select * from Passenger where DOJ>='2020-02-14' and status="Confirmed";

SELECT Train.TrainNum, Train.TrainName, Train.Source, Train.Dest, Passenger.firstName, Passenger.Address, Passenger.category, Passenger.status
FROM Passenger
INNER JOIN Train ON Passenger.TrainNum=Train.TrainNum;

SELECT *
FROM Passenger
INNER JOIN Train ON Passenger.TrainNum=Train.TrainNum where Train.TrainName="CHNY";

select * from Passenger where DOJ='2022-02-14' and status='confirmed';



