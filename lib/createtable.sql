
 CREATE TABLE articles (
  article_id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(250) NOT NULL,
  picture VARCHAR(250),
  original_url VARCHAR(250) NOT NULL,
  lecongolais_url VARCHAR(250),
  message TEXT,
  short_message TEXT,
  tweet_message VARCHAR(250) NOT NULL,
  date_published DATE,
  date_accessed DATE,
  categories VARCHAR(250),
  PRIMARY KEY (article_id)
);
