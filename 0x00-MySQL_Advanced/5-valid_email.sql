-- Reset attribute `valid_email` only when `email` has been changed.
DELIMITER $$ ;
CREATE
TRIGGER update_email
BEFORE UPDATE
ON users FOR EACH ROW
BEGIN
    IF (OLD.email <> NEW.email) THEN
        SET NEW.valid_email = 0;
    ENDIF;
END$$