# ¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año?

SELECT a.id_aeropuerto, e.nombre_aeropuerto, count(*) as Mov_anual
FROM tabla_vuelos a
INNER JOIN aeropuertos e
ON a.id_aeropuerto = e.idaeropuerto
GROUP BY e.nombre_aeropuerto
ORDER BY Mov_anual DESC, a.id_aeropuerto DESC



#¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante el año?


SELECT e.idaerolineas, e.nombre_aerolinea, count(*) as Num_vuelos
FROM aerolineas e
INNER JOIN tabla_vuelos a
ON a.id_aerolinea = e.idaerolineas
GROUP BY e.nombre_aerolinea
ORDER BY Num_vuelos DESC, e.idaerolineas DESC;


#¿En qué día se han tenido mayor número de vuelos?

SELECT dia, count(*) as vuelos_al_dia
FROM tabla_vuelos 
group by dia


#¿Cuáles son las aerolíneas que tienen mas de 2 vuelos por día?

SELECT  a. dia, b.nombre_aerolinea, count(*) as vuelos_al_dia
FROM tabla_vuelos a
INNER JOIN aerolineas b
ON a.id_aerolinea = b.idaerolineas
group by a.dia
HAVING COUNT(vuelos_al_dia) > 2


