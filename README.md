# Proyecto DUA StreamLiner
The preparation of the Single Administrative Document (DUA) required for import and export procedures in Costa Rica is currently a largely manual task that demands significant time and attention. The information needed to complete the document is usually spread across several sources such as Excel files, Word documents, PDFs, and scanned images like invoices or certificates. Since these documents often come from different companies and follow varying structures and formats, extracting and organizing the required data becomes a complex process. This forces customs specialists to spend considerable time reviewing documents, interpreting information, and manually transferring data into the official DUA template, increasing the risk of mistakes or inconsistencies.

To improve this process, we propose the development of DUA Streamliner, a system designed to automate much of the work involved in generating the DUA. The system will allow users to simply provide a folder containing all related documents, which will then be processed using tools capable of reading different file formats, extracting text from PDFs, and applying OCR to scanned images. Through AI-based semantic analysis specialized in customs terminology, the system will detect relevant data such as importer details, product information, values, and transport data, and automatically place it into the corresponding fields of the official DUA template defined by the Ministry of Finance. The system will generate a pre-filled Word document and highlight fields that may require verification, enabling experts to focus mainly on reviewing and confirming the information rather than completing the document from scratch.

## Authors
 * Isaac Villalobos Bonilla, 2024124285
 * Christopher Daniel Vargas Villalta, 2024108443
   
Project 1 Software Design. 

---
## Workflow
* Step 0. The user chooses whether they want to perform an export or import procedure (this is important to determine which template should be used and which fields will be mandatory).

* Step 1. There is a file called "current official DUA template" defined by the Ministerio de Hacienda and other "n" files (these may be Excel, Word, PDF, or images) located in a folder path (environment variable).

* Step 2. Separate the files into 4 categories: Image, Excel, Word, PDF. Additionally, before any embedding is performed, a thematic classification of the entire file is carried out, for example: Commercial invoice, Transport document, Certificate of origin, Packing list, Financial document, Other. This will allow restricting later searches by document type and avoid unnecessary exhaustive comparisons.

* Step 3. Check whether the version of the template used for the comparison hash is still the most updated one. If not, perform step 3.1.

* Step 3.1. Traverse the template using block division through embeddings and store the detected sections in a hash for later comparison. Each block will contain: block hash, embedding, expected field type, validation rules, rendering type (text, table, code, conditional).

* Step 4. Word files are traversed using block division and embeddings. Before comparing against the entire template: the blocks are indexed in a vector store–like structure by document category. In this way it works like an inverted index. For example, if you need country of origin, you know you must search in the certificate of origin.

* Step 5. The same process is performed for Excel and PDF files, considering their structural particularities.

* Step 6. The same process is performed for images using advanced OCR.

* Step 7. Through AI models trained to understand customs terminology, the system will identify and automatically classify within each block the following key fields: Importer/exporter data, Supplier information, Commercial and tariff description of goods, Quantities, weights and FOB/CIF values, Incoterms, Transport information, Invoice number and date, Country of origin and provenance, Applicable customs regime. Once the field is extracted, a syntactic validation is performed ensuring the country is valid, the date is valid, etc.

* Step 8. The 2 texts with the highest similarity percentage are selected, taking into account the document category through one-hot encoding classification. These will be sent to an AI API to determine: Which specific part of the DUA will be filled with that block. Confidence percentage.

##### Warning scale

- x ≤ 30% → Red warning
- 30% < x ≤ 70% → Yellow warning
- x > 70% → Green warning

* Step 9. It must be considered what type of field needs to be filled (text, if there is a required code, dynamic table), the format (date formats, unit conversion), a rule engine considering that if it has "x" it requires section "y", then perform the structured generation of the document respecting the original layout (it will have a color depending on the confidence).

* Step 10. For reprocessing control and cost optimization, to avoid reprocessing everything when files are added or corrected, each block will store the block hash and embedding. When a file is added, the hash is calculated and compared with existing ones; if it already exists, the embedding is reused.

---

### Links

**Documents Required for Completing the DUA**
Here we will detail some examples of documents required to complete the DUA.

