## Practica 8. WebScraping.

El objetivo de esta práctica es aprender a desarrollar scripts en Python que filtren la información de páginas web. 

En [scrap1](./scrap1.py) el script se realiza una solicitud GET a una URL utilizando requests y luego imprime el contenido HTML de la respuesta.

En [scrap2](./scrap2.py)  el script se realiza una solicitud HTTP a una página web, analiza su contenido HTML y encuentra un elemento específico. Luego, imprime el contenido HTML de ese elemento con un formato mejorado.

En [scrap3](./scrap3.py) el script se realiza una solicitud HTTP a una página web, analiza su contenido HTML y encuentra todos los elementos con la clase "card-content". Luego, imprime cada uno de estos elementos.

En [scrap4](./scrap4.py) el script se realiza una solicitud HTTP a una página web, analiza su contenido HTML y encuentra elementos específicos dentro de él. Luego, imprime los elementos encontrados.


En [scrap5](./scrap5.py) el script se realiza una solicitud HTTP a una página web y analiza su contenido HTML. Luego, extrae información específica, como el título, la empresa y la ubicación de trabajos, de los elementos HTML que tienen la clase "card-content". Luego, imprime esta información.


En [scrap6](./scrap6.py) el script se realiza una solicitud HTTP a una página web, analiza su contenido HTML y encuentra los elementos con la clase "card-content". Luego, extrae el título, la empresa y la ubicación de cada elemento y los imprime.

En [scrap7](./scrap7.py) el script se ealiza una solicitud HTTP a una página web, analiza su contenido HTML y cuenta la cantidad de elementos h2 que contienen la palabra "python" en su texto. Luego, imprime la cantidad de elementos encontrados.

En [scrap8](./scrap8.py) el script se realiza una solicitud HTTP a una página web, analiza su contenido HTML y busca los elementos h2 que contienen la palabra "python" en su texto. Luego, obtiene información adicional de esos elementos, como el título, la empresa y la ubicación, y los imprime.

En [scrap9](./scrap9.py) el script se realiza una solicitud HTTP a una página web, analiza su contenido HTML y busca los trabajos que contengan la palabra "python" en su título. Luego, extrae información relevante de estos trabajos, como la empresa, la ubicación y el título, y muestra la información, junto con el enlace de solicitud de empleo.

En [scrap10](./scrap10.py) el script se imprime el nombre de la empresa, la ubicación y el título del trabajo, seguido de los enlaces adicionales encontrados en cada trabajo, junto con su texto y URL

En [scrap11](./scrap11.py) el script se buscarán los elementos que contengan la clase "card-content" y el texto "python" en el elemento h2. Luego, se obtendrán el título, la empresa, la ubicación y los enlaces adicionales para cada trabajo y se mostrarán en la salida.

En [scrap12](./scrap12.py) el script extrae información de trabajos de la página web de una pagina web de fake-jobs que contienen la palabra "python" en su título. Cada trabajo se muestra con el nombre de la empresa, la ubicación, el título del trabajo y un enlace para aplicar.

En [scrap_quote](./scrape_quote.py) se analiza la información de un archivo HTML, se extrae información con la cual se crean dos listas, una que contiene las citas, la otra contiene los autores y con las listas se crea un archivo cvs.