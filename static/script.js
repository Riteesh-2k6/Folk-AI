document.addEventListener('DOMContentLoaded', function() {
    // Get the modal
    const modal = document.getElementById('transformInterface');
    console.log('Modal element:', modal);
    
    // Get all elements that should open the modal
    const openModalElements = [
        document.getElementById('openInterface'),  // The big circle
        document.getElementById('tryItBtn')       // The Try It button
    ];
    console.log('Open modal elements:', openModalElements);
    
    // Get the close button and form
    const closeBtn = document.querySelector('.close');
    const form = document.getElementById('transformForm');
    const progressContainer = document.querySelector('.progress-container');
    
    // Function to open modal
    function openModal() {
        console.log('Opening modal');
        modal.style.display = 'block';
    }
    
    // Function to close modal
    function closeModal() {
        console.log('Closing modal');
        modal.style.display = 'none';
        if (form) {
            form.reset();
            progressContainer.style.display = 'none';
        }
    }
    
    // Add click event to all elements that should open the modal
    openModalElements.forEach((element, index) => {
        if (element) {
            element.addEventListener('click', openModal);
        }
    });
    
    // Close modal when clicking the close button
    if (closeBtn) {
        closeBtn.addEventListener('click', closeModal);
    }
    
    // Close modal when clicking outside of it
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            closeModal();
        }
    });
    
    // Handle form submission
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            
            const folkSong = document.getElementById('folkSongInput').value;
            const artStyle = document.getElementById('artworkType').value;
            
            if (!folkSong.trim()) {
                alert('Please enter a folk song');
                return;
            }
            
            if (!artStyle) {
                alert('Please select an art style');
                return;
            }
            
            // Show progress bar
            progressContainer.style.display = 'block';
            
            // Create form data
            const formData = new FormData();
            formData.append('folkSongInput', folkSong);
            formData.append('artworkType', artStyle);
            
            // Submit the form
            fetch('/transform', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    return response.text().then(text => {
                        throw new Error(text || 'Server error');
                    });
                }
                return response.text();
            })
            .then(html => {
                // Replace page content with response
                document.documentElement.innerHTML = html;
                window.scrollTo(0, 0);
            })
            .catch(error => {
                console.error('Error:', error);
                progressContainer.style.display = 'none';
                alert(error.message || 'An error occurred. Please try again.');
            });
        });
    }
});
