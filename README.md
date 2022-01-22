# TutionWebsite1
This is Website 1 for Tution

# Environment Set-up for Windows
To run Makefile:
	1. Open powershell as an admin
	2. Set-ExecutionPolicy Unrestricted
	3. Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    4. Choco install make

# Environment Set-up for Mac
To run Makefile:
	1. Install Homebrew
	2. Add that to your path
	3. brew install make
	4. Add that to your path