Fundamental documents for the DUA:
* Commercial Invoice: Details the transaction, involved parties, value, and currency.
* Transport Document: Depending on the transport method, it may be a Bill of Lading (maritime), Air Waybill (air), or CMR (land).
* Packing List: Details the contents, weight, and packages of the goods.
* Certificate of Origin: Certifies where the goods were manufactured (e.g., EUR.1).
* Identification (NIF/DNI/EORI): From the importer/exporter or their customs representative.
* Customs Value (DV-1): Required if the value exceeds certain thresholds to determine taxes.

In the case of Costa Rica, it is specified that the selected customs agency or customs broker must be provided with the following documents to initiate the import process:
- Commercial invoice
- B/L, Air Waybill, or waybill, depending on the transport method used to import the goods
- Photocopy of the identity card, passport, or legal entity ID, depending on the case. (Cámara de Comercio de Costa Rica, 2016, p.3).

In addition to these documents, the tariff classification of the goods will be required. If you have a customs broker, they will be responsible for performing the classification and verifying whether any permits are required for the goods to be imported. If any permit is required, the customs agency can request them on your behalf. The permits required will depend on the type of goods you wish to import. According to the Cámara de Comercio de Costa Rica (2016, p.4), the products that require such permits are:

* Ionizing products
* Food products
* Cosmetics and medicines
* Medical surgical equipment and instruments
* Narcotics, psychotropic substances, among others authorized by law
* Domestic and industrial pesticides
* Natural products and herbal infusions
* Chemical products

In general, these permits are obtained from the corresponding ministry. For example, if the goods are cosmetics or medicines, the permit must be requested from the Ministry of Health. According to the Cámara de Comercio de Costa Rica (2016, p.3), once the permits are obtained (if required), the customs agency or broker will prepare the Import Customs Declaration and submit it to the Customs office through which the goods will enter.

1. Instructions: https://procomer.com/wp-content/uploads/2025/04/INSTRUCTIVO-DUAS-EXPORTACIONES-3.0.pdf
2. Use Cases in Costa Rica: https://piea.campus.co.cr/wp-content/uploads/2021/09/Gu%C3%ADa-Requisitos-b%C3%A1sicos-para-realizar-importaciones-y-exportaciones-en-Costa-Rica..pdf
3. Commercial Invoice Format: https://www.scribd.com/document/458411170/factura-comercial
4. Completed Commercial Invoice Example: https://www.slideshare.net/slideshow/modelo-de-factura-comercial-commercial-invoice-llenada/81392481
5. International Transport Documents: https://globalnegotiator.com/blog/documentos-de-transporte-internacional/
6. Bill of Lading: https://www.scribd.com/document/484317652/l-Documento-de-Transporte-Maritimo
7. Airway Bill: https://www.dripcapital.com/es-mx/recursos/blog/air-waybill-que-es
8. CMR: https://www.globalnegotiator.com/files/CMR-carta-de-porte-modelo-ejemplo.pdf
9. Packing List: https://www.scribd.com/document/649777725/FORMATO-PACKING-LIST-2022
10. Certificate of Origin: https://www.comex.go.cr/media/2481/01_anexo-316-certificado-de-origen.pdf
11. Certificate of Origin: https://www.docsity.com/es/docs/certificado-de-origen-1/5523092/
12. Customs Value Example: https://www.scribd.com/doc/273864348/Hoja-de-Calculo-Para-Valor-en-Aduana

---

**Completed DUA Documents**
In this section we include links to completed DUA documents.

1. Costa Rica - Ecuador Guide: https://www.vuce.cr/wp-content/uploads/2024/04/Guia-de-llenado-CO-Ecuador.pdf

---

**Existing solutions that perform similar tasks**
In Costa Rica there are currently no solutions of this type, but in different countries there are similar systems for the automatic completion of customs documents.

1. ACE Secure Data Portal: https://ace.cbp.gov/s/login/?ec=302&startURL=%2Fs%2F

