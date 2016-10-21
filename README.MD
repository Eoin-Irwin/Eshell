# Eshell++

A subset of the previous Eshell which used tsh(Tiny Shell)

It now has been optimised slightly

## Getting Started

Copy the Eshell++ folder onto your server. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need an external library called ipgetter

On some Linux Vanilla servers you may need to install pip first.

```
sudo apt-get install python-pip
```
Then install the requirements text file

```
pip install -r requirements.txt
```

Or

```
pip install ipgetter
```

## Extra Features

Reporting users if they attempt to use a sudo command and they don't belong to that group

```
sudo tail /var/log/syslog
```

A cool visual to look at

```
cmatrix
```

Bringing back the classics, to play enter

```
pacman4console
```

Another cool one, again, to play enter the following command

```
nsnake
```

## Built With

* [Pycharm](http://www.Pycharm.com) - The IDE used
* [Python](https://www.Python.com/) - Language

## Author

* **Eoin Irwin**

## License

This project is licensed under the MIT License - see the [LICENCE.MD](LICENCE.MD) file for details
