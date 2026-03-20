// Singleton store for frontend generation state snapshots.
export class GenerationStore {
  private static instance: GenerationStore | null = null;

  private constructor(private state: { status: string } = { status: 'idle' }) {}

  static getInstance(): GenerationStore {
    if (!GenerationStore.instance) {
      GenerationStore.instance = new GenerationStore();
    }

    return GenerationStore.instance;
  }

  getState(): { status: string } {
    return this.state;
  }

  setStatus(status: string): void {
    this.state = { ...this.state, status };
  }
}
