-- Volcando estructura para tabla flask_mvc.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `Precio_venta` float(8,2) NOT NULL DEFAULT 0.00,
  `Precio_compra` float(8,2) NOT NULL DEFAULT 0.00,
  `ganancia` float(8,2) NOT NULL DEFAULT 0.00,
  `estado` text NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla flask_mvc.productos: ~7 rows (aproximadamente)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` (`id`, `nombre`, `descripcion`, `Precio_venta`, `Precio_compra`, `ganancia`, `estado`) VALUES
	(44, 'Papas', 'fritas', 1300.00, 53.00, 2000.00, 'Activo'),
	(45, 'Pony', 'Gaseosa', 1300.00, 23.00, 1600.00, 'Inactivo'),
	(47, 'arroz', 'grano', 2500.00, 2000.00, 25.00, 'Activo'),
	(48, 'Jabon', 'lavar ropa', 1500.00, 1000.00, 50.00, 'Inactivo'),
	(49, 'cambio_gaseosa', 'crud', 1000.00, 50.00, 1500.00, 'Activo'),
	(51, 'prueba', 'add', 40000.00, 30000.00, 33.00, 'Activo'),
	(52, 'carne', 'de cerdo', 20100.00, 15000.00, 34.00, 'Activo');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
