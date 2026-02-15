const players = [
    {name: "Senne Lammens", position: "Goalkeeper", number: 31, nationality: "Belgium"},
    {name: "Harry Maguire", position: "Defender", number: 5, nationality: "England"},
    {name: "Lisandro Martínez", position: "Defender", number: 6, nationality: "Argentina"},
    {name: "Luke Show", position: "Left-back", number: 23, nationality: "England"},
    {name: "Diogo Dalot", position: "Right-back", number: 2, nationality: "Portugal"},
    {name: "Bruno Fernandes", position: "Midfielder", number: 8, nationality: "Portugal"},
    {name: "Casemiro", position: "Midfielder", number: 18, nationality: "Brazil"},
    {name: "Bryan Mbuemo", position: "Forward", number: 19, nationality: "Camerun"},
    {name: "Mateus Cunha", position: "Forward", number: 10, nationality: "Brazil"},
    {name: "Amad Diallo", position: "Forward", number: 16, nationality: "Ivory Coast"},
    {name: "Benjamin Šeško", position: "Striker", number: 30, nationality: "Slovenia"},
    ];

    const table = document.getElementById("players-table");

    players.forEach(player => {
    const row = table.insertRow();
    row.insertCell(0).textContent = player.name;
    row.insertCell(1).textContent = player.position;
    row.insertCell(2).textContent = player.number;
    row.insertCell(3).textContent = player.nationality;
    });