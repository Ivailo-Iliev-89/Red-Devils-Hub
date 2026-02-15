async function loadPlayers() {
    try {
      const response = await fetch('/api/players/');
      if (!response.ok) throw new Error("Error with API");
      const players = await response.json();
      const table = document.getElementById("players-table");

      table.innerHTML = `
        <tr>
          <th>Player</th>
          <th>Position</th>
          <th>Number</th>
          <th>Nationality</th>
        </tr>
      `;

      players.forEach(player => {
        const row = table.insertRow();
        row.insertCell(0).textContent = player.name;
        row.insertCell(1).textContent = player.position;
        row.insertCell(2).textContent = player.number;
        row.insertCell(3).textContent = player.nationality;
      });

    } catch (error) {
      console.error("Error with loading the players:", error);
    }
  }

  window.onload = loadPlayers;