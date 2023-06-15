-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: fyp
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `patientinfo`
--

DROP TABLE IF EXISTS `patientinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patientinfo` (
  `idinfo` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `age` varchar(45) DEFAULT NULL,
  `sex` varchar(45) DEFAULT NULL,
  `income` varchar(45) DEFAULT NULL,
  `education` varchar(45) DEFAULT NULL,
  `country` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `postal_code` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `phone` int DEFAULT NULL,
  `doctor_id` int DEFAULT NULL,
  PRIMARY KEY (`idinfo`),
  UNIQUE KEY `idinfo_UNIQUE` (`idinfo`),
  KEY `FK_docterid` (`doctor_id`),
  CONSTRAINT `FK_docterid` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patientinfo`
--

LOCK TABLES `patientinfo` WRITE;
/*!40000 ALTER TABLE `patientinfo` DISABLE KEYS */;
INSERT INTO `patientinfo` VALUES (61,'saad','ali','22','male','100000','bsit','pakistan','lahore','12143','saadali@gmail.com',1234567891,20),(63,'qwe','ewq','12','male','2000','abc','pakistan','islamabad','12345','qwe@gmail.com',1234567890,20),(64,'talha','sohail','21','male','60000','bsit','pakistan','gujrawala','14135','talha@gmail.com',361555060,21),(65,'naruto','uzumaki','21','male','12345','undergraduate','pakistan','islamabad','12345','abc@gmail.com',1234567890,20),(66,'ali','saadi','21','male','12345','undergraduate','pakistan','islamabad','12345','ali@gmail.com',1234567890,20),(67,'a','a','1','male','1','undergraduate','pakistan','islamabad','12345','a1@gmail.com',1234567890,20),(68,'q','q','1','male','1','undergraduate','pakistan','islamabad','12345','a@gmail.com',1234567890,20),(70,'talha','sohail','21','male','60000','graduate','pakistan','gujrawala','45000','talha@gmail.com',331300123,21),(71,'badar','doja','23','male','20000','undergraduate','pakistan','peshawar','32145','badar@gmail.com',333169021,20),(74,'talha','sohail','21','male','20000','undergraduate','pakistan','gujrawala','43214','talha@gmail.com',335114572,20),(75,'sadaqat','aslam','21','male','40000','undergraduate','pakistan','lahore','43215','sadaqat@gmail.com',334567829,20),(76,'aslam','talha','23','male','30000','postgraduate','pakistan','karachi','12345','aslam@gmail.com',22,20),(77,'sohail','ahmed','23','male','100000','phd','pakistan','peshawar','43215','sohail@gmail.com',334567890,20),(78,'zubair','khan','24','male','12000','undergraduate','pakistan','gujrawala','43214','zubair@gmail.com',337612534,20),(79,'ayesha','zafar','25','female','30000','graduate','pakistan','karachi','34215','ays@gmail.com',336771476,20),(80,'ayesha','zafar','25','female','40000','graduate','pakistan','lahore','43215','ayesha@gmail.com',323789465,20),(81,'osama','ali','30','male','12000','undergraduate','pakistan','islamabad','1232','t@g.com',32112121,20),(82,'ayesha','zafar','20','female','12000','undergraduate','pakistan','islamabad','1324','a@g.com',375677679,20),(83,'ayesha','zafar','30','female','12301','undergraduate','pakistan','islamabad','1233','a@gm.com',32112122,20),(84,'Ayesha','Zafar','20','female','12000','undergraduate','pakistan','islamabad','2312','a@gmail.com',31221122,20),(85,'Osama','Zafar','20','male','12000','undergraduate','pakistan','islamabad','3021','t@gmail.com',3123121,20),(86,'munawar','ali','23','male','23000','undergraduate','pakistan','islamabad','43215','munawar@gmail.com',324149846,21),(87,'ali','khan','24','male','24000','undergraduate','pakistan','islamabad','54231','ali@gmail.com',378576365,21),(88,'sohaib','ali','21','male','34000','postgraduate','pakistan','islamabad','23541','sohaib@gmail.com',339838375,21),(89,'salman','ali','34','male','65000','phd','pakistan','peshawar','54321','ali321@gmail.com',387164474,21),(90,'badar','khan','43','male','460000','undergraduate','pakistan','islamabad','12345','kha@gmail.com',335487374,21),(91,'haider','ali','21','male','100000','undergraduate','pakistan','islamabad','12345','haider@gmai.com',331276543,21),(92,'badar','rajput','21','male','200000','undergraduate','pakistan','islamabad','12345','abc@gmail.com',33143524,21);
/*!40000 ALTER TABLE `patientinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-15 19:54:36
