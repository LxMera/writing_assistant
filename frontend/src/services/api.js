import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000,
});

export const writingService = {
  async rephraseText(text, provider = 'azure') {
    const response = await api.post('/writing/rephrase', { text, provider});
    return response.data;
  },

  async rephraseTextStream(text, provider, onChunk, onError, signal) {
    try {
      const response = await fetch(`${API_BASE_URL}/writing/rephrase-stream`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text, provider }),
        signal,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';

      while (true) {
        const { done, value } = await reader.read();
        
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        
        // Procesar líneas completas
        const lines = buffer.split('\n');
        buffer = lines.pop() || ''; // Guardar línea incompleta

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            try {
              const data = JSON.parse(line.slice(6));
              console.log('Stream data received:', data); // ← DEBUG
              onChunk(data);
            } catch (e) {
              console.error('Error parsing SSE data:', e, 'Line:', line);
            }
          }
        }
      }
    } catch (error) {
      if (error.name !== 'AbortError') {
        console.error('Stream error:', error);
        onError(error);
      }
    }
  }
};

export default api;