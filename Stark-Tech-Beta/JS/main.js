const { jstoXml } = require('./functions/jstoXml');
const {jstoIO} = require('./functions/jstoIO')
const {directory} = require('./functions/spreadsheetdirectory')
const fs = require('fs');
const path = require('path');
const { app, BrowserWindow, ipcMain, dialog,remote } = require('electron');

// Serialize data into JSON format

function createWindow() {
  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 900,
    height: 600,
    icon: `../../Stark-Tech-Beta/Icon/favicon.ico`,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      devTools: true,
      autoHideMenuBar: true,
    }
  });
  mainWindow.setMenuBarVisibility(false)
  const basePath = path.resolve(__dirname, '../../Stark-Tech-Beta/HTML');
    
    const directoryPaths = path.join(basePath, 'home.html')

  const indexPath = directoryPaths;
  console.log("Base path:", basePath);
  console.log("Full path to home.html:", directoryPaths);

  // Load your app's HTML file using the correct path
  
  mainWindow.loadFile('HTML/home.html');
  
}

SCRVAV = '';
CoolingOnlyVAV = '';
Spreadsheet ='';
StagedVaV = '';
iospreadsheet = '';
ipcMain.on('testMessage', (event, message) => {
  console.log('Received message from renderer:', message);
});

ipcMain.on('selectedFile2', (event, filePath1) => {

  // Print the values of the variables
  iospreadsheet=filePath1
  print(filePath1);
});
ipcMain.on('selectedFile', (event, filePath) => {
  if (filePath.includes("Spreadsheets"))
      Spreadsheet = filePath;
 
  if (filePath.includes("Template Cooling Only VAV Controlers"))
      CoolingOnlyVAV = filePath;

  if (filePath.includes("Template VAV SCR Controlers"))
      SCRVAV = filePath;
  
  if (filePath.includes("Template Staged Heating VAV Controlers"))
      StagedVaV = filePath;
  
  // Print the values of the variables
  print(Spreadsheet, CoolingOnlyVAV, SCRVAV, StagedVaV);
});


function print(Spreadsheet, CoolingOnlyVAV, SCRVAV, StagedVaV) {
  console.log("ioiospreadsheet",iospreadsheet)
  console.log("Spreadsheet:", Spreadsheet);
  console.log("CoolingOnlyVAV:", CoolingOnlyVAV);
  console.log("SCRVAV:", SCRVAV);
  console.log("StagedVaV:", StagedVaV);
}



ipcMain.on('trigger-python-code', async () => {
  if (Spreadsheet && CoolingOnlyVAV && SCRVAV && StagedVaV) {
    try {
      const dataToSend = JSON.stringify({ SCRVAV, CoolingOnlyVAV, Spreadsheet, StagedVaV });
      const information = await jstoXml(dataToSend);
      //console.log(information); // Log the information received from Python
      // Inside your trigger-python-code handler
if (mainWindow && !mainWindow.isDestroyed() && mainWindow.webContents) {
  console.log('Sending information to renderer process:', information);
  mainWindow.webContents.send('data-from-main', information);
} else {
  console.error('Error: Unable to send data to mainWindow');
}

    } catch (error) {
      console.error('Error:', error);
    }
  } else {
    alert.apply("select a option")
    console.log('No file selected.');
  }
});

ipcMain.on('trigger2-python2-code2', async () => {
  console.log('here')
  if (iospreadsheet) {
    try {
      
      const information2 = await jstoIO(iospreadsheet);
      console.log(information2); // Log the information received from Python

      if (mainWindow && !mainWindow.isDestroyed() && mainWindow.webContents) {
        console.log('Sending information to renderer process:', information2);
        mainWindow.webContents.send('data2-from2-main2', information2);
      } else {
        console.error('Error: Unable to send data to mainWindow');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }
});






ipcMain.on('file-selected', (event, filePath) => {
  console.log('Selected file path:', filePath);
  // Do something with the selected file path
});


app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
