// Adapter that normalizes Auth0 token payloads for app consumption.
export class Auth0TokenAdapter {
  adapt(rawToken: unknown): { accessToken: string } {
    void rawToken;
    // TODO: Map Auth0 response shape to internal auth contract.
    return { accessToken: '' };
  }
}
