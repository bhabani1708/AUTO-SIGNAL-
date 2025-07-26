const { exec } = require("child_process");

// Start keep_alive.js
require("./keep_alive");

// Run Python bot
exec("python3 main.py", (error, stdout, stderr) => {
  if (error) {
    console.error(`❌ Error: ${error.message}`);
    return;
  }
  if (stderr) {
    console.error(`⚠️ Stderr: ${stderr}`);
    return;
  }
  console.log(`✅ Output: ${stdout}`);
});
