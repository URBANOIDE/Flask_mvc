-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.6.7-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para papeleria
CREATE DATABASE IF NOT EXISTS `papeleria` /*!40100 DEFAULT CHARACTER SET utf8mb3 */;
USE `papeleria`;

-- Volcando estructura para tabla papeleria.acceso_admin
CREATE TABLE IF NOT EXISTS `acceso_admin` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `usuario` varchar(50) NOT NULL DEFAULT '0',
  `password` varchar(50) NOT NULL DEFAULT '0',
  `nombre` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla papeleria.acceso_admin: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `acceso_admin` DISABLE KEYS */;
INSERT INTO `acceso_admin` (`id`, `usuario`, `password`, `nombre`) VALUES
	(1, '1006946655', '1273', 'Albeiro');
/*!40000 ALTER TABLE `acceso_admin` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.cargo
CREATE TABLE IF NOT EXISTS `cargo` (
  `id_cargo` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `sueldo` int(50) DEFAULT NULL,
  PRIMARY KEY (`id_cargo`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla papeleria.cargo: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `cargo` DISABLE KEYS */;
INSERT INTO `cargo` (`id_cargo`, `nombre`, `sueldo`) VALUES
	(11, 'Secretaria', 2000000),
	(13, 'Cajero(a)', 1000000);
/*!40000 ALTER TABLE `cargo` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.clientes
CREATE TABLE IF NOT EXISTS `clientes` (
  `id_cliente` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `id_empresa_cliente` int(11) unsigned NOT NULL,
  `cedula_cliente` int(11) unsigned DEFAULT NULL,
  `nombres_cliente` varchar(50) DEFAULT NULL,
  `apellidos_cliente` varchar(50) DEFAULT NULL,
  `telefono_cliente` varchar(500) DEFAULT NULL,
  `direccion_cliente` varchar(50) DEFAULT NULL,
  `sexo_cliente` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_cliente`),
  KEY `FK_clientes_empresa` (`id_empresa_cliente`),
  CONSTRAINT `FK_clientes_empresa` FOREIGN KEY (`id_empresa_cliente`) REFERENCES `empresa` (`id_empresa`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla papeleria.clientes: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` (`id_cliente`, `id_empresa_cliente`, `cedula_cliente`, `nombres_cliente`, `apellidos_cliente`, `telefono_cliente`, `direccion_cliente`, `sexo_cliente`) VALUES
	(23, 3, 1006946655, 'Diana', 'Congote', '3023465789', 'Mocoa', 'F'),
	(24, 1, 0, 'Bryan', 'Soto', '999121232', 'Putumayo', 'M');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.empleados
CREATE TABLE IF NOT EXISTS `empleados` (
  `id_empleado` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `id_cargo_empleado` int(11) unsigned NOT NULL,
  `cedula_empleado` varchar(50) DEFAULT NULL,
  `nombres_empleado` varchar(50) DEFAULT NULL,
  `apellidos_empleado` varchar(50) DEFAULT NULL,
  `telefono_empleado` varchar(50) DEFAULT NULL,
  `direccion_empleado` varchar(50) DEFAULT NULL,
  `sexo_empleado` varchar(50) DEFAULT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`id_empleado`),
  KEY `FK_empleados_cargo` (`id_cargo_empleado`),
  CONSTRAINT `FK_empleados_cargo` FOREIGN KEY (`id_cargo_empleado`) REFERENCES `cargo` (`id_cargo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla papeleria.empleados: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `empleados` DISABLE KEYS */;
INSERT INTO `empleados` (`id_empleado`, `id_cargo_empleado`, `cedula_empleado`, `nombres_empleado`, `apellidos_empleado`, `telefono_empleado`, `direccion_empleado`, `sexo_empleado`, `password`) VALUES
	(28, 13, '1006946655', 'Hugo', 'Chavez', '3155447848', 'Mocoa', 'M', '1273'),
	(29, 13, '1006946666', 'Albeiro', 'Chindoy', '3155447848', 'Mocoa', 'M', '1273');
