# Python GroupMe Minyanim Bot
- real minyan data not implemented yet - Coming later

## To start:  
- Clone this repo: ```git clone https://github.com/SZRabinowitz/groupme-minyan-bot```
- cd to the bot dir `cd groupme-minyan-bot`
- [Make a groupme bot](https://dev.groupme.com/bots). For now, leave the callback url empty.
- Install wasmer: 
```curl https://get.wasmer.io -sSfL | sh```
- Install uv ```curl -LsSf https://astral.sh/uv/install.sh | sh```
- login using `wasmer login`
- open wasmer.toml and replace `abc123` with the actual groupme bot id. 
 ```
 uv venv .env
source .env/bin/activate
uv pip install -r requirements.txt
wasmer deploy
```

Wasmer deploy will give you a deployement URL, use it for groupme bot callback url, with /minyanim at the end. 

Now, send /minyan in your group to get the minyan list. 
