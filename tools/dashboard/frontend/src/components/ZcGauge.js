import React from 'react';

const ZcGauge = ({ zc, zone }) => {
  const getZoneColor = (zone) => {
    switch (zone) {
      case 'GREEN':
        return '#16a34a';
      case 'YELLOW':
        return '#f59e0b';
      case 'RED':
        return '#dc2626';
      default:
        return '#808080';
    }
  };

  const getZoneEmoji = (zone) => {
    switch (zone) {
      case 'GREEN':
        return '🟢';
      case 'YELLOW':
        return '🟡';
      case 'RED':
        return '🔴';
      default:
        return '⚪';
    }
  };

  const color = getZoneColor(zone);
  const emoji = getZoneEmoji(zone);

  // Calculate gauge fill percentage (cap at 200% for display)
  const percentage = Math.min((zc / 2.0) * 100, 100);

  return (
    <div className="zc-gauge">
      <div className="gauge-container">
        <svg width="200" height="120" viewBox="0 0 200 120">
          {/* Background arc */}
          <path
            d="M 20 100 A 80 80 0 0 1 180 100"
            fill="none"
            stroke="#e5e7eb"
            strokeWidth="20"
            strokeLinecap="round"
          />
          {/* Colored arc */}
          <path
            d="M 20 100 A 80 80 0 0 1 180 100"
            fill="none"
            stroke={color}
            strokeWidth="20"
            strokeLinecap="round"
            strokeDasharray={`${percentage * 2.51} 251`}
            style={{ transition: 'stroke-dasharray 0.5s ease' }}
          />
          {/* Center text */}
          <text
            x="100"
            y="90"
            textAnchor="middle"
            fontSize="32"
            fontWeight="bold"
            fill={color}
          >
            {zc.toFixed(2)}
          </text>
        </svg>
      </div>
      <div className="zone-indicator">
        <span className="zone-emoji">{emoji}</span>
        <span className="zone-label" style={{ color }}>
          {zone} ZONE
        </span>
      </div>
    </div>
  );
};

export default ZcGauge;
