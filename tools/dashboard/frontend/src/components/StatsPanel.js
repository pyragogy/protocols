import React from 'react';

const StatsPanel = ({ stats }) => {
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

  return (
    <div className="stats-panel">
      <div className="stat-card">
        <div className="stat-label">Current Zc</div>
        <div className="stat-value" style={{ color: getZoneColor(stats.current_zone) }}>
          {stats.current_zc.toFixed(2)}
        </div>
      </div>

      <div className="stat-card">
        <div className="stat-label">7-Day Average</div>
        <div className="stat-value">{stats.avg_zc.toFixed(2)}</div>
      </div>

      <div className="stat-card">
        <div className="stat-label">Current Zone</div>
        <div className="stat-value" style={{ color: getZoneColor(stats.current_zone) }}>
          {stats.current_zone}
        </div>
      </div>

      <div className="stat-card">
        <div className="stat-label">Trend</div>
        <div className="stat-value">{stats.trend}</div>
      </div>

      <div className="stat-card full-width">
        <div className="stat-label">Zone Distribution (Last 7 Days)</div>
        <div className="zone-bars">
          <div className="zone-bar">
            <span className="zone-bar-label">🟢 Green</span>
            <div className="zone-bar-fill" style={{ 
              width: `${(stats.zone_distribution.GREEN / stats.data_points) * 100}%`,
              backgroundColor: '#16a34a'
            }}></div>
            <span className="zone-bar-count">{stats.zone_distribution.GREEN}</span>
          </div>
          <div className="zone-bar">
            <span className="zone-bar-label">🟡 Yellow</span>
            <div className="zone-bar-fill" style={{ 
              width: `${(stats.zone_distribution.YELLOW / stats.data_points) * 100}%`,
              backgroundColor: '#f59e0b'
            }}></div>
            <span className="zone-bar-count">{stats.zone_distribution.YELLOW}</span>
          </div>
          <div className="zone-bar">
            <span className="zone-bar-label">🔴 Red</span>
            <div className="zone-bar-fill" style={{ 
              width: `${(stats.zone_distribution.RED / stats.data_points) * 100}%`,
              backgroundColor: '#dc2626'
            }}></div>
            <span className="zone-bar-count">{stats.zone_distribution.RED}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default StatsPanel;
