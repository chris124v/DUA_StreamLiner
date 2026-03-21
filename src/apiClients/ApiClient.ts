// Template Method base client that standardizes request flow.
export abstract class ApiClient {
  constructor(private readonly baseUrl: string) {}

  async requestTemplate<TInput, TOutput>(path: string, input: TInput): Promise<TOutput> {
    const payload = this.serializeInput(input);
    const rawResponse = await this.executeRequest(path, payload);
    return this.mapResponse<TOutput>(rawResponse);
  }

  protected abstract serializeInput<TInput>(input: TInput): unknown;

  protected abstract mapResponse<TOutput>(rawResponse: unknown): TOutput;

  protected async executeRequest(path: string, payload: unknown): Promise<unknown> {
    void path;
    void payload;
    // TODO: Add HTTP calls, retries, and telemetry instrumentation.
    return { baseUrl: this.baseUrl };
  }
}
