type ProgressEvent = {
  stage: string;
  progressPercent: number;
};

type ProgressListener = (event: ProgressEvent) => void;

// Event bus coordinates progress updates between modules.
export class ProgressEventBus {
  private listeners = new Set<ProgressListener>();

  register(listener: ProgressListener): () => void {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  }

  emit(event: ProgressEvent): void {
    for (const listener of this.listeners) {
      listener(event);
    }
  }
}
