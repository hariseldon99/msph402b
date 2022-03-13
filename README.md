MSPH402B
============================================

Python lectures and codes for MSPH402B - Computational Physics, taught at the Department of Physics, The University of Burdwan

A repository of all my codes, tutorial lectures and simulations used to teach [Computational Physics](https://bit.ly/mphys0402b) to masters students at the 
[Department of Physics](https://sites.google.com/a/phys.buruniv.ac.in/physics/) in [The University of Burdwan](https://www.buruniv.ac.in/)

The simulations are written in the [Python programming language](https://www.python.org/about/gettingstarted/).

The lecture slides can be found @ [My Google Drive](https://drive.google.com/drive/folders/0B1MOUTtP6VgCS3FzLUNJSkU3T00?resourcekey=0-Anxa-FXoffLqaPimLzAAWQ&usp=sharing{/google_docs)

The website for this Course is @ [https://bit.ly/msph402b](https://bit.ly/msph402b)

Background
=========================

* For a quick introduction to the Python programming language, as well as [Numerical Python](https://numpy.org), [Scientific Python](https://scipy.org) and [Matplotlib](https://matplotlib.org), see [this tutorial](https://cs231n.github.io/python-numpy-tutorial/)

* For a more detailed introduction to the abovementioned topics, see Robert Johansson's [Scientific Python Lectures](https://github.com/jrjohansson/scientific-python-lectures).

# Instructions

You can run these python codes by installing the requisite software in your computer, or online through [Google Colab](https://colab.research.google.com/).

1. **Recommended:** In case you cannot install Python locally on your computer, you may run the codes through [Google Colab](https://colab.research.google.com/) by clicking on the links to the jupyter notebooks below, then clicking on the "Open in Colab" button at the top of the notebook. This will work on any computer, mobile or tablet that has internet access and a standard web browser like Google Chrome, Microsoft Edge, Firefox or whatever. However, these codes will run on colab servers, rather than locally on your computer. This is usually not a problem, although the servers might be slow.

2. In order to run these programs locally in your computer (instead of Google Colab), perform the following steps.
   
   * **On regular console computers** (desktops or laptops):
     * Install GitHub Desktop after downloading it from its website @ [desktop.github.com](https://desktop.github.com/)
     * Then, download this repository by cloning it using GitHub Desktop (see [this doc](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop)  for details).
     * Finally, download and install the anaconda python distribution (anaconda @ https://www.anaconda.com/). Anaconda includes [Jupyter notebooks](https://jupyter.org/) and the [Spyder IDE](https://www.spyder-ide.org/), either of which can be readily used for designing and running python code. Also, see [this blog entry](https://fangohr.github.io/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html) on how to install anaconda.
   * **On Android devices**: 
     * You can install [Pydroid](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) to design and run python programs. 
     * See [this video](https://drive.google.com/file/d/1xnr4iZRtfbx4LQ2d7Cl3fOdQ6Utb80zI/view?usp=sharing) for setup instructions. 
     * I do not recommend using Git or jupyter on mobile phones (too complicated for small screens), although git apps for Android do exist in the store. You can check them out if you wish. Alternative ways of getting these codes are discussed below.

3. If you're having problems with Git, and do not want to use Google Colab, you can simply copy-paste the codes individually into your local python setup:
   
   * Click on the "Copy raw contents" button on the top-right corner of the github page of a particular code (to the right of the 'Blame' button).
   
   * Then, paste it into a text editor or a running python IDE like [Spyder](https://www.spyder-ide.org/) or [Pydroid](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) in order to execute it. 
   
   * **However**, this will only work for regular Python, not for Jupyter notebooks. For the latter, you can either run them in Google Colab, or copy-paste each code cell from the jupyter notebook to a local Python file in your device. This should work well on Android devices, where it is difficult to run jupyter locally. Note, however, that IPython magics won't work in regular Python, and you'll have to delete or rewrite them.

List of Tutorials and Codes
=========================

Use the following links:

## Scientific Python Tutorials:

* [Scientific Python Tutorials (including numpy and matplotlib)](https://github.com/hariseldon99/scientific-python-lectures)

## Numerical Methods, Example Codes:

* [Simple code for determining machine precision](01-MachinePrecision/mprecis.py) 
* [Examples of Numerical Interpolation](Interpolation_all.ipynb)
* [Examples of Solving Systems of Linear Equations](Computational_Linear_Algebra_all.ipynb)
* [Numerical Root Finding Examples](Root_Finding.ipynb)
* [Examples of Numerical Integration of Functions](Integration.ipynb)
* [Examples of Ordinary Differential Equations (IVP) - Part 1](ODE_IVP_Pt1.ipynb)
* [Examples of Ordinary Differential Equations (IVP) - Part 2](ODE_IVP_Pt2.ipynb)
* [Examples of Ordinary Differential Equations (BVP)](ODE_BVP.ipynb)
* [Examples of Fast Fourier Transforms (FFT)](FFT.ipynb)
* [Examples from Special Topics](Special_Topics.ipynb)

License
=======

This work is licensed under a [MIT License](LICENSE)

Author
=======

Analabha Roy  
Assistant Professor,  
[Department of Physics](https://sites.google.com/a/phys.buruniv.ac.in/physics/),  
[The University of Burdwan](https://www.buruniv.ac.in/)  
[Bardhaman](https://en.wikivoyage.org/wiki/Bardhaman), India 713104  
Webpage: https://www.ph.utexas.edu/~daneel
