-- SQLite

CREATE TABLE Customers (
    CustomerID int PRIMARY,
    FirstName text,
    LastName text,
    Email text,
);

CREATE TABLE Orders (
    ClusterID int PRIMARY,
    ClientID int,
    CustomerID int,
    OrderDate date,
    FOREIGN (CustomerID) REFERENCES Customers(CustomerID)
);
