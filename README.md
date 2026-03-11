# Proyecto DUA StreamLiner
The preparation of the Single Administrative Document (DUA) required for import and export procedures in Costa Rica is currently a largely manual task that demands significant time and attention. The information needed to complete the document is usually spread across several sources such as Excel files, Word documents, PDFs, and scanned images like invoices or certificates. Since these documents often come from different companies and follow varying structures and formats, extracting and organizing the required data becomes a complex process. This forces customs specialists to spend considerable time reviewing documents, interpreting information, and manually transferring data into the official DUA template, increasing the risk of mistakes or inconsistencies.

To improve this process, we propose the development of DUA Streamliner, a system designed to automate much of the work involved in generating the DUA. The system will allow users to simply provide a folder containing all related documents, which will then be processed using tools capable of reading different file formats, extracting text from PDFs, and applying OCR to scanned images. Through AI-based semantic analysis specialized in customs terminology, the system will detect relevant data such as importer details, product information, values, and transport data, and automatically place it into the corresponding fields of the official DUA template defined by the Ministry of Finance. The system will generate a pre-filled Word document and highlight fields that may require verification, enabling experts to focus mainly on reviewing and confirming the information rather than completing the document from scratch.

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

---

# 1. Frontend design

## 1.1 Technology stack 
Tecnología de frontend, de seguridad, librerías de terceros, frameworks, hosting; todos con su respectiva versión

- Application type: Server Side Rendering (SSR) Web App
- Web framework: ReactJS 19.2
- Web server: NodeJS 21
- Coding Language: TypeScript 5.9.3
- Unit testing framework: Jest 30.2.0
- Data validation framework: Zod 3.23.8
- Code prettier framework: Prettier 3.3.3
- Code style framework: ESLint 9.18.0
- Integration testing tools: Playwright 1.58.2
- Cloud service: Google Cloud Platform
- Hosted services within the cloud service: Google App Engine
- Code repositories service: GitHub
- Code automation task tool: GitHub Actions
- CI CD pipelines technology: GitHub Actions
- Environments: Development, Stage, Production
- Environment deployments tools: GitHub Environments
- Observability framework: Google Cloud Operations Suite (Cloud Logging + Cloud Monitoring)
  
## 1.2 UX UI analysis
Incluye los atributos de usabilidad deseables del aplicativo, un diseño preliminar del UX a modo wireframes, y las evidencias de las pruebas de UX con usuarios reales que validan diseño diseño preliminar

### Core Bussines Proccesses 
Describir lo que sucede paso a paso en cada pantalla en terminos de acciones (no hablen de botones, ni listas ni de ningun componente visua, solo acciones de usuario y el resultado de cada accion)

#### Login
1. The user enters their login identifier, password, and one-time authentication token.
2. The system validates the provided credentials and the token.
3. If the credentials are incorrect, the system rejects the authentication attempt and informs the user that the username or password is invalid.
4. If the credentials are valid, the system authenticates the user and grants access to the system.
5. After successful authentication, the user proceeds to the generator configuration stage.

**Imagen de Login**

![Imagen del Login](Images/LoginScreen.png)


#### Configurar el generador
1. The user specifies whether the declaration corresponds to an import or export process.
2. The user provides the folder path that contains the documents required for the process.
3. The user starts the automated generation process.

**Imagen del Generator**

![Imagen del Generator](Images/GeneratorConfiguration.png)

#### Monitoreo del avance
1. The user checks the status of the generation process.
2. The user can repeatedly check the process status until the generation is completed.
3. Once the process finishes, the system informs the user that the result is available.

**Imagen del Monitoreo**

![Imagen del Monitoreo](Images/ProgressMonitoring.png)

#### Obtencion del resultado
1. The user requests the generated DUA document.
2. The system provides the completed DUA document generated from the processed information and informs the user.
3. The user reviews the generated document and verifies the extracted information and confidence levels.
4. If the user identifies incorrect or incomplete information, the user modifies the corresponding data.
5. The user confirms the final version of the generated DUA document for further use.
6. The user downloads the final version of the DUA document.

**Imagen del Resultado**

![Imagen del Resultado](Images/ResultRetrieval.png)

#### Logout
1. The user decides to end the session.
2. The user is returned to the authentication stage and no longer has access to the system.

**Imagen del Logout**

![Imagen del Logout](Images/LogoutConfirmation.png)


### UX test results
En este apartado encontraremos los resultados del test de UX sobre los wireframes usados anteriormente. Las tecnologias que se utilizaron para esto fueron Figma Make y Maze.

| Pregunta | Tipo | Participante 1 (509270528) | Participante 2 (509834609) | Participante 3 (509831198) | Participante 4 |
|----------|------|:-------------------------:|:-------------------------:|:-------------------------:|:--------------:|
| ¿Hubo algún elemento que no entendió para qué servía? | Pregunta abierta | Nada, todo bien | Muy útil IA | No | |
| ¿Los botones que tiene el sistema les pareció clara su función? | Selección múltiple | Bien clara | Bien clara | Bastante clara | |
| ¿Qué tan intuitivo le pareció el sistema? (1-5) | Escala de opinión | 5 | 5 | 4 | |
| ¿Del 1 al 10 qué tan fácil considera aprender a usar el sistema? | Escala de opinión | 8 | 8 | 9 | |
| ¿Recomendaría este sistema para la automatización del DUA? | Sí/No | ✅ Sí | ✅ Sí | ✅ Sí | |

#### HeatMaps

#### Evidencias


- Escoger alguna app para ejecutar el UX test usando esos wireframes.
- El test se lo van a aplicar en forma remota compartiendo un URL  a 3 estudiantes o amigos
- Eso va a generar un reporte de resultados
- Crear un markdown table con los resultados
- Evidencias
- Screenshots de cada persona que los testeo 

## 1.3 Component design strategy
Define la técnica y los principios de diseño de componentes del frontend, cómo se logra la reutilización de componentes, cómo se logra centralizar los estilos, el branding, la internacionalización y la responsividad.

## 1.4 Security
Tecnologías, técnicas y classes con su respectiva ubicación en la estructura del proyecto responsables de la autenticación y la autorización de permisos y sesiones. 

## 1.5 Layered design
diseño y explicación de las diversas capas de la aplicación en el frontend. 

## 1.6  Design patterns
Diseño de classes con su respectiva ubicación en la estructura del proyecto, donde sea necesario aplicar patrones de diseño orientado a objetos, como por ejemplo: seguridad, refrescado de UI, recepción de notificaciones, almacenamiento de estados, llamadas a api, operaciones asíncronas, invalidación de sesiones, programación por eventos, creación de objetos. 

## 1.7 un folder en /src que contiene el scaffold del proyecto, el cual se genera a partir de toda la especificación de los puntos del 1.1 al 1.6. 

Otros aspectos
- Todo debe hacerse en inglés
- Respete la nomenclatura de Markdown, sus niveles y formatos
- Evite ser verboso o llenar esta documentación de diseño técnico, con narrativas que no aportan valor al diseño
- Recuerde que el lector final de un diseño es el equipo de desarrollo del sistema y bien agentes de AI que van a crear el proyecto base, por ende evite explicaciones innecesarias

--- 

# 2. Backend design 

# 3. Data Design

