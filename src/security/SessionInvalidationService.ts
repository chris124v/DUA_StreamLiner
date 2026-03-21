type SessionInvalidationListener = (reason: string) => void;

// Observer service that broadcasts session invalidation events.
export class SessionInvalidationService {
  private listeners = new Set<SessionInvalidationListener>();

  subscribe(listener: SessionInvalidationListener): () => void {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  }

  invalidate(reason: string): void {
    for (const listener of this.listeners) {
      listener(reason);
    }
  }
}
