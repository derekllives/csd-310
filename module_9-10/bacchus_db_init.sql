/*
    Title: bacchus_db_init.sql
    Author: Brandon Hackett, Darnell Lewis, Derek Livermont, Lindsey Yin
    Date: 12/2/23
    Description: bacchus database initialization script.
*/

-- drop database user if exists 
DROP USER IF EXISTS 'bacchus_user'@'localhost';


-- create movies_user and grant them all privileges to the movies database 
CREATE USER 'bacchus_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'ILoveWine!';

-- grant all privileges to the movies database to user movies_user on localhost 
GRANT ALL PRIVILEGES ON bacchus.* TO 'bacchus_user'@'localhost';


-- drop tables if they are present
DROP TABLE IF EXISTS employee_clock;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS supply_order_line;
DROP TABLE IF EXISTS supply_order;
DROP TABLE IF EXISTS supplier;
DROP TABLE IF EXISTS component;
DROP TABLE IF EXISTS wine_order_line;
DROP TABLE IF EXISTS wine_order;
DROP TABLE IF EXISTS wine;
DROP TABLE IF EXISTS distributor;

-- create the employee table 
CREATE TABLE employee (
    emp_id     INT             NOT NULL        AUTO_INCREMENT,
    emp_first   VARCHAR(50)     NOT NULL,
    emp_last   VARCHAR(50)     NOT NULL,
    emp_position   VARCHAR(50)     NOT NULL,
    emp_rate DECIMAL(6,2) NOT NULL,
    emp_hire_date   DATE           NOT NULL,

    PRIMARY KEY(emp_id)
); 

-- create the employee_clock table 
CREATE TABLE employee_clock (
    clock_id     INT             NOT NULL        AUTO_INCREMENT,
    emp_id   INT     NOT NULL,
    clock_in  DATETIME   NOT NULL,
    clock_out DATETIME, 
    PRIMARY KEY(clock_id),
    CONSTRAINT fk_employee
    FOREIGN KEY(emp_id)
        REFERENCES employee(emp_id)
); 
-- create the supplier table
CREATE TABLE supplier (
    supplier_id   INT             NOT NULL        AUTO_INCREMENT,
    supplier_name  VARCHAR(75)     NOT NULL,
    supplier_contact   VARCHAR(75),
	supplier_email VARCHAR(75),
	supplier_phone VARCHAR(15) NOT NULL,
    PRIMARY KEY(supplier_id)
);
-- create component table
CREATE TABLE component (
    component_id   INT             NOT NULL        AUTO_INCREMENT,
    component_name  VARCHAR(75)     NOT NULL,
    component_inv_qty INT NOT NULL,
    PRIMARY KEY(component_id)
);

-- create supply_order table
CREATE TABLE supply_order (
    supply_order_id   INT             NOT NULL        AUTO_INCREMENT,
    supplier_id  INT     NOT NULL,
    order_date DATE NOT NULL,
    expected_delivery DATE,
    actual_delivery DATE,
    PRIMARY KEY (supply_order_id),
    CONSTRAINT fk_supplier
    FOREIGN KEY(supplier_id)
        REFERENCES supplier(supplier_id)
);

CREATE TABLE supply_order_line (
    supply_order_line_id   INT             NOT NULL        AUTO_INCREMENT,
    supply_order_id  INT     NOT NULL,
    component_id INT NOT NULL,
    component_quantity INT NOT NULL,
    component_price DECIMAL(8,2) NOT NULL,
    PRIMARY KEY (supply_order_line_id),
    CONSTRAINT fk_order_id
    FOREIGN KEY(supply_order_id)
        REFERENCES supply_order(supply_order_id),
    CONSTRAINT fk_component_id
    FOREIGN KEY(component_id)
        REFERENCES component(component_id)
);

CREATE TABLE distributor (
    distributor_id   INT             NOT NULL        AUTO_INCREMENT,
    distributor_name  VARCHAR(75)     NOT NULL,
    distributor_contact   VARCHAR(75),
	distributor_email VARCHAR(75),
	distributor_phone VARCHAR(15) NOT NULL,
    PRIMARY KEY(distributor_id)
);
-- create wine table
CREATE TABLE wine (
    wine_id   INT             NOT NULL        AUTO_INCREMENT,
    wine_type  VARCHAR(75)     NOT NULL,
    wine_production_date DATE NOT NULL,
    wine_qty_produced INT NOT NULL,
    PRIMARY KEY(wine_id)
);

-- create wine_order table
CREATE TABLE wine_order (
    wine_order_id   INT    NOT NULL        AUTO_INCREMENT,
    distributor_id  INT     NOT NULL,
    order_date DATE NOT NULL,
    expected_delivery DATE,
    actual_delivery DATE,
    PRIMARY KEY (wine_order_id),
    CONSTRAINT fk_distributor
    FOREIGN KEY(distributor_id)
        REFERENCES distributor(distributor_id)
);

