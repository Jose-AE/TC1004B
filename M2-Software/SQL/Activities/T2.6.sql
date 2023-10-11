CREATE DATABASE T2_6;
USE T2_6;
show tables drop table member;
drop table video;
show tables;
--
--
CREATE TABLE member(
    memberNo integer primary key auto_increment,
    fname varchar(100) NOT NULL,
    lName varchar(100) NOT NULL,
    sex BOOLEAN NOT NULL,
    DOB date NOT NULL,
    adress varchar(100) NOT NULL,
    dateJoined date NOT NULL
);
--
CREATE TABLE director(
    directorNo integer primary key auto_increment,
    directorName varchar(100) not NULL
);
--
CREATE TABLE video(
    catalogNo integer primary key auto_increment,
    title varchar(100) NOT NULL,
    `certificate` varchar(100) NOT NULL,
    category varchar(100) NOT NULL,
    dailyRental BOOLEAN NOT NULL,
    price float NOT NULL,
    directorNo integer not NULL,
    foreign key (directorNo) references director(directorNo)
);
--
CREATE TABLE video_for_rent(
    videoNo integer primary key auto_increment,
    available BOOLEAN NOT NULL,
    catalogNo integer NOT NULL,
    foreign key (catalogNo) references `catalog`(catalogNo)
);
--
CREATE TABLE rental_agreement(
    rentalNo integer primary key auto_increment,
    memberNo integer NOT NULL,
    videoNo integer NOT NULL,
    dateOut date NOT NULL,
    dateReturn date not NULL,
    foreign key (videoNo) references video_for_rent(videoNo),
    foreign key (memberNo) references member(memberNo)
);
--Show tables
DESCRIBE video;
DESCRIBE director;
DESCRIBE video_for_rent;
DESCRIBE rental_agreement;
DESCRIBE member;
DESCRIBE video;
--
INSERT INTO member (
        memberNo,
        fname,
        lName,
        sex,
        DOB,
        adress,
        dateJoined
    )
VALUES (
        'John',
        'Doe',
        TRUE,
        '1985-01-15',
        '123 Main St, Springfield',
        '2020-05-01'
    ),
    (
        'Jane',
        'Smith',
        FALSE,
        '1990-06-20',
        '456 Elm St, Rivertown',
        '2019-03-15'
    ),
    (
        'Alice',
        'Johnson',
        FALSE,
        '1987-02-28',
        '789 Maple St, Greendale',
        '2021-01-10'
    ),
    (
        'Bob',
        'Williams',
        TRUE,
        '1992-10-05',
        '321 Oak St, Hillside',
        '2018-11-12'
    ),
    (
        'Charlie',
        'Brown',
        TRUE,
        '1988-03-25',
        '654 Pine St, Lakeside',
        '2017-09-05'
    ),
    (
        'Daisy',
        'Miller',
        FALSE,
        '1986-12-10',
        '987 Birch St, Westview',
        '2022-02-20'
    ),
    (
        'Edward',
        'Jones',
        TRUE,
        '1991-04-17',
        '147 Cedar St, Eastvale',
        '2020-10-13'
    ),
    (
        'Fiona',
        'Green',
        FALSE,
        '1989-07-23',
        '258 Spruce St, Northtown',
        '2019-06-18'
    ),
    (
        'George',
        'Taylor',
        TRUE,
        '1993-08-31',
        '369 Redwood St, Southville',
        '2018-04-24'
    ),
    (
        'Hannah',
        'White',
        FALSE,
        '1990-05-09',
        '159 Fir St, Centreville',
        '2021-07-01'
    );
--
DESCRIBE table member;
SELECT *
FROM video;
--
INSERT INTO director (directorName)
VALUES ('Christopher Nolan'),
    ('Sofia Coppola'),
    ('James Cameron'),
    ('Ava DuVernay'),
    ('Steven Spielberg'),
    ('Greta Gerwig'),
    ('Martin Scorsese'),
    ('Wes Anderson'),
    ('Patty Jenkins'),
    ('Quentin Tarantino');
--
DESCRIBE table director;
SELECT *
FROM director;
--
--
INSERT INTO video (
        title,
        `certificate`,
        category,
        dailyRental,
        price,
        directorNo
    )
