fetch('/api/projects')
    .then(response => response.json())
    .then(data => {
        console.log('Projects:', data);
    });