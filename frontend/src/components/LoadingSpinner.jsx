import React from 'react';

const LoadingSpinner = ({ size = 24 }) => {
  return (
    <div className="loading-spinner-container">
      <div 
        className="loading-spinner"
        style={{ 
          width: size, 
          height: size,
          border: `${size/8}px solid #f3f3f3`,
          borderTop: `${size/8}px solid #007bff`
        }}
      />
    </div>
  );
};

export default LoadingSpinner;