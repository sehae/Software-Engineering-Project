-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: poswithinventorysystem
-- ------------------------------------------------------
-- Server version	8.4.0

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
-- Table structure for table `user_logs`
--

DROP TABLE IF EXISTS `user_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_logs` (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `action_id` int NOT NULL,
  `log_date` date NOT NULL,
  `log_time` time NOT NULL,
  `parameter` longtext NOT NULL,
  PRIMARY KEY (`log_id`,`action_id`),
  KEY `action_id` (`action_id`),
  CONSTRAINT `user_logs_ibfk_1` FOREIGN KEY (`action_id`) REFERENCES `user_actions` (`action_id`)
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_logs`
--

LOCK TABLES `user_logs` WRITE;
/*!40000 ALTER TABLE `user_logs` DISABLE KEYS */;
INSERT INTO `user_logs` VALUES (1,'MH2401',2,'2024-06-27','00:36:48','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(2,'MH2401',9,'2024-06-27','00:37:05','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(3,'MH2401',2,'2024-06-27','00:41:12','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(4,'MH2401',2,'2024-06-27','00:42:37','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(5,'MH2401',2,'2024-06-27','00:43:53','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(6,'MH2401',2,'2024-06-27','00:46:40','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(7,'MH2401',9,'2024-06-27','00:46:44','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(8,'MH2401',2,'2024-06-27','00:48:56','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(9,'MH2401',2,'2024-06-27','00:50:58','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(10,'MH2401',2,'2024-06-27','00:52:00','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(11,'MH2401',2,'2024-06-27','00:56:21','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(12,'MH2401',9,'2024-06-27','00:56:24','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(13,'MH2401',2,'2024-06-27','00:57:48','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(14,'MH2401',9,'2024-06-27','00:57:55','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(15,'0',1,'2024-06-27','00:57:55','User:\"System\" using LAPTOP-A220H6MF: attempted to login'),(16,'MH2401',2,'2024-06-27','01:06:36','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(17,'MH2401',1,'2024-06-27','01:33:51','User:\"LV0101\" using LAPTOP-A220H6MF: attempted to login'),(18,'MH2401',2,'2024-06-27','01:33:58','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(19,'MH2401',2,'2024-06-27','01:36:13','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(20,'MH2401',9,'2024-06-27','01:36:17','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(21,'MH2401',2,'2024-06-27','01:37:48','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(22,'MH2401',2,'2024-06-27','01:44:32','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(23,'MH2401',9,'2024-06-27','01:44:36','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(24,'MH2401',2,'2024-06-27','01:46:08','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(25,'MH2401',2,'2024-06-27','01:51:41','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(26,'MH2401',2,'2024-06-27','01:58:57','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(27,'MH2401',9,'2024-06-27','01:59:00','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(28,'MH2401',2,'2024-06-27','02:00:42','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(29,'MH2401',2,'2024-06-27','02:09:29','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(30,'MH2401',2,'2024-06-27','02:14:28','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(31,'MH2401',2,'2024-06-27','02:26:39','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(32,'MH2401',2,'2024-06-27','02:30:03','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(33,'MH2401',2,'2024-06-27','02:42:13','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(34,'MH2401',2,'2024-06-27','02:44:12','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(35,'MH2401',2,'2024-06-27','02:48:05','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(36,'MH2401',2,'2024-06-27','02:53:09','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(37,'MH2401',2,'2024-06-27','03:02:34','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(38,'MH2401',2,'2024-06-27','03:06:03','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(39,'MH2401',2,'2024-06-27','03:08:22','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(40,'MH2401',1,'2024-06-27','03:09:29','User:\"LV0101\" using LAPTOP-A220H6MF: attempted to login'),(41,'MH2401',1,'2024-06-27','03:09:29','User:\"LV0101\" using LAPTOP-A220H6MF: attempted to login'),(42,'MH2401',2,'2024-06-27','03:09:37','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(43,'MH2401',2,'2024-06-27','03:10:11','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(44,'MH2401',2,'2024-06-27','03:13:26','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(45,'MH2401',2,'2024-06-27','03:14:32','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(46,'MH2401',2,'2024-06-27','03:15:16','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(47,'MH2401',2,'2024-06-27','03:20:46','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(48,'MH2401',2,'2024-06-27','03:35:30','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(49,'MH2401',2,'2024-06-27','03:47:45','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(50,'MH2401',2,'2024-06-27','04:00:37','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(51,'MH2401',2,'2024-06-27','04:01:44','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(52,'MH2401',2,'2024-06-27','04:07:39','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(53,'MH2401',9,'2024-06-27','04:07:50','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(54,'0',1,'2024-06-27','04:08:57','User:\"System\" using LAPTOP-A220H6MF: attempted to login'),(55,'0',1,'2024-06-27','04:09:31','User:\"System\" using LAPTOP-A220H6MF: attempted to login'),(56,'0',1,'2024-06-27','04:09:31','User:\"System\" using LAPTOP-A220H6MF: attempted to login'),(57,'0',1,'2024-06-27','04:09:35','User:\"System\" using LAPTOP-A220H6MF: attempted to login'),(58,'0',1,'2024-06-27','04:09:41','User:\"System\" using LAPTOP-A220H6MF: attempted to login'),(59,'MH2401',2,'2024-06-27','04:10:19','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(60,'MH2401',2,'2024-06-27','04:19:15','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(61,'MH2401',2,'2024-06-27','04:22:07','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(62,'MH2401',2,'2024-06-27','04:23:38','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(63,'MH2401',2,'2024-06-27','04:30:30','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(64,'MH2401',9,'2024-06-27','04:30:38','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(65,'MH2401',2,'2024-06-27','04:52:43','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(66,'MH2401',2,'2024-06-27','04:55:04','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(67,'MH2401',9,'2024-06-27','04:56:57','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(68,'MH2401',2,'2024-06-27','04:59:27','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(69,'MH2401',9,'2024-06-27','04:59:39','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(70,'MH2401',1,'2024-06-27','05:00:16','User:\"LV0101\" using LAPTOP-A220H6MF: attempted to login'),(71,'MH2401',1,'2024-06-27','05:00:17','User:\"LV0101\" using LAPTOP-A220H6MF: attempted to login'),(72,'MH2401',2,'2024-06-27','05:00:23','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(73,'MH2401',9,'2024-06-27','05:00:32','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(74,'MH2401',2,'2024-06-27','08:11:24','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(75,'MH2401',9,'2024-06-27','08:11:39','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(76,'MH2401',2,'2024-06-27','08:11:53','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(77,'MH2401',9,'2024-06-27','08:12:00','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(78,'MH2401',2,'2024-06-27','08:16:45','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(79,'MH2401',2,'2024-06-27','08:19:04','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(80,'MH2401',2,'2024-06-27','08:20:41','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(81,'MH2401',2,'2024-06-27','08:25:21','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(82,'MH2401',9,'2024-06-27','08:25:23','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(83,'MH2401',2,'2024-06-27','08:28:35','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(84,'MH2401',9,'2024-06-27','08:28:37','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(85,'MH2401',2,'2024-06-27','08:29:46','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(86,'MH2401',9,'2024-06-27','08:29:51','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(87,'MH2401',2,'2024-06-27','08:36:03','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(88,'MH2401',9,'2024-06-27','08:36:06','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(89,'MH2401',2,'2024-06-27','08:37:00','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(90,'MH2401',9,'2024-06-27','08:37:02','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(91,'MH2401',2,'2024-06-27','08:41:03','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(92,'MH2401',9,'2024-06-27','08:41:09','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(93,'MH2401',2,'2024-06-27','08:43:05','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(94,'MH2401',9,'2024-06-27','08:43:07','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(95,'MH2401',2,'2024-06-27','08:43:23','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(96,'MH2401',2,'2024-06-27','08:47:35','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(97,'MH2401',9,'2024-06-27','08:47:36','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(98,'MH2401',2,'2024-06-27','09:05:34','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(99,'MH2401',9,'2024-06-27','09:05:39','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(100,'MH2401',2,'2024-06-27','09:06:00','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(101,'MH2401',9,'2024-06-27','09:06:00','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(102,'MH2401',2,'2024-06-27','09:06:08','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(103,'MH2401',9,'2024-06-27','09:06:09','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(104,'MH2401',2,'2024-06-27','09:06:41','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(105,'MH2401',9,'2024-06-27','09:06:46','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(106,'MH2401',1,'2024-06-27','09:07:46','User:\"LV0101\" using LAPTOP-A220H6MF: attempted to login'),(107,'MH2401',2,'2024-06-27','09:07:51','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(108,'MH2401',9,'2024-06-27','09:07:58','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(109,'MH2401',2,'2024-06-27','09:08:32','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(110,'MH2401',9,'2024-06-27','09:08:51','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(111,'MH2401',2,'2024-06-27','09:10:46','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(112,'MH2401',9,'2024-06-27','09:17:04','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(113,'MH2401',2,'2024-06-27','09:58:00','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(114,'MH2401',2,'2024-06-27','09:58:59','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(115,'MH2401',9,'2024-06-27','10:03:20','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(116,'MH2401',2,'2024-06-27','10:20:14','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(117,'MH2401',2,'2024-06-27','10:43:27','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(118,'MH2401',2,'2024-06-27','21:31:42','User:\"LV0101\" using DESKTOP-MVAR96E: successfully logged in'),(119,'MH2401',2,'2024-06-27','21:34:50','User:\"LV0101\" using DESKTOP-MVAR96E: successfully logged in'),(120,'MH2401',2,'2024-06-27','21:42:48','User:\"LV0101\" using DESKTOP-MVAR96E: successfully logged in');
/*!40000 ALTER TABLE `user_logs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-27 21:46:34
