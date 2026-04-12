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
- Cloud Secret Storage: Google Secret Manager
  
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

**Google Secret Manager is responsible for storing:**

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

| Class / Interface | Location | Responsibility | Pattern | Justification |
|------------------|----------|----------------|---------|--------------|
| AuthSessionGuard | [src/security/AuthSessionGuard.ts](src/security/AuthSessionGuard.ts) | Protects private routes and validates active session | Guard | Prevents unauthorized access before rendering protected views |
| SessionManager | [src/security/SessionManager.ts](src/security/SessionManager.ts) | Stores and manages session state | Singleton | A single shared session instance is required across the application |
| SessionInvalidationService | [src/security/SessionInvalidationService.ts](src/security/SessionInvalidationService.ts) | Handles session expiration and invalidation events | Observer | Reacts to session state changes and notifies dependent components |
| ApiClient | [src/apiClients/ApiClient.ts](src/apiClients/ApiClient.ts) | Base HTTP client with reusable request logic | Template Method | Defines a common request flow reused by specialized API clients |
| NotificationHub | [src/notifications/NotificationHub.ts](src/notifications/NotificationHub.ts) | Publishes system-wide notifications | Observer (Pub-Sub) | Enables decoupled communication between components |
| ProgressEventBus | [src/events/ProgressEventBus.ts](src/events/ProgressEventBus.ts) | Handles async process events | Event Bus | Centralizes asynchronous event distribution across the system |
| GenerationStoreRepository | [src/state/store/GenerationStoreRepository.ts](src/state/store/GenerationStore.ts) | Stores each DUA generation state | Repository | It manages multiple GenerationStore instances (one per generation); the Repository is a Singleton, but each GenerationStore is independent. |
| UIRefreshCoordinator | [src/ui/UIRefreshCoordinator.ts](src/ui/UIRefreshCoordinator.ts) | Coordinates UI updates across components | Mediator | Reduces direct dependencies between UI components |
| DocumentProcessingStrategy | [src/services/documentProcessing/strategies/DocumentProcessingStrategy.ts](src/services/documentProcessing/strategies/DocumentProcessingStrategy.ts) | Defines contract for processing different document types | Strategy | Enables interchangeable processing logic for PDF, Excel, Word, and images |
| DUAFieldMapper | [src/utils/DUAFieldMapper.ts](src/utils/DUAFieldMapper.ts) | Maps extracted data into DUA field structure | Adapter | Transforms heterogeneous extracted data into a unified DUA format |

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
│   ├── SessionInvalidationService.ts
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

## Technology Stack

- API type: REST API, HTTPS
- API standard: OpenAPI 3.1
- API gateway: Google Cloud API Gateway
- Hosting: Google Cloud Run
- Architecture: Monorepo with Domain-Driven Design (DDD)
- Coding language: Python 3.12
- Web framework: FastAPI 0.115
- Unit testing framework: Pytest 8.3
- Data validation framework: Pydantic 2.7
- Asynchronous operations & notifications: Google Cloud Pub/Sub and Google Cloud Tasks
- Document & file storage: Google Cloud Storage
- OCR processing: Google Cloud Document AI
- AI/ML extraction: Google Vertex AI (Gemini)
- Secret management: Google Secret Manager
- Code repository: GitHub (monorepo compartido con el frontend)
- CI/CD automation: GitHub Actions
- Environments: Development, Stage, Production
- Environment deployments: GitHub Environments
- Observability: Google Cloud Operations Suite (Cloud Logging + Cloud Monitoring)
- Authentication verification: Auth0 (validación de tokens JWT en sincronía con el frontend)
- No load balancer required
- Services architecture: Domain-driven services
- Database: Google Cloud SQL (PostgreSQL 16)
- Encryption key management: Google Cloud KMS
- Container registry: Google Artifact Registry 
- Session cache: Google Cloud Memorystore (Redis)
- Agent orchestration framework: LangGraph (LangChain) 0.2
---

## Security

