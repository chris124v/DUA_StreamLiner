import { BaseValidationHandler } from './BaseValidationHandler';

// TODO: Replace with a Zod schema once package dependencies are installed.
export const duaInputSchema = {
  operation: ['import', 'export'],
  folderPath: 'non-empty'
} as const;

// Executes schema-first and chain-based validation rules.
export class ValidationRuleEngine<T> {
  constructor(private readonly rootHandler?: BaseValidationHandler<T>) {}

  validate(input: T): boolean {
    // TODO: Integrate field-level warnings and confidence color mapping.
    return this.rootHandler ? this.rootHandler.validate(input) : true;
  }
}
