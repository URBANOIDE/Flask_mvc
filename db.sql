-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.10.2-MariaDB - mariadb.org binary distribution
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
CREATE DATABASE IF NOT EXISTS `papeleria` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci */;
USE `papeleria`;

-- Volcando estructura para tabla papeleria.acceso_admin
CREATE TABLE IF NOT EXISTS `acceso_admin` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `usuario` varchar(50) NOT NULL DEFAULT '0',
  `password` varchar(50) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL DEFAULT '0',
  `nombre` varchar(50) NOT NULL DEFAULT '0',
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Volcando datos para la tabla papeleria.acceso_admin: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `acceso_admin` DISABLE KEYS */;
INSERT INTO `acceso_admin` (`id`, `usuario`, `password`, `nombre`, `email`) VALUES
	(1, '1006946655', 'NubiaUrban0', 'Alberto Albeiro', 'albertochindoy2020@itp.edu.co');
/*!40000 ALTER TABLE `acceso_admin` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.cargo
CREATE TABLE IF NOT EXISTS `cargo` (
  `id_cargo` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `sueldo` int(50) DEFAULT NULL,
  PRIMARY KEY (`id_cargo`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Volcando datos para la tabla papeleria.cargo: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `cargo` DISABLE KEYS */;
INSERT INTO `cargo` (`id_cargo`, `nombre`, `sueldo`) VALUES
	(11, 'Secretaria', 2000000),
	(14, 'Cajero', 1200000);
/*!40000 ALTER TABLE `cargo` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.clientes
CREATE TABLE IF NOT EXISTS `clientes` (
  `id_cliente` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `id_empresa_cliente` int(11) unsigned NOT NULL,
  `cedula_cliente` varchar(50) DEFAULT NULL,
  `nombres_cliente` varchar(50) DEFAULT NULL,
  `apellidos_cliente` varchar(50) DEFAULT NULL,
  `telefono_cliente` varchar(500) DEFAULT NULL,
  `direccion_cliente` varchar(50) DEFAULT NULL,
  `sexo_cliente` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_cliente`),
  KEY `FK_clientes_empresa` (`id_empresa_cliente`),
  CONSTRAINT `FK_clientes_empresa` FOREIGN KEY (`id_empresa_cliente`) REFERENCES `empresa` (`id_empresa`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Volcando datos para la tabla papeleria.clientes: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
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
  `password` varchar(50) CHARACTER SET latin1 COLLATE latin1_general_cs DEFAULT NULL,
  PRIMARY KEY (`id_empleado`),
  KEY `FK_empleados_cargo` (`id_cargo_empleado`),
  CONSTRAINT `FK_empleados_cargo` FOREIGN KEY (`id_cargo_empleado`) REFERENCES `cargo` (`id_cargo`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Volcando datos para la tabla papeleria.empleados: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `empleados` DISABLE KEYS */;
INSERT INTO `empleados` (`id_empleado`, `id_cargo_empleado`, `cedula_empleado`, `nombres_empleado`, `apellidos_empleado`, `telefono_empleado`, `direccion_empleado`, `sexo_empleado`, `password`) VALUES
	(32, 11, '1006946655', 'Alberto', 'Albeiro', '3155447848', 'Mocoa', 'M', '1273'),
	(33, 14, '1006946655', 'Alberto', 'Albeiro', '3155447848', 'Mocoa', 'M', 'NubiaUrban0');
/*!40000 ALTER TABLE `empleados` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.empresa
CREATE TABLE IF NOT EXISTS `empresa` (
  `id_empresa` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `nombre_empresa` varchar(50) DEFAULT NULL,
  `nit_empresa` varchar(50) DEFAULT NULL,
  `lugar_empresa` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_empresa`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Volcando datos para la tabla papeleria.empresa: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `empresa` DISABLE KEYS */;
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
  `total_con_iva` int(50) DEFAULT NULL,
  `fecha` date DEFAULT current_timestamp(),
  PRIMARY KEY (`id_factura`),
  KEY `FK_factura_empleados` (`id_empleado_factura`),
  KEY `FK_factura_clientes` (`id_cliente_factura`),
  KEY `FK_factura_productos` (`id_producto_factura`),
  CONSTRAINT `FK_factura_clientes` FOREIGN KEY (`id_cliente_factura`) REFERENCES `clientes` (`id_cliente`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `FK_factura_empleados` FOREIGN KEY (`id_empleado_factura`) REFERENCES `empleados` (`id_empleado`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `FK_factura_productos` FOREIGN KEY (`id_producto_factura`) REFERENCES `productos` (`id_producto`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=333357 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Volcando datos para la tabla papeleria.factura: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
/*!40000 ALTER TABLE `factura` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.marcas
CREATE TABLE IF NOT EXISTS `marcas` (
  `id_marca` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `id_empresa_marca` int(11) unsigned NOT NULL,
  `nombre_marca` varchar(50) DEFAULT NULL,
  `nacionalidad_marca` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_marca`),
  KEY `FK_marcas_empresa` (`id_empresa_marca`),
  CONSTRAINT `FK_marcas_empresa` FOREIGN KEY (`id_empresa_marca`) REFERENCES `empresa` (`id_empresa`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Volcando datos para la tabla papeleria.marcas: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `marcas` DISABLE KEYS */;
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
  CONSTRAINT `FK_productos_marca` FOREIGN KEY (`id_marca_producto`) REFERENCES `marcas` (`id_marca`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `FK_productos_provedor` FOREIGN KEY (`id_provedor_producto`) REFERENCES `provedores` (`id_provedor`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Volcando datos para la tabla papeleria.productos: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
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
  CONSTRAINT `FK_provedores_empresa` FOREIGN KEY (`id_empresa_provedor`) REFERENCES `empresa` (`id_empresa`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Volcando datos para la tabla papeleria.provedores: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `provedores` DISABLE KEYS */;
/*!40000 ALTER TABLE `provedores` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
