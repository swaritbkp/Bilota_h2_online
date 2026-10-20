const { spawnSync } = require('child_process');
const prompt = "Option 2: Holistic Wellness & Lifestyle Companion with Personal Health & Vitals Hub. Mobile app screen for Bilota Abu Dhabi Feline Health Companion featuring a living Arabian Sand Cat avatar that reflects recovery vitals, Judge Control Bar with Malaffi age and biometric sync, daily vitals telemetry cards for heat index, hydration, resting heart rate, and sleep, non-punitive momentum bank with streak shield, BCT 8.7 micro-action recommendations, and family oasis blessings.";

console.log("Generating screen with prompt:", prompt);
const res = spawnSync('stitch.cmd', [
  'generate', 'screen',
  '-p', '2571664629787442847',
  '--device', 'MOBILE',
  '--title', 'Bilota Living Companion Screen',
  '--prompt', `"${prompt.replace(/"/g, '\\"')}"`,
  '--json'
], {
  shell: true,
  env: { ...process.env, HOME: process.env.USERPROFILE },
  encoding: 'utf-8',
  maxBuffer: 20 * 1024 * 1024
});

if (res.error) {
  console.error("Execution error:", res.error);
} else {
  console.log(res.stdout || res.stderr);
}
