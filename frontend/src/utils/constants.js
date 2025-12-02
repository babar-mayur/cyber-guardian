export const API_BASE_URL = 'http://localhost:5000/api';

export const RISK_LEVELS = {
  CRITICAL: { min: 85, color: '#FF3B5C' },
  HIGH: { min: 70, color: '#FF8C42' },
  MEDIUM: { min: 60, color: '#FFD700' },
  LOW: { min: 0, color: '#00E676' }
};

export const FRAUD_TYPES = [
  'UPI Fraud',
  'Phishing',
  'Card Cloning',
  'Investment Scam',
  'SIM Swap',
  'ATM Skimming'
];
