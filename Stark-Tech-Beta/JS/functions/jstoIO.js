const { spawn } = require('child_process');
const path = require('path');
function getNewString(str) {
    // Find the last occurrence of the backslash
    const lastBackslashIndex = str.lastIndexOf('\\');
  
    // If a backslash is found, extract the substring to the right of it
    if (lastBackslashIndex !== -1) {
      return str.substring(lastBackslashIndex + 1);
    }
  
    // If no backslash is found, return the original string
    return str;
  }
function jstoIO(dataToSend) {
console.log('here')
  return new Promise((resolve, reject) => {

    const basePath = path.resolve(__dirname, './../../../../../../Stark-Tech-Beta-Backend/IO-Creator');
    
    const directoryPaths = path.join(basePath, 'get_datatojs.py')
    
    const pythonProcess = spawn('python', [directoryPaths]);
    dataToSend=getNewString(dataToSend)
    console.log("datatosend",dataToSend)
    // Send data to Python script
    pythonProcess.stdin.write(dataToSend);
    pythonProcess.stdin.end();

    let jsonData = [];

    // Handle output from Python script
    pythonProcess.stdout.on('data', (data) => {
      try {
        jsonData += data.toString(); // Append data to jsonData
      } catch (error) {
        console.error('Error parsing JSON:', error);
        reject(error); // Reject the Promise in case of parsing error
      }
    });

    // Handle errors
    pythonProcess.stderr.on('data', (data) => {
      console.error(`Error from Python script: ${data}`);
      reject(data); // Reject the Promise in case of error from Python script
    });

    // Handle process exit
    pythonProcess.on('close', (code) => {
      console.log(`Python process exited with code ${jsonData}`);
      resolve(jsonData); // Resolve the Promise with jsonData once the Python process exits
    });
  });
}

module.exports = { jstoIO };
