import React, { useState, useEffect } from 'react';
import './App.css';
import ZcGauge from './components/ZcGauge';
import HistoryChart from './components/HistoryChart';
import Recommendations from './components/Recommendations';
import StatsPanel from './components/StatsPanel';

function App() {
  const [currentZc, setCurrentZc] = useState(null);
  const [history, setHistory] = useState([]);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch data on mount and every 60 seconds
  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 60000);
    return () => clearInterval(interval);
  }, []);

  const fetchData = async () => {
    try {
      setLoading(true);
      
      // Fetch current Zc
      const currentRes = await fetch('/api/zc/current');
      if (currentRes.ok) {
        const currentData = await currentRes.json();
        setCurrentZc(currentData);
      }

      // Fetch history (last 7 days)
      const historyRes = await fetch('/api/zc/history?hours=168');
      if (historyRes.ok) {
        const historyData = await historyRes.json();
        setHistory(historyData.data || []);
      }

      // Fetch stats
      const statsRes = await fetch('/api/stats/summary');
      if (statsRes.ok) {
        const statsData = await statsRes.json();
        setStats(statsData);
      }

      setError(null);
    } catch (err) {
      setError('Failed to fetch data. Is the API running?');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (loading && !currentZc) {
    return (
      <div className="App">
        <div className="loading">
          <div className="spinner"></div>
          <p>Loading Curator AI Dashboard...</p>
        </div>
      </div>
    );
  }

  if (error && !currentZc) {
    return (
      <div className="App">
        <div className="error">
          <h2>Connection Error</h2>
          <p>{error}</p>
          <p>Make sure the backend API is running on port 8000:</p>
          <code>python tools/dashboard/backend/api.py</code>
        </div>
      </div>
    );
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>🎯 Curator AI Dashboard</h1>
        <p className="tagline">Real-time Cognitive Impedance Monitoring</p>
      </header>

      <div className="dashboard-grid">
        {/* Current Status */}
        <div className="panel panel-main">
          <h2>Current Status</h2>
          {currentZc ? (
            <>
              <ZcGauge zc={currentZc.zc} zone={currentZc.zone} />
              <div className="status-details">
                <div className="detail-item">
                  <span className="label">Mode:</span>
                  <span className={`mode mode-${currentZc.mode.toLowerCase().replace(' ', '-')}`}>
                    {currentZc.mode}
                  </span>
                </div>
                <div className="detail-item">
                  <span className="label">Trend:</span>
                  <span className={`trend trend-${currentZc.trend.toLowerCase()}`}>
                    {currentZc.trend}
                  </span>
                </div>
                <div className="detail-item">
                  <span className="label">Confidence:</span>
                  <span className="confidence">{(currentZc.confidence * 100).toFixed(0)}%</span>
                </div>
              </div>
              <div className="recommendation-box">
                <strong>Recommendation:</strong>
                <p>{currentZc.recommendation}</p>
              </div>
            </>
          ) : (
            <p>No data available. Calculate Zc to get started.</p>
          )}
        </div>

        {/* Stats Panel */}
        <div className="panel panel-stats">
          <h2>7-Day Statistics</h2>
          {stats && <StatsPanel stats={stats} />}
        </div>

        {/* History Chart */}
        <div className="panel panel-chart">
          <h2>Zc History (Last 7 Days)</h2>
          {history.length > 0 ? (
            <HistoryChart data={history} />
          ) : (
            <p>No historical data available.</p>
          )}
        </div>

        {/* AI Recommendations */}
        <div className="panel panel-recommendations">
          <h2>AI Recommendations</h2>
          <Recommendations currentZc={currentZc} />
        </div>
      </div>

      <footer className="App-footer">
        <p>CIM Pattern v3.0 | Curator AI Dashboard</p>
        <p>
          <a href="https://github.com/pyragogy/protocols" target="_blank" rel="noopener noreferrer">
            Documentation
          </a>
        </p>
      </footer>
    </div>
  );
}

export default App;
