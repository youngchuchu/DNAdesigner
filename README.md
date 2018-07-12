# DNA Designer

## A double-stranded DNA origami and nanostructure design tool
A software tool to simplify the production of double-stranded DNA origami nanostructures *in vivo* and *ex vivo* using the TAL-staple method of Praetorius and Dietz. Functions include primary DNA sequence generation, and estimation of physical properties of the nanostructure.

## Features and Functions
There are currently three programs bundled in this software package, all complementary to each other.

- The first is a simple **Recommended TAL-structure selector**, which allows a user to dictate a general shape of DNA structure, and acquire the closest structure that has been empirically proven to work (as per the supplementary from Praetorius and Dietz' 2017 paper). The software provides important physical properties of each structure, such as interenzyme distance between TAL N-terminal-mounted proteins, and the likelihood that the selected structure will produce higher order structures (i.e. do the TAL-structures dimerize?). 

<p float="middle">
  <img align="middle" src="https://github.com/malyalar/DNAdesigner/blob/master/RudimentaryFiles/sample1.PNG" width="300" />
  <img align="middle" src="https://github.com/malyalar/DNAdesigner/blob/master/RudimentaryFiles/sample2.PNG" width="300" /> 
</p>

- The second is a more complex software tool: **New TAL-structure generator**. This program generates *de novo* DNA origami shapes and primary sequences, made ready-to-order. The software, using established physical properties of DNA and the dsDNA origami design rules laid out by Praetorius et al., takes user input in the form of selected spaces between TAL-staples (in integer base pairs) and predicts the shape, structure, and other physical properties of the nanostructure. This greatly simplifies the process of dsDNA origami design, although as usual, it is important to carefully look over the output before placing any order.

<img align="middle" src="https://github.com/malyalar/DNAdesigner/blob/master/Communications/Screencapture.PNG" width="500" />

-The third tool is a game: **ShapeMaker**, in which players are tasked with creating shapes from a chain of virtual links, by selecting specific links that will bind specifically to each other. This mimics the TAL-staple approach of making shapes from a line of DNA (the chain). The purpose of the game is two-fold: to promote high-level spatial reasoning development in its players, and to potentially suggest new, efficient methods of TAL-structure arrangement. The game is scored based on how close to the desired shape you can set up your chain, as well as how few TALs you use. By gamifying the complex process of TAL-structure precognitition, we effectively crowdsource one of the difficult aspects of DNA origami design: to figure out where the TALs should bind!

