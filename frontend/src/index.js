import React from 'react';
import ReactDOM from 'react-dom/client';
import './App.css';
import App from './App';

// Performance monitoring
const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Performance reporting (optional)
if (process.env.NODE_ENV === 'production') {
  // You can add performance monitoring here
  const reportWebVitals = (metric) => {
    console.log(metric);
    // Send to analytics service
  };
  
  // Dynamic import to avoid increasing bundle size
  import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
    getCLS(reportWebVitals);
    getFID(reportWebVitals);
    getFCP(reportWebVitals);
    getLCP(reportWebVitals);
    getTTFB(reportWebVitals);
  }).catch(() => {
    // web-vitals not available
  });
}