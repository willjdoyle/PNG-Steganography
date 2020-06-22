# PNG-Steganography

PNG Steganography embeds a message into a .png and uses a two-layered encryption system to attempt to fulfill Shannon's Maxim. PNG Steganography is current on v1.0.

## Installation

To encrypt and embed a message in an .png, download encrypter.py. To decrypt an image that was put through the encrypter, use decrypter.py. If you would like to reset an image back to its original form and delete its message, use reset.py.

## How to Run

Start the relevant file and follow the prompts.

### Additional Notes:

To encrypt/decrypt an image, the program will look for a file in the same folder named "target.png". Once the encryption/decryption is complete you may rename the file.

The encryper will ask you for your message. Currently, it can only accept the A-Z Latin alphabet, which means that it will not accept special characters, spaces, and numbers. It will then OVERWRITE "target.png" with the encoded image. To the naked eye, it will appear identical.

## Issues

### Issue Templates
To submit a bug report or request a feature, please use the templates located in [template folder](.github/ISSUE_TEMPLATE).

### Known Issues
No special characters are currently allowed. Support will be added in a later version. I am still working on improving the efficiency of the decrypter.

## Versioning

PNG Steganography is currently on v1.0. A full changelog can be found in the Dev Roadmap in the Projects tab.

## Authors

PNG Steganography was developed in its entirity by William Doyle.

## License

This project is licensed under the GNU AGPL v3.0 License. Please see [LICENSE](LICENSE) for more details.