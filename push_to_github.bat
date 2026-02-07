@echo off
cd /d "D:\Samera portfolio"
echo Adding all files...
git add -A
echo Committing changes...
git commit -m "Update portfolio pg28, add conversion scripts, cache-busting v4"
echo Pushing to GitHub...
git push origin main
echo Done!
pause
