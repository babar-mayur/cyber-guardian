import { API_BASE_URL } from './constants';

const fetchAPI = async (endpoint, options = {}) => {
  try {
    const response = await fetch(\\\\, {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    });
    
    if (!response.ok) throw new Error(\API Error: \\);
    return await response.json();
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

export const api = {
  getPredictions: () => fetchAPI('/predictions'),
  getAlerts: () => fetchAPI('/alerts'),
  getLocations: () => fetchAPI('/locations'),
  submitComplaint: (data) => fetchAPI('/complaints', {
    method: 'POST',
    body: JSON.stringify(data),
  }),
};

export default api;
