-- SQLite
PRAGMA table_info(estados_municipio);

SELECT * FROM estados_estado;

INSERT INTO estados_estado (id, nombre, habitantes, region) VALUES
(1, 'Aguascalientes', 1434631, 'Centro'),
(2, 'Baja California', 3769020, 'Noroeste'),
(3, 'Baja California Sur', 798447, 'Noroeste'),
(4, 'Campeche', 928363, 'Sureste'),
(5, 'Chiapas', 5543828, 'Sureste'),
(6, 'Chihuahua', 3899382, 'Norte'),
(7, 'Ciudad de México', 9209944, 'Centro'),
(8, 'Coahuila', 3146771, 'Norte'),
(9, 'Colima', 731391, 'Occidente'),
(10, 'Durango', 1944792, 'Norte'),
(11, 'Estado de México', 17427750, 'Centro'),
(12, 'Guanajuato', 6375036, 'Centro-Occidente'),
(13, 'Guerrero', 3533251, 'Sur'),
(14, 'Hidalgo', 3167562, 'Centro'),
(15, 'Jalisco', 8570409, 'Occidente'),
(16, 'Michoacán', 4882032, 'Occidente'),
(17, 'Morelos', 2004396, 'Centro'),
(18, 'Nayarit', 1360301, 'Occidente'),
(19, 'Nuevo León', 5784442, 'Norte'),
(20, 'Oaxaca', 4341944, 'Sur'),
(21, 'Puebla', 6606229, 'Centro'),
(22, 'Querétaro', 2416810, 'Centro'),
(23, 'Quintana Roo', 1977403, 'Sureste'),
(24, 'San Luis Potosí', 2899582, 'Centro-Norte'),
(25, 'Sinaloa', 3212157, 'Noroeste'),
(26, 'Sonora', 3101849, 'Noroeste'),
(27, 'Tabasco', 2443708, 'Sureste'),
(28, 'Tamaulipas', 3793401, 'Norte'),
(29, 'Tlaxcala', 1342977, 'Centro'),
(30, 'Veracruz', 8008208, 'Golfo'),
(31, 'Yucatán', 2361054, 'Sureste'),
(32, 'Zacatecas', 1645357, 'Centro-Norte');


INSERT INTO estados_municipio (id, nombre, habitantes, estado_id) VALUES
-- Aguascalientes (1)
(1, 'Aguascalientes', 934424, 1),
(2, 'Jesús María', 130000, 1),
(3, 'Calvillo', 56000, 1),
(4, 'Rincón de Romos', 48000, 1),
(5, 'Pabellón de Arteaga', 46000, 1),

-- Baja California (2)
(6, 'Tijuana', 2000000, 2),
(7, 'Mexicali', 1100000, 2),
(8, 'Ensenada', 522000, 2),
(9, 'Tecate', 110000, 2),
(10, 'Playas de Rosarito', 130000, 2),

-- Baja California Sur (3)
(11, 'La Paz', 300000, 3),
(12, 'Los Cabos', 350000, 3),
(13, 'Comondú', 74000, 3),
(14, 'Loreto', 21000, 3),
(15, 'Mulegé', 59000, 3),

-- Campeche (4)
(16, 'Campeche', 300000, 4),
(17, 'Ciudad del Carmen', 220000, 4),
(18, 'Champotón', 83000, 4),
(19, 'Escárcega', 60000, 4),
(20, 'Calkiní', 50000, 4),

-- Chiapas (5)
(21, 'Tuxtla Gutiérrez', 600000, 5),
(22, 'San Cristóbal de las Casas', 200000, 5),
(23, 'Tapachula', 350000, 5),
(24, 'Palenque', 150000, 5),
(25, 'Comitán de Domínguez', 160000, 5),

-- Chihuahua (6)
(26, 'Chihuahua', 950000, 6),
(27, 'Ciudad Juárez', 1500000, 6),
(28, 'Delicias', 150000, 6),
(29, 'Cuauhtémoc', 170000, 6),
(30, 'Parral', 110000, 6),

-- Ciudad de México (7)
(31, 'Álvaro Obregón', 750000, 7),
(32, 'Iztapalapa', 1820000, 7),
(33, 'Coyoacán', 620000, 7),
(34, 'Miguel Hidalgo', 370000, 7),
(35, 'Tlalpan', 700000, 7),

-- Coahuila (8)
(36, 'Saltillo', 880000, 8),
(37, 'Torreón', 800000, 8),
(38, 'Monclova', 250000, 8),
(39, 'Piedras Negras', 170000, 8),
(40, 'Acuña', 180000, 8),

-- Colima (9)
(41, 'Colima', 150000, 9),
(42, 'Manzanillo', 185000, 9),
(43, 'Tecomán', 115000, 9),
(44, 'Villa de Álvarez', 150000, 9),
(45, 'Comala', 20000, 9),

-- Durango (10)
(46, 'Durango', 654000, 10),
(47, 'Gómez Palacio', 375000, 10),
(48, 'Lerdo', 170000, 10),
(49, 'Canatlán', 35000, 10),
(50, 'Pueblo Nuevo', 25000, 10);

SELECT * FROM estados_municipio;