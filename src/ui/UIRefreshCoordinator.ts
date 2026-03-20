// Mediator coordinates UI refresh requests among widgets.
export class UIRefreshCoordinator {
  requestRefresh(scope: 'progress' | 'result' | 'session'): void {
    void scope;
    // TODO: Trigger specific render channels based on scope.
  }
}
