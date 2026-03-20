// Chain of Responsibility base handler for validation rules.
export abstract class BaseValidationHandler<T> {
  private nextHandler?: BaseValidationHandler<T>;

  setNext(handler: BaseValidationHandler<T>): BaseValidationHandler<T> {
    this.nextHandler = handler;
    return handler;
  }

  validate(input: T): boolean {
    if (!this.check(input)) {
      return false;
    }

    return this.nextHandler ? this.nextHandler.validate(input) : true;
  }

  protected abstract check(input: T): boolean;
}
