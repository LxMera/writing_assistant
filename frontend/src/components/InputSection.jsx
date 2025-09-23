import React, { useState } from 'react';
import LoadingSpinner from './LoadingSpinner';

const InputSection = ({ onProcess, isProcessing, onCancel, onClear }) => {
  const [text, setText] = useState('');
  const [useStreaming, setUseStreaming] = useState(true);

  const handleSubmit = (e) => {
    e.preventDefault();
    onProcess(text, useStreaming);
  };

  const handleClear = () => {
    setText('');
    onClear();
  };

  return (
    <div className="input-section">
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <label htmlFor="text-input">Enter your text:</label>
          <textarea
            id="text-input"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Type your text here..."
            rows={4}
            disabled={isProcessing}
            className="text-input"
          />
        </div>
        
        <div className="options-group">
          <label className="checkbox-label">
            <input
              type="checkbox"
              checked={useStreaming}
              onChange={(e) => setUseStreaming(e.target.checked)}
              disabled={isProcessing}
            />
            Enable streaming output
          </label>
        </div>

        <div className="button-group">
          <button 
            type="submit" 
            disabled={isProcessing || !text.trim()}
            className="btn btn-primary"
          >
            {isProcessing && <LoadingSpinner size={16} />}
            Process Text
          </button>
          
          {isProcessing && (
            <button 
              type="button" 
              onClick={onCancel}
              className="btn btn-secondary"
            >
              Cancel
            </button>
          )}
          
          <button 
            type="button" 
            onClick={handleClear}
            disabled={isProcessing}
            className="btn btn-outline"
          >
            Clear
          </button>
        </div>
      </form>
    </div>
  );
};

export default InputSection;