/*!40000 ALTER TABLE `empleados` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.empresa
CREATE TABLE IF NOT EXISTS `empresa` (
  `id_empresa` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `nombre_empresa` varchar(50) DEFAULT NULL,
  `nit_empresa` varchar(50) DEFAULT NULL,
  `lugar_empresa` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_empresa`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla papeleria.empresa: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `empresa` DISABLE KEYS */;
INSERT INTO `empresa` (`id_empresa`, `nombre_empresa`, `nit_empresa`, `lugar_empresa`) VALUES
	(1, 'Norma', '859-48-0407', 'Colombia'),
	(3, 'Andina', '528-04-6285', 'Colombia'),
	(6, 'Papelería Maxima', '400-332-3443', 'Alemania');
/*!40000 ALTER TABLE `empresa` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.factura
CREATE TABLE IF NOT EXISTS `factura` (
  `id_factura` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `n_factura` varchar(50) NOT NULL DEFAULT '0',
  `id_empleado_factura` int(11) unsigned NOT NULL,
  `id_cliente_factura` int(11) unsigned NOT NULL,
  `id_producto_factura` int(11) unsigned NOT NULL,
  `cantidad` int(50) DEFAULT NULL,
  `total` int(50) DEFAULT NULL,
  PRIMARY KEY (`id_factura`),
  KEY `FK_factura_empleados` (`id_empleado_factura`),
  KEY `FK_factura_clientes` (`id_cliente_factura`),
  KEY `FK_factura_productos` (`id_producto_factura`),
  CONSTRAINT `FK_factura_clientes` FOREIGN KEY (`id_cliente_factura`) REFERENCES `clientes` (`id_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_factura_empleados` FOREIGN KEY (`id_empleado_factura`) REFERENCES `empleados` (`id_empleado`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_factura_productos` FOREIGN KEY (`id_producto_factura`) REFERENCES `productos` (`id_producto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla papeleria.factura: ~31 rows (aproximadamente)
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
INSERT INTO `factura` (`id_factura`, `n_factura`, `id_empleado_factura`, `id_cliente_factura`, `id_producto_factura`, `cantidad`, `total`) VALUES
	(16, 'bkeaij62wv', 28, 23, 29, 1, 2000),
	(17, 'bkeaij62wv', 28, 23, 29, 1, 2000),
	(18, 'eñadfhr9g0', 28, 23, 29, 1, 2000),
	(19, 'kgr4ao2okc', 28, 23, 31, 1, 2000),
	(20, '3adgqlioo7', 28, 23, 29, 3, 4000),
	(21, '3adgqlioo7', 28, 23, 30, 4, 5000),
	(22, '3adgqlioo7', 28, 23, 31, 5, 10000),
	(23, '3adgqlioo7', 28, 23, 31, 5, 10000),
	(24, 'tbñihrmsx5', 28, 23, 31, 2, 5000),
	(25, 'tbñihrmsx5', 28, 23, 31, 2, 5000),
	(26, '07vd6lwy4c', 28, 23, 30, 3, 7500),
	(27, '7x96k7bzfh', 29, 23, 29, 3, 9000),
	(28, '3btei4p33m', 29, 23, 29, 4, 12000),
	(29, '3btei4p33m', 29, 23, 30, 5, 12500),
	(30, '9os22gñmf6', 28, 23, 31, 4, 10000),
	(31, '9os22gñmf6', 28, 23, 30, 2, 5000),
	(32, '9os22gñmf6', 28, 23, 30, 2, 5000),
	(33, '7pñfqbqktb', 28, 24, 29, 5, 15000),
	(34, '7pñfqbqktb', 28, 24, 31, 6, 15000),
	(35, '7pñfqbqktb', 28, 24, 30, 2, 5000),
	(36, 'erbigt40c4', 29, 24, 29, 4, 12000),
	(37, 'erbigt40c4', 29, 24, 30, 4, 10000),
	(38, 'erbigt40c4', 29, 24, 31, 4, 10000),
	(39, '8g8v01z63k', 28, 23, 29, 3, 9000),
	(40, '8g8v01z63k', 28, 23, 30, 3, 7500),
	(41, '8g8v01z63k', 28, 23, 31, 3, 7500),
	(42, 'fgt2c3uxeb', 28, 24, 29, 5, 15000),
	(43, 'fgt2c3uxeb', 28, 24, 30, 3, 7500),
	(44, 'fgt2c3uxeb', 28, 24, 31, 8, 20000),
	(45, 'fgt2c3uxeb', 28, 24, 29, 10, 30000),
	(46, 'fgt2c3uxeb', 28, 24, 31, 20, 50000);
/*!40000 ALTER TABLE `factura` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.marcas
CREATE TABLE IF NOT EXISTS `marcas` (
  `id_marca` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `id_empresa_marca` int(11) unsigned NOT NULL,
  `nombre_marca` varchar(50) DEFAULT NULL,
  `nacionalidad_marca` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_marca`),
  KEY `FK_marcas_empresa` (`id_empresa_marca`),
  CONSTRAINT `FK_marcas_empresa` FOREIGN KEY (`id_empresa_marca`) REFERENCES `empresa` (`id_empresa`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla papeleria.marcas: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `marcas` DISABLE KEYS */;
