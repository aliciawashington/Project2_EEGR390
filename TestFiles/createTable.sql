create table parking_availability(
  rownum BIGSERIAL NOT NULL PRIMARY KEY,
  spaceid int NOT NULL,
  availabilty VARCHAR(10) NOT NULL,
  date DATE NOT NULL,
  time TIMETZ NOT NULL
);

