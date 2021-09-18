# fantasy-football
 
This is a simple website that uses Flask to render a webpage.

It is hosted on AWS using Elastic BeanStalk.

## Deployment steps

```
eb create flask-env

eb init -p python-3.6 fantasy-football --region us-east-1

eb open
````