The official U.S. platform for electronic submission of customs data. All commercial data (including import declarations) is submitted through this system.It allows uploading structured data for goods entry, ISF 10+2, among others.

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
- Authentication Server: Auth0
- Credential Verification Server: NodeJS Backend
- Cloud Secret Storage: Google Cloud
  
## 1.2 UX UI analysis
Here we define the desired usability attributes of the application, a preliminary UX design in the form of wireframes, and evidence of UX testing with real users that validates the preliminary design.

### Core Bussines Proccesses 
In this section we describe via wireframes what the user will interact with, we include images of each wireframe and a step by step on how to do it.

#### Login
1. The user enters their login identifier, password, and one-time authentication token.
2. The system validates the provided credentials and the token.
3. If the credentials are incorrect, the system rejects the authentication attempt and informs the user that the username or password is invalid.
4. If the credentials are valid, the system authenticates the user and grants access to the system.
5. After successful authentication, the user proceeds to the generator configuration stage.

**Login Image**

![Login](Images/LoginScreen.png)


#### Set up the generator
1. The user specifies whether the declaration corresponds to an import or export process.
2. The user provides the folder path that contains the documents required for the process.
3. The user starts the automated generation process.

**Generator Image**

![Generator](Images/GeneratorConfiguration.png)

#### Progress monitoring
1. The user checks the status of the generation process.
2. The user can repeatedly check the process status until the generation is completed.
3. Once the process finishes, the system informs the user that the result is available.

**Progress Monitoring Image**

![Progress monitoring](Images/ProgressMonitoring.png)

#### Results Obtained
1. The user requests the generated DUA document.
2. The system provides the completed DUA document generated from the processed information and informs the user.
3. The user reviews the generated document and verifies the extracted information and confidence levels.
4. If the user identifies incorrect or incomplete information, the user modifies the corresponding data.
5. The user confirms the final version of the generated DUA document for further use.
6. The user downloads the final version of the DUA document.

**Results Wireframe**

![Results](Images/ResultRetrieval.png)

#### Logout
1. The user decides to end the session.
2. The user is returned to the authentication stage and no longer has access to the system.

**LogOut Wireframe**

![LogOut Wireframe](Images/LogoutConfirmation.png)


### UX Test Tesults
In this section, you will find the results of the UX test on the wireframes used previously. The technologies used for this were Figma Make and Maze.

Figma Website: https://smoke-chill-65130003.figma.site

Maze UX Text: https://t.maze.co/509306099

| Question | Type | Tester 1: Chris's Brother (509270528) | Tester 2: Chris's Father (509834609) | Tester 3: Arturo Carranza - Student (509831198) | Tester 4: Jose Zumbado - Student (509847370) |
|----------|------|:-------------------------:|:-------------------------:|:-------------------------:|:--------------:|
| Was there any element whose purpose you did not understand? | Open question | Nothing, everything was clear | Very useful AI | No | I understood everything |
| Did the system buttons have a clear function? | Multiple choice | Very clear | Very clear | Quite clear | Very clear |
| How intuitive did you find the system? (1-5) | Opinion scale | 5 | 5 | 4 | 5 |
| From 1 to 10, how easy do you think it is to learn how to use the system? | Opinion scale | 8 | 8 | 9 | 10 |
| Would you recommend this system for DUA automation? | Yes/No | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |

Results Report From Maze: https://app.maze.co/report/DUA-Test/1fi4m37mmldarq1/intro

#### HeatMaps

In this section we include the respective heatmaps for each of the testers and how they interacted with the prototype of the system.

##### Tester 1: Chris's Brother (509270528)

<p align="center">
  <img src="Images/JVheat.jpg" width="450"/>
  <img src="Images/JVheat2.jpg" width="450"/>
</p>
<p align="center">
  <img src="Images/JVheat3.jpg" width="450"/>
  <img src="Images/JVheat4.jpg" width="450"/>
</p>

##### Tester 2: Chris's Father (509834609)

<p align="center">
  <img src="Images/JHheat.jpg" width="450"/>
  <img src="Images/JHheat2.jpg" width="450"/>
