import { useState, useCallback, useRef } from 'react';
import { writingService } from '../services/api';

export const useWritingProcessor = () => {
  const [isProcessing, setIsProcessing] = useState(false);
  const [results, setResults] = useState({
    professional: '',
    casual: '',
    polite: '',
    social_media: ''
  });
  const [streamingResults, setStreamingResults] = useState({
    professional: '',
    casual: '',
    polite: '',
    social_media: ''
  });
  const [error, setError] = useState(null);
  const [isStreaming, setIsStreaming] = useState(false);
  
  const abortControllerRef = useRef(null);

  const processText = useCallback(async (text, useStreaming = false) => {
    if (!text.trim()) {
      setError('Please enter some text to process');
      return;
    }

    setIsProcessing(true);
    setError(null);
    setResults({
      professional: '',
      casual: '',
      polite: '',
      social_media: ''
    });
    setStreamingResults({
      professional: '',
      casual: '',
      polite: '',
      social_media: ''
    });

    try {
      if (useStreaming) {
        setIsStreaming(true);
        abortControllerRef.current = new AbortController();

        await writingService.rephraseTextStream(
          text,
          (chunk) => {
            if (chunk.style && chunk.style !== 'error') {
              setStreamingResults(prev => ({
                ...prev,
                [chunk.style]: chunk.content
              }));
            }
          },
          (error) => {
            setError('Streaming error: ' + error.message);
          },
          abortControllerRef.current.signal
        );

        setIsStreaming(false);
      } else {
        const response = await writingService.rephraseText(text);
        setResults(response);
      }
    } catch (error) {
      if (error.name !== 'AbortError') {
        setError('Failed to process text: ' + error.message);
      }
    } finally {
      setIsProcessing(false);
      setIsStreaming(false);
    }
  }, []);

  const cancelProcessing = useCallback(() => {
    if (abortControllerRef.current) {
      abortControllerRef.current.abort();
    }
    setIsProcessing(false);
    setIsStreaming(false);
  }, []);

  const clearResults = useCallback(() => {
    setResults({
      professional: '',
      casual: '',
      polite: '',
      social_media: ''
    });
    setStreamingResults({
      professional: '',
      casual: '',
      polite: '',
      social_media: ''
    });
    setError(null);
  }, []);

  return {
    isProcessing,
    results,
    streamingResults,
    error,
    isStreaming,
    processText,
    cancelProcessing,
    clearResults
  };
};