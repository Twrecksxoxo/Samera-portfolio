@echo off
cd /d "D:\Samera portfolio"
echo Adding all files...
git add -A
echo Committing changes...
git commit -m "Replace pg28 with new WhatsApp image, cache-busting v5"
echo Pushing to GitHub...
git push origin main
echo Done!
pause