CREATE TABLE wine_order_line (
    wine_order_line_id   INT             NOT NULL        AUTO_INCREMENT,
    wine_order_id  INT     NOT NULL,
    wine_id INT NOT NULL,
    wine_quantity INT NOT NULL,
    wine_price DECIMAL(8,2) NOT NULL,
    PRIMARY KEY (wine_order_line_id),
    CONSTRAINT fk_wine_order_id
    FOREIGN KEY(wine_order_id)
        REFERENCES wine_order(wine_order_id),
    CONSTRAINT fk_wine_id
    FOREIGN KEY(wine_id)
        REFERENCES wine(wine_id)
);

INSERT INTO employee
    VALUES
    (NULL, "Debrah", "Messing","Production", 18.00,'2020-03-20'),
    (NULL, "Brad", "Pitt","Shift Lead", 20.00,'2018-08-21'),
    (NULL, "Tina", "Fey","Custodian", 17.00,'2019-04-07'),
    (NULL, "Debbie", "Reynolds","Production", 18.00,'2021-03-02'),
    (NULL, "Alec", "Baldwin","Production", 18.00,'2022-05-28'),
    (NULL, "Amy", "Poehler","Quality Assurance", 23.00,'2022-05-28');

INSERT INTO employee_clock
    VALUES
    (NULL, 1,'2023-11-27 08:00','2023-11-27 16:00'),
    (NULL, 2,'2023-11-27 07:30','2023-11-27 15:30'),
    (NULL, 3,'2023-11-27 12:00','2023-11-27 20:00'),
    (NULL, 4,'2023-11-27 08:00','2023-11-27 16:00'),
    (NULL, 5,'2023-11-27 08:00','2023-11-27 16:00'),
    (NULL, 6,'2023-11-27 09:00','2023-11-27 17:00');

INSERT INTO supplier
    VALUES
    (NULL, "Wine Time","Joe Smith", "joesmith@winetime.com", "8003224567"),
    (NULL, "Boxes and Things","Mary Johnson", "mjohnson@boxesnthings.com", "8004567892"),
    (NULL, "Brewing Buds","Jeff Field", "jeff.field@brewingbuds.com", "6053725555");

INSERT INTO supply_order
    VALUES
    (NULL, 1, '2023-11-01','2023-11-08','2023-11-09'),
    (NULL, 1, '2023-11-05','2023-11-12','2023-11-13'),
    (NULL, 2, '2023-11-02','2023-11-06','2023-11-06'),
    (NULL, 2, '2023-11-10','2023-11-16','2023-11-15'),
    (NULL, 3, '2023-11-03','2023-11-06','2023-11-07'),
    (NULL, 3, '2023-11-28','2023-12-02', NULL);

INSERT INTO component
    VALUES
    (NULL, "750ml Glass Bottle", 200),
    (NULL, "Standard Cork", 500),
    (NULL, "Labels", 1000),
    (NULL, "12-bottle Cardboard Box", 100),
    (NULL, "225 Liter Vat ", 10),
    (NULL, "Vinyl Tubing Ft.", 300);

INSERT INTO supply_order_line
    VALUES
    (NULL, 1, 1, 300, 0.98),
    (NULL, 2, 2, 200, 0.38),
    (NULL, 3, 3, 500, 0.22),
    (NULL, 4, 4, 100, 1.25),
    (NULL, 5, 5, 20, 638),
    (NULL, 6, 6, 200, 1.20);

INSERT INTO wine
    VALUES
    (NULL, "Chardonnay", '2023-09-15', 300),
    (NULL, "Chablis", '2023-08-15', 300),
    (NULL, "Merlot", '2023-08-30', 300),
    (NULL, "Cabernet", '2023-09-05', 300),
    (NULL, "Red Blend", '2023-08-20', 300),
    (NULL, "White Blend", '2023-10-01', 300);

INSERT INTO distributor
    VALUES
    (NULL, "Ben's Distribution Co", "Jeff Stevens", "jstevens@bensdistco.com", "6884598764"),
    (NULL, "Larry's Liquor Store", "Larry Jones", NULL, "6235761234"),
    (NULL, "Betty's Wine and Spirits Wholesale", "Jessica Lee", "jlee@bettyswinenspirits.com","6665551234"),
    (NULL, "Cask and Cork Wine Distribution", "Sam Rogers", "srogers@caskncork.com","3654511572"),
    (NULL, "Wine World", "Jeff Goldblum", "jeff.goldblum@wineworld.com","8887776543"),
    (NULL, "In Vino Veritas", "Vicki Vivacious", "v.vivacious@invinoveritas.com","6055558888");

INSERT INTO wine_order
    VALUES
    (NULL, 1, '2023-11-02','2023-11-09','2023-11-10'),
    (NULL, 2, '2023-11-04','2023-11-11','2023-11-12'),
    (NULL, 3, '2023-11-04','2023-11-08','2023-11-08'),
    (NULL, 4, '2023-11-11','2023-11-17','2023-11-17'),
    (NULL, 5, '2023-11-02','2023-11-07','2023-11-07'),
    (NULL, 6, '2023-11-30','2023-12-03', NULL);

INSERT INTO wine_order_line
    VALUES
    (NULL, 1, 1, 120, 24.50),
    (NULL, 2, 2, 24, 24.50),
    (NULL, 3, 3, 60, 24.50),
    (NULL, 4, 4, 100, 24.50),
    (NULL, 5, 5, 72, 24.50),
    (NULL, 6, 6, 96, 24.50);
