// Strategy contract for processing a categorized source document.
export interface DocumentProcessingStrategy {
  process(sourcePath: string): Promise<void>;
}
