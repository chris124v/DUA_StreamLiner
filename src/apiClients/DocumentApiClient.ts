import { ApiClient } from './ApiClient';

// Specialized API client for DUA generation and retrieval endpoints.
export class DocumentApiClient extends ApiClient {
  async requestGeneration(payload: object): Promise<void> {
    await this.requestTemplate('/dua/generation', payload);
  }

  protected serializeInput<TInput>(input: TInput): unknown {
    // TODO: Transform domain payload to backend contract.
    return input;
  }

  protected mapResponse<TOutput>(rawResponse: unknown): TOutput {
    // TODO: Map backend response into typed view models.
    return rawResponse as TOutput;
  }
}
