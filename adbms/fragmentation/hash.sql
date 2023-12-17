use fragmentation;

CREATE TABLE Customer3(
Customer3ID INT PRIMARY KEY,
CustomerName VARCHAR(50),
LastName VARCHAR(50),
Country VARCHAR(50),
Age int(2),
Phone int(15)
)
PARTITION BY hash (Customer3ID) (
PARTITION c1,
PARTITION c2,
PARTITION c3,
PARTITION c4
);
INSERT INTO Customer3 (Customer3ID, CustomerName, LastName, Country, Age, Phone)
VALUES (1, 'Shubham', 'Thakur', 'India','23','965856587'),
(2, 'Aman ', 'Chopra', 'Australia','21','895647854'),
(3, 'Naveen', 'Tulasi', 'Sri lanka','24','965895478'),
(4, 'Aditya', 'Arpan', 'Austria','21','745487954'),
(5, 'Nishant. Salchichas S.A.', 'Jain', 'Spain','22','895326547'),
(6, 'Alok', 'Thakur', 'India','23','965856597'),
(7, 'Naman ', 'Chopra', 'Australia','21','895678547'),
(8, 'Naveen', 'Tulasi', 'Sri lanka','24','965895478'),
(9, 'Harsh', 'Arpan', 'Austria','21','745487964'),
(10, 'Shubham. Salchichas S.A.', 'Jain', 'Spain','22','895326547'),
(11, 'Shubham', 'Thakur', 'India','23','965856597'),
(12, 'Aman ', 'Chopra', 'Australia','21','895648547'),
(13, 'Naveen', 'Tulasi', 'Sri lanka','24','965875478'),
(14, 'Kiran', 'Arpan', 'Austria','21','745487954'),
(15, 'Nishant. Salchichas S.A.', 'Jain', 'Spain','22','896326547'),
(16, 'Khush', 'Thakur', 'India','23','965865897'),
(17, 'Aman ', 'Chopra', 'Australia','21','895678547'),
(18, 'Dev', 'Tulasi', 'Sri lanka','24','965895478'),
(19, 'Rohan', 'Arpan', 'Austria','21','745487954'),
(20, 'Nishant. Salchichas S.A.', 'Jain', 'Spain','22','895632647');
select * from Customer3 partition(c1);
select * from Customer3 partition(c2);

SHOW TABLES;