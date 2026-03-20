// Factory creates draft objects by customs operation type.
export class DUADocumentFactory {
  createForOperation(operation: 'import' | 'export'): object {
    // TODO: Return typed default shape per operation and template version.
    return { operation };
  }
}
