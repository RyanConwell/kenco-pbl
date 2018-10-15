DROP TABLE IF EXISTS device;
DROP TABLE IF EXISTS request;


CREATE TABLE device (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  product TEXT NOT NULL,
  location TEXT NOT NULL
);

CREATE TABLE request (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  device_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (device_id) REFERENCES device (id)
);