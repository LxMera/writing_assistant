import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import WritingAssistant from '../components/WritingAssistant';
import * as api from '../services/api';

// Mock the API service
jest.mock('../services/api');

describe('WritingAssistant', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('renders main components', () => {
    render(<WritingAssistant />);
    
    expect(screen.getByText('AI Writing Assistant')).toBeInTheDocument();
    expect(screen.getByText('Transform your text into different writing styles')).toBeInTheDocument();
    expect(screen.getByLabelText('Enter your text:')).toBeInTheDocument();
    expect(screen.getByText('Process Text')).toBeInTheDocument();
  });

  test('displays placeholder message initially', () => {
    render(<WritingAssistant />);
    
    expect(screen.getByText(/Enter some text above and click "Process Text"/)).toBeInTheDocument();
  });

  test('processes text successfully', async () => {
    const mockResponse = {
      professional: 'Professional version',
      casual: 'Casual version',
      polite: 'Polite version',
      social_media: 'Social media version'
    };

    api.writingService.rephraseText.mockResolvedValueOnce(mockResponse);

    render(<WritingAssistant />);
    
    const textarea = screen.getByLabelText('Enter your text:');
    const processButton = screen.getByText('Process Text');
    const streamingCheckbox = screen.getByLabelText('Enable streaming output');

    // Disable streaming for this test
    fireEvent.click(streamingCheckbox);
    
    fireEvent.change(textarea, { target: { value: 'Hello world' } });
    fireEvent.click(processButton);

    await waitFor(() => {
      expect(screen.getByText('Professional version')).toBeInTheDocument();
      expect(screen.getByText('Casual version')).toBeInTheDocument();
      expect(screen.getByText('Polite version')).toBeInTheDocument();
      expect(screen.getByText('Social media version')).toBeInTheDocument();
    });
  });

  test('handles API errors gracefully', async () => {
    api.writingService.rephraseText.mockRejectedValueOnce(
      new Error('API Error')
    );

    render(<WritingAssistant />);
    
    const textarea = screen.getByLabelText('Enter your text:');
    const processButton = screen.getByText('Process Text');
    const streamingCheckbox = screen.getByLabelText('Enable streaming output');

    // Disable streaming for this test
    fireEvent.click(streamingCheckbox);
    
    fireEvent.change(textarea, { target: { value: 'Hello world' } });
    fireEvent.click(processButton);

    await waitFor(() => {
      expect(screen.getByText(/Failed to process text/)).toBeInTheDocument();
    });
  });

  test('disables process button when no text is entered', () => {
    render(<WritingAssistant />);
    
    const processButton = screen.getByText('Process Text');
    expect(processButton).toBeDisabled();
  });

  test('clears results when clear button is clicked', async () => {
    const mockResponse = {
      professional: 'Professional version',
      casual: 'Casual version',
      polite: 'Polite version',
      social_media: 'Social media version'
    };

    api.writingService.rephraseText.mockResolvedValueOnce(mockResponse);

    render(<WritingAssistant />);
    
    const textarea = screen.getByLabelText('Enter your text:');
    const processButton = screen.getByText('Process Text');
    const clearButton = screen.getByText('Clear');
    const streamingCheckbox = screen.getByLabelText('Enable streaming output');

    // Disable streaming for this test
    fireEvent.click(streamingCheckbox);
    
    fireEvent.change(textarea, { target: { value: 'Hello world' } });
    fireEvent.click(processButton);

    await waitFor(() => {
      expect(screen.getByText('Professional version')).toBeInTheDocument();
    });

    fireEvent.click(clearButton);

    expect(textarea.value).toBe('');
    expect(screen.getByText(/Enter some text above and click "Process Text"/)).toBeInTheDocument();
  });
});