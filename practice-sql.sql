-- this is DDL in sql
-- stands  for data definition language basically used for making or destrou=ying the table or structure not the data inside it

CREATE TABLE students(
    studentid INT,
    studentname VARCHAR,
    age INT  
);
-- now performing the crud operations,
--

-- this is create operation where we insert the values
INSERT INTO students(studenid,studentname,age);
VALUES (3240576,"shivam",21);
VALUES (3240922,"Bangalan",19);

-- this is read  operation where we select the data
SELECT *FROM students;

-- this is update operation where we update the data
UPDATE students
SET age=22
WHERE studentid =3240576
--now this is delete operation where  we delete the data
DELETE FROM students
WHERE studentid=3240922;

