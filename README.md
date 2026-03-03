# Proyecto DUA StreamLiner
El problema al que esta orientado este proyecto es el resolver los tramites pertinentes del llenado del DUA. La intención propiamente es desarrollar un sistema automatizado que permita a importadores y exportadores simplificar drásticamente el proceso de elaboración del DUA.

## Integrantes 
 * Isaac Villalobos Bonilla, 2024124285
 * Christopher Daniel Vargas Villalta, 2024108443
   
Caso 1 de Diseño de Software. 

---
### Flujo de trabajo
- Paso 1. Tiene un archivo "plantilla oficial vigente del DUA" definido por el ministerio de hacienda y otros "n" archivos (puede ser excel, word, pdf, imagenes) en un folder path (variable de entorno).
- Paso 2. Separar archivos en 4 categorias (imagen, excel, word, pdf).
- Paso 3. Revisar si la version de la plantilla usada para el hash de comparacion sigue siendo la más actualizada, si no es asi hacer el paso 3.1. para actualizarla.
- Paso 3.1. Recorrer la plantilla usando division en bloques, mediante embedding y se guarda las secciones encontradas en un hash para comparacion luego.
- Paso 4. Se recorren los archivos word (mediante division por bloques y embedding) y se compara las secciones con las de la plantilla (cada seccion tendra simitud de palabras con sentence berte) y se guarda en un diccionario la seccion, porcentaje de similitud y el bloque de textro)
- Paso 5. Se realiza el mismo proceso para los archivos excel, pdf pero con las distinciones de formato.
- Paso 6. Se realiza el mismo proceso para las imagenes mediante OCR avanzado.
- Paso 7. Adicionalmente, mediante modelos de IA entrenados para comprender terminología aduanera, el sistema identificará y clasificará automáticamente dentro de cada bloque los siguientes campos clave:
Datos del importador/exportador

-- Información del proveedor
-- Descripción comercial y arancelaria de mercancías
-- Cantidades, pesos y valores FOB/CIF
-- Incoterms
-- Información de transporte
-- Número y fecha de factura
-- País de origen y procedencia
-- Régimen aduanero aplicable

De esta manera, no solo se realiza una comparación estructural por similitud semántica, sino también una extracción de información para el llenado automatizado del documento aduanero.

- Paso 8. Se eligen 2 textos con mayor porcentaje de similud, tomando en cuenta a que categoria pertenecen mediante una clasificacion one-hot encoding que seran enviados a una api de IA para elegir que parte del documento será llenado con ese bloque de datos y dará un porcentaje de seguridad (30% >= x ; advertencia al usuario tipo rojo, 30% < x <= 70% ; advetencia tipo amarillo, x > 70% ; advertencia color verde), guardando todo en el diccionario con formato {bloque al que matcheo en la plantilla: advertencia, datos del bloque}
- Paso 9. Se pone todos los valores del diccionario conforme a la plantilla y se avisa al usuario en cada elemento su porcentaje de seguridad.





### Links

**Documentos del llenado del DUA**
Aqui detalleremos algunos ejemplos de documentos necesarios para llenar el DUA.

Documentos fundamentales para el DUA:
* Factura Comercial: Detalla la transacción, partes implicadas, valor y moneda.
* Documento de Transporte: Dependiendo del medio, puede ser Bill of Lading (marítimo), Air Waybill (aéreo) o CMR (terrestre).
* Packing List (Lista de Contenido): Detalla el contenido, peso y bultos de la mercancía.
* Certificado de Origen: Certifica dónde se fabricó la mercancía (ej. EUR.1).
* Identificación (NIF/DNI/EORI): Del importador/exportador o su representante aduanero.
* Valor en Aduana (DV-1): Requerido si el valor supera ciertos límites para determinar impuestos.

En el caso de Costa Rica se especifica que a la agencia o agente de aduanas seleccionado  le debe llevar para el inicio de la importación los siguientes documentos: 
- Factura comercial
- B/L, Guía Aérea o carta de porte, dependiendo del medio de transporte por el cual se ha importado la mercancía
- Fotocopia de la cédula de identidad, pasaporte o cédula jurídica; según sea el caso. (Cámara de Comercio de Costa Rica, 2016, p.3).

Además de estos documentos, necesitará de la clasificación arancelaria de la mercancía, si cuenta con un agente aduanero él será el encargado de hacer la clasificación y verificar si requieren algún permiso para ser importados.  En caso de requerir algún permiso la agencia de aduanas puede solicitarlos a su nombre. Los permisos que se requieran dependerán del tipo de mercancía que desee importar. Los productos que necesitan de estos permisos según la Cámara de Comercio de Costa Rica (2016, p. 4) son:  
* Productos Ionizantes 
* Alimentos 
* Cosméticos y Medicamentos 
* Equipo e implementos Médicos Quirúrgicos 
* Estupefacientes, Sustancias Psicotrópicas, entre otros autorizados por ley 
* Plaguicidas de uso doméstico e industrial 
* Productos Naturales y Tisanas 
* Productos Químicos 

En general estos permisos se consiguen en su respectivo ministerio, por ejemplo, si se trata de cosméticos y medicamentos debe solicitar el permiso al Ministerio de Salud.  Según, la Cámara de Comercio de Costa Rica (2016, p. 3), una vez que se cuenten con los permisos (si se requieren) la Agencia o Agente de aduanas confeccionarán la Declaración Aduanera de Importación y la deberán presentar ante la Aduana por la cual ingresarán los productos.  

1. Instructivo: https://procomer.com/wp-content/uploads/2025/04/INSTRUCTIVO-DUAS-EXPORTACIONES-3.0.pdf
2. Casos de Uso en CR: https://piea.campus.co.cr/wp-content/uploads/2021/09/Gu%C3%ADa-Requisitos-b%C3%A1sicos-para-realizar-importaciones-y-exportaciones-en-Costa-Rica..pdf
3. Formato de Factura Comercial: https://www.scribd.com/document/458411170/factura-comercial
4. Modelo de Factura Comercial Llenada: https://www.slideshare.net/slideshow/modelo-de-factura-comercial-commercial-invoice-llenada/81392481
5. Documentos de Transporte Internacional: https://globalnegotiator.com/blog/documentos-de-transporte-internacional/
6. Bill of Landing: https://www.scribd.com/document/484317652/l-Documento-de-Transporte-Maritimo
7. Airway Bill: https://www.dripcapital.com/es-mx/recursos/blog/air-waybill-que-es
8. CMR: https://www.globalnegotiator.com/files/CMR-carta-de-porte-modelo-ejemplo.pdf
9. Packing List: https://www.scribd.com/document/649777725/FORMATO-PACKING-LIST-2022
10. Certificado de Origen: https://www.comex.go.cr/media/2481/01_anexo-316-certificado-de-origen.pdf
11. Certificado de Origen: https://www.docsity.com/es/docs/certificado-de-origen-1/5523092/
12. Valor en Aduana Ejemplo: https://www.scribd.com/doc/273864348/Hoja-de-Calculo-Para-Valor-en-Aduana

---

**Documentos DUA Llenados**
En este apartado incluimos links de documentos DUA llenos.

1. Instructivo Costa Rica - Ecuador: https://www.vuce.cr/wp-content/uploads/2024/04/Guia-de-llenado-CO-Ecuador.pdf
