import { useMemo } from 'react';

// Hook centralizes status text shaping for generation progress.
export function useGenerationStatus(progressPercent: number) {
  return useMemo(() => {
    // TODO: Map confidence and status ranges according to product rules.
    return `Generation progress: ${progressPercent}%`;
  }, [progressPercent]);
}
