CREATE DATABASE practicas_pro
USE practicas_pro

CREATE TABLE ofertas(
	id_oferta int identity primary key,
	nombre_empresa nvarchar (100),
	carrera nvarchar(50),
	descripcion nvarchar(MAX),
	requisitos nvarchar(MAX),
	fecha_limit nvarchar(10),
	ciudad nvarchar(50),
	direccion nvarchar (250),
	correo nvarchar(100)
)


INSERT INTO ofertas(nombre_empresa,carrera,descripcion,requisitos,fecha_limit,ciudad,direccion,correo) -- Ingenieria electrica
VALUES ('Mazda','Ingenieria Electrica','Practicante en Manufactura','Disponibilidad de 6 meses, cursar el último semestre, seguro facultativo, no adeudo de materias, Promedio minimo de 8','NA','Salamanca','Av. Hiroshima 1000, Complejo Industrial Salamanca','talento.mail@mx.mazda.mx'),
		('Nucor-JFE Steel México (NJSM)','Ingenieria Electrica','Mantenimiento eléctrico','Estudiantes próximos a graduarse,  inglés preferible, Contar con seguro facultativo (Indispensable), Disponibilidad para trabajar en planta en días laborales','NA','Silao','Ejido Menores, Prol. Paseo de Los Industriales Norte No. 2200','daniela.segura@nucor.com')


INSERT INTO ofertas(nombre_empresa,carrera,descripcion,requisitos,fecha_limit,ciudad,direccion,correo) -- Ingenerieria electronica
VALUES ('Mazda','Ingenieria Electronica','Practicante en Manufactura','Disponibilidad de 6 meses, cursar el último semestre, seguro facultativo, no adeudo de materias, Promedio minimo de 8','NA','Salamanca','Av. Hiroshima 1000, Complejo Industrial Salamanca','talento.mail@mx.mazda.mx')


INSERT INTO ofertas(nombre_empresa,carrera,descripcion,requisitos,fecha_limit,ciudad,direccion,correo) -- Ingenieiria Sistemas comp.
	VALUES ('CIE Pemsa','Ingenieria Sistemas Comp.','Practicante en Tecnologias de la Informacion','Estar cursando el ultimo año de la carrera, disponibilidad de horario, contar cn seguro facultativo','NA','Celaya','Carretera Celaya - Salamanca Km. 5, Poniente, Zona Industrial','estefania.diezmarina@cieautomotive.mx'),
			('Mazda','Ingenieria Sistemas Comp.','Practicante en Tecnologias de la Informacion','Disponibilidad de 6 meses, Cursar el último semestre, Seguro facultativo, No adeudo de materias, Promedio minimo de 8','NA','Salamanca','Av. Hiroshima 1000, Complejo Industrial Salamanca','talento.mail@mx.mazda.mx'),
			('Nucor-JFE Steel México (NJSM)','Ingenieria Sistemas Comp.','Practicante en Mantenimiento','Estudiantes próximos a graduarse,  inglés preferible, Contar con seguro facultativo (Indispensable), Disponibilidad para trabajar en planta en días laborales, Comprensión de la programación en lenguaje C++ y C-Chart','NA','Silao','Ejido Menores, Prol. Paseo de Los Industriales Norte No. 2200','daniela.segura@nucor.com'),
			('DENSO','Ingenieria Sistemas Comp.','Practicante de Sistemas','Ser estudiante vigente, disponibilidad de horario, seguro facultativo vigente','NA','Silao','Boulevard Mineral de Peñafiel, Guanajuato Puerto Interior #330,','diana.montero@na.denso.com'),
			('Flecha Amarilla','Ingenieria Sistemas Comp.','Practicante en Desarrollo de Software','Ser estudiante activo de una carrera universitaria afin a la tecnologia, contar con conociminetos basicos o intermedios en programación, disponibilidad de tiempo, firma de convenio de persona fisica','31/03/2025','Leon','Blvd. la Luz 2011, Killian, 37270','ev.ayala@flecha-amarilla.com'),
			('Amber Mexico','Ingenieria Sistemas Comp.','Practicante en Desarrollo de Videojuegos','Ser estudiante activo de una universidad publica, tener disponibilidad de horario, contar con el respaldo de la institución edicativa','05/06/2025','Guadalajara','C. Independencia 55, Zona Centro, 44100','maria.murillo@amberstudio.com')