</p>
<p align="center">
  <img src="Images/JHheat3.jpg" width="450"/>
  <img src="Images/JHheat4.jpg" width="450"/>
</p>

##### Tester 3: Arturo Carranza - Student (509831198)

<p align="center">
  <img src="Images/ACheat.jpg" width="450"/>
  <img src="Images/ACheat2.jpg" width="450"/>
</p>
<p align="center">
  <img src="Images/ACheat3.jpg" width="450"/>
  <img src="Images/ACheat4.jpg" width="450"/>
</p>

##### Tester 4: Jose Zumbado - Student (509847370)

<p align="center">
  <img src="Images/JCheat.jpg" width="450"/>
  <img src="Images/JCheat2.jpg" width="450"/>
</p>
<p align="center">
  <img src="Images/JCheat3.jpg" width="450"/>
  <img src="Images/JCheat4.jpg" width="450"/>
</p>

#### Proofs

In this section we include proofs on how we contacted the participants or tester for the wireframes we created in the previous sections.

<p align="center">
  <img src="Images/ScreenPapito.png" width="450"/>
  <img src="Images/ScreenJoseph.png" width="450"/>
</p>
<p align="center">
  <img src="Images/ScreenArturo.jpeg" width="450"/>
  <img src="Images/ScreenJoche.png" width="450"/>
</p>

## 1.3 Component design strategy

The frontend interface will follow a modular component-based architecture using React as stated in the technolgy stack.

Component development will follow the Atomic Design methodology in order to maintain a scalable and reusable UI structure. 

The components will be organized into the following levels:

- Atoms: basic UI elements such as buttons, inputs, labels, and icons.
- Molecules: small combinations of atoms such as form fields or input groups.
- Organisms: larger UI sections composed of molecules and atoms such as document upload panels, result viewers, or navigation bars.
- Templates: layout structures that define how organisms are arranged within a page.
- Pages: full application screens such as the document upload page or the generated DUA review page.

CSS styles will be scoped per component in order to avoid conflicts and ensure maintainability. Each component will contain its own style file when necessary.

A consistent naming convention will be used for CSS classes following the pattern:

- ComponentName-ElementName

Example:
- UploadPanel-Container  
- UploadPanel-Button

Responsive design will be supported using relative units such as `em` and `rem` to ensure proper scaling across different screen sizes.

Also the design will prioritize clarity and simplicity since the primary users are customs specialists who need to process documents efficiently.

The interface components will also support future internationalization (i18n) if the system needs to be adapted to other countries or languages.

In this case, we do not include accessible requirements. 

## 1.4 Security

Authentication is handled through Google OAuth using Auth0 as the authentication provider.

The application does not use Multi-Factor Authentication (MFA).
Authentication is performed through a Google account login only.

The system is designed as a single application, therefore Single Sign-On (SSO) is not required.

When a user authenticates with Google, the frontend obtains a Google OAuth ID Token.
This token is sent to the backend where it is verified.

The NodeJS backend server acts as the credential verification server.
It validates the Google ID Token to confirm the user's identity and then creates a secure application session for subsequent requests.

The authentication flow is therefore:

* User clicks login with Google.

* Auth0 handles the Google OAuth authentication process.

* Google returns an ID Token.

* The frontend sends the ID Token to the backend.

* The NodeJS server verifies the token.

* If the token is valid, a secure session is created.

Sensitive configuration data and secrets are stored in Google Cloud secure storage services.

**Google Cloud is responsible for storing:**

- API keys

- Database credentials

- Encryption keys

- Environment variables

- Other sensitive configuration data

These secrets are never stored directly in the source code and are accessed securely by the backend during runtime.

* Roles: Manager, Customs Agent
Permissions by Role:

Manager
- Permission Code: MANAGE_USERS
-- Description: Manage user crud
- Permission Code: VIEW_REPORTS
-- Description: Access operational and performance reports.
- Permission Code: EDIT_TEMPLATES
-- Description: Change or update DUA templates available

