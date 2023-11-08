-- @block
-- select database
USE RECAP;
-- @block
CREATE TABLE USERS(
    id int primary key auto_increment,
    email varchar(255) NOT NULL UNIQUE,
    bio TEXT,
    country varchar(2)
);
-- @block
INSERT INTO USERS (email, bio, country)
VALUES ("test@gmail.com", "my bio", "US");
-- @block
SELECT *
FROM USERS;
-- @block
SELECT email,
    id
FROM USERS;
-- @block
SELECT *
FROM users
WHERE id = 3;
-- @block
SELECT *
FROM users
WHERE (
        id = 1
        AND bio = 'hello'
    )
    OR EMAIL = 'test@gmail.com';
-- @block
CREATE TABLE ROOMS(
    id int auto_increment primary key,
    street varchar(255),
    owner_id int NOT NULL,
    foreign key (id) references USERS(id)
);
--@block
SELECT email
FROM USERS
    INNER JOIN ROOMS ON USERS.id = ROOMS.owner_id;