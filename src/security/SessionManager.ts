// Session manager centralizes auth session lifecycle metadata.
export class SessionManager {
  private static instance: SessionManager | null = null;
  private sessionToken: string | null = null;

  private constructor() {}

  static getInstance(): SessionManager {
    if (!SessionManager.instance) {
      SessionManager.instance = new SessionManager();
    }

    return SessionManager.instance;
  }

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
