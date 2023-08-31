SELECT SP.*
FROM SalesPeople SP
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders O
    WHERE O.Snum = SP.Snum AND O.Amt <= 2000
);
