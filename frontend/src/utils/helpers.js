export const formatCurrency = (amount) => {
  if (amount >= 10000000) return \₹\Cr\;
  if (amount >= 100000) return \₹\L\;
  if (amount >= 1000) return \₹\K\;
  return \₹\\;
};

export const timeAgo = (date) => {
  const seconds = Math.floor((new Date() - new Date(date)) / 1000);
  if (seconds < 60) return 'just now';
  if (seconds < 3600) return \\ min ago\;
  if (seconds < 86400) return \\ hours ago\;
  return \\ days ago\;
};

export const getRiskColor = (risk) => {
  if (risk >= 85) return '#FF3B5C';
  if (risk >= 70) return '#FF8C42';
  if (risk >= 60) return '#FFD700';
  return '#00E676';
};
