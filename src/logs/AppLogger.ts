// Central logging facade for observability integration.
export class AppLogger {
  info(message: string): void {
    void message;
    // TODO: Pipe logs to Google Cloud Logging.
  }

  error(message: string): void {
    void message;
    // TODO: Attach correlation IDs and error codes.
  }
}
