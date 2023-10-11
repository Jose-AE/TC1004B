USE a_2;
CREATE TABLE student(
    id integer primary key auto_increment,
    name varchar(100) NOT NULL,
    age integer NOT NULL,
    studentNumber varchar(100) NOT NULL
);
DESCRIBE student;
DROP table student;
INSERT INTO student (name, studentNumber, age)
VALUES ("Jose", "A010", 19);
CREATE TABLE teacher(
    id integer primary key auto_increment,
    name varchar(100) NOT NULL
);
CREATE TABLE class(
    id integer primary key auto_increment,
    name varchar(100) NOT NULL,
    id_teacher integer,
    foreign key (id_teacher) references teacher(id)
);
INSERT INTO class (name);
VALUES ("Data structures");
SELECT *
from class;
UPDATE class
set id_teacher = 1
where id = 1;