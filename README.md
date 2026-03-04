# Proyecto DUA StreamLiner
El problema al que esta orientado este proyecto es el resolver los tramites pertinentes del llenado del DUA. La intención propiamente es desarrollar un sistema automatizado que permita a importadores y exportadores simplificar drásticamente el proceso de elaboración del DUA.

## Integrantes 
 * Isaac Villalobos Bonilla, 2024124285
 * Christopher Daniel Vargas Villalta, 2024108443
   
Caso 1 de Diseño de Software. 

---
## Flujo de trabajo
- Paso 0. El usuario elige si quiere hacer el trámite de exportación o importación (importante para saber cuál plantilla usar y qué campos serán obligatorios).
- Paso 1. Se tiene un archivo "plantilla oficial vigente del DUA" definido por el Ministerio de Hacienda y otros "n" archivos (pueden ser excel, word, pdf, imágenes) en un folder path (variable de entorno).
- Paso 2.Separar archivos en 4 categorías: Imagen, Excel, Word, PDF, Adicionalmente, antes de cualquier embedding, se realiza una clasificación temática del archivo completo, por ejemplo: Factura comercial, Documento de transporte, Certificado de origen, Packing list, Documento financiero, Otro. Esto permitirá restringir búsquedas posteriores por tipo de documento y evitar comparación exhaustiva innecesaria.
- Paso 3. Revisar si la versión de la plantilla usada para el hash de comparación sigue siendo la más actualizada. Si no es así, hacer el paso 3.1.
- Paso 3.1. Recorrer la plantilla usando división en bloques mediante embedding y guardar las secciones encontradas en un hash para comparación posterior. Cada bloque tendrá: hash del bloque, embedding, tipo de campo esperado, reglas de validación, tipo de renderizado (texto, tabla, código, condicional).
- Paso 4. Se recorren los archivos Word mediante división por bloques y embedding. Antes de comparar contra toda la plantilla: Se indexan los bloques en una estructura tipo vector store por categoría documental. De esta manera funciona como un indice invertido, si ocupas - pais de origen sabes que debes buscar en certificado de origen.
- Paso 5. Se realiza el mismo proceso para archivos Excel y PDF, considerando sus particularidades estructurales.
- Paso 6. Se realiza el mismo proceso para imágenes mediante OCR avanzado.
- Paso 7. Mediante modelos de IA entrenados para comprender terminología aduanera, el sistema identificará y clasificará automáticamente dentro de cada bloque los siguientes campos clave: Datos del importador/exportador, Información del proveedor, Descripción comercial y arancelaria de mercancías, Cantidades, pesos y valores FOB/CIF, Incoterms, Información de transporte, Número y fecha de factura, País de origen y procedencia, Régimen aduanero aplicable.  Una vez se extrae el campo se hace una validacion sintactica sabiendo que el pais sea valido, fecha valida, etc. 

- Paso 8. Se eligen los 2 textos con mayor porcentaje de similitud, tomando en cuenta la categoría documental mediante clasificación one-hot encoding. Estos serán enviados a una API de IA para determinar: Qué parte específica del DUA será llenada con ese bloque. Porcentaje de seguridad. 

**Escala de advertencia**
x ≤ 30% → Advertencia roja
30% < x ≤ 70% → Advertencia amarilla
x > 70% → Advertencia verde

- Paso 9. Se debe considerar que tipo de campo debe llenar (texto, si hay un codigo obligatorio, tabla dinamica), el formato (de las fechas, conversion de unidades), motor de reglas tomando en cuenta si tiene "x" ocupa seccion "y", despues hacer la generacion estructurada del documento respetando layout original (tendra un color dependiendo de la confianza)
- Paso 10. Para el control de reprocesamiento y optimización de costos, Para evitar reprocesar todo cuando se agregan o corrigen archivos se tendra que cada bloque guarde hash del bloque y embedding, cuando se agrega un archivo se calcula el hash y compara con existentes, si ya existe se reusa el embedding.
---

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

---

**Diseños de soluciones hechas que hagan algo similar**
En Costa Rica no hay actualmente soluciones de este estilo, pero en diferentes paises hay similutes para el llenado automatico de documentos de aduanas.

1. ACE Secure Data Portal: https://ace.cbp.gov/s/login/?ec=302&startURL=%2Fs%2F
La plataforma oficial de EE. UU. para carga electrónica de datos aduaneros. Todos los datos comerciales (incluyendo declaraciones de importación) se ingresan por aquí.
Permite subir datos estructurados para entrada de mercancías, ISF 10+2, entre otros.

