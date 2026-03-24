# Random Number Generator
This python program is for generating random numbers. You can input the range in which the random number will be pointed out in.
> [!Note]
> I do not make an executable for Linux. So if you use Linux, please, build it your own. It only takes less than 3 minutes, and it's effortless.

## Downloading binaries
I have build the Windows binaries myself, and can be downloaded in the releases page.
> [!Warning]
> If Windows smartscreen flags the file, it is a false positive. It flags my software because it does not have proper certificate/signed binary. And doing so can cost me money, which I don't really have right now.

## Building the software
If you want to build the software on your own, you can. The instructions to do so are listed below.
### For Windows
Open CMD in any directory, and then clone the GitHub repository by typing in this command:
```bash
git clone https://github.com/pixelated11/random-number-generator.git
```
And locate yourself to the directory by running:
```bash
cd random-number-generator
```
After that, install the required pip packages by running:
```bash
pip install -r requirements.txt
```
After that, run this command to build the executable:
```bash
pyinstaller --onefile --noconsole program.py
```
After the building is complete, your executable should be located in the `dists` folder.
### For Linux
Open up your terminal, then clone the repository:
```bash
git clone https://github.com/pixelated11/random-number-generator.git
```
Then, install pip requirements by running:
```bash
pip install -r requirements.txt --break-system-packages
```
After that, try to find the pyinstaller location, and type in this command:
```bash
pyinstaller --onefile program.py
```
And your executable should be in the `dists` folder. To run it, just simply type:
```bash
./dists/program
```
Without changing directories.

## Contributing
It would be appreciated to contribute in this project. If you want any improvements, please, do e-mail me at: itspixelatd@proton.me
**Starring the repo is very kind, and I appreciate it.**