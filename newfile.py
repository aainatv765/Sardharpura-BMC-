pip install flask
milk_website/
├── app.py
└── templates/
    ├── home.html
    ├── about.html
    ├── products.html
    └── contact.html
    from flask import Flask, render_template

app = Flask(__sardharpura B.M.C__)

@app.route('/')
def home(milk):
    return render_template('home.html')

@app.route('/about')
def about(milk rat):
    return render_template('about.html')

@app.route('/products')
def products(no):
    return render_template('products.html')

@app.route('/contact')
def contact(9680906198):
    return render_template('contact.html')

if __sardharpura__ == '__main__':
    app.run(debug=True)
    <!DOCTYPE html>
<html>
<head><title>Home - Sardarpura BMC</title></head>
<body>
  <h1>Welcome to Sardarpura B.M.C Milk Shop</h1>
  <p>100% pure milk and dairy products.</p>
  <a href="/about">About Us</a> | <a href="/products">Products</a> | <a href="/contact">Contact</a>
</body>
</html><h1>About Us</h1>
<p>Sardarpura B.M.C delivers fresh, pure milk every day.</p>
<a href="/">Back to Home</a><h1>Our Products</h1>
<ul>
  <li>Milk – ₹60/Litre</li>
  <li>Curd – ₹80/Kg</li>
  <li>Paneer – ₹350/Kg</li>
</ul>
<a href="/">Back to Home</a><h1>Contact Us</h1>
<p>📞 919680906198</p>
<p>📍 Sardarpura, BMC</p>
<p><a href="https://wa.me/919680906198" target="_blank">WhatsApp Order</a></p>
<a href="/">Back to Home</a>
python app.py