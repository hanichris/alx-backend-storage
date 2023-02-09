-- Trigger to decrease the quantity of an item after placing a new order.
CREATE
TRIGGER quantity_count
AFTER INSERT
ON orders FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.name;