### Authentication & Authorization
- Authentication delegated to Auth0 with Google OAuth 
- JWT tokens validated on every request; expiration: 1 hour, automatic rotation with refresh token
- Roles and permissions validated at the backend level: `Manager` and `Customs Agent` with the same permission codes defined in the frontend
- Per-endpoint authorization enforced using permission claims from the JWT payload
 
### Transport
- All communication between backend services and GCP managed services (Cloud SQL, Storage, Pub/Sub) is secured via HTTPS/TLS 1.3 using Google-managed certificates
 
### Encryption at Rest
- The Encryption algorithm will use AES-256 to storage sensitive content in google cloud sql.
- Encryption keys are managed through Google Cloud KMS (Customer-Managed Encryption Keys - CMEK).
- Encryption is handled transparently by the cloud provider; no application-level encryption of the database is performed.
 
### Secrets
- All secrets managed in Google Secret Manager; never stored in the repository or hardcoded as environment variables.
 
### API Surface
- General maximum payload size: 10 MB; exception on the document upload endpoint: 50 MB
- Rate limit: maximum 100 concurrent requests per user
- Input validation with Pydantic on all endpoints
- OWASP API Top 10 protections applied
 
### Network
- Backend deployed within a private VPC on GCP
- Google Cloud SQL configured with no public IP, accessible only within the VPC
- Google Cloud Armor configured as firewall for the API Gateway
 
### Data Retention
* Production data retention: 3 years (Costa Rica customs law requirement)
* Active database: Stores current + previous 2 years of DUAs and documents in Google Cloud SQL
* Archive storage: After 3 years, data moves to Google Cloud Storage Archive class 
* Archive location: us-central1 or us-west1 
* Retention schedule
  - Year 1: Hot storage we use Google Cloud SQL production data
  - Year 2: Cool storage (Google Cloud Storage Standard) for the files
  - Year 3: Archive storage (Cloud Storage Archive class, minimum 90 days retention)
  - After 5 years (Automated Purge): Cloud Scheduler job runs monthly to archive data older than 3 years to Cloud Storage Archive
* Audit trail: All data movements logged to Cloud Logging with timestamp and reason

--- 

## Observability
 
### Logs
* Format: Structured JSON with trace_id, request_id, user_id, user_role, timestamp, level, message, service, enviroment, version, endpoint, method, statuscode
* Destination: Google Cloud Logging (same as frontend)
* Correlation: X-Trace-ID header propagated across all requests (unified with frontend logs)
 
### Metrics
* What to measure: Latency (P95, P99), error rate, CPU utilization, memory usage, Pub/Sub queue depth
* Destination: Google Cloud Monitoring
* Tool: Google Cloud Monitoring dashboards
 
### Distributed Traces
* Instrumentation: OpenTelemetry SDK for Python (FastAPI)
* Destination: Google Cloud Trace
* Scope: Trace every HTTP request from entry to exit, including Cloud SQL queries and Pub/Sub messages
 
### Application Patterns
 
* Health Checks: /health/live (liveness), /health/ready (readiness) endpoints checked every 30 seconds by Cloud Run
* Correlation IDs: X-Trace-ID injected into all logs, metrics, and spans; same ID across Frontend and Backend
* Service Level Indcators: 
  - Availability: 99.9% (max 43 min downtime/month)
  - Latency: 95% of requests < 500ms
  - Error rate: < 0.5%
 
### Events to Register
 
* User login (success/failure), JWT validation failures, unauthorized access attempts
* DUA created/updated/validated, document uploaded, OCR processing (started/completed), DUA generation completed
* API requests (received/completed), database queries, Pub/Sub messages (enqueued/processed)
* Exceptions/errors, health check results, performance degradation
 
### Centralization
 
* Events Platform: Google Cloud Operations Suite (Cloud Logging + Cloud Monitoring + Cloud Trace)
* Log Storage: Cloud Logging (structured logs retained 1 year; audit logs follow the retention schedule: Year 1 hot storage, Year 2 cool storage, Year 3+ archive, purged after 5 years via Cloud Scheduler)
* Dashboard Tool: Google Cloud Monitoring Dashboards 
* Frontend Synchronization: Same X-Trace-ID and Cloud Logging workspace for full-stack tracing

