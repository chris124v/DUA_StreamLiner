export type Permission = 'dua:generate' | 'dua:view' | 'dua:download';

// Security policy validates user permissions for actions.
export class PermissionPolicy {
  can(permission: Permission, grantedPermissions: Permission[]): boolean {
    return grantedPermissions.includes(permission);
  }
}
