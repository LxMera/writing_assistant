import React from 'react';
import { useWritingProcessor } from '../hooks/useWritingProcessor';
import InputSection from './InputSection';
import OutputSection from './OutputSection';

const WritingAssistant = () => {
  const {
    isProcessing,
    results,
    streamingResults,
    error,
    isStreaming,
    processText,
    cancelProcessing,
    clearResults
  } = useWritingProcessor();

  return (
    <div className="writing-assistant">
      <header className="app-header">
        <h1>AI Writing Assistant</h1>
        <p>Transform your text into different writing styles</p>
      </header>
      
      <main className="app-main">
        <InputSection
          onProcess={processText}
          isProcessing={isProcessing}
          onCancel={cancelProcessing}
          onClear={clearResults}
        />
        
        <OutputSection
          results={results}
          streamingResults={streamingResults}
          isStreaming={isStreaming}
          isProcessing={isProcessing}
          error={error}
        />
      </main>
    </div>
  );
};

export default WritingAssistant;