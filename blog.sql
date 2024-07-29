-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 29, 2024 at 08:15 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blog`
--

-- --------------------------------------------------------

--
-- Table structure for table `articles`
--

CREATE TABLE `articles` (
  `ID` int(11) NOT NULL,
  `TITLE` text NOT NULL,
  `AUTHOR` text NOT NULL,
  `CONTENT` text NOT NULL,
  `CREATED_DATE` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `articles`
--

INSERT INTO `articles` (`ID`, `TITLE`, `AUTHOR`, `CONTENT`, `CREATED_DATE`) VALUES
(4, 'Octopuses', 'toygun2003', 'The octopus is a marine mollusk and a member of the class Cephalopoda, more commonly called cephalopods. Cephalopoda means “head foot” in Greek, and in this class of organisms, the head and feet are merged. A ring of eight equally-long arms surround the head. They use their arms to \"walk\" on seafloor. The undersides of the arms are covered with suction cups that are very sensitive to touch and taste. The sack-like body is perched atop the head, which has two complex and sensitive eyes, while the mouth is on the underside. Octopuses have a hard beak, which they use to pierce the shells of crustacean prey.', '2024-07-28 19:48:23'),
(5, 'World War 1', 'toygun2003', 'The First World War was the first truly global conflict. From 1914 to 1918, fighting took place across several continents, at sea and, for the first time, in the air. This was war on an unprecedented scale, with battles often lasting months instead of days. In Britain, industry, technology and the population were all mobilised for a conflict that would cost the lives of over ten million soldiers worldwide.', '2024-07-28 19:49:29'),
(6, 'What is the AI', 'toygun2003', 'Artificial intelligence (AI) refers to computer systems capable of performing complex tasks that historically only a human could do, such as reasoning, making decisions, or solving problems. \r\n\r\nToday, the term “AI” describes a wide range of technologies that power many of the services and goods we use every day – from apps that recommend tv shows to chatbots that provide customer support in real time. But do all of these really constitute artificial intelligence as most of us envision it? And if not, then why do we use the term so often? \r\n\r\nIn this article, you’ll learn more about artificial intelligence, what it actually does, and different types of it. In the end, you’ll also learn about some of its benefits and dangers and explore flexible courses that can help you expand your knowledge of AI even further.  ', '2024-07-28 19:50:30'),
(7, 'About Me', 'mutux', 'Hi i am Murat Tutuk and i am a math teacher', '2024-07-29 16:39:55'),
(9, 'Iron Man', 'toygun2003', 'Tony Stark is the wealthy son of industrialist and weapons manufacturer Howard Stark and his wife, Maria. Tony grew up a genius with a brilliant mind for technology and inventions and, naturally, followed in his father’s footsteps, inheriting Stark Industries upon his parents’ untimely death. Tony designed many weapons of war for Stark Industries, far beyond what any other company was creating, while living the lifestyle of a bon vivant...', '2024-07-29 17:04:29');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `ID` int(11) NOT NULL,
  `NAME` text NOT NULL,
  `EMAIL` text NOT NULL,
  `USERNAME` text NOT NULL,
  `PASSWORD` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `NAME`, `EMAIL`, `USERNAME`, `PASSWORD`) VALUES
(5, 'Mehmet Toygun Tutuk', 'tygn2003@gmail.com', 'toygun2003', '$5$rounds=535000$nSNQQVHdUrrJ4Rhx$ydRhx7aCY76BOe9v5GmG.magyNrwuEKG2xzRYu.h34/'),
(6, 'Aynur Tutuk', 'aynurtutuk70@gmail.com', 'tutuk_aynur', '$5$rounds=535000$Vttrk2qhjfpF4cnG$.s1sWK.S4ucec1zlBwws0Bf8ZF2GfbBhFBpzDrWry27'),
(7, 'Murat Tutuk', 'mrtttk71@gmail.com', 'mutux', '$5$rounds=535000$ZDr.xtF/s8T5d/Sh$57U5pA6P4mD36aHEbrj2ORmoFE7ulD.kUX7oghAIa73');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `articles`
--
ALTER TABLE `articles`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `articles`
--
ALTER TABLE `articles`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
