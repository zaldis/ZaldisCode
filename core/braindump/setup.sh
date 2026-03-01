cp ./braindump.py ~/.local/bin/braindump
{ echo "#!/usr/bin/python3"; cat ~/.local/bin/braindump; } > tmp && mv tmp ~/.local/bin/braindump
chmod +x ~/.local/bin/braindump
echo "Now you can dump your knowledge with 'braindump' command"
