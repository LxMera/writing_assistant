import React from 'react';
import LoadingSpinner from './LoadingSpinner';

const OutputSection = ({ results, streamingResults, isStreaming, isProcessing, error }) => {
  const styles = [
    { key: 'professional', label: 'Professional', icon: '👔' },
    { key: 'casual', label: 'Casual', icon: '😊' },
    { key: 'polite', label: 'Polite', icon: '🙏' },
    { key: 'social_media', label: 'Social Media', icon: '📱' }
  ];

  const getDisplayText = (styleKey) => {
    if (isStreaming) {
      return streamingResults[styleKey] || '';
    }
    return results[styleKey] || '';
  };

  const hasAnyContent = () => {
    return styles.some(style => getDisplayText(style.key));
  };

  if (error) {
    return (
      <div className="output-section">
        <div className="error-message">
          <span className="error-icon">⚠️</span>
          {error}
        </div>
      </div>
    );
  }

  if (!hasAnyContent() && !isProcessing) {
    return (
      <div className="output-section">
        <div className="placeholder-message">
          Enter some text above and click "Process Text" to see the rephrased versions.
        </div>
      </div>
    );
  }

  return (
    <div className="output-section">
      <h2>Rephrased Versions</h2>
      
      <div className="results-grid">
        {styles.map(({ key, label, icon }) => {
          const text = getDisplayText(key);
          const isEmpty = !text;
          
          return (
            <div key={key} className="result-card">
              <div className="result-header">
                <span className="result-icon">{icon}</span>
                <h3>{label}:</h3>
                {isProcessing && isEmpty && <LoadingSpinner size={16} />}
              </div>
              
              <div className="result-content">
                {text ? (
                  <p>{text}</p>
                ) : isProcessing ? (
                  <p className="loading-text">Processing...</p>
                ) : (
                  <p className="empty-text">No content generated</p>
                )}
                
                {isStreaming && text && (
                  <span className="streaming-indicator">●</span>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default OutputSection;