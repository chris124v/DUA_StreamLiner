// Session manager centralizes auth session lifecycle metadata.
export class SessionManager {
  private sessionToken: string | null = null;

  setSessionToken(token: string): void {
    this.sessionToken = token;
  }

  clearSession(): void {
    this.sessionToken = null;
  }

  isSessionActive(): boolean {
    return this.sessionToken !== null;
  }
}
