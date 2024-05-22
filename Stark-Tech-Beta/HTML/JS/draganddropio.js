const { ipcRenderer } = require('electron');
const fs = require('fs');
const path = require('path');

// Base directory path for spreadsheets
const basePath = path.resolve(__dirname, './../../../../../Stark-Tech-Beta-Backend/IO-Creator');
const spreadsheetPath = path.join(basePath, 'SpreadSheets');

// Prevent default drag behaviors
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  document.body.addEventListener(eventName, preventDefaults, false);
});

// Add event listeners for the drop area
const dropArea = document.getElementById('drop-areaIO');
['dragenter', 'dragover'].forEach(eventName => {
  dropArea.addEventListener(eventName, highlight, false);
});
['dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, unhighlight, false);
});
dropArea.addEventListener('drop', handleDrop, false);

function preventDefaults(e) {
  e.preventDefault();
  e.stopPropagation();
}

function highlight() {
  dropArea.classList.add('highlight');
}

function unhighlight() {
  dropArea.classList.remove('highlight');
}

function handleDrop(e) {
  const dt = e.dataTransfer;
  const files = dt.files;

  handleFiles(files);
  window.location.reload(); // Reload the page
}

// Handle files dropped into the drop area
function handleFiles(files) {
  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const filePath = file.path;
    const fileName = path.basename(filePath);
    const destinationPath = path.join(spreadsheetPath, fileName);

    // Copy the file to the destination directory
    fs.copyFile(filePath, destinationPath, (err) => {
      if (err) {
        console.error('Error copying file:', err);
      } else {
        console.log('File copied successfully:', fileName);
      }
    });
  }
}
