few_shots = [
    {
        'Question': "What is the total quantity of Amoxicillin in stock?",
        'SQLQuery': "SELECT SUM(Quantity) FROM Inventory JOIN Medicines ON Inventory.MedicineID = Medicines.MedicineID WHERE Medicines.Name = 'Amoxicillin'",
        'SQLResult': "Result of the SQL query",
        'Answer': "320"
    },
    {
        'Question': "How many different medicines are supplied by 'PharmaSupply Co.'?",
        'SQLQuery': "SELECT COUNT(DISTINCT MedicineID) FROM Inventory JOIN Suppliers ON Inventory.SupplierID = Suppliers.SupplierID WHERE Suppliers.Name = 'PharmaSupply Co.'",
        'SQLResult': "Result of the SQL query",
        'Answer': "5"
    },
    {
        'Question': "What is the total sales amount for February 2024?",
        'SQLQuery': "SELECT SUM(TotalAmount) FROM Sales WHERE SaleDate BETWEEN '2024-02-01' AND '2024-02-28'",
        'SQLResult': "Result of the SQL query",
        'Answer': "1543.75"
    },
    {
        'Question': "List all medicines that have less than 200 units in stock.",
        'SQLQuery': "SELECT Medicines.Name FROM Inventory JOIN Medicines ON Inventory.MedicineID = Medicines.MedicineID WHERE Inventory.Quantity < 200",
        'SQLResult': "Result of the SQL query",
        'Answer': "Medicine names with less than 50 units in stock"
    },
    {
        'Question': "Which customer made the most purchases in January 2024?",
        'SQLQuery': "SELECT Customers.Name FROM Sales JOIN Customers ON Sales.CustomerID = Customers.CustomerID WHERE SaleDate BETWEEN '2024-01-01' AND '2024-01-31' GROUP BY Sales.CustomerID ORDER BY SUM(Sales.Quantity) DESC LIMIT 1",
        'SQLResult': "Result of the SQL query",
        'Answer': "Customer name with the most purchases"
    },
    {
        'Question': "How many unique suppliers are there for the medicine 'Lisinopril'?",
        'SQLQuery': "SELECT COUNT(DISTINCT SupplierID) FROM Inventory JOIN Medicines ON Inventory.MedicineID = Medicines.MedicineID WHERE Medicines.Name = 'Lisinopril'",
        'SQLResult': "Result of the SQL query",
        'Answer': "3"
    },
    {
        'Question': "What is the average sale amount per transaction in March 2024?",
        'SQLQuery': "SELECT AVG(TotalAmount) FROM Sales WHERE SaleDate BETWEEN '2024-03-01' AND '2024-03-31'",
        'SQLResult': "Result of the SQL query",
        'Answer': "27.89"
    },
    {
        'Question': "Find the name and contact information of customers who have purchased 'Metformin' more than once.",
        'SQLQuery': "SELECT DISTINCT Customers.Name, Customers.ContactInfo FROM Sales JOIN Customers ON Sales.CustomerID = Customers.CustomerID JOIN Medicines ON Sales.MedicineID = Medicines.MedicineID WHERE Medicines.Name = 'Metformin' GROUP BY Sales.CustomerID HAVING COUNT(Sales.SaleID) > 1",
        'SQLResult': "Result of the SQL query",
        'Answer': "Customer names and contact information"
    },
    {
        'Question': "List all customers who have not made any purchases in the last 3 months.",
        'SQLQuery': "SELECT Customers.Name FROM Customers LEFT JOIN Sales ON Customers.CustomerID = Sales.CustomerID WHERE Sales.SaleDate <= DATE_SUB(NOW(), INTERVAL 3 MONTH) OR Sales.SaleID IS NULL",
        'SQLResult': "Result of the SQL query",
        'Answer': "List of customers who have not made any purchases"
    },
    {
        'Question': "Find the top 5 best-selling medicines in terms of total revenue generated.",
        'SQLQuery': "SELECT Medicines.Name, SUM(Sales.Quantity * Sales.TotalAmount) AS Revenue FROM Sales JOIN Medicines ON Sales.MedicineID = Medicines.MedicineID GROUP BY Medicines.MedicineID ORDER BY Revenue DESC LIMIT 5",
        'SQLResult': "Result of the SQL query",
        'Answer': "Top 5 best-selling medicines by revenue"
    },
    {
        'Question': "Calculate the average quantity of medicines purchased by each customer.",
        'SQLQuery': "SELECT Customers.Name, AVG(Sales.Quantity) AS AvgQuantity FROM Sales JOIN Customers ON Sales.CustomerID = Customers.CustomerID GROUP BY Customers.CustomerID",
        'SQLResult': "Result of the SQL query",
        'Answer': "Average quantity of medicines purchased by each customer"
    },
    {
        'Question': "List all medicines that are about to expire within the next month, sorted by expiry date.",
        'SQLQuery': "SELECT Medicines.Name, Inventory.ExpiryDate FROM Inventory JOIN Medicines ON Inventory.MedicineID = Medicines.MedicineID WHERE Inventory.ExpiryDate BETWEEN NOW() AND DATE_ADD(NOW(), INTERVAL 1 MONTH) ORDER BY Inventory.ExpiryDate",
        'SQLResult': "Result of the SQL query",
        'Answer': "List of medicines about to expire within the next month"
    },
    {
        'Question': "Find the total sales amount for each month of the year 2024.",
        'SQLQuery': "SELECT DATE_FORMAT(SaleDate, '%Y-%m') AS Month, SUM(TotalAmount) AS TotalSales FROM Sales WHERE YEAR(SaleDate) = 2024 GROUP BY Month",
        'SQLResult': "Result of the SQL query",
        'Answer': "Total sales amount for each month of 2024"
    },
    {
        'Question': "Identify the suppliers who have supplied all available medicines.",
        'SQLQuery': "SELECT Suppliers.Name FROM Suppliers WHERE NOT EXISTS (SELECT DISTINCT MedicineID FROM Medicines WHERE NOT EXISTS (SELECT MedicineID FROM Inventory WHERE Inventory.MedicineID = Medicines.MedicineID AND Inventory.SupplierID = Suppliers.SupplierID))",
        'SQLResult': "Result of the SQL query",
        'Answer': "Suppliers who have supplied all available medicines"
    }
]