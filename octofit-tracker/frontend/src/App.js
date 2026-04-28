import './App.css';

function App() {
  return (
    <div className="App">
      {/* Navigation Bar */}
      <nav className="navbar">
        <div className="navbar-container">
          <div className="navbar-brand">
            <img src="/octofitapp-small.svg" alt="OctoFit Logo" className="navbar-logo" />
            <span className="navbar-title">OctoFit Tracker</span>
          </div>
          <ul className="nav-menu">
            <li><a href="#home" className="nav-link">Home</a></li>
            <li><a href="#users" className="nav-link">Users</a></li>
            <li><a href="#activities" className="nav-link">Activities</a></li>
            <li><a href="#workouts" className="nav-link">Workouts</a></li>
            <li><a href="#leaderboard" className="nav-link">Leaderboard</a></li>
          </ul>
        </div>
      </nav>

      {/* Header */}
      <header className="app-header">
        <div className="header-content">
          <img src="/octofitapp-small.svg" alt="OctoFit" className="header-logo" />
          <h1 className="main-title">Welcome to OctoFit Tracker</h1>
          <p className="header-subtitle">Track your fitness journey with your team</p>
        </div>
      </header>

      {/* Main Content */}
      <main className="main-content">
        <section className="dashboard">
          <h2>Dashboard</h2>
          <div className="stats-grid">
            <div className="stat-card">
              <h3>Total Users</h3>
              <p className="stat-number">8</p>
            </div>
            <div className="stat-card">
              <h3>Teams</h3>
              <p className="stat-number">2</p>
            </div>
            <div className="stat-card">
              <h3>Workouts</h3>
              <p className="stat-number">3</p>
            </div>
          </div>

          {/* Sample Table */}
          <div className="table-container">
            <h2>Recent Activities</h2>
            <table className="data-table">
              <thead>
                <tr>
                  <th>User</th>
                  <th>Activity</th>
                  <th>Duration</th>
                  <th>Calories</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Iron Man</td>
                  <td>Running</td>
                  <td>60 min</td>
                  <td>600</td>
                </tr>
                <tr>
                  <td>Captain America</td>
                  <td>Weightlifting</td>
                  <td>75 min</td>
                  <td>500</td>
                </tr>
                <tr>
                  <td>Spider-Man</td>
                  <td>Swimming</td>
                  <td>60 min</td>
                  <td>550</td>
                </tr>
              </tbody>
            </table>
          </div>

          {/* Action Buttons */}
          <div className="action-buttons">
            <button className="btn btn-primary">View All Activities</button>
            <button className="btn btn-secondary">Add New Activity</button>
            <button className="btn btn-success">View Leaderboard</button>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="app-footer">
        <p>&copy; 2026 OctoFit Tracker. Build Applications with Copilot Agent Mode.</p>
      </footer>
    </div>
  );
}

export default App;