---

## Infrastructure  (DevOps)

### CI/CD Tool
* GitHub Actions: Automates build, test, and deployment from code repository
* Trigger: Automatic on push to develop (Dev) and main (Staging → Prod)
 
### Deployment Tool
* Terraform: Infrastructure as Code for Google Cloud resources (Cloud Run, Cloud SQL, Cloud Storage, Secret Manager)
* Environments: 
  - Dev: Cloud Run with 2 minimum instances (automatic deploy)
  - Staging: Cloud Run with 3 minimum instances (automatic deploy)
  - Prod: Cloud Run with auto-scale 1-10 instances (manual approval required, blue-green deployment), we use small instances because its cheaper and most external APIs will hit a limit before we get need more than those 10 instances.
 
### Container Registry
* Google Artifact Registry: Store Docker images with automatic vulnerability scanning and binary authorization (approval)

---

## Availability

### SLA (Service Level Agreement) Target For The Business
* 99.9% uptime: Maximum 8.7 hours downtime per year
* Applies to production environment only

### Component SLAs & Recovery From the Providers

| Component | Native SLA | Recovery Strategy |
|-----------|-----------|-------------------|
| **Google Cloud Run** | 99.95% | Multi-region deployment (us-central1 + us-west1); auto-failover < 1 min |
| **Google Cloud SQL** | 99.99% (HA) | Cloud SQL HA with automatic failover and automated backups; RTO < 30 sec |
| **Google Cloud Storage** | 99.99% | Geo-redundant storage; automatic failover to secondary region |
| **Google Secret Manager** | 99.99% | Geo-replicated; retry with backoff on transient failures |
| **Google Cloud API Gateway** | 99.95% | Premium tier; circuit breaker for backend failures |
| **Google Cloud Pub/Sub** | 99.99% | Dead Letter Policy for failed messages; exponential backoff retry |
| **Google Cloud Document AI** | 99.9% | Retry with exponential backoff; degraded mode returns partial data |
| **Google Vertex AI (Gemini)** | 99.9% | Circuit breaker on 3 consecutive failures; fallback to manual review flag |
| **Auth0** | 99.99% | Managed HA by Auth0; JWT cache allows short-term offline tolerance |
| **Google Cloud Logging** | 99.95% | Best-effort; non-critical for availability |

### Single Point of Failure Analysis
* Vertex AI: If unavailable, DUA generation fails entirely; mitigated with circuit breaker and degraded mode
* Document AI: If unavailable, OCR fails; mitigated with retry and partial response fallback
* Cloud SQL: Mitigated with Cloud SQL HA (Secondary Instance of the DB) and automatic failover

### Resilience Patterns (Production)
* Circuit Breaker: Vertex AI and Document AI failures trigger circuit breaker (3 failures → 30s break)
* Retry with Backoff: Exponential backoff (100ms → 200ms → 400ms) for transient failures
* Bulkhead: OCR processing isolated to 20 max concurrent threads via Pub/Sub concurrency limits
* Degraded Mode: If OCR or AI unavailable, respond with partial data and flag fields for manual review
* Health Checks: /health/ready endpoint checked every 30 seconds by Cloud Run; auto-restart if unhealthy

---

## Scalability

### Elements That Scale with Request Volume
 
* Cloud Run: Auto-scale 5-50 instances (trigger: CPU > 70% or request concurrency > 80)
* Cloud SQL: Vertical scaling; read replicas for read-heavy workloads
* Pub/Sub: Auto-scales throughput; subscriber concurrency auto-adjusts (max 1000 concurrent pulls per subscription)
* Background Workers (Cloud Tasks): Auto-scale job processing threads based on queue depth
* Cloud Memorystore (Redis): Vertical scaling (Basic < Standard < Premium); auto-failover in Standard+ tiers
* Cloud Storage: Auto-scales (unlimited capacity, unlimited throughput)
 
### Auto-Scaling Triggers
 
