const os = require('os');

const userDirectory = os.homedir(); // Get the user's home directory

document.addEventListener('DOMContentLoaded', function () {
    const radioGroupsDiv = document.getElementById('radioGroups');
    const basePath = path.resolve(__dirname, './../../../../../Stark-Tech-Beta-Backend/VaV Replicator');

const directoryPaths = [
    path.join(basePath, 'Template Cooling Only VAV Controlers'),
    path.join(basePath, 'Spreadsheets'),
    path.join(basePath, 'Template VAV SCR Controlers'),
    path.join(basePath, 'Template Staged Heating VAV Controlers')
];

    directoryPaths.forEach(function (directoryPath, index) {
        createRadioGroup(`Radio Group ${index + 1}`, directoryPath);
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const radioGroupsDiv = document.getElementById('radioGroups2');
    const basePath = path.resolve(__dirname, './../../../../../Stark-Tech-Beta-Backend/IO-Creator');

const directoryPaths = [
    path.join(basePath, 'SpreadSheets')
];

    directoryPaths.forEach(function (directoryPath, index) {
        createRadioGroup2(`Radio Group ${index + 1}`, directoryPath);
    });
});

function createRadioGroup(groupName, directoryPath) {
    const groupDiv = document.createElement('div');

    
    // Use a regular expression to find the last occurrence of '\'
// Use a regular expression to find the last occurrence of '\'
const lastBackslashRegex = /\\([^\\]+)\\?$/;
const lastBackslashMatch = directoryPath.match(lastBackslashRegex);

if (lastBackslashMatch) {
    // Extract the path before the last '\'
    const pathBeforeLastBackslash = directoryPath.substring(0, lastBackslashMatch.index);

    // Extract the path after the last '\'
    const pathAfterLastBackslash = lastBackslashMatch[1];

    // Construct the new HTML content
    const newHTML = `<h2>${pathAfterLastBackslash}</h2>`;

    // Set the new HTML content
    groupDiv.innerHTML = newHTML;
} else {
    // If no match is found, set the groupDiv inner HTML with just the directoryPath
    groupDiv.innerHTML = `<h2>${directoryPath}</h2>`;
}


    fs.readdir(directoryPath, function (err, files) {
        if (err) {
            console.error('Error reading directory:', err);
            return;
        }

        files.forEach(function (file) {
          const filePath = path.join(directoryPath, file);
          const optionName = path.basename(file, path.extname(file));
          const div = document.createElement('div');
          const input = document.createElement('input');
          input.type = 'radio';
          input.name = groupName;
          input.value = filePath; // Set the value to the file path
          input.id = optionName;
      
          const label = document.createElement('label');
          label.setAttribute('for', optionName);
          label.textContent = optionName;
      
          input.addEventListener('change', function () {
              if (this.checked) {
                  console.log('Selected file:', filePath); // Check if this log appears in the console
                  ipcRenderer.send('selectedFile', filePath); // Sending the file path
              }
          });
      
          div.appendChild(input);
          div.appendChild(label);
          groupDiv.appendChild(div);
      });
    });

    document.getElementById('radioGroups').appendChild(groupDiv);
}
function createRadioGroup2(groupName, directoryPath) {
    const groupDiv = document.createElement('div');

    
    // Use a regular expression to find the last occurrence of '\'
// Use a regular expression to find the last occurrence of '\'
const lastBackslashRegex = /\\([^\\]+)\\?$/;
const lastBackslashMatch = directoryPath.match(lastBackslashRegex);

if (lastBackslashMatch) {
    // Extract the path before the last '\'
    const pathBeforeLastBackslash = directoryPath.substring(0, lastBackslashMatch.index);

    // Extract the path after the last '\'
    const pathAfterLastBackslash = lastBackslashMatch[1];

    // Construct the new HTML content
    const newHTML = `<h2>${pathAfterLastBackslash}</h2>`;

    // Set the new HTML content
    groupDiv.innerHTML = newHTML;
} else {
    // If no match is found, set the groupDiv inner HTML with just the directoryPath
    groupDiv.innerHTML = `<h2>${directoryPath}</h2>`;
}


    fs.readdir(directoryPath, function (err, files) {
        if (err) {
            console.error('Error reading directory:', err);
            return;
        }

        files.forEach(function (file) {
          const filePath2 = path.join(directoryPath, file);
          const optionName = path.basename(file, path.extname(file));
          const div = document.createElement('div');
          const input = document.createElement('input');
          input.type = 'radio';
          input.name = groupName;
          input.value = filePath2; // Set the value to the file path
          input.id = optionName;
      
          const label = document.createElement('label');
          label.setAttribute('for', optionName);
          label.textContent = optionName;
      
          input.addEventListener('change', function () {
              if (this.checked) {
                  console.log('Selected file:', filePath2); // Check if this log appears in the console
                  ipcRenderer.send('selectedFile2', filePath2); // Sending the file path
              }
          });
      
          div.appendChild(input);
          div.appendChild(label);
          groupDiv.appendChild(div);
      });
    });

    document.getElementById('radioGroups2').appendChild(groupDiv);
}


ipcRenderer.on('data-from-main', (event, information) => {
  console.log('Received information from main process:', information);
  information = information.replace(/\(|\)/g, '\n');

  // Replace new line characters with HTML line breaks
  information = information.replace(/\n/g, '<br>');

  // Display the updated information in HTML
  const informationContainer = document.getElementById('information-container');
  informationContainer.innerHTML = information;

  // Your code for fetching file list and generating file links
  const { readdirSync } = require('fs');
  const { shell } = require('electron');
  const path = require('path');

  const basePath2 = path.resolve(__dirname, './../../../../../Stark-Tech-Beta-Backend/VaV Replicator/CreatedVAV');
  const directory = path.join(basePath2, '4-5-2024');

  function fetchFileList() {
      try {
          const files = readdirSync(directory);
          return files;
      } catch (error) {
          console.error('Error fetching file list:', error);
          return [];
      }
  }

  function handleLinkClick(event) {
      event.preventDefault(); // Prevent default link behavior
      const filePath = this.getAttribute('data-filepath');
      shell.openPath(directory); // Open the folder in the system file explorer
  }

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
  const files = fetchFileList();
  generateFileLinks(files);
});



ipcRenderer.on('data2-from2-main2', (event, information) => {
    console.log('Received information from main process:', information);
    information = information.replace(/\(|\)/g, '\n');
  
    // Replace new line characters with HTML line breaks
    information = information.replace(/\n/g, '<br>');
  
    // Display the updated information in HTML
    const informationContainer = document.getElementById('information2-container2');
    informationContainer.innerHTML = information;
  
    // Your code for fetching file list and generating file links
    const { readdirSync } = require('fs');
    const { shell } = require('electron');
    const path = require('path');
  
    const basePath2 = path.resolve(__dirname, './../../../../../Stark-Tech-Beta-Backend/IO-Creator');
    const directory = path.join(basePath2, 'CreatedIO');
  
    function fetchFileList() {
        try {
            const files = readdirSync(directory);
            return files;
        } catch (error) {
            console.error('Error fetching file list:', error);
            return [];
        }
    }
  
    function handleLinkClick(event) {
        event.preventDefault(); // Prevent default link behavior
        const filePath = this.getAttribute('data-filepath');
        shell.openPath(directory); // Open the folder in the system file explorer
    }
  
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
    const files = fetchFileList();
    generateFileLinks(files);
  });



console.log('Renderer process initialized.');

document.addEventListener('DOMContentLoaded', () => {
    const ioGenerateButton = document.getElementById('iogenerateiobutton');
    const generateVavButton = document.getElementById('generatevavbutton');
  
    if (ioGenerateButton) {
      ioGenerateButton.addEventListener('click', () => {
        // Trigger Python code
        console.log('we are here');
        ipcRenderer.send('trigger2-python2-code2');
      });
    } else {
      console.error('Element with id "iogenerateiobutton" not found.');
    }
  
    if (generateVavButton) {
      generateVavButton.addEventListener('click', () => {
        // Trigger Python code
        console.log('we are here');
        ipcRenderer.send('trigger-python-code');
      });
    } else {
      console.error('Element with id "generatevavbutton" not found.');
    }
  });

document.getElementById('opendirectory').addEventListener('click', () => {
  // Open directory
  
  ipcRenderer.send('trigger-directory-code');
});

document.getElementById('coolingButton').addEventListener('click', () => {
  // Trigger Python code
  ipcRenderer.send('trigger-CoolingDirectory-code');
});

document.getElementById('scrButton').addEventListener('click', () => {
  // Open directory
  ipcRenderer.send('trigger-scrdirectory-code');
});

document.getElementById('stagedButton').addEventListener('click', () => {
  // Trigger Python code
  ipcRenderer.send('trigger-stageddirectory-code');
});



// Listen for selected directory event
ipcRenderer.on('selected-directory', (event, directory) => {
  console.log('Selected directory:', directory);
  // Do something with the selected directory path
});