Customs Agent
- Permission Code: LOAD_FILES
-- Description: Set and upload a folder with data files.
- Permission Code: GENERATE_DUA
-- Description: Starts the AI process of generating a DUA
- Permission Code: DOWNLOAD_DUA
-- Description: Downloads the DUA generated

## 1.5 Layered design

* The frontend application is built using React and follows a layered architecture with component-based rendering.

* When the user accesses the application, the Routing Layer determines the requested page.

* If there is no authenticated session, the Authentication Layer is invoked using Auth0 with Google OAuth.

* If authentication is successful, the visual interface is rendered within the Components Layer.

* Components follow the Atomic Design methodology (atoms, molecules, organisms, templates, and pages).

* Within components, the Hooks Layer connects user actions with the Services Layer.

* The user selects whether the operation corresponds to an import or export procedure, which determines the template and required fields.

* The user uploads documents that may include Word, Excel, PDF, or image files.

* The Services Layer manages application logic such as document handling, workflow orchestration, and data preparation.

* To perform these operations, Services interact with the ApiClients Layer.

* The ApiClients Layer handles communication with external services and APIs.

* ApiClients read API endpoints and configuration parameters from the Settings Layer.

* The Settings Layer accesses environment variables and configuration data required during runtime.

* All requests and responses exchanged through ApiClients are mapped to domain classes defined in the Models Layer.

* The DataValidation Layer validates incoming and outgoing data structures to ensure format and integrity.

* All layers can access shared resources such as Models, Utils, and the State Management Layer.

* The State Management Layer maintains application state including user session, uploaded files, and document processing status.

* Long-running operations such as document processing or AI-based extraction are handled asynchronously.

* The Notification Service Layer allows the application to react to asynchronous events and update the UI accordingly.

* Once processing is completed, the resulting structured data is used to generate the final DUA document representation.

* The frontend updates the user interface and displays the generated document along with confidence indicators.

* The Logs Layer records system events and interactions for monitoring and debugging purposes.

* The Exception Handling Layer provides centralized error management across all layers.

**Mermaid Diagram Architecture Workflow**

```mermaid
flowchart TD

User --> RoutingLayer
RoutingLayer --> AuthenticationLayer
AuthenticationLayer --> ComponentsLayer

ComponentsLayer --> HooksLayer
HooksLayer --> ServicesLayer

ServicesLayer --> ApiClientsLayer
ApiClientsLayer --> ExternalServices

ExternalServices --> NotificationServiceLayer

NotificationServiceLayer --> ServicesLayer
ServicesLayer --> StateManagementLayer
StateManagementLayer --> ComponentsLayer

ComponentsLayer --> User
```

User
 ↓
Routing
 ↓
Authentication
 ↓
React Components
 ↓
Hooks
 ↓
Services
 ↓
API Clients
 ↓
NodeJS Backend
 ↓
AI Document Processing
 ↓
DUA Generation
 ↓
Response
 ↓
State Management
 ↓
UI Update

## 1.6  Design patterns
Design of classes with their corresponding placement within the project structure, where necessary applying object-oriented design patterns, such as: security, UI refresh, notification handling, state management, API calls, asynchronous operations, session invalidation, event-driven programming, and object creation.

The following classes are proposed to keep the frontend architecture modular, testable, and aligned with the workflow defined in this document.

