import { ApiClient } from './ApiClient';

// Specialized API client for DUA generation and retrieval endpoints.
export class DocumentApiClient extends ApiClient {
  async requestGeneration(payload: object): Promise<void> {
    void payload;
    // TODO: POST generation request to backend orchestrator.
  }
}
