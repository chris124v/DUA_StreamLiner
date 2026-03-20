import type { DUAField } from '../models/DUAField';

// Maps generic extraction output into DUA-specific key-value fields.
export class DUAFieldMapper {
  map(rawData: unknown): DUAField[] {
    void rawData;
    // TODO: Map by template hash block and semantic category.
    return [];
  }
}
