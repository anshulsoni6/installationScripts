import os

os.system('sudo apt-get update && sudo apt-get install build-essential libssl-dev && curl -sL https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh -o install_nvm.sh && bash install_nvm.sh && source ~/.profile')

nodeJsVersion = input('Enter Node.js version that you want to install : ')

if(nodeJsVersion == 'lts'):
    os.system('nvm install --' + nodeJsVersion + '&& node -v')
else:
    os.system('nvm install '+ nodeJsVersion + ' && nvm use ' + nodeJsVersion + ' && node -v')