INSERT INTO `marcas` (`id_marca`, `id_empresa_marca`, `nombre_marca`, `nacionalidad_marca`) VALUES
	(7, 3, 'Aluminum', 'Greece');
/*!40000 ALTER TABLE `marcas` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `id_producto` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `id_provedor_producto` int(11) unsigned NOT NULL,
  `id_marca_producto` int(11) unsigned NOT NULL,
  `nombres_producto` varchar(50) DEFAULT NULL,
  `precio_compra` int(50) DEFAULT NULL,
  `precio_venta` int(50) DEFAULT NULL,
  `ganancia` int(50) DEFAULT NULL,
  PRIMARY KEY (`id_producto`),
  KEY `FK_productos_marca` (`id_marca_producto`),
  KEY `FK_prooductos_provedor` (`id_provedor_producto`),
  CONSTRAINT `FK_productos_marca` FOREIGN KEY (`id_marca_producto`) REFERENCES `marcas` (`id_marca`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_prooductos_provedor` FOREIGN KEY (`id_provedor_producto`) REFERENCES `provedores` (`id_provedor`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla papeleria.productos: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` (`id_producto`, `id_provedor_producto`, `id_marca_producto`, `nombres_producto`, `precio_compra`, `precio_venta`, `ganancia`) VALUES
	(29, 27, 7, 'Cuaderno', 1000, 3000, 200),
	(30, 26, 7, 'Gatorade', 2000, 2500, 25),
	(31, 27, 7, 'Block', 2000, 2500, 25);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.provedores
CREATE TABLE IF NOT EXISTS `provedores` (
  `id_provedor` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `id_empresa_provedor` int(11) unsigned NOT NULL,
  `cedula_provedor` varchar(50) DEFAULT NULL,
  `nombres_provedor` varchar(50) DEFAULT NULL,
  `apellidos_provedor` varchar(50) DEFAULT NULL,
  `telefono_provedor` varchar(20) DEFAULT NULL,
  `direccion_provedor` varchar(50) DEFAULT NULL,
  `sexo_provedor` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_provedor`),
  KEY `FK_provedores_empresa` (`id_empresa_provedor`),
  CONSTRAINT `FK_provedores_empresa` FOREIGN KEY (`id_empresa_provedor`) REFERENCES `empresa` (`id_empresa`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla papeleria.provedores: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `provedores` DISABLE KEYS */;
INSERT INTO `provedores` (`id_provedor`, `id_empresa_provedor`, `cedula_provedor`, `nombres_provedor`, `apellidos_provedor`, `telefono_provedor`, `direccion_provedor`, `sexo_provedor`) VALUES
	(26, 1, '1006946655', 'Prueba', 'Pruebax', '30254478448', 'Mocoa', 'M'),
	(27, 3, '1934304395', 'Arnoldo', 'Dayer', '6702531923', '6514 Grim Junction', 'F');
/*!40000 ALTER TABLE `provedores` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
