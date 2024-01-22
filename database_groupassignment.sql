CREATE DATABASE doctor;
USE doctor;

CREATE TABLE `doctor_availability_AM` (
  `Doctor` varchar(45) DEFAULT NULL,
  `08:00-08:15` int(11) DEFAULT NULL,
  `08:00-08:15-patient-id` varchar(20) DEFAULT NULL,
  `08:15-08:30` int(11) DEFAULT NULL,
  `08:15-08:30-patient-id` varchar(20) DEFAULT NULL,
  `08:30-08:45` int(11) DEFAULT NULL,
  `08:30-08:45-patient-id` varchar(20) DEFAULT NULL,
  `08:45-09:00` int(11) DEFAULT NULL,
  `08:45-09:00-patient-id` varchar(20) DEFAULT NULL,
  `09:00-09:15` int(11) DEFAULT NULL,
  `09:00-09:15-patient-id` varchar(20) DEFAULT NULL,
  `09:15-09:30` int(11) DEFAULT NULL,
  `09:15-09:30-patient-id` varchar(20) DEFAULT NULL,
  `09:30-09:45` int(11) DEFAULT NULL,
  `09:30-09:45-patient-id` varchar(20) DEFAULT NULL,
  `09:45-10:00` int(11) DEFAULT NULL,
  `10:00-10:15-patient-id` varchar(20) DEFAULT NULL,
  `10:15-10:30` int(11) DEFAULT NULL,
  `10:15-10:30-patient-id` varchar(20) DEFAULT NULL,
  `10:30-10:45` int(11) DEFAULT NULL,
  `10:30-10:45-patient-id` varchar(20) DEFAULT NULL,
  `10:45-11:00` int(11) DEFAULT NULL,
  `10:45-11:00-patient-id` varchar(20) DEFAULT NULL,
  `11:00-11:15` int(11) DEFAULT NULL,
  `11:00-11:15-patient-id` varchar(20) DEFAULT NULL,
  `11:15-11:30` int(11) DEFAULT NULL,
  `11:15-11:30-patient-id` varchar(20) DEFAULT NULL,
  `11:30-11:45` int(11) DEFAULT NULL,
  `11:30-11:45-patient-id` varchar(20) DEFAULT NULL,
  `11:45-12:00` int(11) DEFAULT NULL,
  `bookingDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `filldates`(dateStart DATE, dateEnd DATE, doctor VARCHAR(20))
BEGIN
  WHILE dateStart <= dateEnd DO
    INSERT INTO doctor_availability_AM (doctor, bookingDate) VALUES (doctor, dateStart);
    SET dateStart = date_add(dateStart, INTERVAL 1 DAY);
  END WHILE;
END$$
DELIMITER ;

select * from doctor_availability_AM;
CALL `doctor`.`filldates`(20231023, 20231027, 'Dr A');
CALL `doctor`.`filldates`(20231023, 20231027, 'Dr B');
CALL `doctor`.`filldates`(20231023, 20231027, 'Dr C');
CALL `doctor`.`filldates`(20231023, 20231027, 'Dr D');
CALL `doctor`.`filldates`(20231023, 20231027, 'Dr E');



CREATE TABLE patient_records (
  patient_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  patient_surname VARCHAR(50) NOT NULL,
  patient_firstname VARCHAR(50) NOT NULL,
  patient_DOB DATE NOT NULL,
  gender VARCHAR(10),
  date_joined DATE NOT NULL,
  date_last_appt DATE
  
);


INSERT INTO patient_records
(patient_surname, patient_firstname, patient_DOB, gender, date_joined, date_last_appt)
VALUES
('Smith', 'Blue', '2000-12-04', 'female', '2001-01-02', '2023-03-12'),
('Stace', 'Oprah', '1967-03-23', 'female', '2003-09-18', '2021-01-12'),
('Wicks', 'Beyonce', '1984-04-19', 'female', '1999-01-03', '2015-05-19'),
('Williams', 'Serena', '1995-09-27', 'female', '2021-08-08', '2023-04-19'),
('Boanu', 'Michelle', '1999-03-07', 'female', '2021-09-07', '2021-10-10'),
('Swayzee', 'Casper', '1967-07-18', 'male', '1993-04-18', '2000-02-02'),
('Lee', 'Mike', '1945-12-12', 'male', '2022-01-03', '2023-02-15'),
('Inka', 'Boo', '2020-11-03', 'female', '2020-12-01', '2021-09-08'),
('Crema', 'Cookie', '1966-09-02', 'female', '1981-09-03', '2023-08-19'),
('McIver', 'Sally', '2019-05-05', 'female', '2020-06-07', '2021-06-07');

SELECT * FROM patient_records -- check correctly populated table