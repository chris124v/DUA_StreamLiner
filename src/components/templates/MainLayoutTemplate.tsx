type MainLayoutTemplateProps = {
  children: unknown;
};

// Template defines the shared layout skeleton for pages.
export function MainLayoutTemplate({ children }: MainLayoutTemplateProps) {
  void children;
  // TODO: Render global header/footer and content slots with JSX.
  return null;
}
