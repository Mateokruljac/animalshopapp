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
-- Table structure for table `pets_animal`
--

DROP TABLE IF EXISTS `pets_animal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pets_animal` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `about` longtext NOT NULL,
  `img` varchar(100) NOT NULL,
  `price` double NOT NULL,
  `owner_id` int NOT NULL,
  `species_id` bigint NOT NULL,
  `status_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pets_animal_species_id_18ff54bc_fk_pets_category_id` (`species_id`),
  KEY `pets_animal_status_id_f89fd7a9_fk_pets_status_id` (`status_id`),
  KEY `pets_animal_owner_id_af88d04b_fk_auth_user_id` (`owner_id`),
  CONSTRAINT `pets_animal_owner_id_af88d04b_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `pets_animal_species_id_18ff54bc_fk_pets_category_id` FOREIGN KEY (`species_id`) REFERENCES `pets_category` (`id`),
  CONSTRAINT `pets_animal_status_id_f89fd7a9_fk_pets_status_id` FOREIGN KEY (`status_id`) REFERENCES `pets_status` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pets_animal`
--

LOCK TABLES `pets_animal` WRITE;
/*!40000 ALTER TABLE `pets_animal` DISABLE KEYS */;
INSERT INTO `pets_animal` VALUES (1,'Buldog','Buldog je opasan pas.','images/buldog.jpg',127.01,1,2,1),(2,'Maltezer','Maltezer je pas bijele boje.','images/maltezer.jpg',212.22,1,2,1);
/*!40000 ALTER TABLE `pets_animal` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-07 13:07:08