* CPU > 70% → add Cloud Run instance
* Request concurrency > 80 → add Cloud Run instance
* Pub/Sub queue depth > 100 messages → increase subscriber concurrency
* Cloud SQL CPU > 80% → scale up (vertical); add read replica if reads spike
* Max limit: 50 Cloud Run instances (cost control)
 

---

## Backend Key Workflows

### Login
Implementation: [`src/backend/api/routers/auth_router.py`](src/backend/api/routers/auth_router.py)

1. The user sends credentials from the frontend to the Auth0 service
2. The frontend sends the JWT to the backend through a GET authorization (the JWT travels in the bearer); here Google Cloud API Gateway is responsible for validating that the endpoint exists and verifying the rate limit
3. Google Cloud API routes the request to Cloud Run (where the backend is hosted)
4. FastAPI validates the JWT with Auth0 (JWKS)
5. If validated, it performs a mapping to Domain-Driven Design (stores the user values in a class)
6. Executes the "Session Cache" workflow

### Session Cache
1. It checks if Google Cloud Memorystore (Redis) contains the user; if it does then it returns the user with the response.
2. It it doesnt: Reads the database for the auth0_id then maps it to DDD (from DB user to Domain user) and save it in Redis

### Set up the generator
1. The backend receive an option between "Import" and "Export" process.
2. The backend choose the type of dua template used based on the selection.
3. The backend receive files and executes the "Upload files to generate dua" workflow

### Upload files to generate dua
Implementation: [`src/backend/api/routers/upload_router.py`](src/backend/api/routers/upload_router.py)

1. The backend receive the list of files to be uploaded
2. Open a streaming transfer file by file to received the files content in raw format
3. All the files are store in Google Cloud Service and map in the database

### Comparison between files of the user (not an image).
1. The backend loads all uploaded files from the configured folder path and already process files of the same user
2. The backend divides the new files in blocks and creates embeddings.
3. The backend then calculate the hash and compared with existing ones; if it already exists, the embedding is reused.
4. if it doesnt exist it sends them to the workflow of thematic classification.

### Comparison between files of the user (image).
1. The backend loads all uploaded files from the configured folder path and already process files of the same user
2. The backend sends the image to "ocr" workflow to extract text, layout structure, bounding boxes
2. The backend divides the extracted information into blocks and creates embeddings.
3. The backend then calculate the hash and compared with existing ones; if it already exists, the embedding is reused.
4. if it doesnt exist it sends them to the workflow of thematic classification.

### Comparison between Dua Templates 
1. The backend loads the dua template hash and embedding from the GCS.
2. The backend loads the "updated" dua template.
2. The backend divides the new files in blocks and creates embeddings.
3. The backend then calculate the hash and compared with existing ones; if it already exists, the embedding is reused.
4. if it doesnt exist its send to the workflow of thematic classification.

### Thematic classification.
1. The backend sends the embeddings of blocks to Vertex Ai AutoML classification model
2. it receivs a probability vector (0-1) for categories:
- Commercial invoice
- Transport document
- Certificate of origin
- Packing list
- Financial document
- Other
3. Selects the top 2 categories with highest probability
4. Stores: File type category, thematic categories, confidence scores, embedding, block, file usage (DUA template, User files), Expected field type (can be null, its used in DUA Templates), validation rules(can be null, its used in DUA Templates), rendering type(can be null, its used in DUA Templates).
5. The blocks are indexed in a vector store group by thematic cateogry, file type (creating an inverted index).

### OCR.
Implementation: [`src/backend/infrastructure/ocr/document_ai_adapter.py`](src/backend/infrastructure/ocr/document_ai_adapter.py)

1. The backend uses Vertex AI Vision API.
2. Extracts: Text, Layout structure, bounding boxes.
3. Return the extracted information as a json.

### Extracts structured fields from embeddings.
1. The backend sends each block to a NLP (Natural Language Processing) model specialized in customs
2. It returns: 
- Importer/exporter data
- Supplier info
- Goods description
- Quantities, weights, FOB/CIF values
- Incoterms
- Transport info
- Invoice number/date
- Country of origin
- Customs regime
- syntactic validation:{Country codes validation, Date format validation, Numeric consistency checks}
3. Its stored as normalized structured data asociated with the vector database.
4. Execute "Dua template mapping" workflow.

