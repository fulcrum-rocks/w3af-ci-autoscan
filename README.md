<h1 align="center">Automatic web Security testing with w3af in Docker</h1>
<p align="center">
<img align="center" src="http://ForTheBadge.com/images/badges/made-with-python.svg" alt="demo"/>
</p>

> The tool allows quickly and easily scan a website for known vulnerabilities. <br /> `docker run w3af-scan fulcrum.rocks` will return result for fulcrum.rocks website.

## ✨ Description

`w3af` is a Web Application Attack and Audit Framework. The project’s goal is to create a framework to help you secure your web applications by finding and exploiting all web application vulnerabilities.

<p align="center">
  <img width="700" align="center" src="https://i.imgur.com/4BEv5yVl.png" alt="demo"/>
</p>

## 🚀 Usage

Build:

```sh
docker build -t w3af-scan .
```

Run:

```sh
docker run w3af-scan <url>
```

## 📝 License

This project is [MIT](https://github.com/kefranabg/readme-md-generator/blob/master/LICENSE) licensed.
