// Get tour data from the backend API
fetch('/api/tours')
    .then(response => response.json())
    .then(tours => {
        // Display tours on the page
        const tourList = document.getElementById('tour-list');
        tours.forEach(tour => {
            const tourItem = document.createElement('div');
            tourItem.innerHTML = `
                <h2>${tour.tour_name}</h2>
                <p>${tour.description}</p>
                <button>Book Now</button>
            `;
            tourList.appendChild(tourItem);
        });
    });