| Class / Interface | Suggested Location | Responsibility | Pattern | What the Pattern Usually Does |
|----------|----------|----------|----------|----------|
| `AuthSessionGuard` | `src/security/AuthSessionGuard.ts` | Protects private routes and validates active session before page rendering. | Guard | Stops unauthorized access before executing protected logic. |
| `PermissionPolicy` | `src/security/PermissionPolicy.ts` | Centralizes role and permission checks (`MANAGE_USERS`, `GENERATE_DUA`, etc.). | Strategy | Switches behavior at runtime based on interchangeable rules. |
| `SessionManager` | `src/security/SessionManager.ts` | Stores session metadata, refresh windows, and logout triggers. | Facade | Exposes one simplified API over several internal operations. |
| `SessionInvalidationService` | `src/security/SessionInvalidationService.ts` | Invalidates session on token expiration, revocation, or backend rejection. | Observer | Reacts to state changes by notifying subscribed components/services. |
| `ApiClient` | `src/api/ApiClient.ts` | Base HTTP client with headers, retries, timeout, and error mapping. | Template Method | Defines a fixed processing skeleton and lets subclasses customize steps. |
| `AuthApiClient` | `src/api/AuthApiClient.ts` | Handles authentication-related calls and token exchange. | Adapter | Converts one interface/protocol into another expected by the app. |
| `DocumentApiClient` | `src/api/DocumentApiClient.ts` | Sends folder/file metadata and starts DUA generation jobs. | Repository | Encapsulates data access and hides transport/storage details. |
| `NotificationHub` | `src/notifications/NotificationHub.ts` | Publishes process status updates across the app. | Publisher-Subscriber | Broadcasts messages to multiple listeners without tight coupling. |
| `ProgressEventBus` | `src/events/ProgressEventBus.ts` | Event bus for generation progress, completion, and failure events. | Event Bus | Routes events through a central channel for decoupled communication. |
| `GenerationStore` | `src/state/GenerationStore.ts` | Stores processing state, confidence map, and active document context. | Singleton Store | Maintains a single shared instance and global access point. |
| `UIRefreshCoordinator` | `src/ui/UIRefreshCoordinator.ts` | Coordinates selective UI refresh after state changes. | Mediator | Centralizes collaboration rules between components to reduce direct dependencies. |
| `DUAFieldMapper` | `src/domain/DUAFieldMapper.ts` | Maps extracted values to official DUA fields and format rules. | Adapter | Converts extracted source structures into the DUA target field contract expected by the system. |
| `DUADocumentFactory` | `src/domain/DUADocumentFactory.ts` | Creates the final domain object for generated DUA output. | Factory Method | Delegates object creation to specialized creators instead of direct `new`. |
| `ValidationRuleEngine` | `src/validation/ValidationRuleEngine.ts` | Executes syntax and business validation rules before document output. | Chain of Responsibility | Passes a request through multiple handlers until one handles or rejects it. |

## 1.7 Scaffold SRC

The following structure represents the frontend project scaffold.  
It reflects the layered architecture, atomic design principles, and design patterns defined in previous sections.

```plaintext
src
├── index.ts
├── apiClients
│   ├── ApiClient.ts
│   ├── DocumentApiClient.ts
│   └── adapters
│       └── Auth0TokenAdapter.ts
├── components
│   ├── atoms
│   │   └── StatusBadge.tsx
│   ├── molecules
│   │   └── LoginForm.tsx
│   ├── organisms
│   │   └── GeneratorPanel.tsx
│   ├── templates
│   │   └── MainLayoutTemplate.tsx
│   └── pages
│       └── DUAStreamlinerPage.tsx
├── hooks
│   └── useGenerationStatus.ts
├── services
│   └── documentProcessing
│       ├── strategies
│       │   ├── DocumentProcessingStrategy.ts
│       │   └── PdfProcessingStrategy.ts
│       └── builders
│           ├── DUADocumentBuilder.ts
│           └── DUADirector.ts
├── models
│   └── DUAField.ts
├── utils
│   └── DUAFieldMapper.ts
├── settings
│   └── AppConfig.ts
├── state
│   └── store
│       ├── GenerationStore.ts
│       └── index.ts
├── notifications
│   └── NotificationHub.ts
├── logs
│   └── AppLogger.ts
├── exceptions
│   └── AppException.ts
├── security
│   ├── AuthSessionGuard.ts
│   ├── PermissionPolicy.ts
│   └── SessionManager.ts
├── validation
│   ├── BaseValidationHandler.ts
│   └── ValidationRuleEngine.ts
├── domain
│   └── DUADocumentFactory.ts
├── events
│   └── ProgressEventBus.ts
└── ui
    └── UIRefreshCoordinator.ts
```

--- 

# 2. Backend design 

# 3. Data Design

