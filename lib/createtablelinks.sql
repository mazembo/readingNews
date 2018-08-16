CREATE TABLE links (
 id INT NOT NULL AUTO_INCREMENT,
 root_url VARCHAR(100),
 full_url VARCHAR(250),
 subject VARCHAR(50),
 custom BOOLEAN NULL DEFAULT FALSE,
 date_accessed DATE,
 PRIMARY KEY (id)
);
