import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const codespaceBase = process.env.REACT_APP_CODESPACE_NAME || 'localhost:8000';
        const apiUrl = codespaceBase.includes('http')
          ? `${codespaceBase}/api/teams/`
          : `https://${codespaceBase}-8000.app.github.dev/api/teams/`;

        console.log('API URL:', apiUrl);

        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Fetched Teams Data:', data);

        // Handle both paginated and plain array responses
        const teamsData = data.results || data;
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching teams:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchTeams();
  }, []);

  if (loading) return <div className="loading">Loading teams...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <div className="table-container">
      <h2>Teams</h2>
      <table className="data-table table table-striped table-hover">
        <thead>
          <tr>
            <th>Team Name</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {teams.length > 0 ? (
            teams.map((team, index) => (
              <tr key={index}>
                <td>
                  <span className="badge bg-primary">{team.name}</span>
                </td>
                <td>{team.description || 'No description'}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="2" className="text-center">
                No teams found
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default Teams;
