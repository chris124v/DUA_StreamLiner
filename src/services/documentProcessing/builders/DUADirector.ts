import { DUADocumentBuilder } from './DUADocumentBuilder';

// Director orchestrates builder steps for a standard draft.
export class DUADirector {
  createStandardDraft(builder: DUADocumentBuilder): object {
    return builder.withMetadata().withItemsTable().build();
  }
}
