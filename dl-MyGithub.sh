mkdir /home/pi/Scripts/github
cd /home/pi/Scripts/github
USER=mattsage;PAGE=1; curl "https://api.github.com/users/$USER/repos?page=$PAGE&per_page=100" | grep -e 'git_url*' | cut -d \" -f 4 | xargs -L1 git clone
cd