VALUES (
        'The Sunset Journey',
        'PG',
        'Adventure',
        TRUE,
        2.50,
        1
    ),
    (
        'Moonlight Tales',
        'PG-13',
        'Drama',
        TRUE,
        3.00,
        2
    ),
    (
        'Chronicles of the Galaxy',
        'PG',
        'Sci-Fi',
        FALSE,
        4.00,
        3
    ),
    (
        'Mysteries of the Jungle',
        'R',
        'Adventure',
        TRUE,
        2.75,
        1
    ),
    (
        'Heartfelt Stories',
        'PG',
        'Romance',
        TRUE,
        2.25,
        4
    ),
    (
        'Crimson Shadows',
        'R',
        'Thriller',
        FALSE,
        3.50,
        5
    ),
    (
        'The Magical Kingdom',
        'G',
        'Fantasy',
        TRUE,
        3.00,
        6
    ),
    (
        'Beyond the Ocean',
        'PG-13',
        'Mystery',
        TRUE,
        3.25,
        2
    ),
    (
        'The Lost Civilization',
        'PG',
        'History',
        FALSE,
        4.25,
        3
    ),
    (
        'Tales of the Desert',
        'R',
        'Adventure',
        TRUE,
        3.75,
        1
    );
--
DESCRIBE table video;
SELECT *
FROM video;
--
--
INSERT INTO video_for_rent (available, catalogNo)
VALUES (TRUE, 3),
    (TRUE, 7),
    (FALSE, 4),
    (TRUE, 1),
    (TRUE, 6),
    (FALSE, 2),
    (TRUE, 10),
    (TRUE, 5),
    (TRUE, 3),
    (FALSE, 8),
    (TRUE, 7),
    (TRUE, 2),
    (FALSE, 2),
    (TRUE, 9),
    (TRUE, 4),
    (TRUE, 1),
    (FALSE, 7),
    (TRUE, 6),
    (TRUE, 5),
    (FALSE, 10),
    (TRUE, 3),
    (TRUE, 8),
    (FALSE, 9),
    (TRUE, 1),
    (FALSE, 5),
    (FALSE, 6),
    (TRUE, 7),
    (TRUE, 2),
    (TRUE, 4),
    (FALSE, 3) --
    --
    DESCRIBE table video_for_rent;
SELECT *
FROM video_for_rent;
--
--
INSERT INTO rental_agreement (memberNo, videoNo, dateOut, dateReturn)
VALUES (7, 21, '2023-08-23', '2023-08-26'),
    (3, 23, '2023-09-05', '2023-09-12'),
    (9, 34, '2023-08-28', '2023-09-02'),
    (1, 45, '2023-09-01', '2023-09-07'),
    (2, 50, '2023-09-15', '2023-09-17'),
    (8, 26, '2023-08-30', '2023-09-03'),
    (6, 27, '2023-09-04', '2023-09-06'),
    (4, 38, '2023-08-29', '2023-09-01'),
    (5, 49, '2023-09-10', '2023-09-15'),
    (10, 22, '2023-09-02', '2023-09-05'),
    (4, 34, '2023-08-21', '2023-08-24'),
    (7, 47, '2023-09-06', '2023-09-11'),
    (2, 41, '2023-08-29', '2023-09-04'),
    (9, 32, '2023-09-03', '2023-09-08'),
    (5, 42, '2023-09-14', '2023-09-19'),
    (1, 38, '2023-08-31', '2023-09-03'),
    (3, 48, '2023-09-07', '2023-09-10'),
    (6, 36, '2023-08-28', '2023-08-30'),
    (8, 23, '2023-09-09', '2023-09-14'),
    (10, 35, '2023-09-05', '2023-09-09');
--
select *
from video;
--
DESCRIBE rental_agreement;
SELECT *
FROM rental_agreement;
--
--1.Hacer una consulta para obtener la cardinalidad de la tabla videos, 
--renombrando la columna con el nombre de “Cardinalidad”. 
SELECT Count(*) as cardinality
FROM video;
--2.Hacer una consulta que regrese el nombre de los clientes (member) 
--ordenados por fName y lname.