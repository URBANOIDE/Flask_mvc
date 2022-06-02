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

-- Volcando estructura para tabla papeleria.cargo
CREATE TABLE IF NOT EXISTS `cargo` (
  `id_cargo` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `id_empresa_cargo` int(11) unsigned NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `sueldo` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_cargo`),
  KEY `FK_cargo_empresa` (`id_empresa_cargo`),
  CONSTRAINT `FK_cargo_empresa` FOREIGN KEY (`id_empresa_cargo`) REFERENCES `empresa` (`id_empresa`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla papeleria.cargo: ~10 rows (aproximadamente)
/*!40000 ALTER TABLE `cargo` DISABLE KEYS */;
INSERT IGNORE INTO `cargo` (`id_cargo`, `id_empresa_cargo`, `nombre`, `sueldo`) VALUES
	(1, 4, 'Nurse Practicioner', 1311300),
	(2, 3, 'Account Representative I', 1021083),
	(3, 3, 'Statistician I', 1718547),
	(4, 1, 'Recruiter', 1454948),
	(5, 3, 'Web Developer III', 1421697),
	(6, 1, 'Registered Nurse', 1205533),
	(7, 3, 'VP Accounting', 1548052),
	(8, 1, 'Occupational Therapist', 1365434),
	(9, 1, 'Software Consultant', 1893117),
	(10, 4, 'Product Engineer', 1801776);
/*!40000 ALTER TABLE `cargo` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.clientes
CREATE TABLE IF NOT EXISTS `clientes` (
  `id_cliente` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `id_empresa_cliente` int(11) unsigned NOT NULL,
  `cedula_cliente` varchar(20) DEFAULT NULL,
  `nombres_cliente` varchar(50) DEFAULT NULL,
  `apellidos_cliente` varchar(50) DEFAULT NULL,
  `telefono_cliente` varchar(20) DEFAULT NULL,
  `direccion_cliente` varchar(50) DEFAULT NULL,
  `sexo_cliente` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_cliente`),
  KEY `FK_clientes_empresa` (`id_empresa_cliente`),
  CONSTRAINT `FK_clientes_empresa` FOREIGN KEY (`id_empresa_cliente`) REFERENCES `empresa` (`id_empresa`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla papeleria.clientes: ~20 rows (aproximadamente)
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT IGNORE INTO `clientes` (`id_cliente`, `id_empresa_cliente`, `cedula_cliente`, `nombres_cliente`, `apellidos_cliente`, `telefono_cliente`, `direccion_cliente`, `sexo_cliente`) VALUES
	(1, 4, '4879270377', 'Myrvyn', 'Ovens', '7872182629', '662 Division Hill', 'M'),
	(2, 4, '9471304091', 'Loydie', 'Barme', '4746978220', '86 Johnson Street', 'M'),
	(3, 3, '4319186567', 'Mildrid', 'Ennor', '2323016873', '1850 Hanson Parkway', 'F'),
	(4, 1, '3355715158', 'Alverta', 'Benbrick', '6611090428', '37 Rutledge Pass', 'F'),
	(5, 2, '1934304395', 'Arnoldo', 'Dayer', '6702531923', '6514 Grim Junction', 'M'),
	(6, 3, '9199978474', 'Carmel', 'Golightly', '9399520463', '48652 Portage Trail', 'F'),
	(7, 1, '9573250241', 'Warren', 'Becraft', '4982892466', '2214 Talmadge Circle', 'M'),
	(8, 1, '3089754215', 'Boyce', 'Pardi', '5256155660', '01 Eastlawn Pass', 'M'),
	(9, 2, '4822915581', 'Jasper', 'Van Driel', '0590787543', '0037 Lawn Trail', 'M'),
	(10, 3, '9675648589', 'Gilberte', 'Katz', '4771313709', '44 Mariners Cove Circle', 'F'),
	(11, 3, '2941515550', 'Hogan', 'Comusso', '5552660056', '7 Spenser Plaza', 'M'),
	(12, 2, '2176585895', 'Nelia', 'Boumphrey', '3732227626', '46373 Karstens Plaza', 'F'),
	(13, 3, '6931496999', 'Ninnette', 'Turbefield', '6139973724', '1215 Mariners Cove Trail', 'F'),
	(14, 3, '6834910158', 'Sheila-kathryn', 'Emms', '3694723005', '1 Lakewood Gardens Point', 'F'),
	(15, 4, '9148863912', 'Andy', 'Biford', '4274285456', '957 Waywood Parkway', 'M'),
	(16, 1, '1606469789', 'Laurens', 'Leuchars', '3956511697', '54258 Sachs Center', 'M'),
	(17, 2, '6696150668', 'Fax', 'Panting', '7115405700', '4 Ilene Crossing', 'M'),
	(18, 4, '6779389404', 'Austin', 'Ainscough', '7452802799', '25741 Debra Avenue', 'M'),
	(19, 1, '7884031809', 'Sherlock', 'Windrass', '0794733395', '1 Barby Center', 'M'),
	(20, 1, '2499753765', 'Niccolo', 'Gregorin', '7898295161', '269 Huxley Circle', 'M');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.empleados
CREATE TABLE IF NOT EXISTS `empleados` (
  `id_empleado` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `id_cargo_empleado` int(11) unsigned NOT NULL,
  `cedula_empleado` varchar(50) DEFAULT NULL,
  `nombres_empleado` varchar(50) DEFAULT NULL,
  `apellidos_empleado` varchar(50) DEFAULT NULL,
  `telefono_empleado` varchar(20) DEFAULT NULL,
  `direccion_empleado` varchar(50) DEFAULT NULL,
  `sexo_empleado` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_empleado`),
  KEY `FK_empleados_cargo` (`id_cargo_empleado`),
  CONSTRAINT `FK_empleados_cargo` FOREIGN KEY (`id_cargo_empleado`) REFERENCES `cargo` (`id_cargo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla papeleria.empleados: ~20 rows (aproximadamente)
/*!40000 ALTER TABLE `empleados` DISABLE KEYS */;
INSERT IGNORE INTO `empleados` (`id_empleado`, `id_cargo_empleado`, `cedula_empleado`, `nombres_empleado`, `apellidos_empleado`, `telefono_empleado`, `direccion_empleado`, `sexo_empleado`) VALUES
	(1, 2, '1056593261', 'Urbain', 'Kersting', '2308286806', '64497 Magdeline Park', 'M'),
	(2, 5, '7351400822', 'Anthiathia', 'Biasio', '0807134147', '01022 Park Meadow Alley', 'F'),
	(3, 9, '4633664557', 'Kimmy', 'Ducarne', '5814647051', '17 Tennessee Center', 'F'),
	(4, 7, '9682433967', 'Alia', 'Antoniewski', '0760845417', '6937 Petterle Circle', 'F'),
	(5, 4, '3390198105', 'Elijah', 'Jolly', '1993790411', '70130 Pennsylvania Terrace', 'M'),
	(6, 5, '4299783689', 'Jeanne', 'Wrankling', '3807411623', '94618 Meadow Vale Junction', 'F'),
	(7, 8, '5619365115', 'Clareta', 'Lovering', '7638544714', '9 Nova Court', 'F'),
	(8, 8, '2470602645', 'Edy', 'Pritchitt', '4550020113', '03 Dennis Lane', 'F'),
	(9, 5, '5616218138', 'Iona', 'Ivanenkov', '6255661962', '08260 Petterle Court', 'F'),
	(10, 4, '5218921289', 'Lauretta', 'Hollerin', '5815584894', '1 Evergreen Center', 'F'),
	(11, 5, '7565254320', 'Craggie', 'Lambden', '3736706146', '81198 Huxley Junction', 'M'),
	(12, 5, '2348818981', 'Lettie', 'Davisson', '4474206355', '49356 Sommers Center', 'F'),
	(13, 4, '6776464804', 'Kip', 'Maric', '6058297079', '8731 Esch Court', 'M'),
	(14, 8, '2618343247', 'Drucie', 'Askin', '9117837308', '30689 Stephen Avenue', 'F'),
	(15, 4, '4549091932', 'Jule', 'Petrusch', '4516774003', '2490 Cordelia Crossing', 'M'),
	(16, 8, '0064872769', 'Skye', 'McIlwrick', '5681237729', '217 Eastwood Junction', 'M'),
	(17, 7, '4015097602', 'Jamima', 'Assel', '6362795830', '88 Kedzie Place', 'F'),
	(18, 10, '2999868774', 'Phedra', 'Gossage', '2512765636', '83514 Toban Terrace', 'F'),
	(19, 8, '4880777226', 'Mateo', 'Beynon', '3437196111', '692 Jackson Street', 'M'),
	(20, 5, '0801644984', 'Ingeborg', 'Stibbs', '6201421459', '7 Sauthoff Center', 'F');
/*!40000 ALTER TABLE `empleados` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.empresa
CREATE TABLE IF NOT EXISTS `empresa` (
  `id_empresa` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `nombre_empresa` varchar(20) DEFAULT NULL,
  `nit_empresa` varchar(20) DEFAULT NULL,
  `lugar_empresa` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_empresa`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla papeleria.empresa: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `empresa` DISABLE KEYS */;
INSERT IGNORE INTO `empresa` (`id_empresa`, `nombre_empresa`, `nit_empresa`, `lugar_empresa`) VALUES
	(1, 'Predovic and Sons', '859-48-0407', 'Gujrāt'),
	(2, 'Mayert LLC', '489-99-3697', 'Maple Plain'),
	(3, 'Hodkiewicz Inc', '528-04-6285', 'Mianhu'),
	(4, 'Braun LLC', '244-57-2805', 'Baisha');
/*!40000 ALTER TABLE `empresa` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.factura
CREATE TABLE IF NOT EXISTS `factura` (
  `id_factura` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `id_empleado_factura` int(11) unsigned NOT NULL,
  `id_cliente_factura` int(11) unsigned NOT NULL,
  `id_producto_factura` int(11) unsigned NOT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_factura`),
  KEY `FK_factura_empleados` (`id_empleado_factura`),
  KEY `FK_factura_clientes` (`id_cliente_factura`),
  KEY `FK_factura_productos` (`id_producto_factura`),
  CONSTRAINT `FK_factura_clientes` FOREIGN KEY (`id_cliente_factura`) REFERENCES `clientes` (`id_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_factura_empleados` FOREIGN KEY (`id_empleado_factura`) REFERENCES `empleados` (`id_empleado`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_factura_productos` FOREIGN KEY (`id_producto_factura`) REFERENCES `productos` (`id_producto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla papeleria.factura: ~10 rows (aproximadamente)
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
INSERT IGNORE INTO `factura` (`id_factura`, `id_empleado_factura`, `id_cliente_factura`, `id_producto_factura`, `cantidad`, `total`) VALUES
	(1, 5, 2, 15, 62, 51236),
	(2, 5, 14, 8, 74, 65341),
	(3, 15, 9, 5, 35, 78331),
	(4, 14, 16, 9, 75, 77754),
	(5, 17, 4, 17, 4, 88558),
	(6, 9, 15, 9, 86, 56462),
	(7, 8, 4, 1, 34, 83515),
	(8, 12, 4, 15, 37, 84499),
	(9, 2, 4, 1, 32, 51976),
	(10, 3, 12, 20, 41, 52879);
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla papeleria.marcas: ~20 rows (aproximadamente)
/*!40000 ALTER TABLE `marcas` DISABLE KEYS */;
INSERT IGNORE INTO `marcas` (`id_marca`, `id_empresa_marca`, `nombre_marca`, `nacionalidad_marca`) VALUES
	(1, 4, 'Brass', 'Finland'),
	(2, 2, 'Steel', 'Philippines'),
	(3, 2, 'Brass', 'Russia'),
	(4, 4, 'Brass', 'Bosnia and Herzegovina'),
	(5, 3, 'Glass', 'Philippines'),
	(6, 3, 'Aluminum', 'Ukraine'),
	(7, 3, 'Aluminum', 'Greece'),
	(8, 4, 'Glass', 'Brazil'),
	(9, 2, 'Aluminum', 'Thailand'),
	(10, 4, 'Steel', 'China'),
	(11, 2, 'Plexiglass', 'Sweden'),
	(12, 4, 'Steel', 'Nigeria'),
	(13, 3, 'Granite', 'Indonesia'),
	(14, 1, 'Plastic', 'Sweden'),
	(15, 2, 'Aluminum', 'Afghanistan'),
	(16, 2, 'Rubber', 'Portugal'),
	(17, 3, 'Stone', 'China'),
	(18, 3, 'Brass', 'China'),
	(19, 4, 'Plastic', 'Kenya'),
	(20, 4, 'Plexiglass', 'Russia');
/*!40000 ALTER TABLE `marcas` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `id_producto` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `id_provedor_producto` int(11) unsigned NOT NULL,
  `id_marca_producto` int(11) unsigned NOT NULL,
  `nombres_producto` varchar(50) DEFAULT NULL,
  `precio_compra` int(11) DEFAULT NULL,
  `precio_venta` int(11) DEFAULT NULL,
  `ganancia` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_producto`),
  KEY `FK_productos_marca` (`id_marca_producto`),
  KEY `FK_prooductos_provedor` (`id_provedor_producto`),
  CONSTRAINT `FK_productos_marca` FOREIGN KEY (`id_marca_producto`) REFERENCES `marcas` (`id_marca`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_prooductos_provedor` FOREIGN KEY (`id_provedor_producto`) REFERENCES `provedores` (`id_provedor`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla papeleria.productos: ~20 rows (aproximadamente)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT IGNORE INTO `productos` (`id_producto`, `id_provedor_producto`, `id_marca_producto`, `nombres_producto`, `precio_compra`, `precio_venta`, `ganancia`) VALUES
	(1, 7, 7, 'Napkin White - Starched', 597, 1176, 295),
	(2, 20, 18, 'Cake - Sheet Strawberry', 416, 903, 89),
	(3, 3, 5, 'Sauce Bbq Smokey', 402, 1244, 74),
	(4, 7, 14, 'Gatorade - Lemon Lime', 719, 1144, 259),
	(5, 15, 3, 'Syrup - Golden, Lyles', 663, 1125, 183),
	(6, 12, 4, 'Coffee - Almond Amaretto', 492, 921, 40),
	(7, 9, 10, 'Carbonated Water - Strawberry', 685, 1314, 419),
	(8, 10, 9, 'Turnip - White', 439, 1322, 437),
	(9, 4, 13, 'Capon - Breast, Double, Wing On', 555, 1246, 24),
	(10, 17, 4, 'Grapes - Red', 753, 1432, 367),
	(11, 14, 5, 'Extract Vanilla Pure', 608, 1340, 93),
	(12, 17, 6, 'Rolled Oats', 492, 1027, 309),
	(13, 15, 20, 'Ice Cream - Super Sandwich', 500, 1035, 15),
	(14, 13, 8, 'Gelatine Leaves - Envelopes', 458, 1237, 295),
	(15, 14, 11, 'Beef - Rib Roast, Capless', 425, 1155, 434),
	(16, 20, 9, 'Beef - Chuck, Boneless', 620, 1053, 107),
	(17, 8, 7, 'Soup - Campbells, Spinach Crm', 715, 1438, 8),
	(18, 2, 12, 'Tart - Lemon', 406, 1030, 15),
	(19, 5, 13, 'Wine - Alsace Riesling Reserve', 557, 1179, 188),
	(20, 6, 17, 'Wine - Chenin Blanc K.w.v.', 713, 993, 233);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

-- Volcando estructura para tabla papeleria.provedores
CREATE TABLE IF NOT EXISTS `provedores` (
  `id_provedor` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `id_empresa_provedor` int(11) unsigned NOT NULL,
  `cedula_provedor` varchar(20) DEFAULT NULL,
  `nombres_provedor` varchar(50) DEFAULT NULL,
  `apellidos_provedor` varchar(50) DEFAULT NULL,
  `telefono_provedor` varchar(20) DEFAULT NULL,
  `direccion_provedor` varchar(50) DEFAULT NULL,
  `sexo_provedor` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_provedor`),
  KEY `FK_provedores_empresa` (`id_empresa_provedor`),
  CONSTRAINT `FK_provedores_empresa` FOREIGN KEY (`id_empresa_provedor`) REFERENCES `empresa` (`id_empresa`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla papeleria.provedores: ~20 rows (aproximadamente)
/*!40000 ALTER TABLE `provedores` DISABLE KEYS */;
INSERT IGNORE INTO `provedores` (`id_provedor`, `id_empresa_provedor`, `cedula_provedor`, `nombres_provedor`, `apellidos_provedor`, `telefono_provedor`, `direccion_provedor`, `sexo_provedor`) VALUES
	(1, 1, '9119852185', 'Ilyssa', 'Olliver', '9674812199', '72081 Mcbride Pass', 'F'),
	(2, 1, '0546415962', 'Ollie', 'Haldane', '3845879394', '205 Heath Point', 'F'),
	(3, 4, '8855433350', 'Wendy', 'Pirrone', '8515344866', '0153 Derek Alley', 'F'),
	(4, 3, '2982446340', 'Diarmid', 'Pulster', '0595934242', '9 Mifflin Pass', 'M'),
	(5, 3, '3769337336', 'Weider', 'Glasper', '7675656660', '21867 Wayridge Center', 'M'),
	(6, 1, '6447541051', 'Chev', 'Tanman', '9337643340', '142 Oakridge Trail', 'M'),
	(7, 3, '2235412246', 'Warde', 'Pinchbeck', '3592463306', '76957 Rusk Court', 'M'),
	(8, 2, '9706202315', 'Andie', 'Montez', '1660981476', '978 Glendale Way', 'M'),
	(9, 1, '2328055192', 'Angel', 'Ridout', '3183738775', '52 Grover Crossing', 'F'),
	(10, 2, '1124993606', 'Mel', 'Fox', '8075024354', '0 Golf View Terrace', 'F'),
	(11, 2, '7052828553', 'Barret', 'Babin', '0661530752', '32 Green Drive', 'M'),
	(12, 4, '9579690146', 'Anjela', 'Caldaro', '7955356594', '5932 Corry Park', 'F'),
	(13, 4, '5825024603', 'Pammi', 'Wasiela', '6986401949', '144 Mockingbird Trail', 'F'),
	(14, 3, '0274920476', 'Vin', 'Jenkyn', '3286896152', '32 Hazelcrest Terrace', 'F'),
	(15, 4, '9688337552', 'El', 'Servante', '5243102423', '4 Buell Court', 'M'),
	(16, 3, '7903036580', 'Alfonso', 'Menat', '8086740005', '5 Hintze Plaza', 'M'),
	(17, 3, '3715378409', 'Galvan', 'Hoofe', '1226590292', '15975 Surrey Alley', 'M'),
	(18, 1, '9238098646', 'Cornelia', 'Seedman', '1287743579', '1 Fair Oaks Parkway', 'F'),
	(19, 3, '9078200332', 'Nikolai', 'Vader', '0374469210', '5 Welch Street', 'M'),
	(20, 4, '5423977878', 'Angelia', 'Woollam', '0779056442', '108 Mcbride Crossing', 'F');
/*!40000 ALTER TABLE `provedores` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
