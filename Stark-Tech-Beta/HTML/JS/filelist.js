// In your renderer process JavaScript file (e.g., renderer.js)

const { readdirSync } = require('fs');
const { shell } = require('electron');

// Replace '/path/to/your/directory' with the actual path to your directory
const basePath2 = path.resolve(__dirname, '../../Stark-Tech-Beta-Backend/VaV Replicator/CreatedVAV');
const directory = path.join(basePath2, '4-5-2024');

// Function to fetch file list from the directory
function fetchFileList() {
    try {
        const files = readdirSync(directory);
        return files;
    } catch (error) {
        console.error('Error fetching file list:', error);
        return [];
    }
}

// Function to handle link click event
function handleLinkClick(event) {
    event.preventDefault(); // Prevent default link behavior
    const filePath = this.getAttribute('data-filepath');
    shell.openPath(filePath); // Open the folder in the system file explorer
}

// Function to generate file links
function generateFileLinks(files) {
    const fileList = document.getElementById('fileList');
    fileList.innerHTML = ''; // Clear existing file list

    files.forEach(file => {
        const listItem = document.createElement('li');
        const link = document.createElement('a');
        const filePath = path.join(directory, file);
        link.href = '#'; // Set href to '#' to prevent default navigation behavior
        link.textContent = file;
        link.setAttribute('data-filepath', filePath); // Store file path as a data attribute
        link.addEventListener('click', handleLinkClick); // Attach click event listener
        listItem.appendChild(link);
        fileList.appendChild(listItem);
    });
}

// Call the function to fetch file list and generate file links
document.addEventListener('DOMContentLoaded', () => {
    const files = fetchFileList();
    generateFileLinks(files);
});
