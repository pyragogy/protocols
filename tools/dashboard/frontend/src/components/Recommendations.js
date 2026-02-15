import React, { useState, useEffect } from 'react';

export const Recommendations = ({ currentZc }) => {
  const [recommendations, setRecommendations] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (currentZc) {
      fetchRecommendations();
    }
  }, [currentZc]);

  const fetchRecommendations = async () => {
    try {
      setLoading(true);
      const res = await fetch('/api/recommendations');
      if (res.ok) {
        const data = await res.json();
        setRecommendations(data);
      }
    } catch (err) {
      console.error('Failed to fetch recommendations:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading-small">Loading AI recommendations...</div>;
  }

  if (!recommendations) {
    return <div className="no-data">No recommendations available.</div>;
  }

  return (
    <div className="recommendations">
      <div className="rec-section">
        <h3>📝 Summary</h3>
        <p>{recommendations.summary}</p>
      </div>

      <div className="rec-section">
        <h3>🚨 Immediate Actions</h3>
        <ul>
          {recommendations.immediate_actions.map((action, i) => (
            <li key={i}>{action}</li>
          ))}
        </ul>
      </div>

      <div className="rec-section">
        <h3>📅 This Week</h3>
        <ul>
          {recommendations.this_week.map((task, i) => (
            <li key={i}>{task}</li>
          ))}
        </ul>
      </div>

      <div className="rec-section">
        <h3>❌ Avoid</h3>
        <ul>
          {recommendations.avoid.map((anti, i) => (
            <li key={i}>{anti}</li>
          ))}
        </ul>
      </div>

      <div className="rec-section">
        <h3>✅ Success Criteria</h3>
        <ul>
          {recommendations.success_criteria.map((criteria, i) => (
            <li key={i}>{criteria}</li>
          ))}
        </ul>
      </div>

      {recommendations.context && (
        <div className="rec-context">
          <em>{recommendations.context}</em>
        </div>
      )}
    </div>
  );
};

export const StatsPanel = ({ stats }) => {
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

export default Recommendations;
