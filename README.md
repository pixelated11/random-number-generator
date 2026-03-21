# Random Number Generator
This python program is for generating random numbers. You can input the range in which the random number will be pointed out in.
> [!Warning]
> You must place the file `program` and `_internal` at the same directory to run the program. Unless, it won't run. (for linux only)
## Downloading
Just get the binary in the releases page. It's build using pyinstaller. If you want the python program, download the one in the commits.

## Building 
### For Windows:
Clone the repo, then run
```bash
pip install -r requirements.txt
```
After that, run:
```bash
pyinstaller program.py
```
Your program should be in the dist/programs folder.
### For Linux:
Clone repo, then run:
```bash
pip install -r requirements.txt
```
Then, run:
```bash
pyinstaller program.py
```
Locate to `dist/programs` and then do:
```bash
chmod +x program
```
Then to run it, type in:
```
./program
```
