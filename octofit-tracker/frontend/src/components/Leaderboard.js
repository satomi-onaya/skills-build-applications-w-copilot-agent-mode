import React, { useState, useEffect } from 'react';

const CODESPACE_NAME = process.env.REACT_APP_CODESPACE_NAME || 'localhost';
const API_URL = `https://${CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    console.log('Fetching leaderboard from:', API_URL);
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        console.log('Leaderboard data:', data);
        setLeaderboard(data.results || data);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-3">Leaderboard</h2>
      <table className="table table-striped table-bordered">
        <thead className="table-dark">
          <tr>
            <th>Rank</th>
            <th>User</th>
            <th>Team</th>
            <th>Total Calories Burned</th>
            <th>Total Activities</th>
          </tr>
        </thead>
        <tbody>
          {leaderboard.map((entry, i) => (
            <tr key={i}>
              <td>{entry.rank}</td>
              <td>{entry.user}</td>
              <td>{entry.team}</td>
              <td>{entry.total_calories_burned}</td>
              <td>{entry.total_activities}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Leaderboard;