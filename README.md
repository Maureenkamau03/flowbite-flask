Flowbite is an open-source library of UI components based on the utility-first Tailwind CSS framework featuring dark mode support, a Figma design system, templates, and more.


PostCSS is a JavaScript tool that transforms your CSS code into an abstract syntax tree (AST) and then provides an API (application programming interface) for analyzing and modifying it using JavaScript plugins.

To install tailwindcss and its peer dependencies run
```
$ npm install -d tailwindcss postcss autoprefixer
```

## Install Flowbite 
Install Flowbite as a dependency using NPM:
```
npm install flowbite
```

Require Flowbite as a plugin inside the tailwind.config.js file:
```
module.exports = {

    plugins: [
        require("flowbite/plugin")
    ]

}
```

Include Flowbite inside the content key value pair of the tailwind.config.js file:
```
module.exports = {
  content: [
      "./templates/**/*.html",
      "./static/src/**/*.js",
      "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("flowbite/plugin")
  ],
}
```
Include Flowbite’s JavaScript file inside the index.html file just before the end of the body tag using CDN or by including it directly from the node_modules/ folder:
```
<script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.6.5/flowbite.min.js"></script>

```
Out of css, this is how you use ``` url_for ``` to dynamically generate links to the sections in your flask templates. 

On your nav links for instance a link to your testimonials section you could have this:
```
<a href="{{ url_for('index', _anchor='testimonials') }}">Testimonials</a>

```
You should also create its respective route in routes.py as shown below:
```
def testimonials():
    """testinomials URL"""
    return render_template('index.html', section_anchor='testimonials')
```