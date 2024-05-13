# Odoo Development Cookbook

<a href="https://www.packtpub.com/product/odoo-development-cookbook-fifth-edition/9781805124276?utm_source=github&utm_medium=repository&utm_campaign=9781805124276"><img src="https://m.media-amazon.com/images/I/71tqBvTp1ML._SL1500_.jpg" alt="Odoo Development Cookbook" height="256px" align="right"></a>

This is the code repository for [Odoo Development Cookbook](https://www.packtpub.com/product/odoo-development-cookbook-fifth-edition/9781805124276?utm_source=github&utm_medium=repository&utm_campaign=9781805124276), published by Packt.

**Build effective business applications using the latest features in Odoo 17**

## What is this book about?
In its latest version, the powerful Odoo framework uncovers a wide variety of features for rapid application development. This updated Odoo development cookbook will help you explore the new features in Odoo 17 and learn how to use them to develop applications from scratch.

This book covers the following exciting features:
* Build intuitive websites with Odoo CMS using dynamic building blocks
* Get to grips with advanced concepts such as caching, prefetching, and debugging
* Modify backend JavaScript components and POS applications with the updated OWL framework
* Connect and access any object in Odoo via Remote Procedure Calls (RPCs)
* Manage, deploy, and test an Odoo instance with Odoo.sh
* Configure IoT Box to add and upgrade Point of Sale (POS) hardware
* Find out how to implement in-app purchase services

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1805124277) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders.

The code will look like the following:
```
@http.route('/my_library/books/json', type='json', auth='none')
def books_json(self):
records = request.env['library.book'].sudo().search([]) return 
records.read(['name'])
```

**Following is what you need for this book:**
This book is for developers who are new to the Odoo framework and want to develop effective business applications. Experienced Odoo developers looking to revisit specific topics or discover new features in Odoo 17 may also benefit from this book. Basic knowledge of Python programming and JavaScript programming is necessary to get the most out of this book.

With the following software and hardware list you can run all code files present in the book (Chapter 1-25).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-25 | Odoo 17 | Windows, Mac OS X, and Linux (Any) |
| 24 | Raspberry Pi | Windows, Mac OS X, and Linux (Any) |


### Related products
* Odoo 15 Development Essentials [[Packt]](https://www.packtpub.com/product/odoo-15-development-essentials-fifth-edition/9781800200067?utm_source=github&utm_medium=repository&utm_campaign=9781800200067) [[Amazon]](https://www.amazon.com/dp/1800200064)

* Democratizing RPA with Power Automate Desktop [[Packt]](https://www.packtpub.com/product/democratizing-rpa-with-power-automate-desktop/9781803245942?utm_source=github&utm_medium=repository&utm_campaign=9781803245942) [[Amazon]](https://www.amazon.com/dp/1803245948)


## Get to Know the Author
**Husen Daudi**
a software developer with a Master’s Degree from Gujarat University, India, is also a Six 
Sigma Black Belt consultant. He co-founded Serpent Consulting Services Pvt. Ltd., a prominent Open 
Source ERP Service provider with over 100 IT specialists serving clients in more than 170 countries. 
With extensive experience in ERP implementation since 2007, he brings a unique approach to his 
work. Husen has played a pivotal role in developing and maintaining various ERP implementations 
in both public and private sectors. Outside of work, he is a hobbyist painter and cherishes spending 
time with his sons, Mufaddal and Yusuf.

**Jay Vora**
a software engineer with a bachelor’s degree from Gujarat University, India, is known for his 
thoughtful leadership, passion for development, and enthusiasm for technology. With over a decade 
of experience in ERPs since 2007, he co-founded Serpent Consulting Services Pvt. Ltd., a leading 
provider of Odoo services. The company boasts a team of over 100 IT specialists serving clients across 
170 countries. Jay is known for his sociable nature and active participation in various Odoo forums 
and social platforms. In addition to his technical pursuits, he is also a poet, writer, and avid blogger 
on topics ranging from motivation and cricket to ERP-related subjects.
