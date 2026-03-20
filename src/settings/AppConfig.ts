type EnvironmentName = 'development' | 'stage' | 'production';

// Runtime config for cloud, auth, and API settings.
export type AppConfig = {
  environment: EnvironmentName;
  auth0Domain: string;
  auth0ClientId: string;
  gcpProjectId: string;
  apiBaseUrl: string;
};

export const defaultAppConfig: AppConfig = {
  environment: 'development',
  auth0Domain: '',
  auth0ClientId: '',
  gcpProjectId: '',
  apiBaseUrl: ''
};
