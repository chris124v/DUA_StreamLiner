// Base API client abstraction for HTTP interactions.
export class ApiClient {
  constructor(private readonly baseUrl: string) {}

  async get(path: string): Promise<unknown> {
    void path;
    // TODO: Centralize fetch wrapper with retries and telemetry.
    return { baseUrl: this.baseUrl };
  }
}
