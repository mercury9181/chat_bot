-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 21, 2018 at 08:19 PM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bot`
--

-- --------------------------------------------------------

--
-- Table structure for table `buslist`
--

CREATE TABLE `buslist` (
  `id` int(11) NOT NULL,
  `location` varchar(300) NOT NULL,
  `buses` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `buslist`
--

INSERT INTO `buslist` (`id`, `location`, `buses`) VALUES
(1, 'bashundhora', '\'torongo\', \'bahon\',\'anabil\',\'raida\''),
(2, 'farmgate', '\'6no\',\'bikolpo\',\'bahon\''),
(3, 'mirpur', '\'bahon\',\'baraka\''),
(4, 'khilgaon', '\'shadhin\',\'6no\',\'bikolpo\',\'bahon\''),
(5, 'banglamotor', '\'6no\',\'bahon\',\'akota\',\'eagle\'');

-- --------------------------------------------------------

--
-- Table structure for table `place`
--

CREATE TABLE `place` (
  `id` int(1) NOT NULL,
  `plane_name` varchar(50) NOT NULL,
  `bashundhora` int(20) NOT NULL,
  `farmgate` int(20) NOT NULL,
  `mirpur` int(20) NOT NULL,
  `banglamotor` int(20) NOT NULL,
  `khilgaon` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `place`
--

INSERT INTO `place` (`id`, `plane_name`, `bashundhora`, `farmgate`, `mirpur`, `banglamotor`, `khilgaon`) VALUES
(0, 'bashundhora', 999, 11, 17, 999, 13),
(1, 'farmgate', 11, 999, 15, 4, 999),
(2, 'mirpur', 17, 15, 999, 999, 25),
(3, 'banglamotor', 999, 4, 999, 999, 5),
(4, 'khilgaon', 13, 999, 25, 5, 999);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `buslist`
--
ALTER TABLE `buslist`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `place`
--
ALTER TABLE `place`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `buslist`
--
ALTER TABLE `buslist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `place`
--
ALTER TABLE `place`
  MODIFY `id` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
