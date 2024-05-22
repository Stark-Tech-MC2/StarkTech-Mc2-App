const { remote, dialog } = require('electron');

function directory(opendirectory) {  
    console.log('Attempting to open directory:', opendirectory);
  
    try {
        // Show a file selection dialog for the specified directory
        const result = dialog.showOpenDialogSync({
            defaultPath: opendirectory,
            properties: ['openFile'] // Selects a file
        });
  
        if (result && result.length > 0) {
            // If a file is selected, return its path
            return result[0];
        } else {
            // If no file is selected or selection is canceled, return null
            return null;
        }
    } catch (error) {
        console.error('Error opening directory dialog:', error);
        return null;
    }
  }

module.exports = { directory };
