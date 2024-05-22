const { ipcRenderer } = require('electron');
const fs = require('fs');
const path = require('path');
const basePath = path.resolve(__dirname, './../../../../../Stark-Tech-Beta-Backend/VaV Replicator');
const directoryPaths = [
  path.join(basePath, 'Template Cooling Only VAV Controlers'),
  path.join(basePath, 'Spreadsheets'),
  path.join(basePath, 'Template VAV SCR Controlers'),
  path.join(basePath, 'Template Staged Heating VAV Controlers')
];

// Prevent default drag behaviors
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  document.body.addEventListener(eventName, preventDefaults, false);
});

// Highlight drop area when dragging over
['dragenter', 'dragover'].forEach(eventName => {
  document.getElementById('drop-area').addEventListener(eventName, highlight, false);
});

['dragleave', 'drop'].forEach(eventName => {
  document.getElementById('drop-area').addEventListener(eventName, unhighlight, false);
});

// Handle dropped files
document.getElementById('drop-area').addEventListener('drop', handleDrop, false);
document.getElementById('drop-area1').addEventListener('drop', handleDrop1, false);
document.getElementById('drop-area2').addEventListener('drop', handleDrop2, false);
document.getElementById('drop-area3').addEventListener('drop', handleDrop3, false);

function preventDefaults(e) {
  e.preventDefault();
  e.stopPropagation();
}

function highlight() {
  document.getElementById('drop-area').classList.add('highlight');
}

function unhighlight() {
  document.getElementById('drop-area').classList.remove('highlight');
}

function handleDrop(e) {
  const dt = e.dataTransfer;
  const files = dt.files;

  handleFiles(files);
  window.location.reload(); // Reload the page
}

function handleDrop1(e) {
  const dt = e.dataTransfer;
  const files = dt.files;

  handleFiles1(files);
  window.location.reload(); // Reload the page
}

function handleDrop2(e) {
  const dt = e.dataTransfer;
  const files = dt.files;

  handleFiles2(files);
  window.location.reload(); // Reload the page
}

function handleDrop3(e) {
  const dt = e.dataTransfer;
  const files = dt.files;

  handleFiles3(files);
  window.location.reload(); // Reload the page
}

// Spreadsheets
function handleFiles(files) {
  const destination = directoryPaths[1];

  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const filePath = file.path;
    const fileName = path.basename(filePath);
    const destinationPath = path.join(destination, fileName);

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

// Template VAV SCR Controllers
function handleFiles1(files) {
  const destination = directoryPaths[2];

  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const filePath = file.path;
    const fileName = path.basename(filePath);
    const destinationPath = path.join(destination, fileName);

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

// Cooling Only
function handleFiles2(files) {
  const destination = directoryPaths[0];

  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const filePath = file.path;
    const fileName = path.basename(filePath);
    const destinationPath = path.join(destination, fileName);

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

// Template Staged Heating VAV Controllers
function handleFiles3(files) {
  const destination = directoryPaths[3];

  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const filePath = file.path;
    const fileName = path.basename(filePath);
    const destinationPath = path.join(destination, fileName);

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
