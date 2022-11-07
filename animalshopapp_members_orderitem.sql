-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: animalshopapp
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `members_orderitem`
--

DROP TABLE IF EXISTS `members_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int DEFAULT NULL,
  `date_added` datetime(6) NOT NULL,
  `order_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `members_orderitem_order_id_8f65d3a7_fk_members_order_id` (`order_id`),
  KEY `members_orderitem_product_id_7a4de753_fk_pets_animal_id` (`product_id`),
  CONSTRAINT `members_orderitem_order_id_8f65d3a7_fk_members_order_id` FOREIGN KEY (`order_id`) REFERENCES `members_order` (`id`),
  CONSTRAINT `members_orderitem_product_id_7a4de753_fk_pets_animal_id` FOREIGN KEY (`product_id`) REFERENCES `pets_animal` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members_orderitem`
--

LOCK TABLES `members_orderitem` WRITE;
/*!40000 ALTER TABLE `members_orderitem` DISABLE KEYS */;
INSERT INTO `members_orderitem` VALUES (1,1,'2022-11-03 13:17:35.856551',2,1),(3,3,'2022-11-03 14:41:09.227207',3,1),(4,2,'2022-11-03 14:41:12.980693',3,2);
/*!40000 ALTER TABLE `members_orderitem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-07 13:07:12