### Dua template mapping.
1. the backend performs similarity search using embeddings
2. Applies filtering using: One hot encoding of document categories
3. Selects top 2 candidate blocks
4. Sends them to an Ai API
5. Receives: Target Dua section mapping, confidence score
6. it gives a warning color based on:
- x ≤ 30% → Red warning
- 30% < x ≤ 70% → Yellow warning
- x > 70% → Green warnin

### Dua structure generation.
1. The backend applies formating rules and determines field requirements (text, codes, dynamic tables, images)
2. Generates the final DUA: filling fields automatically and applying color indicatores based on confidence

### Progress monitoring.
Backend Implementation: [`src/backend/api/routers/status_router.py`](src/backend/api/routers/status_router.py) | Frontend: [`src/events/ProgressEventBus.ts`](src/events/ProgressEventBus.ts)

1. The frontend initializes a polling mechanism using `ProgressEventBus` to subscribe to generation events.
2. The user makes a request to the backend `/dua/generation/{id}/status` endpoint with the generation session ID.
3. The backend retrieves the current generation state for that process from `GenerationStoreRepository` which maintains a single source of truth for that process of DUA generation.
4. The backend returns the progress data including: current step (1-10), percentage completion (0-100), current task description, and status (PROCESSING, COMPLETED, FAILED).
5. The `NotificationHub` (Observer/Pub-Sub pattern) publishes progress events to all subscribed frontend components whenever state changes occur.
6. The `ProgressEventBus` (Event Bus pattern) receives these events and distributes them to interested UI listeners without tight coupling.
7. Upon completion, the backend publishes a GENERATION_COMPLETE event through `ProgressEventBus` which triggers:
    - NotificationHub sends a system-wide notification to inform the user
    - UIRefreshCoordinator updates the UI to transition from progress monitoring to results display
8. If generation fails at any step, the backend publishes a GENERATION_FAILED event and stores error details in GenerationStore with step number and error message for user review.


### Results Obtained.
Implementation: [`src/backend/api/routers/result_router.py`](src/backend/api/routers/result_router.py)

1. The backend receive the changes requested on the document by the user and updates it.
2. The backend receive the confirmation that its the final version of the generated DUA document.
3. The backend sends the file for the user to download.

### Logout.
Implementation: [`src/backend/api/routers/logout_router.py`](src/backend/api/routers/logout_router.py)

1. the backend receive a logout request
2. the backend deletes the session cache in redis

---

## Architecture Diagram in Layers
### Context Diagram
![context_diagram.png](Images/context_diagram.png)
### Container Diagram
![container_diagram.png](Images/container_diagram.png)
### Code Diagram
![code_diagram.png](Images/code_diagram.png)


---

## Design Considerations
### Algorithm Selection & Parameters
#### Embedding Generation Algorithm
- **Embedding Model**: Google's Universal Sentence Encoder v5 (via Vertex AI)
- **Embedding Dimension**: 512 dimensions
- **Chunking Strategy**: 
  - Max chunk size: 512 tokens (~2,000 characters) (precise and fast)
  - Overlap: 50 tokens for context preservation (overlapping to not lose context between chunks)
- **Similarity Metric**: Cosine similarity (threshold > 0.7 for semantic relevance)

#### Field Extraction Algorithm
- **Algorithm Type**: Named Entity Recognition (NER) + Structured Extraction via LLM
- **Model**: Google Vertex AI Gemini 1.5 Pro
- **Extraction Fields**:
  - Importer/Exporter Data (regex + entity extraction)
  - Supplier Information (NER for organization names)
  - Product Description (semantic similarity to HS codes)
  - Quantity/Weight (numeric extraction + validation)
  - Incoterms (pattern matching against INCOTERMS 2020 rules)
  - Transport Info (modal detection: maritime/air/land)
  - Invoice Details (date extraction with ISO 8601 validation)
  - Country of Origin (ISO 3166-1 alpha-3 code matching)
  - Customs Regime (Pattern matching to Costa Rican regimes)
