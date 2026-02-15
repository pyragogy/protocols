import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ReferenceLine } from 'recharts';

const HistoryChart = ({ data }) => {
  // Format data for Recharts
  const chartData = data.map(point => ({
    timestamp: new Date(point.timestamp).toLocaleDateString(),
    zc: point.zc,
    zone: point.zone
  }));

  // Custom tooltip
  const CustomTooltip = ({ active, payload }) => {
    if (active && payload && payload.length) {
      const data = payload[0].payload;
      return (
        <div className="custom-tooltip">
          <p className="date">{data.timestamp}</p>
          <p className="zc">Zc: <strong>{data.zc}</strong></p>
          <p className="zone">Zone: <strong>{data.zone}</strong></p>
        </div>
      );
    }
    return null;
  };

  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart data={chartData}>
        <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
        <XAxis 
          dataKey="timestamp" 
          stroke="#9ca3af"
          tick={{ fill: '#9ca3af' }}
        />
        <YAxis 
          stroke="#9ca3af"
          tick={{ fill: '#9ca3af' }}
          domain={[0, 'auto']}
        />
        <Tooltip content={<CustomTooltip />} />
        <Legend />
        
        {/* Reference lines for thresholds */}
        <ReferenceLine 
          y={0.7} 
          label="Green/Yellow" 
          stroke="#f59e0b" 
          strokeDasharray="3 3" 
        />
        <ReferenceLine 
          y={1.0} 
          label="Yellow/Red" 
          stroke="#dc2626" 
          strokeDasharray="3 3" 
        />
        
        {/* Main Zc line */}
        <Line 
          type="monotone" 
          dataKey="zc" 
          stroke="#3b82f6" 
          strokeWidth={3}
          dot={{ r: 4 }}
          activeDot={{ r: 6 }}
        />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default HistoryChart;
