# Datos y scripts de elecciones particulares

Este repositorio contiene datos de elecciones. Algunos de los archivos
son dumps de los sitios oficiales de escrutinios provisorios, mientras
que otros son dumps de bases de datos de [Escrutinio
Social](https://github.com/EscrutinioSocial/escrutinio-social).


## Nacionales

### 2019

  * `muchos_votos.dump` tiene los votos de las PASO nacional 2019 (?)

## Córdoba

  * `ubicaciones.json` mesas y lugares de votación de toda la provincia. No
  tiene información georefenciada.

### 2019

  * `gobernador-cordoba-2019-provisorio-por-mesas.csv` dump de
    datosoficiales.com.ar correspondiente a las elecciones de
    gobernador.

  * `intendente-cordoba-2019-provisorio-por-mesas.csv` dump de
    datosoficiales.com.ar correspondiente a las elecciones de intendente de
	Córdoba capital.



# Scripts

  * `import-intendente-datos-oficiales-com-ar.1.py`, scrapper de datos oficiales
  para intendente de Córdoba capital.
  * `import-gobernador-datos-oficiales-com-ar.py`, lo mismo pero para gobernador
  de Córdoba.