- **Temperature**: 0.2 (low randomness for deterministic extraction)
- **Validation Logic**:
  - Country codes: ISO 3166-1 alpha-3 validation
  - Dates: ISO 8601 format validation (YYYY-MM-DD)
  - Quantities: Positive numeric validation
  - Currency codes: ISO 4217 validation

#### Similarity Matching Algorithm
- **Primary Algorithm**: Vector cosine similarity (embeddings)
- **Secondary Filter**: One-hot encoding classification (document category pre-filtering)
- **Ranking Method**: 
  1. Compute cosine similarity between extracted block and template sections
  2. Apply category filter (only compare within same document type)
  3. Select top 2 candidates with highest similarity

### Agent Prototypes Definition
#### Document Classification Agent
- **Purpose**: Categorize uploaded documents into predefined types
- **Input**: Embedding of a block of the document + file metadata (name, type, size)
- **Output**: Block category, confidence scores for each category
- **Workflow**:
  1. Detect file format (MIME type validation)
  2. Send text to Vertex AI classification model
  3. Return top-2 categories with confidence scores
- **Error Handling**: If no category > 50% confidence, classify as "Other"

#### OCR Processing Agent
- **Purpose**: Extract text and structure from scanned images and PDFs
- **Input**: Document file (PDF/image)
- **Output**: Extracted text, detected tables, layout structure, bounding boxes
- **Workflow**:
  1. Send document to Vertex Ai Vision
  2. Parse OCR response (text regions, confidence scores, tables)
  3. Convert to structured blocks with positional metadata
  4. Filter low-confidence regions 

#### Similarity Matching Agent
- **Purpose**: Match extracted blocks to DUA template sections
- **Input**: Extracted field values + DUA template structure + document category
- **Output**: DUA section mapping + confidence scores + alternative matches (top-2)
- **Workflow**:
  1. Search vector store using cosine similarity
  2. Apply category filter (inverted index by document type)
  3. Rank results by similarity score
  4. Return top-2 candidates with confidence interpolation
- **Confidence Mapping**:
  - Cosine similarity > 0.85 → Green (automatic acceptance)
  - 0.70-0.85 → Yellow (requires user confirmation)
  - < 0.70 → Red (manual review required)

#### Field Extraction Agent
- **Purpose**: Extract key customs fields from document content
- **Input**: Document text block + expected field types + block categories
- **Output**: Extracted field values + confidence scores + validation status
- **Workflow**:
  1. Send text + field schema to Vertex AI Gemini
  2. Extract structured fields using NER + LLM
  3. Validate extracted values (format, range, allowed values)
  4. Return confidence scores per field
  5. Flag fields failing validation for manual review
- **Supported Fields**: 
  - Importer/Exporter data
  - Supplier information
  - Product description (with HS code suggestion)
  - Quantities, weights, FOB/CIF values
  - Incoterms
  - Transport information
  - Invoice number/date
  - Country of origin
  - Customs regime

#### DUA Document Generation Agent
- **Purpose**: Populate DUA fields directly in the web interface with validated values and visual confidence indicators
- **Input**: Mapped field values + confidence scores + DUA template + document generation rules
- **Output**: Web form with fields auto-filled and a color indicator (red, yellow, green) displayed next to each field based on confidence
- **Workflow**:
  1. Load DUA template structure in the web interface (form-based layout)
  2. Apply rule engine (dependency validation between fields)
  3. Format values (date conversion, unit normalization, code validation)
  4. Populate each field in the UI with the corresponding value
  5. Display a visual indicator next to each field based on confidence:
     - Green: Confidence > 70%
     - Yellow: Confidence 30–70%
     - Red: Confidence < 30%
  6. Highlight fields requiring user verification (yellow/red) to guide manual review

---

## Source Code

### Backend (Python/FastAPI - Domain-Driven Design)

**API Layer - REST Endpoints**
- [Auth Routes](src/backend/api/routers/auth_router.py) - Authentication and login endpoints
- [DUA Routes](src/backend/api/routers/dua_router.py) - DUA generation and management endpoints
- [Upload Routes](src/backend/api/routers/upload_router.py) - Document upload endpoints
- [Status Routes](src/backend/api/routers/status_router.py) - Progress monitoring endpoints
- [Health Routes](src/backend/api/routers/health_router.py) - Health check endpoints

