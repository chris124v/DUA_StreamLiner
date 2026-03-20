type NotificationCallback = (message: string) => void;

// Observer/Pub-Sub hub for cross-feature notifications.
export class NotificationHub {
  private subscribers = new Set<NotificationCallback>();

  subscribe(callback: NotificationCallback): () => void {
    this.subscribers.add(callback);
    return () => this.subscribers.delete(callback);
  }

  publish(message: string): void {
    for (const callback of this.subscribers) {
      callback(message);
    }
  }
}
