// Guard enforces authenticated session access to protected flows.
export class AuthSessionGuard {
  canActivate(isAuthenticated: boolean): boolean {
    // TODO: Extend with token expiry and MFA checks.
    return isAuthenticated;
  }
}
