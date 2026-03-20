import type { DocumentProcessingStrategy } from './DocumentProcessingStrategy';

// Concrete strategy placeholder for PDF processing behavior.
export class PdfProcessingStrategy implements DocumentProcessingStrategy {
  async process(sourcePath: string): Promise<void> {
    void sourcePath;
    // TODO: Integrate OCR and semantic extraction pipeline for PDF files.
  }
}