INSERT INTO ofertas(nombre_empresa,carrera,descripcion,requisitos,fecha_limit,ciudad,direccion,correo) -- Ingnieria mecanica 
VALUES ('CIE Pemsa','Ingeniería Mecánica','Practicante en Mecanica','Estar cursando el ultimo año de la carrera, disponibilidad de horario, contar cn seguro facultativo','NA','Celaya','Carretera Celaya - Salamanca Km. 5, Poniente, Zona Industrial','estefania.diezmarina@cieautomotive.mx'),
		('Mazda','Ingenieria Mecanica','Practicante en Manufactura','Disponibilidad de 6 meses, cursar el último semestre, seguro facultativo, no adeudo de materias, Promedio minimo de 8','NA','Salamanca','Av. Hiroshima 1000, Complejo Industrial Salamanca,','talento.mail@mx.mazda.mx'),
		('Nucor-JFE Steel México (NJSM)','Ingenieria Mecanica','Practicante en Mantenimiento Mecánico','Estudiantes próximos a graduarse,  inglés preferible, Contar con seguro facultativo (Indispensable), Disponibilidad para trabajar en planta en días laborales, Comprensión de la programación en lenguaje C++ y C-Chart','NA','Silao','Ejido Menores, Prol. Paseo de Los Industriales Norte No. 2200','daniela.segura@nucor.com')


INSERT INTO ofertas(nombre_empresa,carrera,descripcion,requisitos,fecha_limit,ciudad,direccion,correo) -- Ingenieiria mecatronica
VALUES ('CIE Pemsa','Ingeniería Mecatrónica','Practicante en Mecatronica','Estar cursando el ultimo año de la carrera, disponibilidad de horario, contar cn seguro facultativo','NA','Celaya','Carretera Celaya - Salamanca Km. 5, Poniente, Zona Industrial','estefania.diezmarina@cieautomotive.mx'),
		('Mazda','Ingenieria Mecatrónica','Practicante en Manufactura','Disponibilidad de 6 meses, cursar el último semestre, seguro facultativo, no adeudo de materias, Promedio minimo de 8','NA','Salamanca','Av. Hiroshima 1000, Complejo Industrial Salamanca,','talento.mail@mx.mazda.mx'),
		('DENSO','Ingenieria Mecatrónica','Practicante de Procesos','Ser estudiante vigente, disponibilidad de horario, seguro facultativo vigente','NA','Silao','Boulevard Mineral de Peñafiel, Guanajuato Puerto Interior #330,','diana.montero@na.denso.com')
		


INSERT INTO ofertas(nombre_empresa,carrera,descripcion,requisitos,fecha_limit,ciudad,direccion,correo) -- Gestion empresarial
	VALUES ('CIE Pemsa','Licenciatura en Gestión Empresarial','Practicante en Gestion Empresarial','Estar cursando el ultimo año de la carrera, disponibilidad de horario, contar cn seguro facultativo','NA','Celaya','Carretera Celaya - Salamanca Km. 5, Poniente, Zona Industrial','estefania.diezmarina@cieautomotive.mx'),
			('Mazda','Licenciatura en Gestión Empresarial','Practicante en Recursos Humanos','Disponibilidad de 6 meses, cursar el último semestre, seguro facultativo, no adeudo de materias, Promedio minimo de 8','NA','Salamanca','Av. Hiroshima 1000, Complejo Industrial Salamanca,','talento.mail@mx.mazda.mx')


INSERT INTO ofertas(nombre_empresa,carrera,descripcion,requisitos,fecha_limit,ciudad,direccion,correo) -- Artes Digitales
VALUES ('Mazda','Licenciatura en Artes Digitales','Practicante en Relaciones Publicas','Disponibilidad de 6 meses, cursar el último semestre, seguro facultativo, no adeudo de materias, Promedio minimo de 8','NA','Salamanca','Av. Hiroshima 1000, Complejo Industrial Salamanca,','talento.mail@mx.mazda.mx')



SELECT nombre_empresa, descripcion, requisitos, fecha_limit, ciudad, direccion, correo FROM ofertas 
WHERE carrera = 'Ingenieria Sistemas Comp.'


SELECT nombre_empresa, ciudad FROM ofertas 
WHERE carrera = 'Ingenieria Sistemas Comp.'