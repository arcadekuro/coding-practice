# FreeCodeCamp-projects
Repository to host, track and display projects provided by the freeCodeCamp curriculum


In this repository I will commit all projects outlined in the freeCodeCamp curriculum from start to completion. 
There are 6 certifications provided by the code camp cirriculum. In total,there are 35 individual projects. 

As each project is actioned, I will tick the corresbonding tick box to mark as completed. 

 Responsive Web Design Certification (300 hours) 
 - [x] Build a tribute page (https://codepen.io/arcadek/pen/LaXbyY) 
 - [x] Build a survey Form (https://codepen.io/arcadek/full/eXQRZO)
 - [x] Build a Product Landing page (https://codepen.io/arcadek/pen/WmLZdE) 
 - [x] Build a Personal portfolio Webpage (https://codepen.io/arcadek/pen/GLNKxO)
 
 My Web Design Certification: https://www.freecodecamp.org/certification/arcadekuro/responsive-web-design
 
 Introduction to the JavaScript Algorithims and Data Structures Certification (300 hours) 
 - [ ] Palindrome checker 
 - [ ] Roman Numeral Converter
 - [ ] Ceasears Cipher 
 - [ ] Telephone number Validator 
 - [ ] Cash Register

Front end libraries Certification ( 300 hours) 
- [ ] Build a random quote machine 
- [ ] Buiild a Markdown Previewer 
- [ ] Build a Drum Machine 
- [ ] Build a JavaScript Calculator 
- [ ] Build a pomodoro Clock 


# Learning
The information below is provided in the Free Code Camp tutorials. This is just for my own reference in the case I want to look back.

# HTML
## Input Elements
 Input elements are convenient way to get input from your user.
 `<input type="text">`
 you can also create a form that has the input nested undearneath.
 Placeholder text is what is displayed in your input element before your user has inputed anything using `placeholder="this is placeholder text">`

Fields can also be specified as required input using <input type="text" required>
Radio buttons are another type of input. Each button can be nested withinits ownb label element. It's best practice to set a for attribute on thelabel element with a value that matches the value of id attribute of theinput element. 

checkboxes are an additional input.
When a form gets submitted, the data is sent to the server and includes
entries for the options selected. Inputs of type radio and checkbox report their values from the value attribute.

If you omit the value attribute, the submitted form data uses the default value, which is on. In this scenario, if the user clicked the "indoor"option and submitted the form, the resulting form data would beindoor-outdoor=on, which is not useful. So the value attribute needs to beset to something to identify the option.

You can set a checkbox or radio button to be checked by default using thechecked attribute.
`<input type="radio" name="test-name" checked>`

# CSS

## Overiding CSS libraries

Sometimes our HTML elements will receive multiple styles that conflict with one another.

For example, your h1 element can't be both green and pink at the same time. classes will overide styles set to html elements. 

If two classes are given, the browser reads top to bottom and use whicever CSS decleration  comes last. Like in python.

you can also overide your css class by adding an id.


You can apply multiple classes to an element using its class attribute, by separating each class name with a space. For example:

`<img class="class1 class2">`

ID or class to elements are known as ID and class Selectors. 
There are other CSS selectors. The [attr=value] slector matches and styles elements with a specific attribute value. 

In many situations, you will use CSS libraries. These may accidentally override your own CSS. So when you absolutely need to be sure that an element has specific CSS, you can use !important


## Representing colors in CSS.
There are other ways to represent colours such as hexidecimal code. hexadecimal(hex) are bas 16 numbers - it uses sixteen distinct symbols. 
Like decimals, the symbols 0-9 represent the values zero to nine. Then A,B,C,D,E,F represent the values ten to fifteen. Altogether, 0 to F can represent a digit in hexadecimal, giving us 16 total possible values. 

In CSS, we can use 6 hexadecimal digits to represent colors, two each for the red (R), green (G), and blue (B) components. For example, #000000 is black and is also the lowest possible value. 

### Using Hex Code to Mix colors. 
From these three pure colors (red, green, and blue), we can vary the amounts of each to create over 16 million other colors.
For example, orange is pure red, mixed with some green, and no blue. In hex code, this translates to being `#FFA500`.

The digit `0` is the lowest number in hex code, and represents a complete absence of color.

The digit `F` is the highest number in hex code, and represents the maximum possible brightness.

| colours       | Hex code      | 
| ------------- |:-------------:|
| Dodger Blue   | #1E90FF       | 
| Green         | #00FF00       | 
| Orange        | #FFA500       |
| Red           | #FF0000       |

It can be difficult to remember hex code, but fortunately it can be shortened. #FFOOOO
can be shortened to #F00. 

This reduces the total number of possible colors to around 4,000. But browsers will interpret #FF0000 and #F00 as exactly the same color.

| Colour  | Short Hex code |
| ------ |:--------------:|
| Cyan   | #0FF           |
| Green  | #0F0           |
| Red    | #F00           |
| Fuchsia| #F0F           |

### Using RGB values
Another way you can represent colors in CSS is by using RGB values.

The RGB value for black looks like this:

rgb(0, 0, 0)

The RGB value for white looks like this:

rgb(255, 255, 255)

Instead of using six hexadecimal digits like you do with hex code, with RGB you specify the brightness of each color with a number between 0 and 255.

`body {
  background-color: rgb(255, 165, 0);
}`

### Using RGB to mix colours
Just like with hex code, you can mix colors in RGB by using combinations of different values.

| colours       |   RGB             | 
| ------------- |:-----------------:|
| Blue          | rgb(0, 0, 225)    | 
| Red           | rgb(255, 0, 0)    | 
| orchid        | rgb(218, 112, 214)|
| Sienna        | rgb(160, 82, 45)  |


### Use CSS variables to change several elements at once

CSS Variables are a powerful way to change many CSS style properties at once by changing only one value.

To create a CSS variable, you just need to give it a name with two hyphens in front of it and assign it a value like this:

`--penguin-skin: gray;`

This will create a variable named --penguin-skin and assign it the value of gray. Now you can use that variable elsewhere in your CSS to change the value of other elements to gray.

After you create your variable, you can assign its value to other CSS properties by referencing the name you gave it.

`background: var(--penguin-skin)`

This will change the background of whatever element you are targeting to gray because that is the value of the --penguin-skin variable. Note that styles will not be applied unless the variable names are an exact match.

#### Attach a fallback value to a CSS variable

When using your variable as a CSS property value, you can attach a fallback value that your browser will revert to if the given variable is invalid.

`background: var(--penguin-skin, black);`

### Improve Compatibility with Browser Fallbacks
When working with CSS you will likely run into browser compatibility issues at some point. This is why it's important to provide browser fallbacks to avoid potential problems.

When your browser parses the CSS of a webpage, it ignores any properties that it doesn't recognize or support. For example, if you use a CSS variable to assign a background color on a site, Internet Explorer will ignore the background color because it does not support CSS variables. In that case, the browser will use whatever value it has for that property. If it can't find any other value set for that property, it will revert to the default value, which is typically not ideal.

This means that if you do want to provide a browser fallback, it's as easy as providing another more widely supported value immediately before your declaration. That way an older browser will have something to fall back on, while a newer browser will just interpret whatever declaration comes later in the cascade.

### Inherit CSS Variables
When you create a variable, it is available for you to use inside the selector in which you create it. It also is available in any of that selector's descendants. This happens because CSS variables are inherited, just like ordinary properties.

To make use of inheritance, CSS variables are often defined in the :root element.

:root is a pseudo-class selector that matches the root element of the document, usually the html element. By creating your variables in :root, they will be available globally and can be accessed from any other selector in the style sheet.


## Visual Design
Visual design combine typography, color theory, graphics, animation and page layout.
HTML give structure and semantics to a page's content, and CSS controls the layout and apperance of it. 

### Text-align
Text is often a large part of web content. CSS has several options for how to align it with the text-align property.

text-align: justify; causes all lines of text except the last line to meet the left and right edges of the line box.

text-align: center; centers the text

text-align: right; right-aligns the text

And text-align: left; (the default) left-aligns the text.

### Width & Height
You can specify the width of an element using the width property in CSS. Values can be given in relative length units (such as em), absolute length units (such as px), or as a percentage of its containing parent element. Here's an example that changes the width of an image to 220px

`img {
  width: 220px;
  height: 20px;
}`

You can specify the height of an element using the height property in CSS, similar to the width property. 

### Bold, underline, strikethrough & italicise
To make text bold, you can use the strong tag. This is often used to draw attention to text and symbolize that it is important. With the strong tag, the browser applies the CSS of font-weight: bold; to the element. `<strong>`

To underline text, you can use the u tag. This is often used to signify that a section of text is important, or something to remember. With the u tag, the browser applies the CSS of text-decoration: underline; to the element. `<u></u>`

To emphasize text, you can use the em tag. This displays text as italicized, as the browser applies the CSS of font-style: italic; to the element. `<em></em>`

You can use the hr tag to add a horizontal line across the width of its containing element. This can be used to define a change in topic or to visually separate groups of content.

### Adjust the background-color Property of Text
Instead of adjusting your overall background or the color of the text to make the foreground easily readable, you can add a background-color to the element holding the text you want to emphasize. This challenge uses rgba() instead of hex codes or normal rgb().

rgba stands for:
  r = red
  g = green
  b = blue
  a = alpha/level of opacity
The RGB values can range from 0 to 255. The alpha value can range from 1, which is fully opaque or a solid color, to 0, which is fully transparent or clear. rgba() is great to use in this case, as it allows you to adjust the opacity. This means you don't have to completely block out the background.  rgba(45, 45, 45, 0.1) produces a dark gray color that is nearly transparent given the low opacity value of 0.1.

### Add a box-shadow to a Card-like Element

The box-shadow property applies one or more shadows to an element.

The box-shadow property takes values for

offset-x (how far to push the shadow horizontally from the element),
offset-y (how far to push the shadow vertically from the element),
blur-radius,
spread-radius and
color, in that order.
The blur-radius and spread-radius values are optional.

Multiple box-shadows can be created by using commas to separate properties of each box-shadow element.

Here's an example of the CSS to create multiple shadows with some blur, at mostly-transparent black colors:

`box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);`


### Opacity
The opacity property in CSS is used to adjust the opacity, or conversely, the transparency for an item.

A value of 1 is opaque, which isn't transparent at all.
A value of 0.5 is half see-through.
A value of 0 is completely transparent.
The value given will apply to the entire element, whether that's an image with some transparency, or the foreground and background colors for a block of text.

### use the text-transform Property to Make Text Uppercase

The text-transform property in CSS is used to change the appearance of text. It's a convenient way to make sure text on a webpage appears consistently, without having to change the text content of the actual HTML elements. `text-transform: uppercase;`

There different text-transformvalues:

*lowercase
* uppercase
* cappitalize
* initial - use the default value
* inherit - use the text-transform value from the parent element 
* none - Default: use the original text

### Line height
CSS offers the line-height property to change the height of each line in a block of text. As the name suggests, it changes the amount of vertical space that each line of text gets.

### Ajust the Hover state of an Anchor Tag
A pseudo-class is a keyword that can be added to selectors, in order to select a specific state of the element.
the styling of an anchor tag can be changed for its hover state using the :hover pseudo-class selector. Here's the CSS to change the color of the anchor tag to red during its hover state:

`a:hover {
  color: red;
}`

### Change an Element's Relative Position
CSS treats each HTML element as its own box, which is usually referred to as the CSS Box Model. Block-level items automatically start on a new line (think headings, paragraphs, and divs) while inline items sit within surrounding content (like images or spans). The default layout of elements in this way is called the normal flow of a document, but CSS offers the position property to override it.

When the position of an element is set to relative, it allows you to specify how CSS should move it relative to its current position in the normal flow of the page. It pairs with the CSS offset properties of left or right, and top or bottom. These say how many pixels, percentages, or ems to move the item away from where it is normally positioned. The following example moves the paragraph 10 pixels away from the bottom:

`p {
  position: relative;
  bottom: 10px;
}`

Changing an element's position to relative does not remove it from the normal flow - other elements around it still behave as if that item were in its default position.

The CSS offsets of top or bottom, and left or right tell the browser how far to offset an item relative to where it would sit in the normal flow of the document. You're offsetting an element away from a given spot, which moves the element away from the referenced side (effectively, the opposite direction). As you saw in the last challenge, using the top offset moved the h2 downwards. Likewise, using a left offset moves an item to the right.

![alt text](https://cdn-media-1.freecodecamp.org/imgr/eWWi3gZ.gif "offset gif")


###  positioning 
The next option for the CSS position property is absolute, which locks the element in place relative to its parent container. Unlike the relative position, this removes the element from the normal flow of the document, so surrounding items ignore it. The CSS offset properties (top or bottom and left or right) are used to adjust the position.

One nuance with absolute positioning is that it will be locked relative to its closest positioned ancestor. If you forget to add a position rule to the parent item, (this is typically done using position: relative;), the browser will keep looking up the chain and ultimately default to the body tag.

fixed position, which is a type of absolute positioning that locks an element relative to the browser window. One key difference between the fixed and absolute positions is that an element with a fixed position won't move when the user scrolls.

The next positioning tool does not actually use position, but sets the float property of an element. Floating elements are removed from the normal flow of a document and pushed to either the left or right of their containing parent element. It's commonly used with the width property to specify how much horizontal space the floated element requires.

When elements are positioned to overlap (i.e. using position: absolute | relative | fixed | sticky), the element coming later in the HTML markup will, by default, appear on the top of the other elements. However, the z-index property can specify the order of how elements are stacked on top of one another. It must be an integer (i.e. a whole number and not a decimal), and higher values for the z-index property of an element move it higher in the stack than those with lower values.

Another positioning technique is to center a block element horizontally. One way to do this is to set its margin to a value of auto.

This method works for images, too. Images are inline elements by default, but can be changed to block elements when you set the display property to blo