**Domain Layer - Core Business Logic**
- [User Entity](src/backend/domain/entities/user.py) - User aggregate root
- [Document Entity](src/backend/domain/entities/document.py) - Document aggregate root with file management
- [DUA Generation Entity](src/backend/domain/entities/dua_generation.py) - DUA generation workflow aggregate
- [Domain Events](src/backend/domain/events/) - Events for document upload, OCR, classification, extraction
- [Domain Services](src/backend/domain/services/) - Document processing, authentication, DUA generation services
- [Value Objects](src/backend/domain/value_objects/) - DocumentType, Block, Embedding, TemplateMapping, OCRResult, CustomsField

**Application Layer - Use Cases**
- [Login Use Case](src/backend/application/use_cases/auth/login_use_case.py) - User authentication workflow
- [Upload Documents Use Case](src/backend/application/use_cases/dua/upload_documents_use_case.py) - File upload handling
- [Create DUA Use Case](src/backend/application/use_cases/dua/create_dua_use_case.py) - DUA generation orchestration
- [Get Status Use Case](src/backend/application/use_cases/dua/get_status_use_case.py) - Progress monitoring

**Infrastructure Layer - External Service Adapters**
- [Vertex AI Adapter](src/backend/infrastructure/ai/vertex_ai_adapter.py) - Embedding, classification, field extraction
- [Auth0 Adapter](src/backend/infrastructure/auth/auth0_adapter.py) - JWT validation
- [Google Cloud Storage Adapter](src/backend/infrastructure/storage/gcs_storage_adapter.py) - Document storage
- [Document AI Adapter](src/backend/infrastructure/ocr/document_ai_adapter.py) - OCR processing
- [Cloud SQL Repository](src/backend/infrastructure/persistence/cloudsql/repositories.py) - PostgreSQL persistence layer
- [Cloud SQL Models](src/backend/infrastructure/persistence/cloudsql/models.py) - Database schema (User, Document, DUAGeneration, Block, etc.)
- [Redis Cache Adapter](src/backend/infrastructure/persistence/redis/redis_cache_adapter.py) - Session caching
- [Cloud Pub/Sub Adapter](src/backend/infrastructure/messaging/pubsub_adapter.py) - Async messaging

**Ports (Integration Contracts)**
- [Ports Directory](src/backend/application/ports/) - Abstract interfaces for all external services

### Frontend (TypeScript/React - Atomic Design)

**Components**
- [Atoms](src/components/atoms/) - Basic UI elements (StatusBadge, etc.)
- [Molecules](src/components/molecules/) - Composite components (LoginForm, etc.)
- [Organisms](src/components/organisms/) - Complex sections (GeneratorPanel, etc.)
- [Templates](src/components/templates/) - Layout templates (MainLayoutTemplate, etc.)
- [Pages](src/components/pages/) - Full page components (DUAStreamlinerPage, etc.)

**Security & State**
- [Auth Session Guard](src/security/AuthSessionGuard.ts) - Route protection
- [Session Manager](src/security/SessionManager.ts) - Session state management
- [Session Invalidation Service](src/security/SessionInvalidationService.ts) - Session expiration handling
- [Progress Event Bus](src/events/ProgressEventBus.ts) - Async event distribution

**Services & Utilities**
- [API Client](src/apiClients/ApiClient.ts) - Base HTTP client
- [Document API Client](src/apiClients/DocumentApiClient.ts) - Document API integration
- [DUA Field Mapper](src/utils/DUAFieldMapper.ts) - Data transformation to DUA format
- [App Config Settings](src/settings/AppConfig.ts) - Configuration management

**Configuration Files**
- [Backend pyproject.toml](src/pyproject.toml) - Python dependencies
- [Backend Dockerfile](src/Dockerfile) - Container configuration
- [Environment Variables](src/.env.example) - Environment template


---

# 3. Data Design

