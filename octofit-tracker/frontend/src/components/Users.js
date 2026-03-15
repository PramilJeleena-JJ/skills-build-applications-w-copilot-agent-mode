import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const endpoint = `${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    const url = `https://${endpoint}`;
    fetch(url)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setUsers(results);
        console.log('Users endpoint:', url);
        console.log('Fetched users:', results);
      })
      .catch(err => console.error('Error fetching users:', err));
  }, [endpoint]);

  return (
    <div className="card mt-4">
      <div className="card-body">
        <h2 className="card-title text-warning">Users</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead>
              <tr>
                <th>Name</th>
                <th>ID</th>
              </tr>
            </thead>
            <tbody>
              {users.map((user, idx) => (
                <tr key={user.id || idx}>
                  <td>{user.name || JSON.stringify(user)}</td>
                  <td>{user.id || idx}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Users;
