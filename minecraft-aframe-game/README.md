# Minecraft A-Frame Game

This folder contains a small A-Frame / WebVR project built by Yixuan Sun.

Files of interest
- `index.html` — open this to run the game: `/minecraft-aframe-game/index.html`
- `models/` — glTF models used by the scene (`model.gltf`, `Hamburger.gltf` and their .bin files)
- `images/` — textures and UI images used by the scene (e.g. `shovel.png`, `silver.jpg`, `Hamburger_BaseColor.png`)
- `sounds/` — audio files used by the scene (e.g. `minecraft.mp3`, `villager.mp3`)

How to run locally
1. Clone the repository and change into the repo root:
   - `git clone https://github.com/chezzycheddars/yixuan-sun-portfolio.git`
   - `cd yixuan-sun-portfolio`
2. Start a simple static server from the repo root (this ensures the models and textures load correctly):
   - Python 3: `python -m http.server 8000`
   - OR: `npx http-server .`
3. Open the game in your browser:
   - `http://localhost:8000/minecraft-aframe-game/index.html`

Publishing with GitHub Pages
- To make the game playable from the web, enable GitHub Pages and publish the repository (Settings → Pages). The game's URL will be:
  `https://chezzycheddars.github.io/yixuan-sun-portfolio/minecraft-aframe-game/`

Notes & troubleshooting
- If the scene fails to load, open the browser Developer Console (F12) and look for 404 errors — they indicate missing files or wrong paths.
- Large textures (e.g. `Hamburger_BaseColor.png`) may slow initial load. Consider optimizing images if load time is an issue.

If you want, I can also add a root-level `index.html` redirect so visiting the repo root opens this game automatically.
