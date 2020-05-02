-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: 2020-05-02 16:45:15
-- 服务器版本： 5.7.25-log
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bmp`
--
CREATE DATABASE IF NOT EXISTS `bmp` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `bmp`;

-- --------------------------------------------------------

--
-- 表的结构 `account`
--

DROP TABLE IF EXISTS `account`;
CREATE TABLE IF NOT EXISTS `account` (
  `aid` int(10) NOT NULL AUTO_INCREMENT,
  `phone` varchar(11) NOT NULL,
  `salt` varchar(10) NOT NULL DEFAULT 'md5',
  `password` varchar(50) NOT NULL,
  `astatus` tinyint(4) NOT NULL,
  `modify_time` timestamp NOT NULL,
  `create_time` timestamp NOT NULL,
  PRIMARY KEY (`aid`),
  UNIQUE KEY `account_phone_uindex` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8 COMMENT='账户表';

-- --------------------------------------------------------

--
-- 表的结构 `order`
--

DROP TABLE IF EXISTS `order`;
CREATE TABLE IF NOT EXISTS `order` (
  `oid` int(10) NOT NULL AUTO_INCREMENT,
  `aid` int(10) NOT NULL,
  `ostatus` tinyint(4) NOT NULL,
  `oratiored` float DEFAULT NULL,
  `oratiogreen` float DEFAULT NULL,
  `oratioother` float DEFAULT NULL,
  `oresulta` tinyint(4) DEFAULT NULL,
  `oresultb` tinyint(4) DEFAULT NULL,
  `oresultall` tinyint(4) DEFAULT NULL,
  `odir` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`oid`),
  KEY `order_account_aid_fk` (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8 COMMENT='订单记录表';

-- --------------------------------------------------------

--
-- 表的结构 `smscode`
--

DROP TABLE IF EXISTS `smscode`;
CREATE TABLE IF NOT EXISTS `smscode` (
  `sid` int(10) NOT NULL AUTO_INCREMENT,
  `phone` varchar(11) NOT NULL,
  `code` varchar(6) NOT NULL,
  `bizcode` varchar(20) NOT NULL,
  `effective_time` timestamp NOT NULL,
  `create_time` timestamp NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COMMENT='短信验证记录表';

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `uid` int(10) NOT NULL AUTO_INCREMENT,
  `aid` int(10) NOT NULL,
  `uname` varchar(30) NOT NULL,
  `ugender` varchar(2) NOT NULL,
  `uemail` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  KEY `user_account_aid_fk` (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='用户表';

--
-- 限制导出的表
--

--
-- 限制表 `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `order_account_aid_fk` FOREIGN KEY (`aid`) REFERENCES `account` (`aid`);

--
-- 限制表 `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_account_aid_fk` FOREIGN KEY (`aid`) REFERENCES `account` (`aid`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
